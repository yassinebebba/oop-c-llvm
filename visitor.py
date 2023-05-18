from io import FileIO

import antlr4.tree.Tree
import llvmlite.ir as ir
from termcolor import colored

from core.CParser import CParser
from core.CVisitor import CVisitor
from manager import Manager
from manager import ClazzMap
from manager import Scope
from manager import ScopeType

# Create a module
module = ir.Module(name="main")
module.triple = "x86_64-redhat-linux-gnu"

i8 = ir.IntType(8)
i16 = ir.IntType(16)
i32 = ir.IntType(32)
i64 = ir.IntType(64)


def print_error(error: str):
    print(colored(error, 'red'))


class Visitor(CVisitor):
    def __init__(self, stream, output):
        # steam is CommonTokenStream to get hidden channel
        self.stream = stream
        self.output: FileIO = output
        self.manager = Manager()

    def write(self, text: str):
        self.output.write(text)

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
        type_specifier: list[str] = []
        for terminal_node in ctx.getChildren():
            match terminal_node.getText():
                case 'unsigned':
                    type_specifier.append('unsigned')
                case 'signed':
                    type_specifier.append('signed')
                case 'void':
                    type_specifier.append('void')
                case 'char':
                    type_specifier.append('char')
                case 'short':
                    type_specifier.append('short')
                case 'int':
                    type_specifier.append('int')
                case 'long':
                    type_specifier.append('long')
                case 'float':
                    type_specifier.append('float')
                case 'double':
                    type_specifier.append('double')
                case '*':
                    type_specifier.append('*')
                case _identifier:
                    type_specifier.append(_identifier)

        match type_specifier:
            case 'void', *ptr_count:
                t = ir.VoidType()
                for _ in ptr_count:
                    t = ir.PointerType(t)
                return t
            case 'char', *ptr_count:
                t = i8
                for _ in ptr_count:
                    t = ir.PointerType(t)
                return t
            case 'short', 'int', *ptr_count:
                t = i16
                for _ in ptr_count:
                    t = ir.PointerType(t)
                return t
            case 'short', *ptr_count:
                t = i16
                for _ in ptr_count:
                    t = ir.PointerType(t)
                return t
            case 'int', *ptr_count:
                t = i32
                for _ in ptr_count:
                    t = ir.PointerType(t)
                return t
            case 'long', 'int', *ptr_count:
                t = i64
                for _ in ptr_count:
                    t = ir.PointerType(t)
                return t
            case 'long', 'long', 'int', *ptr_count:
                t = i64
                for _ in ptr_count:
                    t = ir.PointerType(t)
                return t
            case 'long', 'long', *ptr_count:
                t = i64
                for _ in ptr_count:
                    t = ir.PointerType(t)
                return t
            case 'long', *ptr_count:
                t = i64
                for _ in ptr_count:
                    t = ir.PointerType(t)
                return t
            case clazz_name, *ptr_count:
                clazz_name = f'class.{clazz_name}'
                if clazz_name not in module.context.identified_types:
                    print_error(f'Class \'{clazz_name.split(".")[1]}\''
                                ' does not exist!')
                    exit(1)
                t = module.context.get_identified_type(clazz_name)

                for _ in ptr_count:
                    t = ir.PointerType(t)
                return t

                # if cls := self.manager.get_clazz(clazz_name):
                #     return cls
                # print_error('Type was not recognized!')

    def gplp(self, ptr: ir.PointerType):
        # get pointer level and pointee
        ptr_level = 0
        ptr_type = ptr
        while isinstance(ptr_type, ir.PointerType):
            ptr_level += 1
            ptr_type = ptr_type.pointee
        return ptr_type, ptr_level

    def store(self, value, ptr):
        builder = self.manager.builder
        match type(ptr), type(value):
            case ir.AllocaInstr, ir.Constant:
                # check if ptr is pointer
                match type(ptr.type), type(value.type):
                    case ir.PointerType, ir.PointerType:
                        print('1: Not implemented yet!')
                    case ir.PointerType, ir.IntType:
                        # get count of pointer level
                        ptr_type, ptr_level = self.gplp(ptr.type)
                        # check if ptr_type is int
                        if isinstance(ptr_type, ir.IntType):
                            # check if ptr_level is 1
                            if ptr_level == 1:
                                # check if ptr_type width is less than value width
                                if ptr_type.width < value.type.width:
                                    # truncate value
                                    value = builder.trunc(value, ptr_type)
                                    # store truncated value
                                    return builder.store(value, ptr)
                                elif ptr_type.width > value.type.width:
                                    # extend value
                                    value = builder.sext(value, ptr_type)
                                    # store extended value
                                    return builder.store(value, ptr)
                                else:
                                    return builder.store(value, ptr)

                            else:
                                return print_error('Incompatible integer to '
                                                   'pointer conversion '
                                                   'initializing `ptr` with an'
                                                   ' expression of type `int`')
                        print('2: Not implemented yet!')

            case ir.AllocaInstr, ir.GlobalVariable:
                # check global variable type is string
                ptr_type, ptr_level = self.gplp(ptr.type)
                if isinstance(value.value_type, ir.ArrayType):
                    if ptr_level >= 2:
                        start_ptr = value.gep([i64(0), i64(0)])
                        start_ptr = builder.bitcast(
                            start_ptr,
                            ptr.type.pointee
                        )
                        return builder.store(start_ptr, ptr)

                    else:
                        return print_error('Incompatible pointer to integer '
                                           'conversion initializing \'int\' '
                                           'with an expression of type '
                                           f'\'char[{value.value_type.count}]\'')
                # print(ptr.type, '\n\t', value.type)
                # print(type(ptr.type), '\n\t', value.value_type)
                print('3: Not implemented yet!')
            case ir.AllocaInstr, ir.AllocaInstr:
                ptr_type, ptr_level = self.gplp(ptr.type)
                value_type, value_level = self.gplp(value.type)
                if ptr_level == value_level:
                    # load value because it is alloca instruction
                    value = builder.load(value)
                    if ptr_type.width < value_type.width:
                        value = builder.trunc(value, ptr_type)
                        return builder.store(value, ptr)
                    elif ptr_type.width > value_type.width:
                        value = builder.sext(value, ptr_type)
                        return builder.store(value, ptr)
                    else:
                        return builder.store(value, ptr)
                print('4: Not implemented yet!')
            case ir.AllocaInstr, ir.Instruction:
                ptr_type, ptr_level = self.gplp(ptr.type)
                value_type, value_level = self.gplp(value.type)
                match type(ptr_type), type(value_type):
                    case ir.IntType, ir.IntType:
                        if ptr_type.width < value_type.width:
                            value = builder.trunc(value, ptr_type)
                            return builder.store(value, ptr)
                        elif ptr_type.width > value_type.width:
                            value = builder.sext(value, ptr_type)
                            return builder.store(value, ptr)
                        else:
                            return builder.store(value, ptr)
                print('5: Not implemented yet!')
            case _, _:
                # print(type(ptr), '\n\t', type(value))
                # print(ptr.type, '\n\t', value.type)
                print('default: Not implemented yet!')

    def visitVariableDefinition(self, ctx: CParser.VariableDefinitionContext):
        type_specifier = self.visitTypeSpecifier(ctx.typeSpecifier())
        identifier = ctx.identifier().getText()
        expression = self.visitExpression(ctx.expression())
        if self.manager.scope_stack.is_global_scope():
            variable = ir.GlobalVariable(module, type_specifier,
                                         name=identifier)
            variable.initializer = expression
            variable.linkage = 'dso_local'
            self.manager.add_variable(variable)
            return variable
        else:
            builder = self.manager.builder
            variable = builder.alloca(type_specifier, name=identifier)
            self.manager.add_variable(variable)
            self.store(expression, variable)
            return variable

    def visitVariableDeclaration(self,
                                 ctx: CParser.VariableDeclarationContext,
                                 is_clazz_attribute: bool = False):
        type_specifier = self.visitTypeSpecifier(ctx.typeSpecifier())
        identifier = ctx.identifier().getText()
        if self.manager.scope_stack.is_global_scope():
            variable = ir.GlobalVariable(module, type_specifier,
                                         name=identifier)
            variable.initializer = ir.Constant(type_specifier, 0)
            variable.linkage = 'dso_local'
            self.manager.add_variable(variable)
            return variable
        else:
            builder = self.manager.builder
            variable = builder.alloca(type_specifier, name=identifier)
            self.manager.add_variable(variable)
            return variable

    def visitFunctionDeclaration(self,
                                 ctx: CParser.FunctionDeclarationContext):
        rtype = self.visitTypeSpecifier(ctx.typeSpecifier())
        identifier = ctx.identifier().getText()
        args, var_arg = self.visitFunctionArgs(ctx.functionArgs())
        # only type specifiers 1st
        ir_args = [arg[0] for arg in args]
        func_type = ir.FunctionType(rtype, ir_args)
        func_type.var_arg = var_arg
        func = ir.Function(module, func_type, name=identifier)
        for i in range(len(func.args)):
            _, arg_identifier = args[i]
            if arg_identifier:
                func.args[i].name = arg_identifier
        self.manager.add_function(func)
        return func

    def visitFunctionDefinition(self, ctx: CParser.FunctionDefinitionContext):
        rtype = self.visitTypeSpecifier(ctx.typeSpecifier())
        identifier: str = ctx.identifier().getText()
        args, var_arg = self.visitFunctionArgs(ctx.functionArgs())
        # only type specifiers 1st
        ir_args = [arg[0] for arg in args]
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
        self.manager.push_scope(scope)
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
        type_specifier = self.visitTypeSpecifier(ctx.typeSpecifier())
        if ctx.identifier():
            return type_specifier, ctx.identifier().getText()
        return type_specifier, None

    def visitStructDeclaration(self, ctx: CParser.StructDeclarationContext):
        raise NotImplementedError

    def visitStructDefinition(self, ctx: CParser.StructDefinitionContext):
        self.visitStructBlock(ctx.structBlock())
        raise NotImplementedError

    def visitStructBlock(self, ctx: CParser.StructBlockContext):
        if ctx is None:
            return None
        for child in ctx.getChildren():
            match type(child):
                case CParser.FieldContext:
                    self.visitField(child)
                case CParser.BitFieldContext:
                    self.visitBitField(child)
        raise NotImplementedError

    def visitField(self, ctx: CParser.FieldContext):
        _, type_specifier = self.visitTypeSpecifier(ctx.typeSpecifier())
        return f'{type_specifier} {ctx.identifier().getText()};'

    def visitBitField(self, ctx: CParser.BitFieldContext):
        _, type_specifier = self.visitTypeSpecifier(ctx.typeSpecifier())
        identifier: str = ctx.identifier().getText()
        bit_count: str = ctx.INTEGER_CONSTANT()
        return f'{type_specifier} {identifier}: {bit_count};'

    def visitAssignment(self, ctx: CParser.AssignmentContext):
        if ctx.identifier():
            identifier: str = ctx.identifier().getText()
            variable = self.manager.get_variable(identifier)
            expression = self.visitExpression(ctx.expression())
            self.store(expression, variable)
        elif ctx.chainedCall():
            chain: CParser.ChainedCallContext = ctx.chainedCall()
            identifier: str = chain.identifier(0).getText()
            obj = self.manager.get_variable(identifier)
            builder = self.manager.builder
            try:
                # this is if allocated so pointee is needed
                elements = obj.type.pointee.elements
                clazz_map: ClazzMap = obj.type.pointee.map
            except AttributeError:
                # this is if like it is in func args
                elements = obj.type.elements
                clazz_map: ClazzMap = obj.type.map
            attribute = None

            for child in chain.children[1:]:
                if isinstance(child, CParser.IdentifierContext):
                    identifier = child.getText()
                    for element, name in zip(elements, clazz_map.attributes):
                        if name == identifier:
                            try:
                                # this is if allocated so pointee is needed
                                idx = [
                                    i32(0),
                                    i32(clazz_map.attributes[name]['index'])
                                ]
                                attribute = builder.gep(obj, idx)
                            except AttributeError:
                                # this is if like it is in func args
                                attribute = obj.type.gep(i32(0))
                            break
                    else:
                        print_error(
                            f'AttributeError: \'{obj.name}\' object has'
                            f' no attribute \'{identifier}\'')
                        exit(1)
            expression = self.visitExpression(ctx.expression())
            self.store(expression, attribute)
        else:
            print_error('Assignment was not recognized')

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

    def visitFunctionCall(self, ctx: CParser.FunctionCallContext):
        builder = self.manager.builder
        args = self.visitFunctionCallArgs(ctx.functionCallArgs())
        # TODO: load from pointers this needs more work
        for i, v in enumerate(args):
            if isinstance(v, ir.AllocaInstr):
                args[i] = builder.load(v)
        func = self.manager.get_function(
            ctx.identifier().getText())

        # this code below fixes errors like this
        # TypeError: Type of #1 arg mismatch: i8* != [4 x i8]*
        for (i, arg_type), arg in zip(enumerate(func.args), args):
            if isinstance(arg.type.pointee, ir.ArrayType):
                if arg.type.pointee.element == i8 \
                        and arg_type.type == i8.as_pointer():
                    start_ptr = args[i].gep([i64(0), i64(0)])
                    start_ptr = builder.bitcast(
                        start_ptr,
                        i8.as_pointer()
                    )
                    args[i] = start_ptr

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
        func = self.manager.current_function
        if expression is None:
            self.manager.builder.ret_void()
        elif func.return_value.type == expression.type:
            self.manager.builder.ret(expression)
        elif func.return_value.type.as_pointer() == expression.type:
            val = self.manager.builder.load(expression)
            self.manager.builder.ret(val)
        elif isinstance(expression, ir.GlobalVariable):
            if isinstance(expression.type, ir.PointerType):
                if isinstance(expression.type.pointee, ir.ArrayType):
                    expr_type = expression.type.pointee.element.as_pointer()
                    if func.return_value.type == i8.as_pointer() == expr_type:
                        start_ptr = expression.gep([i64(0), i64(0)])
                        start_ptr = self.manager.builder.bitcast(
                            start_ptr,
                            i8.as_pointer()
                        )
                        self.manager.builder.ret(start_ptr)
        else:
            # TODO: this code down below was not reviewed
            print(ctx.getText())
            temp = self.castType(expression, func.return_value)
            self.manager.builder.ret(temp)

    def visitIfStatementStructure(self,
                                  ctx: CParser.IfStatementStructureContext):
        for child in ctx.getChildren():
            match type(child):
                case CParser.IfStatementContext:
                    self.visitIfStatement(child)
                case CParser.ElseIfStatementContext:
                    self.visitElseIfStatement(child)
                case CParser.ElseStatementContext:
                    self.visitElseStatement(child)
        raise NotImplementedError

    def visitIfStatement(self, ctx: CParser.IfStatementContext):
        conditions: list[CParser.ConditionContext] = [
            condition for condition in ctx.getChildren()
            if isinstance(condition, CParser.ConditionContext)
        ]
        map(self.visitCondition, conditions)
        self.visitBlock(ctx.block())
        raise NotImplementedError

    def visitElseIfStatement(self, ctx: CParser.ElseIfStatementContext):
        if_statement: str = self.visitIfStatement(ctx.ifStatement())
        return f'else {if_statement}'

    def visitElseStatement(self, ctx: CParser.ElseStatementContext):
        self.visitBlock(ctx.block())
        raise NotImplementedError

    def visitWhileStatement(self, ctx: CParser.WhileStatementContext):
        conditions: list[CParser.ConditionContext] = [
            condition for condition in ctx.getChildren()
            if isinstance(condition, CParser.ConditionContext)
        ]
        map(self.visitCondition, conditions)
        self.visitBlock(ctx.block())
        raise NotImplementedError

    def visitDoWhileStatement(self, ctx: CParser.DoWhileStatementContext):
        conditions: list[CParser.ConditionContext] = [
            condition for condition in ctx.getChildren()
            if isinstance(condition, CParser.ConditionContext)
        ]
        map(self.visitCondition, conditions)
        self.visitBlock(ctx.block())
        raise NotImplementedError

    def visitCondition(self, ctx: CParser.ConditionContext):
        result = ''
        for child in ctx.getChildren():
            match type(child):
                case CParser.ExpressionContext:
                    result += ' ' + self.visitExpression(child)
                case _:
                    result += ' ' + child.getText()
        return result

    def visitExpression(self, ctx):
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
                # should be empty return?
                return None

    def visitSizeofExpression(self, ctx: CParser.SizeofExpressionContext):
        return ctx.getText()

    def visitMultiplyExpression(self, ctx: CParser.MultiplyExpressionContext):
        expr1_ir = self.visitExpression(ctx.expression(0))
        expr2_ir = self.visitExpression(ctx.expression(1))
        return self.manager.builder.mul(expr1_ir, expr2_ir)

    def visitDivideExpression(self, ctx: CParser.DivideExpressionContext):
        expr1_ir = self.visitExpression(ctx.expression(0))
        expr2_ir = self.visitExpression(ctx.expression(1))
        return self.manager.builder.sdiv(expr1_ir, expr2_ir)

    def visitAddExpression(self, ctx: CParser.AddExpressionContext):
        expr1_ir = self.visitExpression(ctx.expression(0))
        expr2_ir = self.visitExpression(ctx.expression(1))
        if expr1_ir.type.is_pointer:
            expr1_ir = self.manager.builder.load(expr1_ir)
        if expr2_ir.type.is_pointer:
            expr2_ir = self.manager.builder.load(expr2_ir)

        # TODO: this code works for now
        expr1_ir, expr2_ir = self.promoteType(expr1_ir, expr2_ir)
        return self.manager.builder.sub(expr1_ir, expr2_ir)

    def visitSubtractExpression(self, ctx: CParser.SubtractExpressionContext):
        expr1_ir = self.visitExpression(ctx.expression(0))
        expr2_ir = self.visitExpression(ctx.expression(1))
        if expr1_ir.type.is_pointer:
            expr1_ir = self.manager.builder.load(expr1_ir)
        if expr2_ir.type.is_pointer:
            expr2_ir = self.manager.builder.load(expr2_ir)

        # TODO: this code works for now
        expr1_ir, expr2_ir = self.promoteType(expr1_ir, expr2_ir)
        return self.manager.builder.sub(expr1_ir, expr2_ir)

    def visitConstantExpression(self, ctx: CParser.ConstantExpressionContext):
        constant: CParser.ConstantContext = ctx.constant()
        if constant.INTEGER_CONSTANT():
            value = constant.INTEGER_CONSTANT()
            sign = 0
            if (constant.unarySign()):
                for i in constant.unarySign().getText():
                    if i == '+':
                        sign += 1
                    if i == '-':
                        sign -= 1
            if sign == 1:
                return i32(f'-{value}')
            else:
                return i32(value)
        if constant.STRING_LITERAL():
            value = ctx.getText()

            chunks: list[str] = []
            temp: str = ''
            inside = False

            for i in value:
                if i == '"':
                    try:
                        if temp[-1] == '\\':
                            temp += i
                            continue
                    except IndexError:
                        pass
                    if not inside:
                        inside = True
                    else:
                        inside = False
                        chunks.append(temp)
                        temp = ''
                    continue
                if inside:
                    temp += i

            value = ''.join(chunks) + '\0'
            value = value.replace('\\n', '\n')
            string_array = ir.GlobalVariable(
                module,
                ir.ArrayType(i8, len(value)),
                name=self.manager.slc,
            )
            string_array.unnamed_addr = True
            string_array.linkage = 'private'
            string_array.global_constant = True
            string_array.initializer = ir.Constant(
                ir.ArrayType(i8, len(value)),
                bytearray(value.encode()))

            return string_array

    def visitIdentifierExpression(self,
                                  ctx: CParser.IdentifierExpressionContext):
        return self.manager.get_variable(ctx.getText())

    def visitChainedCallExpression(self,
                                   ctx: CParser.ChainedCallExpressionContext):
        if ctx.unarySign():
            return self.manager.builder.neg(
                self.visitChainedCall(ctx.chainedCall()))
        return self.visitChainedCall(ctx.chainedCall())

    def visitEqExpression(self, ctx: CParser.EqExpressionContext):
        exp1, exp2 = ctx.expression(0).getText(), ctx.expression(1).getText()
        obj1 = self.manager.get_variable(exp1)
        obj2 = self.manager.get_variable(exp2)
        if obj1 and obj2:
            overridden_method = obj1.clazz.get_method('eq').alias
            return f'{obj1.name}->{overridden_method}' \
                   f'({obj1.name}, {obj2.name})'
        exp1_ir = self.visitExpression(ctx.expression(0))
        exp2_ir = self.visitExpression(ctx.expression(1))
        return self.manager.builder.icmp_signed('==', exp1_ir, exp2_ir)

    def visitGtExpression(self, ctx: CParser.GtExpressionContext):
        exp1, exp2 = ctx.expression(0).getText(), ctx.expression(1).getText()
        obj1 = self.manager.get_variable(exp1)
        obj2 = self.manager.get_variable(exp2)
        if obj1 and obj2:
            overridden_method = obj1.clazz.get_method('gt').alias
            return f'{obj1.name}->{overridden_method}' \
                   f'({obj1.name}, {obj2.name})'
        return ctx.getText()

    def visitGteExpression(self, ctx: CParser.GteExpressionContext):
        exp1, exp2 = ctx.expression(0).getText(), ctx.expression(1).getText()
        obj1 = self.manager.get_variable(exp1)
        obj2 = self.manager.get_variable(exp2)
        if obj1 and obj2:
            overridden_method = obj1.clazz.get_method('gte').alias
            return f'{obj1.name}->{overridden_method}' \
                   f'({obj1.name}, {obj2.name})'
        return ctx.getText()

    def visitLtExpression(self, ctx: CParser.LtExpressionContext):
        exp1, exp2 = ctx.expression(0).getText(), ctx.expression(1).getText()
        obj1 = self.manager.get_variable(exp1)
        obj2 = self.manager.get_variable(exp2)
        if obj1 and obj2:
            overridden_method = obj1.clazz.get_method('lt').alias
            return f'{obj1.name}->{overridden_method}' \
                   f'({obj1.name}, {obj2.name})'
        return ctx.getText()

    def visitLteExpression(self, ctx: CParser.LteExpressionContext):
        exp1, exp2 = ctx.expression(0).getText(), ctx.expression(1).getText()
        obj1 = self.manager.get_variable(exp1)
        obj2 = self.manager.get_variable(exp2)
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
                    obj2 = self.manager.get_variable(expr2.getText())
                    overridden_method = obj2.clazz.get_method('lshift').alias
                    result: str = f'{_result}->{overridden_method}' \
                                  f'({_obj1.name}, {obj2.name})'
                    return result, _obj1
        obj1 = self.manager.get_variable(expr1.getText())
        obj2 = self.manager.get_variable(expr2.getText())
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
                                print_error('Statement was not recognized!')
                case CParser.ClassInstantiationContext:
                    self.visitClassInstantiation(child)

    def visitClassDefinition(self, ctx: CParser.ClassDefinitionContext):
        identifier: str = f'class.{ctx.identifier().getText()}'
        clazz = module.context.get_identified_type(identifier)
        # using a list instead of set_body() bc it returns a tuple
        # so I cannot modify it later on unless I copy it
        clazz.elements = []
        # to map elements to their names and position in memory
        clazz.map = ClazzMap()
        self.manager.add_clazz(clazz)
        # count struct elements padding in memory
        clazz.counter = -1
        self.manager.current_clazz = clazz
        scope = Scope(ScopeType.CLAZZ)
        self.manager.scope_stack.push(scope)
        self.visitClassBlock(ctx.classBlock())

    def visitClassAttributeDeclaration(
            self,
            ctx: CParser.ClassAttributeDeclarationContext):
        clazz = self.manager.current_clazz
        type_specifier = self.visitTypeSpecifier(ctx.typeSpecifier())
        identifier = ctx.identifier().getText()
        clazz.elements.append(type_specifier)
        clazz.counter += 1
        clazz.map.add_attribute(clazz.counter, identifier)

    def createConstructor(self, constructor: CParser.ClassMethodContext):
        clazz = self.manager.current_clazz
        rtype = self.visitTypeSpecifier(constructor.typeSpecifier())
        method_name: str = constructor.identifier().getText()
        args, var_arg = self.visitFunctionArgs(constructor.functionArgs())
        args = [(clazz.as_pointer(), 'this'), *args]
        ir_args = [arg[0] for arg in args]
        method_type = ir.FunctionType(rtype, ir_args)
        method_type.var_arg = var_arg

        # get method mangled name
        clazz_name = clazz.name.split('.')[1]
        mangled_name: str = f'_ZN{len(clazz_name)}{clazz_name}' \
                            f'{len(method_name)}{method_name}E'
        for arg in method_type.args:
            mangled_name += self.getArgMangledName(arg)

        method: ir.Function = module.get_global(mangled_name)

        for i in range(len(method.args)):
            _, arg_identifier = args[i]
            if arg_identifier:
                method.args[i].name = arg_identifier

        block = method.append_basic_block(name='entry')
        builder = ir.IRBuilder(block)

        self.manager.builder = builder
        self.manager.current_function = method
        self.manager.add_function(method)

        scope = Scope(ScopeType.FUNC, function=method)
        self.manager.scope_stack.push(scope)
        self.visitBlock(constructor.block())

        if rtype == ir.VoidType() and not builder.block.is_terminated:
            builder.ret_void()

    def autoDeclareConstructor(self):
        clazz = self.manager.current_clazz
        # create an empty constructor
        method_type = ir.FunctionType(ir.VoidType(), [clazz.as_pointer()])
        # get method mangled name
        clazz_name = clazz.name.split('.')[1]
        mangled_name: str = f'_ZN{len(clazz_name)}{clazz_name}' \
                            f'{len(clazz_name)}{clazz_name}E'
        for arg in method_type.args:
            mangled_name += self.getArgMangledName(arg)
        method = ir.Function(module, method_type, mangled_name)
        method.args[0].name = 'this'
        clazz.map.add_method(clazz_name, mangled_name, True)
        self.manager.current_function = method

    def autoDefineConstructor(self):
        clazz = self.manager.current_clazz
        for _, info in clazz.map.methods.items():
            if info['is_constructor']:
                constructor = module.get_global(info['mangled_name'])
                block = constructor.append_basic_block(name='entry')
                builder = ir.IRBuilder(block)

                self.manager.builder = builder
                scope = Scope(ScopeType.FUNC, function=constructor)
                self.manager.scope_stack.push(scope)
                self.manager.current_function = constructor
                self.manager.add_function(constructor)
                # self.visitBlock(ctx.block())
                builder.ret_void()
                break

    def visitClassBlock(self, ctx: CParser.ClassBlockContext):
        clazz = self.manager.current_clazz
        for attribute in ctx.classAttributeDeclaration():
            self.visitClassAttributeDeclaration(attribute)

        # this will create method ptr in the class structure
        # before creating the body of the method
        # bc if a method 1 created before method 2
        # and method 1 calls method 2, without this
        # it will cause a problem

        class_name = clazz.name.split('.')[1]
        has_constructor = False
        for method in ctx.classMethod():
            if method.identifier().getText() == class_name:
                has_constructor = True
            self.createClassMethodDeclaration(method)

        if not has_constructor:
            self.autoDeclareConstructor()
            self.autoDefineConstructor()

        for method in ctx.classMethod():
            if method.identifier().getText() == class_name:
                self.createConstructor(method)
                continue
            self.visitClassMethod(method)

    def getArgMangledName(self, arg: ir.Argument) -> str:
        if arg == i8:
            return 'c'
        elif arg == i16:
            return 's'
        elif arg == i32:
            return 'i'
        elif arg == i64:
            return 'l'
        elif arg == self.manager.current_clazz:
            return 'S_'
        elif isinstance(arg, ir.IdentifiedStructType):
            # this is a different class
            clazz_name = arg.name.split('.')[1]
            return f'{len(clazz_name)}{clazz_name}'
        elif isinstance(arg, ir.PointerType):
            return 'P' + self.getArgMangledName(arg.pointee)
        else:
            print(type(arg))

    def createClassMethodDeclaration(self, method: CParser.ClassMethodContext):
        # this method need to be executed before function block
        # gets created so methods can have access to each other
        # despite being declared after it
        clazz = self.manager.current_clazz
        rtype = self.visitTypeSpecifier(method.typeSpecifier())
        method_name: str = method.identifier().getText()
        args, var_arg = self.visitFunctionArgs(method.functionArgs())
        args = [(clazz.as_pointer(), 'this'), *args]
        method_type = ir.FunctionType(rtype, [arg[0] for arg in args])
        method_type.var_arg = var_arg

        # get method mangled name
        clazz_name = clazz.name.split('.')[1]
        mangled_name: str = f'_ZN{len(clazz_name)}{clazz_name}' \
                            f'{len(method_name)}{method_name}E'
        for arg in method_type.args:
            mangled_name += self.getArgMangledName(arg)

        ir.Function(module, method_type, mangled_name)

        is_constructor = False
        if method_name == clazz_name:
            is_constructor = True
        clazz.map.add_method(method_name, mangled_name, is_constructor)

    def visitClassMethod(self, ctx: CParser.ClassMethodContext):
        clazz = self.manager.current_clazz
        rtype = self.visitTypeSpecifier(ctx.typeSpecifier())
        method_name: str = ctx.identifier().getText()
        args, var_arg = self.visitFunctionArgs(ctx.functionArgs())
        args = [(clazz.as_pointer(), 'this'), *args]

        # get method mangled name
        clazz_name = clazz.name.split('.')[1]
        mangled_name: str = f'_ZN{len(clazz_name)}{clazz_name}' \
                            f'{len(method_name)}{method_name}E'
        for arg in args:
            mangled_name += self.getArgMangledName(arg[0])

        # assign method mangled name to its method definition
        method_type = ir.FunctionType(rtype, [arg[0] for arg in args])
        method_type.var_arg = var_arg
        method = module.get_global(mangled_name)

        clazz_map: ClazzMap = clazz.map
        clazz_map.add_method(method_name, mangled_name)

        for i in range(len(method.args)):
            _, arg_identifier = args[i]
            if arg_identifier:
                method.args[i].name = arg_identifier

        block = method.append_basic_block(name='entry')
        builder = ir.IRBuilder(block)

        self.manager.builder = builder
        scope = Scope(ScopeType.FUNC, function=method)
        self.manager.scope_stack.push(scope)
        self.manager.current_function = method
        self.manager.add_function(method)
        self.visitBlock(ctx.block())

        if rtype == ir.VoidType() and not builder.block.is_terminated:
            builder.ret_void()

    def visitClassInstantiation(self, ctx: CParser.ClassInstantiationContext):
        # TODO: fix this
        clazz = self.visitTypeSpecifier(ctx.typeSpecifier())
        identifier: str = ctx.identifier(0).getText()
        builder = self.manager.builder
        obj = builder.alloca(clazz, name=identifier)
        self.manager.add_variable(obj)

        for name, info in clazz.map.methods.items():
            if info['is_constructor']:
                constructor = module.get_global(info['mangled_name'])
                args = self.visitFunctionCallArgs(ctx.functionCallArgs())
                if args is None:
                    args = [obj]
                else:
                    args = [obj, *args]
                builder.call(constructor, args)
        return obj

    def castType(self, src, dest):
        # TODO: this code down below was not reviewed

        src: ir.Instruction
        src_ptr_count = 0
        src_temp = src
        if hasattr(src, 'type'):
            src_temp = src.type

        while src_temp.is_pointer:
            src_ptr_count += 1
            src_temp = src.type.pointee

        dest_ptr_count = 0
        dest_temp = dest
        if hasattr(dest, 'type'):
            dest_temp = dest.type
        while dest_temp.is_pointer:
            dest_ptr_count += 1
            dest_temp = dest_temp.pointee

        if src_ptr_count != dest_ptr_count:
            print_error('Incompatible function return type and return value')
        print(src_temp, dest_temp, src_ptr_count, dest_ptr_count)

        if isinstance(src_temp, ir.IntType) \
                and isinstance(dest_temp, ir.IntType):
            c = src_ptr_count - dest_ptr_count
            for _ in range(c):
                src = self.manager.builder.load(src)
            return self.manager.builder.sext(src, dest_temp)

    def promoteType(self, src1, src2):
        # TODO: this code down below was not reviewed
        if src1.type.width > src2.type.width:
            return src1, self.manager.builder.sext(src2, src1.type)
        elif src1.type.width < src2.type.width:
            return self.manager.builder.sext(src1, src2.type), src2
        else:
            return src1, src2

    def castFunctionArg(self, func, args):
        for fa, a in zip(func.args, args):
            # if f
            if isinstance(fa.type, ir.IdentifiedStructType):
                if isinstance(a.type, ir.PointerType):
                    if fa.type == a.type.pointee:
                        # copy the object
                        print('#################')
                        print(func.name)
                        print('yes')
        return args

    def visitChainedCall(self, ctx: CParser.ChainedCallContext):
        obj_name: str = ctx.identifier(0).getText()
        obj = self.manager.get_variable(obj_name)
        builder = self.manager.builder
        attribute = None
        elements = obj.type.pointee.elements
        clazz_map: ClazzMap = obj.type.pointee.map

        for child in list(ctx.getChildren())[1:]:
            match type(child):
                case CParser.IdentifierContext:
                    for element, name in zip(elements, clazz_map.attributes):
                        if name == child.getText():
                            idx = clazz_map.attributes[name]['index']
                            attr_idx = [i32(0), i32(idx)]
                            attribute = builder.gep(obj, attr_idx)
                            attribute = builder.load(attribute)
                case CParser.FunctionCallExpressionContext:
                    identifier = child.identifier().getText()
                    for name in clazz_map.methods:
                        if name == identifier:
                            mn = clazz_map.methods[name]['mangled_name']
                            method = module.get_global(mn)
                            args = self.visitFunctionCallArgs(
                                child.functionCallArgs())
                            if args is None:
                                args = [obj]
                            else:
                                args = [obj, *args]
                            args = self.castFunctionArg(method, args)
                            attribute = builder.call(method, args)
                case antlr4.tree.Tree.TerminalNodeImpl:
                    # this is to check -> or . later on
                    continue

        return attribute
