import os
from enum import Enum
from termcolor import colored
from core.CParser import CParser
from core.CListener import CListener
from io import FileIO
from antlr4.tree.Tree import TerminalNodeImpl
from antlr4.tree.Tree import Token


class Scope(Enum):
    GLOBL = 0  # for globals
    FUNC_LOCAL = 1
    CLAZZ_LOCAL = 2
    CLAZZ_METHOD_LOCAL = 3


class State:
    def __init__(self):
        self.global_scope = True
        self.block_scope = False
        self.scope_level = 0

    @property
    def tabs(self):
        return '\t' * self.scope_level

    def enter_block_scope(self):
        self.scope_level += 1
        self.global_scope = False
        self.block_scope = True

    def exit_block_scope(self):
        self.scope_level -= 1
        if self.scope_level == 0:
            self.global_scope = True
            self.block_scope = False


def print_error(error: str):
    print(colored(error, 'red'))


class Listener(CListener):
    def __init__(self, output):
        self.output: FileIO = output
        self.state = State()
        self.identifiers = {
            'declared_variables': [],
            'initialized_variables': [],
            'functions': {},
            'clazzes': {}
        }

    def write(self, text: str):
        self.output.write(text)

    def add_newline(self) -> None:
        self.output.write('\n')

    def add_indentation(self):
        if self.state.block_scope:
            self.output.write('\t' * self.state.scope_level)

    def ungetch(self):
        cur = self.output.tell()
        self.output.seek(cur - 1, os.SEEK_SET)
        self.output.truncate()

    def check_variable_declaration(self,
                                   ctx: CParser.VariableDeclarationContext):
        for var in self.identifiers['declared_variables']:
            if var.identifier().getText() == ctx.identifier().getText() \
                    and var.scope_level == ctx.scope_level:
                prev_symbol: Token = var.identifier().getChild(0).symbol
                symbol: Token = ctx.identifier().getChild(0).symbol
                print(f'{ctx.getText()}')
                print(' ' * symbol.column + '^')
                print_error(
                    f'Error <line {symbol.line}>: '
                    f'Identifier \'{var.identifier().getText()}\' has already '
                    f'been declared in the same scope. '
                    f'Previous declaration at <line {prev_symbol.line}>')
                exit(-1)
        else:
            self.identifiers['declared_variables'].append(ctx)

    def check_variable_assignment(self,
                                  ctx: CParser.InplaceAssignmentContext | CParser.AssignmentContext):
        for var in self.identifiers['declared_variables']:
            if var.identifier().getText() == ctx.identifier().getText():
                # identifier was declared good
                return
        else:
            symbol: Token = ctx.identifier().getChild(0).symbol
            print(f'{ctx.getText()}')
            print(' ' * symbol.column + '^')
            print_error(
                f'Error <line {symbol.line}>: use of undeclared identifier \'{ctx.identifier().getText()}\'.')
            exit(-1)

    def check_var_definition(self, ctx: CParser.VariableDefinitionContext):
        for var in self.identifiers['declared_variables']:
            if var.identifier().getText() == ctx.identifier().getText():
                # identifier was declared good
                return
        else:
            symbol: Token = ctx.identifier().getChild(0).symbol
            print(f'{ctx.getText()}')
            print(' ' * symbol.column + '^')
            print_error(
                f'Error <line {symbol.line}>: use of undeclared identifier \'{ctx.identifier().getText()}\'.')
            exit(-1)

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

        return ' '.join(chunks)

    def get_args(self, parent, func_args: list):  # for parent node
        """
        recursively getting func args because of this
        grammar rule :(
        functionArgs
            : typeSpecifier identifier? COMMA?
            | functionArgs COMMA functionArgs
            ;
        which will result in if you input: (int a, int b, int c)
        it will not create one node functionArgs ctx
        with many children it will create something like
        [functionArgs, COMMA, typeSpecifier, identifier]
        conforming to the recursive rule and so on the more args
        you add
        """
        if parent is None: return
        if isinstance(parent.getChild(0),
                      CParser.TypeSpecifierContext):
            func_args.append(' '.join(
                [
                    tn.getText() for tn in parent.getChildren()
                ]
            ))
            return
        # if isinstance(parent, TerminalNodeImpl):
        #     # uncommenting this line will result in args having
        #     # this value:
        #     # ['int a', ',', 'int b', ',', 'Point s', ',', 'Point']
        #     # this line: >>> args.append(parent.getText())
        #
        #     #
        #     return

        # doing it in EAFP
        # Easier to Ask Forgiveness Than Permission
        try:
            for expr in parent.getChildren():
                self.get_args(expr, func_args)
        except AttributeError:
            # we reached a TerminalNodeImpl it does not have
            # children, guess why, hehe because it is terminal
            return

    def enterCompilationUnit(self, ctx: CParser.CompilationUnitContext):
        for child in ctx.getChildren():
            match type(child):
                case CParser.DeclarationListContext:
                    for declaration in child.getChildren():
                        match type(declaration):
                            case CParser.VariableDeclarationContext:
                                self.add_indentation()
                                value = self.enterVariableDeclaration(
                                    declaration)
                                self.write(value)
                                self.add_newline()
                            case CParser.FunctionDeclarationContext:
                                self.add_indentation()
                                value = self.enterFunctionDeclaration(
                                    declaration)
                                self.write(value)
                                self.add_newline()
                case CParser.DefinitionListContext:
                    for definition in child.getChildren():
                        match type(definition):
                            case CParser.VariableDefinitionContext:
                                self.add_indentation()
                                value = self.enterVariableDefinition(
                                    definition)
                                self.write(value)
                                self.add_newline()
                            case CParser.FunctionDefinitionContext:
                                self.add_indentation()
                                value = self.enterFunctionDefinition(
                                    definition)
                                self.write(value)
                                self.add_newline()
                case CParser.FunctionCallContext:
                    self.add_indentation()
                    value = self.enterFunctionCall(child)
                    self.write(value)
                    self.add_newline()
                case CParser.AssignmentContext:
                    self.add_indentation()
                    value = self.enterAssignment(child)
                    self.write(value)
                    self.add_newline()

    def enterTypeSpecifier(self, ctx: CParser.TypeSpecifierContext):
        return self.match_type_specifier(ctx)

    def enterVariableDefinition(self, ctx: CParser.VariableDefinitionContext):
        type_specifier = self.enterTypeSpecifier(ctx.typeSpecifier())
        identifier = ctx.identifier().getText()
        expression = self.enterExpression(ctx.expression())
        return f'{type_specifier} {identifier} = {expression};'

    def enterVariableDeclaration(self,
                                 ctx: CParser.VariableDeclarationContext):
        ctx.scope_level = self.state.scope_level
        # self.check_variable_declaration(ctx)
        type_specifier = self.enterTypeSpecifier(ctx.typeSpecifier())
        identifier = ctx.identifier().getText()
        return f'{type_specifier} {identifier};'

    def enterFunctionDeclaration(self,
                                 ctx: CParser.FunctionDeclarationContext):
        type_specifier = self.match_type_specifier(ctx.typeSpecifier())
        identifier = ctx.identifier().getText()
        func_args = []
        # recursive func to visit nodes
        self.get_args(ctx.functionArgs(), func_args)
        args = ', '.join(func_args)
        return f'{type_specifier} {identifier}({args});'

    def enterFunctionDefinition(self, ctx: CParser.FunctionDefinitionContext):
        # typeSpecifier? identifier LP functionArgs? RP block
        self.state.enter_block_scope()
        rtype: str = self.match_type_specifier(ctx.typeSpecifier())
        identifier: str = ctx.identifier().getText()
        args: str = self.enterFunctionArgs(ctx.functionArgs())
        block: str = self.enterBlock(ctx.block())
        self.state.exit_block_scope()

        return f'{rtype} {identifier}({args}) {"{"}\n {block}\n{"}"}'

    def enterFunctionArgs(self, ctx: CParser.FunctionArgsContext):
        func_args = []
        # recursive func to visit nodes
        self.get_args(ctx, func_args)
        return ', '.join(func_args)

    def enterAssignment(self, ctx: CParser.AssignmentContext):
        # identifier ASSIGN expression SEMI
        self.check_variable_assignment(ctx)
        identifier: str = ctx.identifier().getText()
        expression: CParser.ExpressionContext = ctx.expression()
        return f'{identifier} = {self.enterExpression(expression)};'

    def enterInplaceAssignment(self, ctx: CParser.InplaceAssignmentContext):
        identifier: str = ctx.identifier().getText()
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

        expression: str = self.enterExpression(ctx.expression())

        return f'{identifier} {operator} {expression};'

    def enterFunctionCall(self, ctx: CParser.FunctionCallContext):
        return ctx.getText()

    def enterFunctionReturn(self, ctx: CParser.FunctionReturnContext):
        if ctx.expression():
            return f'return {ctx.expression().getText()};'
        else:
            return 'return;'

    def enterIfStatementStructure(self,
                                  ctx: CParser.IfStatementStructureContext):
        result: str = ''
        tabs = '\t' * self.state.scope_level
        for child in ctx.getChildren():
            match type(child):
                case CParser.IfStatementContext:
                    result += tabs
                    value = self.enterIfStatement(child)
                    result += value
                    result += '\n'
                case CParser.ElseIfStatementContext:
                    result += tabs
                    value = self.enterElseIfStatement(child)
                    result += value
                    result += '\n'
                case CParser.ElseStatementContext:
                    result += tabs
                    value = self.enterElseStatement(child)
                    result += value
                    result += '\n'
        return result

    def enterIfStatement(self, ctx: CParser.IfStatementContext):
        self.state.enter_block_scope()
        conditions: list[CParser.ConditionContext] = [
            condition for condition in ctx.getChildren()
            if isinstance(condition, CParser.ConditionContext)
        ]
        values: list[str] = list(map(self.enterCondition, conditions))
        block: str = self.enterBlock(ctx.block())
        self.state.exit_block_scope()
        return f'if ({", ".join(values)}) {"{"}\n {block}\n{self.state.tabs}{"}"}'

    def enterElseIfStatement(self, ctx: CParser.ElseIfStatementContext):
        if_statement: str = self.enterIfStatement(ctx.ifStatement())
        return f'else {if_statement}'

    def enterElseStatement(self, ctx: CParser.ElseStatementContext):
        self.state.enter_block_scope()
        block: str = self.enterBlock(ctx.block())
        self.state.exit_block_scope()
        return f'else {"{"}\n {block}\n{self.state.tabs}{"}"}'

    def enterWhileStatement(self, ctx: CParser.WhileStatementContext):
        self.state.enter_block_scope()
        conditions: list[CParser.ConditionContext] = [
            condition for condition in ctx.getChildren()
            if isinstance(condition, CParser.ConditionContext)
        ]
        values = list(map(self.enterCondition, conditions))
        block: str = self.enterBlock(ctx.block())
        self.state.exit_block_scope()

        return f'while ({", ".join(values)}) {"{"}\n {block}\n{self.state.tabs}{"}"}'

    def enterDoWhileStatement(self, ctx: CParser.DoWhileStatementContext):
        self.state.enter_block_scope()
        conditions: list[CParser.ConditionContext] = [
            condition for condition in ctx.getChildren()
            if isinstance(condition, CParser.ConditionContext)
        ]
        values = list(map(self.enterCondition, conditions))
        block: str = self.enterBlock(ctx.block())
        self.state.exit_block_scope()

        return f'do {"{"}\n {block}\n{self.state.tabs}{"}"} while ({", ".join(values)});'

    def enterCondition(self, ctx: CParser.ConditionContext):
        expressions: list[CParser.ExpressionContext] = [
            expression for expression in ctx.getChildren()
            if isinstance(expression, CParser.ExpressionContext)
        ]
        values = list(map(self.enterExpression, expressions))
        return ' '.join(values)

    def enterExpression(self, ctx: CParser.ExpressionContext):
        values = []
        for child in ctx.getChildren():
            if isinstance(child, CParser.ExpressionContext):
                values.append(self.enterExpression(child))
            elif isinstance(child, CParser.UnarySignContext):
                values.append(child.getText())
            elif isinstance(child, CParser.ConstantContext):
                values.append(child.getText())
            elif isinstance(child, CParser.FunctionCallExpressionContext):
                values.append(child.getText())
            elif isinstance(child, CParser.IdentifierContext):
                values.append(child.getText())
            elif isinstance(child, TerminalNodeImpl):
                values.append(child.getText())
        return ' '.join(values)

    def enterBlock(self, ctx: CParser.BlockContext):
        """
                block
            : LC (
                expression
              | ifStatementStructure
              | whileStatement
              | doWhileStatement
              | variableDefinition
              | definitionList
              | declarationList
              | functionCall
              | assignment
              | inplaceAssignment
              | functionReturn
             )* RC
           ;
        """
        result: str = ''
        tabs = '\t' * self.state.scope_level
        for child in ctx.getChildren():
            match type(child):
                case CParser.DeclarationListContext:
                    for declaration in child.getChildren():
                        match type(declaration):
                            case CParser.VariableDeclarationContext:
                                result += tabs
                                value = self.enterVariableDeclaration(
                                    declaration)
                                result += value
                                result += '\n'
                case CParser.DefinitionListContext:
                    for definition in child.getChildren():
                        match type(definition):
                            case CParser.VariableDefinitionContext:
                                result += tabs
                                value = self.enterVariableDefinition(
                                    definition)
                                result += value
                                result += '\n'
                case CParser.FunctionCallContext:
                    result += tabs
                    value = self.enterFunctionCall(child)
                    result += value
                    result += '\n'
                case CParser.VariableDefinitionContext:
                    result += tabs
                    value = self.enterVariableDefinition(child)
                    result += value
                    result += '\n'
                case CParser.AssignmentContext:
                    result += tabs
                    value = self.enterAssignment(child)
                    result += value
                    result += '\n'
                case CParser.InplaceAssignmentContext:
                    result += tabs
                    value = self.enterInplaceAssignment(child)
                    result += value
                    result += '\n'
                case CParser.IfStatementStructureContext:
                    value = self.enterIfStatementStructure(child)
                    result += value
                    result += '\n'
                case CParser.WhileStatementContext:
                    result += tabs
                    value = self.enterWhileStatement(child)
                    result += value
                    result += '\n'
                case CParser.DoWhileStatementContext:
                    result += tabs
                    value = self.enterDoWhileStatement(child)
                    result += value
                    result += '\n'
                case CParser.FunctionReturnContext:
                    result += tabs
                    value = self.enterFunctionReturn(child)
                    result += value
                    result += '\n'

        # remove the last new line result[:-1]
        # self.ungetch()
        return result[:-1]

    def exitBlock(self, ctx: CParser.BlockContext):
        self.state.exit_block_scope()
