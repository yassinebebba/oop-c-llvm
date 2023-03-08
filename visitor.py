import os
import re
import antlr4.tree.Tree
from io import FileIO
from termcolor import colored
from core.CVisitor import CVisitor
from core.CParser import CParser
from manager import Manager
from manager import Clazz
from manager import Attribute
from manager import Function
from manager import Variable
from manager import Obj
from manager import Arg


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
        except:
            return None, ' '.join(chunks)

    def visitCompilationUnit(self, ctx: CParser.CompilationUnitContext):
        self.write('/*\n')
        self.write('############################################\n')
        self.write('THIS FILE IS NOT MEANT TO BE EDITED BY HAND\n')
        self.write('############################################\n')
        self.write('*/\n\n')
        for child in ctx.getChildren():
            match type(child):
                case CParser.IncludeDirectiveContext:
                    self.write(child.getText())
                case CParser.DeclarationListContext:
                    for declaration in child.getChildren():
                        match type(declaration):
                            case CParser.VariableDeclarationContext:
                                value = self.state.tabs
                                value += self.visitVariableDeclaration(
                                    declaration)
                                self.write(value)
                                self.add_newline()
                            case CParser.FunctionDeclarationContext:
                                value = self.state.tabs
                                value += self.visitFunctionDeclaration(
                                    declaration)
                                self.write(value)
                                self.add_newline()
                            case CParser.StructDeclarationContext:
                                value = self.state.tabs
                                value += self.visitStructDeclaration(
                                    declaration)
                                self.write(value)
                                self.add_newline()
                case CParser.DefinitionListContext:
                    for definition in child.getChildren():
                        match type(definition):
                            case CParser.VariableDefinitionContext:
                                value = self.state.tabs
                                value += self.visitVariableDefinition(
                                    definition)
                                self.write(value)
                                self.add_newline()
                            case CParser.FunctionDefinitionContext:
                                value = self.state.tabs
                                _, func_string = self.visitFunctionDefinition(
                                    definition)
                                value += func_string
                                self.write(value)
                                self.add_newline()
                            case CParser.StructDefinitionContext:
                                value = self.state.tabs
                                value += self.visitStructDefinition(
                                    definition)
                                self.write(value)
                                self.add_newline()
                case CParser.FunctionCallContext:
                    value = self.state.tabs
                    value += self.visitFunctionCall(child)
                    self.write(value)
                    self.add_newline()
                case CParser.AssignmentContext:
                    value = self.state.tabs
                    value += self.visitAssignment(child)
                    self.write(value)
                    self.add_newline()
                case CParser.ClassDefinitionContext:
                    value = self.state.tabs
                    value += self.visitClassDefinition(child)
                    self.write(value)
                    self.add_newline()

    def visitTypeSpecifier(self, ctx: CParser.TypeSpecifierContext):
        clazz, type_specifier = self.match_type_specifier(ctx)
        return clazz, type_specifier

    def visitVariableDefinition(self, ctx: CParser.VariableDefinitionContext):
        _, type_specifier = self.visitTypeSpecifier(ctx.typeSpecifier())
        identifier = ctx.identifier().getText()
        # check if this is a class object variable definition
        clazz_name, *_ = type_specifier.split()
        try:
            clazz = self.manager.get_clazz(clazz_name)
            obj: Obj = Obj(name=identifier, clazz=clazz)
            self.manager.add_obj(obj)
        except:
            pass
        variable = Variable(name=identifier, type_specifier=type_specifier)
        self.manager.add_variable(variable)
        expression = self.visitExpression(ctx.expression())
        return f'{type_specifier} {identifier} = {expression};'

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

    def visitFunctionDeclaration(self, ctx:
    CParser.FunctionDeclarationContext) -> tuple[Function, str]:
        _, rtype = self.match_type_specifier(ctx.typeSpecifier())
        identifier = ctx.identifier().getText()
        args, args_string = self.visitFunctionArgs(ctx.functionArgs())
        func: Function = Function(
            rtype=rtype,
            name=identifier,
            args=args,
            alias=None
        )
        return func, f'{rtype} {identifier}({args});'

    def visitFunctionDefinition(self, ctx:
    CParser.FunctionDefinitionContext) -> tuple[Function, str]:
        # typeSpecifier? identifier LP functionArgs? RP block
        self.state.visit_block_scope()
        _, rtype = self.match_type_specifier(ctx.typeSpecifier())
        identifier: str = ctx.identifier().getText()
        args, args_string = self.visitFunctionArgs(ctx.functionArgs())
        func = Function(
            rtype=rtype,
            name=identifier,
            args=args,
            alias=None
        )
        self.manager.current_function = func
        if ctx.functionArgs():
            try:
                for arg in ctx.functionArgs().getChildren():
                    if isinstance(arg, CParser.ArgContext):
                        arg_name = arg.identifier().getText()
                        # possible class type
                        clazz, _ = self.match_type_specifier(
                            arg.typeSpecifier())
                        # print(class_name)
                        arg = Arg(name=arg_name, clazz=clazz,
                                  type_specifier=clazz.name)
                        self.manager.current_function.add_arg(arg)
            except KeyError:
                # no args
                pass

        block: str = self.visitBlock(ctx.block())
        self.state.exit_block_scope()
        self.manager.current_function = None
        return func, f'{rtype} {identifier}({args_string}) {"{"}\n {block}\n{self.state.tabs}{"}"}'

    def visitFunctionArgs(self, ctx: CParser.FunctionArgsContext) -> tuple[
        list[Arg], str]:
        if ctx is None:
            return [], ''

        args: list[CParser.ArgContext] = [
            arg for arg in ctx.getChildren()
            if isinstance(arg, CParser.ArgContext)
        ]

        # check for duplicate args
        temp: dict = {}
        for arg in args:
            identifier = arg.identifier().getText()
            if identifier == 'this':
                print_error(
                    'Error: can\' use`this` as an identifier, `this` is a reserved keyword')
                exit(-1)
            if identifier in temp:
                print_error(
                    f'Error: duplicate function argument `{identifier}`')
                exit(-1)
            else:
                temp[identifier] = 1

        processed_arguments: list[Arg] = []
        result: list[str] = []
        for arg in args:
            arg, string = self.visitArg(arg)
            processed_arguments.append(arg)
            result.append(string)
        return processed_arguments, ', '.join(result)

    def visitArg(self, ctx: CParser.ArgContext) -> tuple[Arg, str]:
        clazz, type_specifier = self.visitTypeSpecifier(ctx.typeSpecifier())
        arg: Arg = Arg(type_specifier=type_specifier, name=None, clazz=clazz)
        if ctx.identifier():
            identifier: str = ctx.identifier().getText()
            arg.name = identifier
            return arg, f'{type_specifier} {identifier}'
        return arg, type_specifier

    def visitStructDeclaration(self, ctx: CParser.StructDeclarationContext):
        return f'struct {ctx.identifier().getText()};'

    def visitStructDefinition(self, ctx: CParser.StructDefinitionContext):
        self.state.visit_block_scope()
        struct_block: str = self.visitStructBlock(ctx.structBlock())
        self.state.exit_block_scope()
        return f'struct {ctx.identifier().getText()} {"{"}\n{struct_block}\n{self.state.tabs}{"}"};'

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
        # self.check_variable_assignment(ctx)
        identifier: str = (ctx.identifier() or ctx.chainedCall()).getText()
        expression: CParser.ExpressionContext = ctx.expression()
        return f'{identifier} = {self.visitExpression(expression)};'

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
        return f'{unary}{self.visitFunctionCall(ctx.functionCallExpression())}'

    def visitFunctionCall(self, ctx: CParser.FunctionCallContext):
        args = self.visitFunctionCallArgs(ctx.functionCallArgs())
        return f'{ctx.identifier().getText()}({args});'

    def visitFunctionCallArgs(self, ctx: CParser.FunctionCallArgsContext):
        if ctx is None:
            return ''
        expressions: list[CParser.ExpressionContext] = [
            arg for arg in ctx.getChildren()
            if isinstance(arg, CParser.ExpressionContext)
        ]
        values: list[str] = list(map(self.visitExpression, expressions))
        return ', '.join(values)

    def visitFunctionReturn(self, ctx: CParser.FunctionReturnContext):
        if ctx.expression():
            return f'return {ctx.expression().getText()};'
        else:
            return 'return;'

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
        return f'if ({", ".join(values)}) {"{"}\n {block}\n{self.state.tabs}{"}"}'

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

        return f'while ({", ".join(values)}) {"{"}\n {block}\n{self.state.tabs}{"}"}'

    def visitDoWhileStatement(self, ctx: CParser.DoWhileStatementContext):
        self.state.visit_block_scope()
        conditions: list[CParser.ConditionContext] = [
            condition for condition in ctx.getChildren()
            if isinstance(condition, CParser.ConditionContext)
        ]
        values = list(map(self.visitCondition, conditions))
        block: str = self.visitBlock(ctx.block())
        self.state.exit_block_scope()

        return f'do {"{"}\n {block}\n{self.state.tabs}{"}"} while ({", ".join(values)});'

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
            case CParser.FuncCallExpressionContext:
                return self.visitFuncCallExpression(ctx)
            case CParser.MultiplyExpressionContext:
                return self.visitMultiplyExpression(ctx)
            case CParser.AddExpressionContext:
                result, _ = self.visitAddExpression(ctx)
                return result
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
        exp1, exp2 = ctx.expression(0), ctx.expression(1)

        exp1 = exp1.getText()
        exp2 = exp2.getText()

        obj1, obj2 = self.manager.get_obj(exp1), self.manager.get_obj(exp2)
        if obj1 and obj2:
            overridden_method = obj1.clazz.get_method('mult').alias
            return f'{obj1.name}->{overridden_method}({obj1.name}, {obj2.name})'
        return ctx.getText()

    def visitAddExpression(self, ctx: CParser.AddExpressionContext):
        result: str = ''
        expr1, expr2 = ctx.expression(0), ctx.expression(1)
        _exp1: str = ''
        _exp2: str = ''
        # parsing expr should return info about the operands
        # result: str, expr1: class?, expr2: class? probably expr2 is not needed
        if isinstance(expr1, CParser.AddExpressionContext):
            _result, _obj1 = self.visitAddExpression(expr1)
            if _obj1:
                if isinstance(expr2, CParser.IdentifierExpressionContext):
                    obj2 = self.manager.get_obj(expr2.getText())
                    overridden_method = obj2.clazz.get_method('add').alias
                    result: str = f'{_result}->{overridden_method}({_obj1.name}, {obj2.name})'
                    return result, _obj1
        obj1 = self.manager.get_obj(expr1.getText())
        obj2 = self.manager.get_obj(expr2.getText())
        if obj1 and obj2:
            overridden_method = obj1.clazz.get_method('add').alias
            result: str = f'{obj1.name}->{overridden_method}({obj1.name}, {obj2.name})'
            return result, obj1
        return ctx.getText(), None

    def visitSubtractExpression(self, ctx: CParser.SubtractExpressionContext):
        return ctx.getText()

    def visitConstantExpression(self, ctx: CParser.ConstantExpressionContext):
        return ctx.getText()

    def visitIdentifierExpression(self,
                                  ctx: CParser.IdentifierExpressionContext):
        return ctx.getText()

    def visitChainedCallExpression(self,
                                   ctx: CParser.ChainedCallExpressionContext):
        if ctx.unarySign():
            return f'{ctx.unarySign().getText()}{self.visitChainedCall(ctx.chainedCall())}'
        return self.visitChainedCall(ctx.chainedCall())

    def visitEqExpression(self, ctx: CParser.EqExpressionContext):
        exp1, exp2 = ctx.expression(0).getText(), ctx.expression(1).getText()
        obj1, obj2 = self.manager.get_obj(exp1), self.manager.get_obj(exp2)
        if obj1 and obj2:
            overridden_method = obj1.clazz.get_method('eq').alias
            return f'{obj1.name}->{overridden_method}({obj1.name}, {obj2.name})'
        return ctx.getText()

    def visitGtExpression(self, ctx: CParser.GtExpressionContext):
        exp1, exp2 = ctx.expression(0).getText(), ctx.expression(1).getText()
        obj1, obj2 = self.manager.get_obj(exp1), self.manager.get_obj(exp2)
        if obj1 and obj2:
            overridden_method = obj1.clazz.get_method('gt').alias
            return f'{obj1.name}->{overridden_method}({obj1.name}, {obj2.name})'
        return ctx.getText()

    def visitGteExpression(self, ctx: CParser.GteExpressionContext):
        exp1, exp2 = ctx.expression(0).getText(), ctx.expression(1).getText()
        obj1, obj2 = self.manager.get_obj(exp1), self.manager.get_obj(exp2)
        if obj1 and obj2:
            overridden_method = obj1.clazz.get_method('gte').alias
            return f'{obj1.name}->{overridden_method}({obj1.name}, {obj2.name})'
        return ctx.getText()

    def visitLtExpression(self, ctx: CParser.LtExpressionContext):
        exp1, exp2 = ctx.expression(0).getText(), ctx.expression(1).getText()
        obj1, obj2 = self.manager.get_obj(exp1), self.manager.get_obj(exp2)
        if obj1 and obj2:
            overridden_method = obj1.clazz.get_method('lt').alias
            return f'{obj1.name}->{overridden_method}({obj1.name}, {obj2.name})'
        return ctx.getText()

    def visitLteExpression(self, ctx: CParser.LteExpressionContext):
        exp1, exp2 = ctx.expression(0).getText(), ctx.expression(1).getText()
        obj1, obj2 = self.manager.get_obj(exp1), self.manager.get_obj(exp2)
        if obj1 and obj2:
            overridden_method = obj1.clazz.get_method('lte').alias
            return f'{obj1.name}->{overridden_method}({obj1.name}, {obj2.name})'
        return ctx.getText()

    def visitLeftShiftExpression(self, ctx: CParser.LeftShiftExpressionContext):
        result: str = ''
        expr1, expr2 = ctx.expression(0), ctx.expression(1)
        _exp1: str = ''
        _exp2: str = ''
        # parsing expr should return info about the operands
        # result: str, expr1: class?, expr2: class? probably expr2 is not needed
        if isinstance(expr1, CParser.LeftShiftExpressionContext):
            _result, _obj1 = self.visitLeftShiftExpression(expr1)
            if _obj1:
                if isinstance(expr2, CParser.IdentifierExpressionContext):
                    obj2 = self.manager.get_obj(expr2.getText())
                    overridden_method = obj2.clazz.get_method('lshift').alias
                    result: str = f'{_result}->{overridden_method}({_obj1.name}, {obj2.name})'
                    return result, _obj1
        obj1 = self.manager.get_obj(expr1.getText())
        obj2 = self.manager.get_obj(expr2.getText())
        if obj1 and obj2:
            overridden_method = obj1.clazz.get_method('lshift').alias
            result: str = f'{obj1.name}->{overridden_method}({obj1.name}, {obj2.name})'
            return result, obj1
        return ctx.getText(), None

    def visitBlock(self, ctx: CParser.BlockContext):
        result: str = ''
        for child in ctx.getChildren():
            match type(child):
                case CParser.DeclarationListContext:
                    for declaration in child.getChildren():
                        match type(declaration):
                            case CParser.VariableDeclarationContext:
                                result += self.state.tabs
                                value = self.visitVariableDeclaration(
                                    declaration)
                                result += value
                                result += '\n'
                            case CParser.StructDeclarationContext:
                                result += self.state.tabs
                                value = self.visitStructDeclaration(
                                    declaration)
                                result += value
                                result += '\n'
                case CParser.DefinitionListContext:
                    for definition in child.getChildren():
                        match type(definition):
                            case CParser.VariableDefinitionContext:
                                result += self.state.tabs
                                value = self.visitVariableDefinition(
                                    definition)
                                result += value
                                result += '\n'
                            case CParser.StructDefinitionContext:
                                result += self.state.tabs
                                value = self.visitStructDefinition(
                                    definition)
                                result += value
                                result += '\n'
                case CParser.StatementListContext:
                    for statement in child.getChildren():
                        match type(statement):
                            case CParser.ExpressionContext:
                                result += self.state.tabs
                                value = self.visitExpression(statement)
                                result += f'{value}\n'
                            case CParser.FuncCallExpressionContext:
                                result += self.state.tabs
                                value = self.visitFuncCallExpression(statement)
                                result += f'{value}\n'
                            case CParser.ChainedCallExpressionContext:
                                result += self.state.tabs
                                value = self.visitChainedCallExpression(statement)
                                result += f'{value};\n'
                            case CParser.IfStatementStructureContext:
                                value = self.visitIfStatementStructure(statement)
                                result += f'{value}\n'
                            case CParser.AssignmentContext:
                                result += self.state.tabs
                                value = self.visitAssignment(statement)
                                result += f'{value}\n'
                            case CParser.InplaceAssignmentContext:
                                result += self.state.tabs
                                value = self.visitInplaceAssignment(statement)
                                result += f'{value}\n'
                            case CParser.VariableDefinitionContext:
                                result += self.state.tabs
                                value = self.visitVariableDefinition(statement)
                                result += value
                                result += '\n'
                            case CParser.FunctionReturnContext:
                                result += self.state.tabs
                                value = self.visitFunctionReturn(statement)
                                result += f'{value}\n'
                            case CParser.LeftShiftExpressionContext:
                                result += self.state.tabs
                                value, _ = self.visitLeftShiftExpression(statement)
                                result += f'{value};\n'
                            case antlr4.tree.Tree.TerminalNodeImpl:
                                # this is the `;`
                                pass
                            case _:
                                print(type(statement))
                                raise Exception('Statement was not recognized!')
                case CParser.ClassInstantiationContext:
                    result += self.state.tabs
                    value = self.visitClassInstantiation(child)
                    result += value
                    result += '\n'
        # remove the last new line result[:-1]
        # self.ungetch()
        return result[:-1]

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
        attributes, methods, method_declarations = self.visitClassBlock(ctx.classBlock())
        self.state.exit_class()
        self.state.exit_block_scope()
        # self.manager.current_clazz = None
        return f'typedef struct {identifier} {"{"}\n {attributes}\n{"}"} {identifier};\n\n{method_declarations}\n{methods}'

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
            args: list[Arg] = [Arg(name=None, type_specifier=this, clazz=clazz)]
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
            method_block += f'{self.state.tabs}{clazz_name}* this = malloc(sizeof({clazz_name}));\n'
            method_block += f'{self.state.tabs}this->{clazz_name * 2} = &{clazz_name * 2};\n'
            for method in methods:
                if method.name == clazz_name:
                    continue
                name: str = method.name
                new_name: str = f'{clazz_name}{name}'
                method_block += f'{self.state.tabs}this->{new_name} = &{new_name};\n'
            method_block += self.visitBlock(constructor.block())
            return f'{clazz_name}* {method_alias}({args_string}) {"{"}\n{method_block}\n{"}"}'

        else:
            # return f'void {clazz_name}{clazz_name}({clazz_name} * this) {"{"}\n// Not implemented\n{"}"}'
            return f'{clazz_name}* {clazz_name}{clazz_name}() {"{"}\n// Not implemented\n{"}"}'

    def createClassStringRepresentation(self, clazz_name):
        string = f'<{clazz_name} object at 0xFFFFFFF>\n'
        result: str = f'char * {clazz_name}toString({clazz_name} * this) {"{"}\n' \
                      f'\tchar * str = malloc(sizeof(char *) * {len(string)});\n' \
                      f'\tsprintf(str, "<{clazz_name} object at %p>\\n", this);\n' \
                      f'\treturn str;\n' \
                      '}\n'
        return result

    def methodDefinitionToMethodDeclaretion(self, class_name: str, method: CParser.ClassMethodContext):
        ptr = self.getFunctionPointer(class_name, method)
        matches = re.match('(?P<rtype>.*?)\(\*(?P<alias>.*)\)(?P<args>\(.*\))', ptr)
        rtype = matches.group('rtype')
        alias = matches.group('alias')
        args = matches.group('args')
        return f'{rtype}{alias}{args};'

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
                    attributes += f'char * (*{class_name}toString)(struct {class_name} *);'
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

        # TODO: urgent this has to be all Function instance in class constructor
        parsed_constructor = self.createClassConstructor(constructor,
                                                         clean_methods)
        parsed_methods = parsed_constructor + '\n' + parsed_methods

        # so other methods can have access to each other
        method_declarations: str = ''
        for method in methods:
            method_declaration = self.methodDefinitionToMethodDeclaretion(class_name, method)
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
        return method, f'{rtype} {alias}({args_string}) {"{"}\n {block}\n{self.state.tabs}{"}"}'

    def visitClassInstantiation(self, ctx: CParser.ClassInstantiationContext):
        clazz, type_specifier = self.match_type_specifier(ctx.typeSpecifier())
        class_name: str = type_specifier.split()[0]  # to remove the pointer
        identifier: str = ctx.identifier().getText()
        args: str = self.visitFunctionCallArgs(
            ctx.functionCall().functionCallArgs())
        obj: Obj = Obj(name=identifier, clazz=clazz)
        self.manager.add_obj(obj)
        # result: str = f'{type_specifier} {identifier} = malloc(sizeof({class_name}));\n'
        # result += f'{self.state.tabs}{class_name}{class_name}({identifier}, {args});'
        result: str = f'{type_specifier} {identifier} = {class_name}{class_name}({args});'
        return result

    def visitChainedCall(self, ctx: CParser.ChainedCallContext):
        obj_name: str = ctx.identifier(0).getText()
        obj: Obj = self.manager.get_obj(obj_name)
        if obj is not None:
            result: str = ''
            # this is to check if you are accessing nested attributes
            # so it would reference it like this:
            # Pizza * pizza = new Pizza()
            # pizza->topping->get_name() should be pizza->topping.get_name(pizza->topping)
            # instead of pizza->topping.get_name(topping) which might not exist outside the class
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
                                result += f'{method.alias}({original_ref}->{obj.name}, {args})'
                            else:
                                result += f'{method.alias}({obj.name}, {args})'
                        else:
                            if is_nested:
                                result += f'{method.alias}({original_ref}->{obj.name})'
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
                        except:
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
