import os
import antlr4.tree.Tree
from io import FileIO
from termcolor import colored
from core.CVisitor import CVisitor
from core.CParser import CParser
from manager import Manager
from manager import Scope
from manager import ScopeType
from manager import Clazz
from manager import Attribute
from manager import Function
from manager import Variable
from manager import Obj
from manager import Arg
import llvmlite.ir as ir

# Create a module
module = ir.Module(name="main")
module.triple = "x86_64-redhat-linux-gnu"

i8 = ir.IntType(8)
i16 = ir.IntType(16)
i32 = ir.IntType(32)
i64 = ir.IntType(64)


class State:
    def __init__(self):
        self.is_class = False
        self.scope_level = 0

    @property
    def tabs(self):
        return '\t' * self.scope_level

    def visit_block_scope(self):
        self.scope_level += 1

    def exit_block_scope(self):
        if self.scope_level > 0:
            self.scope_level -= 1

    def visit_class(self):
        self.is_class = True

    def exit_class(self):
        self.is_class = False


def print_error(error: str):
    print(colored(error, 'red'))


class Visitor(CVisitor):
    def __init__(self, stream, output):
        # steam is CommonTokenStream to get hidden channel
        self.stream = stream
        self.output: FileIO = output
        self.state = State()
        self.manager = Manager()

    def write(self, text: str):
        self.output.write(text)

    def add_newline(self) -> None:
        self.output.write('\n')

    def ungetch(self):
        cur = self.output.tell()
        self.output.seek(cur - 1, os.SEEK_SET)
        self.output.truncate()

    def match_type_specifier(self, ctx: CParser.TypeSpecifierContext):
        # custom method to not repeat type matching
        chunks: list[str] = []
        for terminal_node in ctx.getChildren():
            match terminal_node.getText():
                case 'unsigned':
                    chunks.append('unsigned')
                case 'signed':
                    chunks.append('signed')
                case 'void':
                    chunks.append('void')
                case 'char':
                    chunks.append('char')
                case 'short':
                    chunks.append('short')
                case 'int':
                    chunks.append('int')
                case 'long':
                    chunks.append('long')
                case 'float':
                    chunks.append('float')
                case 'double':
                    chunks.append('double')
                case '*':
                    chunks.append('*')
                case _identifier:
                    chunks.append(_identifier)
        try:
            return self.manager.get_clazz(chunks[0]), ' '.join(chunks)
        except NameError:
            return None, ' '.join(chunks)

    def expression_to_llvm_ir(self, expression):
        match type(expression):
            case CParser.ConstantExpressionContext:
                constant: CParser.ConstantContext = expression.constant()
                if x := constant.INTEGER_CONSTANT():
                    return ir.Constant(ir.IntType(32), x)
            case CParser.IdentifierExpressionContext:
                return self.manager.scope_stack.get_variable(
                    (expression.identifier().getText()))
            case CParser.MultiplyExpressionContext:
                return self.visitMultiplyExpression(expression)
            case CParser.DivideExpressionContext:
                return self.visitDivideExpression(expression)
            case CParser.AddExpressionContext:
                return self.visitAddExpression(expression)
            case CParser.SubtractExpressionContext:
                return self.visitSubtractExpression(expression)
            case CParser.EqExpressionContext:
                return self.visitEqExpression(expression)

    def visitCompilationUnit(self, ctx: CParser.CompilationUnitContext):
        for child in ctx.getChildren():
            match type(child):
                case CParser.IncludeDirectiveContext:
                    # self.write(child.getText())
                    pass
                case CParser.DeclarationListContext:
                    for declaration in child.getChildren():
                        match type(declaration):
                            case CParser.VariableDeclarationContext:
                                self.visitVariableDeclaration(declaration)
                            case CParser.FunctionDeclarationContext:
                                self.visitFunctionDeclaration(declaration)
                            case CParser.StructDeclarationContext:
                                self.visitStructDeclaration(declaration)
                case CParser.DefinitionListContext:
                    for definition in child.getChildren():
                        match type(definition):
                            case CParser.VariableDefinitionContext:
                                self.visitVariableDefinition(definition)
                            case CParser.FunctionDefinitionContext:
                                self.visitFunctionDefinition(definition)
                            case CParser.StructDefinitionContext:
                                self.visitStructDefinition(definition)
                case CParser.FunctionCallContext:
                    self.visitFunctionCall(child)
                case CParser.AssignmentContext:
                    self.visitAssignment(child)
                case CParser.ClassDefinitionContext:
                    self.visitClassDefinition(child)
        self.write(str(module))

    def visitTypeSpecifier(self, ctx: CParser.TypeSpecifierContext):
        clazz, type_specifier = self.match_type_specifier(ctx)
        return clazz, type_specifier

    def store(self, value, ptr, **kwargs):
        builder = self.manager.builder
        try:
            builder.store(value, ptr)
        except TypeError:
            if ptr.type == i8.as_pointer() \
                    and isinstance(value, ir.GlobalVariable):
                builder.store(value.gep([ir.Constant(i32, 0),
                                         ir.Constant(i32, 0)], ),
                              ptr)
            elif ptr.type == i8.as_pointer().as_pointer() \
                    and isinstance(value, ir.GlobalVariable):
                # this is a sting literal
                start_ptr = value.gep([
                    ir.Constant(i32, 0),
                    ir.Constant(i32, 0)
                ])
                builder.store(start_ptr, ptr)
            elif ptr.type == i16.as_pointer():
                # handle short int
                builder.store(builder.trunc(value, i16), ptr)

    def visitVariableDefinition(self, ctx: CParser.VariableDefinitionContext):
        _, type_specifier = self.visitTypeSpecifier(ctx.typeSpecifier())
        identifier = ctx.identifier().getText()
        # check if this is a class object variable definition
        clazz_name, *_ = type_specifier.split()
        try:
            clazz = self.manager.get_clazz(clazz_name)
            obj: Obj = Obj(name=identifier, clazz=clazz)
            self.manager.add_obj(obj)
        except NameError:
            pass
        expression = self.visitExpression(ctx.expression())
        builder = self.manager.builder
        type_specifier = self.type_specifier_to_ir_type(type_specifier)
        variable = builder.alloca(type_specifier, name=identifier)
        self.manager.scope_stack.add_variable(variable)
        self.store(expression, variable)
        return variable

    def visitVariableDeclaration(self,
                                 ctx: CParser.VariableDeclarationContext,
                                 is_clazz_attribute: bool = False):
        ctx.scope_level = self.state.scope_level
        # self.check_variable_declaration(ctx)
        clazz, type_specifier = self.visitTypeSpecifier(ctx.typeSpecifier())
        identifier = ctx.identifier().getText()
        variable = Variable(name=identifier, type_specifier=type_specifier)
        self.manager.add_variable(variable)
        cells: str = ''
        if ctx.arrayCell():
            for cell in ctx.arrayCell():
                cells += cell.getText()
        if is_clazz_attribute:
            attribute = Attribute(
                type_specifier=type_specifier, name=identifier, clazz=clazz
            )
            self.manager.current_clazz.add_attribute(attribute)
        return f'{type_specifier} {identifier}{cells};'

    def type_specifier_to_ir_type(self, type_specifier: str):
        result = None
        match type_specifier.split():
            case 'short', 'int', *_:
                result = ir.IntType(16)
            case 'long', 'int', *_:
                result = ir.IntType(64)
            case 'long', *_:
                result = ir.IntType(64)
            case 'int', *_:
                result = ir.IntType(32)
            case 'char', *_:
                result = ir.IntType(8)

        if '*' in type_specifier:
            count = type_specifier.count('*')
            result = ir.PointerType(result)
            for i in range(count - 1):
                result = result.as_pointer()
            return result
        return result

    def visitFunctionDeclaration(self,
                                 ctx: CParser.FunctionDeclarationContext
                                 ) -> Function:
        _, rtype = self.match_type_specifier(ctx.typeSpecifier())
        identifier = ctx.identifier().getText()
        args, var_arg = self.visitFunctionArgs(ctx.functionArgs())
        # only type specifiers 1st
        ir_args = [arg[0] for arg in args]
        rtype = self.type_specifier_to_ir_type(rtype)
        func_type = ir.FunctionType(rtype, ir_args)
        func_type.var_arg = var_arg
        func = ir.Function(module, func_type, name=identifier)
        for i in range(len(func.args)):
            _, arg_identifier = args[i]
            if arg_identifier:
                func.args[i].name = arg_identifier
        self.manager.scope_stack.add_function(func)
        return func

    def visitFunctionDefinition(self, ctx: CParser.FunctionDefinitionContext):
        # typeSpecifier? identifier LP functionArgs? RP block
        self.state.visit_block_scope()
        _, rtype = self.match_type_specifier(ctx.typeSpecifier())
        identifier: str = ctx.identifier().getText()
        args, var_arg = self.visitFunctionArgs(ctx.functionArgs())
        # only type specifiers 1st
        ir_args = [arg[0] for arg in args]
        rtype = self.type_specifier_to_ir_type(rtype)
        func_type = ir.FunctionType(rtype, ir_args)
        func_type.var_arg = var_arg
        func = ir.Function(module, func_type, name=identifier)
        for i in range(len(func.args)):
            _, arg_identifier = args[i]
            if arg_identifier:
                func.args[i].name = arg_identifier
        block = func.append_basic_block(name='entry')
        builder = ir.IRBuilder(block)
        self.manager.builder = builder

        self.manager.current_function = func
        scope = Scope(ScopeType.FUNC)
        self.manager.scope_stack.push(scope)
        self.visitBlock(ctx.block())
        self.manager.current_function = None

        return func

    def visitFunctionArgs(self, ctx: CParser.FunctionArgsContext):
        if ctx is None:
            return [], False

        # check for duplicate args
        temp: dict = {}
        for child in ctx.getChildren():
            if isinstance(child, CParser.ArgContext):
                if child.identifier() is None:
                    continue
                identifier = child.identifier().getText()
                if identifier == 'this':
                    print_error(
                        'Error: can\' use`this` as an '
                        'identifier, `this` is a reserved keyword')
                    exit(-1)
                if identifier in temp:
                    print_error(
                        f'Error: duplicate function argument `{identifier}`')
                    exit(-1)
                else:
                    temp[identifier] = 1

        args = []
        var_arg = False
        # parse every arg
        for child in ctx.getChildren():
            if isinstance(child, CParser.ArgContext):
                args.append(self.visitArg(child))
            elif child.getText() == '...':
                var_arg = True

        return args, var_arg

    def visitArg(self, ctx: CParser.ArgContext):
        clazz, type_specifier = self.visitTypeSpecifier(ctx.typeSpecifier())
        type_specifier = self.type_specifier_to_ir_type(type_specifier)
        if ctx.identifier():
            return type_specifier, ctx.identifier().getText()
        return type_specifier, None

    def visitStructDeclaration(self, ctx: CParser.StructDeclarationContext):
        return f'struct {ctx.identifier().getText()};'

    def visitStructDefinition(self, ctx: CParser.StructDefinitionContext):
        self.state.visit_block_scope()
        struct_block: str = self.visitStructBlock(ctx.structBlock())
        self.state.exit_block_scope()
        return f'struct {ctx.identifier().getText()} ' \
               f'{"{"}\n{struct_block}\n{self.state.tabs}{"}"};'

    def visitStructBlock(self, ctx: CParser.StructBlockContext):
        if ctx is None:
            return ''

        result: str = ''
        for child in ctx.getChildren():
            match type(child):
                case CParser.FieldContext:
                    result += self.state.tabs
                    value = self.visitField(child)
                    result += value
                    result += '\n'
                case CParser.BitFieldContext:
                    result += self.state.tabs
                    value = self.visitBitField(child)
                    result += value
                    result += '\n'

        # [:-1] remove the last newline
        return result[:-1]

    def visitField(self, ctx: CParser.FieldContext):
        _, type_specifier = self.match_type_specifier(ctx.typeSpecifier())
        return f'{type_specifier} {ctx.identifier().getText()};'

    def visitBitField(self, ctx: CParser.BitFieldContext):
        _, type_specifier = self.match_type_specifier(ctx.typeSpecifier())
        identifier: str = ctx.identifier().getText()
        bit_count: str = ctx.INTEGER_CONSTANT()
        return f'{type_specifier} {identifier}: {bit_count};'

    def visitAssignment(self, ctx: CParser.AssignmentContext):
        identifier: str = (ctx.identifier() or ctx.chainedCall()).getText()
        variable = self.manager.scope_stack.get_variable(identifier)
        expression = self.expression_to_llvm_ir(ctx.expression())
        self.store(expression, variable)

    def visitInplaceAssignment(self, ctx: CParser.InplaceAssignmentContext):
        operator: str = (ctx.STAR_ASSIGN()
                         or ctx.DIV_ASSIGN()
                         or ctx.MOD_ASSIGN()
                         or ctx.PLUS_ASSIGN()
                         or ctx.MINUS_ASSIGN()
                         or ctx.LEFT_SHIFT_ASSIGN()
                         or ctx.RIGHT_SHIFT_ASSIGN()
                         or ctx.BITWISE_AND_ASSIGN()
                         or ctx.BITWISE_OR_ASSIGN()
                         or ctx.BITWISE_XOR_ASSIGN()).getText()

        expression: str = self.visitExpression(ctx.expression())

        try:
            identifier: str = ctx.identifier().getText()
            return f'{identifier} {operator} {expression};'
        except AttributeError:
            chained_call: str = self.visitChainedCall(ctx.chainedCall())
            return f'{chained_call} {operator} {expression};'

    def visitFuncCallExpression(self, ctx: CParser.FuncCallExpressionContext):
        unary = ''
        if ctx.unarySign():
            unary += ctx.unarySign().getText()
        return self.visitFunctionCall(ctx.functionCallExpression())
        # return f'{unary}{self.visitFunctionCal
        # l(ctx.functionCallExpression())}'

    def visitFunctionCall(self, ctx: CParser.FunctionCallContext):
        builder = self.manager.builder
        args = self.visitFunctionCallArgs(ctx.functionCallArgs())
        # TODO: load from pointers this needs more work
        for i, v in enumerate(args):
            if isinstance(v, ir.AllocaInstr):
                args[i] = builder.load(v)
        func = self.manager.scope_stack.get_function(
            ctx.identifier().getText())
        builder.call(func, args)

    def visitFunctionCallArgs(self, ctx: CParser.FunctionCallArgsContext):
        if ctx is None:
            return None

        args = []
        for child in ctx.getChildren():
            if isinstance(child, CParser.ExpressionContext):
                args.append(self.visitExpression(child))
        return args

    def visitFunctionReturn(self, ctx: CParser.FunctionReturnContext):
        expression = self.visitExpression(ctx.expression())
        if self.manager.current_function.return_value.type == expression.type:
            self.manager.builder.ret(expression)
        elif (self.manager.current_function.return_value.type.as_pointer()
              == expression.type):
            val = self.manager.builder.load(expression)
            self.manager.builder.ret(val)
        else:
            raise Exception(
                'function return type does not match function return type')

    def visitIfStatementStructure(self,
                                  ctx: CParser.IfStatementStructureContext):
        result: str = ''
        for child in ctx.getChildren():
            match type(child):
                case CParser.IfStatementContext:
                    result += self.state.tabs
                    value = self.visitIfStatement(child)
                    result += value
                    result += '\n'
                case CParser.ElseIfStatementContext:
                    result += self.state.tabs
                    value = self.visitElseIfStatement(child)
                    result += value
                    result += '\n'
                case CParser.ElseStatementContext:
                    result += self.state.tabs
                    value = self.visitElseStatement(child)
                    result += value
                    result += '\n'
        return result

    def visitIfStatement(self, ctx: CParser.IfStatementContext):
        self.state.visit_block_scope()
        conditions: list[CParser.ConditionContext] = [
            condition for condition in ctx.getChildren()
            if isinstance(condition, CParser.ConditionContext)
        ]
        values: list[str] = list(map(self.visitCondition, conditions))
        block: str = self.visitBlock(ctx.block())
        self.state.exit_block_scope()
        return f'if ({", ".join(values)}) ' \
               f'{"{"}\n {block}\n{self.state.tabs}{"}"}'

    def visitElseIfStatement(self, ctx: CParser.ElseIfStatementContext):
        if_statement: str = self.visitIfStatement(ctx.ifStatement())
        return f'else {if_statement}'

    def visitElseStatement(self, ctx: CParser.ElseStatementContext):
        self.state.visit_block_scope()
        block: str = self.visitBlock(ctx.block())
        self.state.exit_block_scope()
        return f'else {"{"}\n {block}\n{self.state.tabs}{"}"}'

    def visitWhileStatement(self, ctx: CParser.WhileStatementContext):
        self.state.visit_block_scope()
        conditions: list[CParser.ConditionContext] = [
            condition for condition in ctx.getChildren()
            if isinstance(condition, CParser.ConditionContext)
        ]
        values = list(map(self.visitCondition, conditions))
        block: str = self.visitBlock(ctx.block())
        self.state.exit_block_scope()

        return f'while ({", ".join(values)})' \
               f' {"{"}\n {block}\n{self.state.tabs}{"}"}'

    def visitDoWhileStatement(self, ctx: CParser.DoWhileStatementContext):
        self.state.visit_block_scope()
        conditions: list[CParser.ConditionContext] = [
            condition for condition in ctx.getChildren()
            if isinstance(condition, CParser.ConditionContext)
        ]
        values = list(map(self.visitCondition, conditions))
        block: str = self.visitBlock(ctx.block())
        self.state.exit_block_scope()

        return f'do {"{"}\n {block}\n{self.state.tabs}{"}"} ' \
               f'while ({", ".join(values)});'

    def visitCondition(self, ctx: CParser.ConditionContext):
        result = ''
        for child in ctx.getChildren():
            match type(child):
                case CParser.ExpressionContext:
                    result += ' ' + self.visitExpression(child)
                case _:
                    result += ' ' + child.getText()
        return result

    def visitExpression(self, ctx: CParser.ExpressionContext):
        match type(ctx):
            case CParser.IdentifierExpressionContext:
                return self.visitIdentifierExpression(ctx)
            case CParser.ConstantExpressionContext:
                return self.visitConstantExpression(ctx)
            case CParser.FuncCallExpressionContext:
                return self.visitFuncCallExpression(ctx)
            case CParser.MultiplyExpressionContext:
                return self.visitMultiplyExpression(ctx)
            case CParser.AddExpressionContext:
                return self.visitAddExpression(ctx)
            case CParser.SubtractExpressionContext:
                return self.visitSubtractExpression(ctx)
            case CParser.ConstantExpressionContext:
                return self.visitConstantExpression(ctx)
            case CParser.IdentifierExpressionContext:
                return self.visitIdentifierExpression(ctx)
            case CParser.ChainedCallExpressionContext:
                return self.visitChainedCallExpression(ctx)
            case CParser.EqExpressionContext:
                return self.visitEqExpression(ctx)
            case CParser.GtExpressionContext:
                return self.visitGtExpression(ctx)
            case CParser.GteExpressionContext:
                return self.visitGteExpression(ctx)
            case CParser.LtExpressionContext:
                return self.visitLtExpression(ctx)
            case CParser.LteExpressionContext:
                return self.visitLteExpression(ctx)
            case CParser.SizeofExpressionContext:
                return self.visitSizeofExpression(ctx)
            case _:
                raise Exception('Expression was not recognised!')

    def visitSizeofExpression(self, ctx: CParser.SizeofExpressionContext):
        return ctx.getText()

    def visitMultiplyExpression(self, ctx: CParser.MultiplyExpressionContext):
        expr1_ir = self.expression_to_llvm_ir(ctx.expression(0))
        expr2_ir = self.expression_to_llvm_ir(ctx.expression(1))
        return self.manager.builder.mul(expr1_ir, expr2_ir)

    def visitDivideExpression(self, ctx: CParser.DivideExpressionContext):
        expr1_ir = self.expression_to_llvm_ir(ctx.expression(0))
        expr2_ir = self.expression_to_llvm_ir(ctx.expression(1))
        return self.manager.builder.sdiv(expr1_ir, expr2_ir)

    def visitAddExpression(self, ctx: CParser.AddExpressionContext):
        expr1_ir = self.expression_to_llvm_ir(ctx.expression(0))
        expr2_ir = self.expression_to_llvm_ir(ctx.expression(1))
        if expr1_ir.type.is_pointer:
            expr1_ir = self.manager.builder.load(expr1_ir)
        if expr2_ir.type.is_pointer:
            expr2_ir = self.manager.builder.load(expr2_ir)
        return self.manager.builder.add(expr1_ir, expr2_ir)

    def visitSubtractExpression(self, ctx: CParser.SubtractExpressionContext):
        expr1_ir = self.expression_to_llvm_ir(ctx.expression(0))
        expr2_ir = self.expression_to_llvm_ir(ctx.expression(1))
        if expr1_ir.type.is_pointer:
            expr1_ir = self.manager.builder.load(expr1_ir)
        if expr2_ir.type.is_pointer:
            expr2_ir = self.manager.builder.load(expr2_ir)
        return self.manager.builder.sub(expr1_ir, expr2_ir)

    def visitConstantExpression(self, ctx: CParser.ConstantExpressionContext):
        constant: CParser.ConstantContext = ctx.constant()
        if isinstance(ctx.parentCtx, CParser.VariableDefinitionContext):
            if constant.INTEGER_CONSTANT():
                return ir.Constant(ir.IntType(32), ctx.getText())
            if constant.STRING_LITERAL():
                value = ctx.getText()[1:-1] + '\0'
                value = value.replace('\\n', '\n')
                string_array = ir.GlobalVariable(
                    module,
                    ir.ArrayType(ir.IntType(8), len(value)),
                    name=self.manager.slc,
                )
                string_array.linkage = 'internal'
                string_array.global_constant = True
                string_array.initializer = ir.Constant(
                    ir.ArrayType(ir.IntType(8), len(value)),
                    bytearray(value.encode()))
                # val  = ir.Constant(
                #         ir.ArrayType(ir.IntType(8), len(value)),
                #         bytearray(value.encode("utf8")))

                # fmt_str_ptr = builder.bitcast(str_ptr, ir.IntType(8))
                return string_array
        else:
            if constant.INTEGER_CONSTANT():
                return ir.Constant(ir.IntType(32), ctx.getText())
            if constant.STRING_LITERAL():
                value = ctx.getText()[1:-1] + '\0'
                value = value.replace('\\n', '\n')
                string_array = ir.GlobalVariable(
                    module,
                    ir.ArrayType(ir.IntType(8), len(value)),
                    name=self.manager.slc,
                )
                string_array.linkage = 'internal'
                string_array.global_constant = True
                string_array.initializer = ir.Constant(
                    ir.ArrayType(ir.IntType(8), len(value)),
                    bytearray(value.encode()))
                return string_array

    def visitIdentifierExpression(self,
                                  ctx: CParser.IdentifierExpressionContext):
        return self.manager.scope_stack.get_variable(ctx.getText())

    def visitChainedCallExpression(self,
                                   ctx: CParser.ChainedCallExpressionContext):
        if ctx.unarySign():
            return f'{ctx.unarySign().getText()}' \
                   f'{self.visitChainedCall(ctx.chainedCall())}'
        return self.visitChainedCall(ctx.chainedCall())

    def visitEqExpression(self, ctx: CParser.EqExpressionContext):
        exp1, exp2 = ctx.expression(0).getText(), ctx.expression(1).getText()
        obj1, obj2 = self.manager.get_obj(exp1), self.manager.get_obj(exp2)
        if obj1 and obj2:
            overridden_method = obj1.clazz.get_method('eq').alias
            return f'{obj1.name}->{overridden_method}' \
                   f'({obj1.name}, {obj2.name})'
        exp1_ir = self.expression_to_llvm_ir(ctx.expression(0))
        exp2_ir = self.expression_to_llvm_ir(ctx.expression(1))
        return self.manager.builder.icmp_signed('==', exp1_ir, exp2_ir)

    def visitGtExpression(self, ctx: CParser.GtExpressionContext):
        exp1, exp2 = ctx.expression(0).getText(), ctx.expression(1).getText()
        obj1, obj2 = self.manager.get_obj(exp1), self.manager.get_obj(exp2)
        if obj1 and obj2:
            overridden_method = obj1.clazz.get_method('gt').alias
            return f'{obj1.name}->{overridden_method}' \
                   f'({obj1.name}, {obj2.name})'
        return ctx.getText()

    def visitGteExpression(self, ctx: CParser.GteExpressionContext):
        exp1, exp2 = ctx.expression(0).getText(), ctx.expression(1).getText()
        obj1, obj2 = self.manager.get_obj(exp1), self.manager.get_obj(exp2)
        if obj1 and obj2:
            overridden_method = obj1.clazz.get_method('gte').alias
            return f'{obj1.name}->{overridden_method}' \
                   f'({obj1.name}, {obj2.name})'
        return ctx.getText()

    def visitLtExpression(self, ctx: CParser.LtExpressionContext):
        exp1, exp2 = ctx.expression(0).getText(), ctx.expression(1).getText()
        obj1, obj2 = self.manager.get_obj(exp1), self.manager.get_obj(exp2)
        if obj1 and obj2:
            overridden_method = obj1.clazz.get_method('lt').alias
            return f'{obj1.name}->{overridden_method}' \
                   f'({obj1.name}, {obj2.name})'
        return ctx.getText()

    def visitLteExpression(self, ctx: CParser.LteExpressionContext):
        exp1, exp2 = ctx.expression(0).getText(), ctx.expression(1).getText()
        obj1, obj2 = self.manager.get_obj(exp1), self.manager.get_obj(exp2)
        if obj1 and obj2:
            overridden_method = obj1.clazz.get_method('lte').alias
            return f'{obj1.name}->{overridden_method}' \
                   f'({obj1.name}, {obj2.name})'
        return ctx.getText()

    def visitLeftShiftExpression(self,
                                 ctx: CParser.LeftShiftExpressionContext):
        expr1, expr2 = ctx.expression(0), ctx.expression(1)
        # parsing expr should return info about the operands
        # result: str, expr1: class?,
        # expr2: class? probably expr2 is not needed
        if isinstance(expr1, CParser.LeftShiftExpressionContext):
            _result, _obj1 = self.visitLeftShiftExpression(expr1)
            if _obj1:
                if isinstance(expr2, CParser.IdentifierExpressionContext):
                    obj2 = self.manager.get_obj(expr2.getText())
                    overridden_method = obj2.clazz.get_method('lshift').alias
                    result: str = f'{_result}->{overridden_method}' \
                                  f'({_obj1.name}, {obj2.name})'
                    return result, _obj1
        obj1 = self.manager.get_obj(expr1.getText())
        obj2 = self.manager.get_obj(expr2.getText())
        if obj1 and obj2:
            overridden_method = obj1.clazz.get_method('lshift').alias
            result: str = f'{obj1.name}->{overridden_method}' \
                          f'({obj1.name}, {obj2.name})'
            return result, obj1
        return ctx.getText(), None

    def visitBlock(self, ctx: CParser.BlockContext):
        for child in ctx.getChildren():
            match type(child):
                case CParser.DeclarationListContext:
                    for declaration in child.getChildren():
                        match type(declaration):
                            case CParser.VariableDeclarationContext:
                                self.visitVariableDeclaration(declaration)
                            case CParser.StructDeclarationContext:
                                self.visitStructDeclaration(declaration)
                case CParser.DefinitionListContext:
                    for definition in child.getChildren():
                        match type(definition):
                            case CParser.VariableDefinitionContext:
                                self.visitVariableDefinition(definition)
                            case CParser.StructDefinitionContext:
                                self.visitStructDefinition(definition)
                case CParser.StatementListContext:
                    for statement in child.getChildren():
                        match type(statement):
                            case CParser.ExpressionContext:
                                self.visitExpression(statement)
                            case CParser.FuncCallExpressionContext:
                                self.visitFuncCallExpression(statement)
                            case CParser.ChainedCallExpressionContext:
                                self.visitChainedCallExpression(statement)
                            case CParser.IfStatementStructureContext:
                                self.visitIfStatementStructure(statement)
                            case CParser.AssignmentContext:
                                self.visitAssignment(statement)
                            case CParser.InplaceAssignmentContext:
                                self.visitInplaceAssignment(statement)
                            case CParser.VariableDefinitionContext:
                                self.visitVariableDefinition(statement)
                            case CParser.FunctionReturnContext:
                                self.visitFunctionReturn(statement)
                            case CParser.LeftShiftExpressionContext:
                                self.visitLeftShiftExpression(statement)
                            case antlr4.tree.Tree.TerminalNodeImpl:
                                # this is the `;`
                                pass
                            case _:
                                print(type(statement))
                                raise Exception(
                                    'Statement was not recognized!')
                case CParser.ClassInstantiationContext:
                    self.visitClassInstantiation(child)

    def exitBlock(self, ctx: CParser.BlockContext):
        self.state.exit_block_scope()

    def visitClassDefinition(self, ctx: CParser.ClassDefinitionContext):
        self.state.visit_block_scope()
        self.state.visit_class()
        identifier: str = ctx.identifier().getText()
        clazz: Clazz = Clazz(
            name=identifier,
            alias=None,
        )
        self.manager.current_clazz = clazz
        self.manager.add_clazz(clazz)
        attributes, methods, method_declarations = self.visitClassBlock(
            ctx.classBlock())
        self.state.exit_class()
        self.state.exit_block_scope()
        # self.manager.current_clazz = None
        return f'typedef struct {identifier} {"{"}\n {attributes}\n{"}"}' \
               f' {identifier};\n\n{method_declarations}\n{methods}'

    def getFunctionPointer(self, class_name: str,
                           function: CParser.ClassMethodContext):
        clazz, rtype = self.match_type_specifier(
            function.typeSpecifier())
        if clazz:
            rtype = f'struct {rtype}'

        identifier: str = function.identifier().getText()

        # struct {class_name} * this: is always the 1st arg
        # except for the constructor bc it creates the object reference
        if function.identifier().getText() == class_name:
            args: list[Arg] = []
        else:
            this = f'struct {class_name} *'
            args: list[Arg] = [
                Arg(name=None, type_specifier=this, clazz=clazz)]
        if function.functionArgs():
            for arg in function.functionArgs().getChildren():
                try:
                    clazz, type_specifier = self.match_type_specifier(
                        arg.typeSpecifier())
                    if clazz:
                        type_specifier = f'struct {type_specifier}'
                        arg = Arg(name=None, type_specifier=type_specifier,
                                  clazz=clazz)
                    else:
                        arg = Arg(name=None, type_specifier=type_specifier,
                                  clazz=clazz)
                    args.append(arg)
                except AttributeError:
                    # skip, it is not a func arg
                    continue
        new_args: list[str] = []
        for arg in args:
            new_args.append(arg.type_specifier)
        return f'{rtype} (*{class_name}{identifier})({", ".join(new_args)});'

    def createClassConstructor(self,
                               constructor: CParser.ClassMethodContext | None,
                               methods: list[Function]):

        clazz_name: str = self.manager.current_clazz.name
        if constructor:
            method_name: str = constructor.identifier().getText()
            method_alias: str = f'{clazz_name}{method_name}'
            args, args_string = self.visitFunctionArgs(
                constructor.functionArgs())
            # args_string = ', '.join([f'{clazz_name} * this', args_string])

            method: Function = Function(
                rtype='void',
                name=method_name,
                alias=method_alias,
                args=args,
            )
            self.manager.current_clazz.constructor = method
            self.manager.current_clazz.add_method(method)
            method_block: str = ''
            # `this` malloc is implicit bc it has to be hmmm
            method_block += f'{self.state.tabs}{clazz_name}* this =' \
                            f' malloc(sizeof({clazz_name}));\n'
            method_block += f'{self.state.tabs}this->{clazz_name * 2} = ' \
                            f'&{clazz_name * 2};\n'
            for method in methods:
                if method.name == clazz_name:
                    continue
                name: str = method.name
                new_name: str = f'{clazz_name}{name}'
                method_block += f'{self.state.tabs}' \
                                f'this->{new_name} = &{new_name};\n'
            method_block += self.visitBlock(constructor.block())
            return f'{clazz_name}* {method_alias}({args_string})' \
                   f' {"{"}\n{method_block}\n{"}"}'

        else:
            return f'{clazz_name}* {clazz_name}{clazz_name}' \
                   f'() {"{"}\n// Not implemented\n{"}"}'

    def createClassStringRepresentation(self, clazz_name):
        string = f'<{clazz_name} object at 0xFFFFFFF>\n'
        result: str = f'char * {clazz_name}' \
                      f'toString({clazz_name} * this) {"{"}\n' \
                      f'\tchar * str = ' \
                      f'malloc(sizeof(char *) * {len(string)});\n' \
                      f'\tsprintf(str, ' \
                      f'"<{clazz_name} object at %p>\\n", this);\n' \
                      f'\treturn str;\n' \
                      '}\n'
        return result

    def methodDefinitionToMethodDeclaretion(self,
                                            class_name: str,
                                            method: CParser.ClassMethodContext
                                            ):
        pass
        # ptr = self.getFunctionPointer(class_name, method)
        # matches = re.match(
        #     '(?P<rtype>.*?)\(\*(?P<alias>.*)\)(?P<args>\(.*\))'
        #     , ptr)
        # rtype = matches.group('rtype')
        # alias = matches.group('alias')
        # args = matches.group('args')
        # return f'{rtype}{alias}{args};'

    def visitClassBlock(self, ctx: CParser.ClassBlockContext):
        class_name: str = ctx.parentCtx.identifier().getText()
        attribute_declarations: list[CParser.VariableDeclarationContext] = []
        attribute_definitions: list[CParser.VariableDefinitionContext] = []
        methods: list[CParser.ClassMethodContext] = []

        for child in ctx.getChildren():
            match type(child):
                case CParser.VariableDeclarationContext:
                    attribute_declarations.append(child)
                case CParser.VariableDefinitionContext:
                    attribute_definitions.append(child)
                case CParser.ClassMethodContext:
                    methods.append(child)

        attributes: str = ''

        for attribute in attribute_declarations:
            attributes += self.state.tabs
            value = self.visitVariableDeclaration(attribute,
                                                  is_clazz_attribute=True)
            attributes += value
            attributes += '\n'

        # attribute definition is quite tricky to handle
        # it has to be split into declaration and initialization
        # in the class constructor
        for attribute in attribute_definitions:
            attributes += self.state.tabs
            value = self.visitVariableDefinition(attribute)
            attributes += value
            attributes += '\n'

        parsed_methods: str = ''
        constructor: CParser.ClassMethodContext | None = None

        overridden_magic_methods = {'toString': False}

        clean_methods: list[Function] = []

        method: CParser.ClassMethodContext
        for method in methods:
            # print(self.visitFunctionArgs(method.functionArgs()))
            # print(method.getText())
            method_name = method.identifier().getText()
            if method_name == class_name:
                constructor = method
                attributes += self.state.tabs
                attributes += self.getFunctionPointer(class_name, constructor)
                attributes += '\n'
                continue
            elif method_name == 'toString':
                overridden_magic_methods['toString'] = True

            function_pointer = self.getFunctionPointer(class_name, method)
            attributes += self.state.tabs
            attributes += function_pointer
            attributes += '\n'
            self.state.exit_block_scope()
            self.state.exit_block_scope()
            func, func_string = self.visitClassMethod(method)
            clean_methods.append(func)
            # self.manager.current_clazz.add_method(func)
            self.state.visit_block_scope()
            parsed_methods += func_string
            parsed_methods += '\n'

        # MAGIC METHODS GO HERE
        for k, v in overridden_magic_methods.items():
            match k, v:
                case 'toString', False:
                    # create string representation
                    attributes += self.state.tabs
                    # need function pointer
                    attributes += f'char * (*{class_name}toString)' \
                                  f'(struct {class_name} *);'
                    attributes += '\n'
                    to_string = self.createClassStringRepresentation(
                        class_name)
                    parsed_methods += to_string
                    method: Function = Function(
                        rtype='char *',
                        name='toString',
                        args=Arg(
                            type_specifier=f'{class_name} *',
                            name='this',
                            clazz=self.manager.get_clazz(class_name),
                        ),
                        alias=f'{class_name}toString')
                    clean_methods.append(method)
                    self.manager.current_clazz.add_method(method)

        # TODO: urgent this has to be all Function instance in class
        #  constructor
        parsed_constructor = self.createClassConstructor(constructor,
                                                         clean_methods)
        parsed_methods = parsed_constructor + '\n' + parsed_methods

        # so other methods can have access to each other
        method_declarations: str = ''
        for method in methods:
            method_declaration = self.methodDefinitionToMethodDeclaretion(
                class_name, method)
            method_declarations += method_declaration
            method_declarations += '\n'
        return attributes[:-1], parsed_methods, method_declarations

    def visitClassMethod(self, ctx: CParser.ClassMethodContext):
        original_identifier: str = ctx.identifier().getText()
        # class ctx -> class block ctx -> class method ctx
        clazz_name = ctx.parentCtx.parentCtx.identifier().getText()
        alias = f'{clazz_name}{original_identifier}'
        args, args_string = self.visitFunctionArgs(ctx.functionArgs())

        if args_string:
            args_string = ', '.join([f'{clazz_name} * this', args_string])
        else:
            args_string = f'{clazz_name} * this'

        obj_ref_arg = Arg(
            type_specifier=f'{clazz_name} *',
            name='this',
            clazz=self.manager.get_clazz(clazz_name)
        )
        args.insert(0, obj_ref_arg)
        rtype = ctx.typeSpecifier().getText()
        method: Function = Function(
            rtype=rtype,
            name=original_identifier,
            args=args,
            alias=alias,
        )
        self.state.visit_block_scope()
        block = self.visitBlock(ctx.block())
        self.state.exit_block_scope()
        self.manager.current_clazz.add_method(method)
        return method, f'{rtype} {alias}({args_string}) ' \
                       f'{"{"}\n {block}\n{self.state.tabs}{"}"}'

    def visitClassInstantiation(self, ctx: CParser.ClassInstantiationContext):
        clazz, type_specifier = self.match_type_specifier(ctx.typeSpecifier())
        class_name: str = type_specifier.split()[0]  # to remove the pointer
        identifier: str = ctx.identifier().getText()
        args: str = self.visitFunctionCallArgs(
            ctx.functionCall().functionCallArgs())
        obj: Obj = Obj(name=identifier, clazz=clazz)
        self.manager.add_obj(obj)
        result: str = f'{type_specifier} {identifier} =' \
                      f' {class_name}{class_name}({args});'
        return result

    def visitChainedCall(self, ctx: CParser.ChainedCallContext):
        obj_name: str = ctx.identifier(0).getText()
        obj: Obj = self.manager.get_obj(obj_name)
        if obj is not None:
            result: str = ''
            # this is to check if you are accessing nested attributes
            # so it would reference it like this:
            # Pizza * pizza = new Pizza()
            # pizza->topping->get_name() should be
            # pizza->topping.get_name(pizza->topping)
            # instead of pizza->topping.get_name(topping)
            # which might not exist outside the class
            is_nested: bool = False
            original_ref: str = obj_name
            for child in ctx.getChildren():
                match type(child):
                    case CParser.FunctionCallExpressionContext:
                        method: Function = obj.clazz.get_method(
                            child.identifier().getText())
                        args: str = self.visitFunctionCallArgs(
                            child.functionCallArgs())
                        if args:
                            if is_nested:
                                result += f'{method.alias}({original_ref}' \
                                          f'->{obj.name}, {args})'
                            else:
                                result += f'{method.alias}({obj.name}, {args})'
                        else:
                            if is_nested:
                                result += f'{method.alias}' \
                                          f'({original_ref}->{obj.name})'
                            else:
                                result += f'{method.alias}({obj.name})'
                    case CParser.IdentifierContext:
                        try:
                            attribute = obj.clazz.get_attribute(
                                child.getText())
                            if attribute.clazz:
                                # this means it is an object attribute
                                obj = attribute
                                is_nested = True
                        except NameError:
                            pass
                        result += child.getText()
                    case _:
                        result += child.getText()
            return result
        elif self.manager.current_function:
            result: str = ''
            if obj_name == 'this':
                clazz: Clazz = self.manager.current_clazz
                for child in ctx.getChildren():
                    match type(child):
                        case CParser.FunctionCallContext:
                            method: Function = clazz.get_method(
                                child.identifier().getText())
                            args: str = self.visitFunctionCallArgs(
                                child.functionCallArgs())
                            if args:
                                result += f'{method.alias}({obj.name}, {args})'
                            else:
                                result += f'{method.alias}({obj.name})'
                        case CParser.IdentifierContext:
                            # if not function call it must be an attribute
                            result += child.getText()
                        case _:
                            result += child.getText()
                return result
            else:
                arg: Arg = self.manager.current_function.get_arg(obj_name)
                for child in ctx.getChildren():
                    if isinstance(child,
                                  CParser.FunctionCallExpressionContext):
                        method: Function = arg.clazz.get_method(
                            child.identifier().getText())
                        args: str = self.visitFunctionCallArgs(
                            child.functionCallArgs())
                        if args:
                            result += f'{method.alias}({obj_name}, {args})'
                        else:
                            result += f'{method.alias}({obj_name})'
                    else:
                        result += child.getText()
                return result
        else:
            return ctx.getText()
