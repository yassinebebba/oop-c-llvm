import os
from termcolor import colored
from core.CParser import CParser
from core.CListener import CListener
from io import FileIO
from antlr4.tree.Tree import TerminalNodeImpl
from antlr4.tree.Tree import Token


class State:
    def __init__(self):
        self.is_class = False
        self.scope_level = 0

    @property
    def tabs(self):
        return '\t' * self.scope_level

    def enter_block_scope(self):
        self.scope_level += 1

    def exit_block_scope(self):
        if self.scope_level > 0:
            self.scope_level -= 1

    def enter_class(self):
        self.is_class = True

    def exit_class(self):
        self.is_class = False


def print_error(error: str):
    print(colored(error, 'red'))


class Listener(CListener):
    def __init__(self, stream, output):
        # steam is CommonTokenStream to get hidden channel
        self.stream = stream
        self.output: FileIO = output
        self.state = State()
        self.identifiers = {
            'declared_variables': [],
            'initialized_variables': [],
            'functions': {},
            'clazzes': {}
        }
        self.clazzes = {}
        self.objs = {}

    def write(self, text: str):
        self.output.write(text)

    def add_newline(self) -> None:
        self.output.write('\n')

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

    def enterCompilationUnit(self, ctx: CParser.CompilationUnitContext):
        for token in self.stream.tokens:
            # access hidden channel
            if token.channel == 1:
                self.write(f'{token.text.strip()}\n')

        for child in ctx.getChildren():
            match type(child):
                case CParser.DeclarationListContext:
                    for declaration in child.getChildren():
                        match type(declaration):
                            case CParser.VariableDeclarationContext:
                                value = self.state.tabs
                                value += self.enterVariableDeclaration(
                                    declaration)
                                self.write(value)
                                self.add_newline()
                            case CParser.FunctionDeclarationContext:
                                value = self.state.tabs
                                value += self.enterFunctionDeclaration(
                                    declaration)
                                self.write(value)
                                self.add_newline()
                            case CParser.StructDeclarationContext:
                                value = self.state.tabs
                                value += self.enterStructDeclaration(
                                    declaration)
                                self.write(value)
                                self.add_newline()
                case CParser.DefinitionListContext:
                    for definition in child.getChildren():
                        match type(definition):
                            case CParser.VariableDefinitionContext:
                                value = self.state.tabs
                                value += self.enterVariableDefinition(
                                    definition)
                                self.write(value)
                                self.add_newline()
                            case CParser.FunctionDefinitionContext:
                                value = self.state.tabs
                                value += self.enterFunctionDefinition(
                                    definition)
                                self.write(value)
                                self.add_newline()
                            case CParser.StructDefinitionContext:
                                value = self.state.tabs
                                value += self.enterStructDefinition(
                                    definition)
                                self.write(value)
                                self.add_newline()
                case CParser.FunctionCallContext:
                    value = self.state.tabs
                    value += self.enterFunctionCall(child)
                    self.write(value)
                    self.add_newline()
                case CParser.AssignmentContext:
                    value = self.state.tabs
                    value += self.enterAssignment(child)
                    self.write(value)
                    self.add_newline()
                case CParser.ClassDefinitionContext:
                    value = self.state.tabs
                    value += self.enterClassDefinition(child)
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
        args: str = self.enterFunctionArgs(ctx.functionArgs())
        return f'{type_specifier} {identifier}({args});'

    def enterFunctionDefinition(self, ctx: CParser.FunctionDefinitionContext):
        # typeSpecifier? identifier LP functionArgs? RP block
        self.state.enter_block_scope()
        rtype: str = self.match_type_specifier(ctx.typeSpecifier())
        identifier: str = ctx.identifier().getText()
        args: str = self.enterFunctionArgs(ctx.functionArgs())
        block: str = self.enterBlock(ctx.block())
        self.state.exit_block_scope()

        # i think this block should be somewhere else
        original_identifier: str = identifier
        if self.state.is_class:
            # this is a class method
            # class ctx -> class block ctx -> class method ctx
            class_name = ctx.parentCtx.parentCtx.identifier().getText()
            identifier = f'{class_name}_{identifier}'
            if args:
                args = f'{class_name} * self, {args}'
            else:
                args = f'{class_name} * self'
            self.clazzes[class_name][original_identifier] = {
                'original_name': original_identifier,
                'new_name': identifier,
            }
        return f'{rtype} {identifier}({args}) {"{"}\n {block}\n{self.state.tabs}{"}"}'

    def enterFunctionArgs(self, ctx: CParser.FunctionArgsContext):
        if ctx is None:
            return ''
        args: list[CParser.ArgContext] = [
            arg for arg in ctx.getChildren()
            if isinstance(arg, CParser.ArgContext)
        ]
        values = list(map(self.enterArg, args))
        return ', '.join(values)

    def enterArg(self, ctx: CParser.ArgContext):
        type_specifier: str = self.enterTypeSpecifier(ctx.typeSpecifier())
        if ctx.identifier():
            return f'{type_specifier} {ctx.identifier().getText()}'
        return type_specifier

    def enterStructDeclaration(self, ctx: CParser.StructDeclarationContext):
        return f'struct {ctx.identifier().getText()};'

    def enterStructDefinition(self, ctx: CParser.StructDefinitionContext):
        self.state.enter_block_scope()
        struct_block: str = self.enterStructBlock(ctx.structBlock())
        self.state.exit_block_scope()
        return f'struct {ctx.identifier().getText()} {"{"}\n{struct_block}\n{self.state.tabs}{"}"};'

    def enterStructBlock(self, ctx: CParser.StructBlockContext):
        if ctx is None:
            return ''

        result: str = ''
        for child in ctx.getChildren():
            match type(child):
                case CParser.FieldContext:
                    result += self.state.tabs
                    value = self.enterField(child)
                    result += value
                    result += '\n'
                case CParser.BitFieldContext:
                    result += self.state.tabs
                    value = self.enterBitField(child)
                    result += value
                    result += '\n'

        # [:-1] remove the last newline
        return result[:-1]

    def enterField(self, ctx: CParser.FieldContext):
        type_specifier: str = self.match_type_specifier(ctx.typeSpecifier())
        return f'{type_specifier} {ctx.identifier().getText()};'

    def enterBitField(self, ctx: CParser.BitFieldContext):
        type_specifier: str = self.match_type_specifier(ctx.typeSpecifier())
        identifier: str = ctx.identifier().getText()
        bit_count: str = ctx.INTEGER_CONSTANT()
        return f'{type_specifier} {identifier}: {bit_count};'

    def enterAssignment(self, ctx: CParser.AssignmentContext):
        # identifier ASSIGN expression SEMI
        # self.check_variable_assignment(ctx)
        identifier: str = ''
        try:
            identifier = ctx.identifier().getText()
        except AttributeError:
            for child in ctx.getChildren():
                if child.getText() == '=':
                    break
                identifier += child.getText()
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
        args = self.enterFunctionCallArgs(ctx.functionCallArgs())
        return f'{ctx.identifier().getText()}({args});'

    def enterFunctionCallArgs(self, ctx: CParser.FunctionCallArgsContext):
        if ctx is None:
            return ''
        expressions: list[CParser.ExpressionContext] = [
            arg for arg in ctx.getChildren()
            if isinstance(arg, CParser.ExpressionContext)
        ]
        values: list[str] = list(map(self.enterExpression, expressions))
        return ', '.join(values)

    def enterFunctionReturn(self, ctx: CParser.FunctionReturnContext):
        if ctx.expression():
            return f'return {ctx.expression().getText()};'
        else:
            return 'return;'

    def enterIfStatementStructure(self,
                                  ctx: CParser.IfStatementStructureContext):
        result: str = ''
        for child in ctx.getChildren():
            match type(child):
                case CParser.IfStatementContext:
                    result += self.state.tabs
                    value = self.enterIfStatement(child)
                    result += value
                    result += '\n'
                case CParser.ElseIfStatementContext:
                    result += self.state.tabs
                    value = self.enterElseIfStatement(child)
                    result += value
                    result += '\n'
                case CParser.ElseStatementContext:
                    result += self.state.tabs
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
        return ', '.join(values)

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
            elif isinstance(child, CParser.ChainedCallContext):
                values.append(self.enterChainedCall(child))
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
        for child in ctx.getChildren():
            match type(child):
                case CParser.DeclarationListContext:
                    for declaration in child.getChildren():
                        match type(declaration):
                            case CParser.VariableDeclarationContext:
                                result += self.state.tabs
                                value = self.enterVariableDeclaration(
                                    declaration)
                                result += value
                                result += '\n'
                            case CParser.StructDeclarationContext:
                                result += self.state.tabs
                                value = self.enterStructDeclaration(
                                    declaration)
                                result += value
                                result += '\n'
                case CParser.DefinitionListContext:
                    for definition in child.getChildren():
                        match type(definition):
                            case CParser.VariableDefinitionContext:
                                result += self.state.tabs
                                value = self.enterVariableDefinition(
                                    definition)
                                result += value
                                result += '\n'
                            case CParser.StructDefinitionContext:
                                result += self.state.tabs
                                value = self.enterStructDefinition(
                                    definition)
                                result += value
                                result += '\n'
                case CParser.FunctionCallContext:
                    result += self.state.tabs
                    value = self.enterFunctionCall(child)
                    result += value
                    result += '\n'
                case CParser.VariableDefinitionContext:
                    result += self.state.tabs
                    value = self.enterVariableDefinition(child)
                    result += value
                    result += '\n'
                case CParser.AssignmentContext:
                    result += self.state.tabs
                    value = self.enterAssignment(child)
                    result += value
                    result += '\n'
                case CParser.InplaceAssignmentContext:
                    result += self.state.tabs
                    value = self.enterInplaceAssignment(child)
                    result += value
                    result += '\n'
                case CParser.IfStatementStructureContext:
                    value = self.enterIfStatementStructure(child)
                    result += value
                    result += '\n'
                case CParser.WhileStatementContext:
                    result += self.state.tabs
                    value = self.enterWhileStatement(child)
                    result += value
                    result += '\n'
                case CParser.DoWhileStatementContext:
                    result += self.state.tabs
                    value = self.enterDoWhileStatement(child)
                    result += value
                    result += '\n'
                case CParser.FunctionReturnContext:
                    result += self.state.tabs
                    value = self.enterFunctionReturn(child)
                    result += value
                    result += '\n'
                case CParser.ClassInstantiationContext:
                    result += self.state.tabs
                    value = self.enterClassInstantiation(child)
                    result += value
                    result += '\n'
                case CParser.ChainedCallContext:
                    result += self.state.tabs
                    value = self.enterChainedCall(child)
                    result += f'{value};'
                    result += '\n'

        # remove the last new line result[:-1]
        # self.ungetch()
        return result[:-1]

    def exitBlock(self, ctx: CParser.BlockContext):
        self.state.exit_block_scope()

    def enterClassDefinition(self, ctx: CParser.ClassDefinitionContext):
        self.state.enter_block_scope()
        self.state.enter_class()
        identifier: str = ctx.identifier().getText()
        self.clazzes[identifier] = {}
        attributes, methods = self.enterClassBlock(ctx.classBlock())
        self.state.exit_class()
        self.state.exit_block_scope()
        return f'typedef struct {identifier} {"{"}\n {attributes}\n{"}"} {identifier};\n{methods}'

    def getFunctionPointer(self, class_name: str,
                           function: CParser.FunctionDefinitionContext):
        type_specifier: str = self.match_type_specifier(
            function.typeSpecifier())
        identifier: str = function.identifier().getText()

        # struct {class_name} * self: is always the 1st arg
        args: list[str] = [f'struct {class_name} * self']
        if function.functionArgs():
            for arg in function.functionArgs().getChildren():
                try:
                    args.append(self.match_type_specifier(arg.typeSpecifier()))
                except AttributeError:
                    # skip, it is not a func arg
                    continue
        return f'{type_specifier} (*{class_name}_{identifier})({", ".join(args)});'

    def createClassConstructor(self,
                               class_name: str,
                               constructor: CParser.FunctionDefinitionContext | None,
                               methods: list[
                                   CParser.FunctionDefinitionContext]):
        method_name: str = constructor.identifier().getText()
        new_method_name: str = f'{class_name}_{method_name}'
        args: str = self.enterFunctionArgs(constructor.functionArgs())
        if args:
            args = f'{class_name} * self, {args}'
        else:
            args = f'{class_name} * self'

        self.clazzes[class_name][method_name] = {
            'original_name': method_name,
            'new_name': new_method_name,
        }
        method_block: str = ''
        for method in methods:
            if method.identifier().getText() == '__init__':
                continue
            name: str = method.identifier().getText()
            new_name: str = f'{class_name}_{name}'
            method_block += f'{self.state.tabs}self->{new_name} = &{new_name};\n'
        if constructor:
            method_block += self.enterBlock(constructor.block())

        return f'void {new_method_name}({args}) {"{"}\n{method_block}\n{"}"}'

    def enterClassBlock(self, ctx: CParser.ClassBlockContext):
        class_name: str = ctx.parentCtx.identifier().getText()
        attribute_declarations: list[CParser.VariableDeclarationContext] = []
        attribute_definitions: list[CParser.VariableDefinitionContext] = []
        methods: list[CParser.FunctionDefinitionContext] = []

        for child in ctx.getChildren():
            match type(child):
                case CParser.VariableDeclarationContext:
                    attribute_declarations.append(child)
                case CParser.VariableDefinitionContext:
                    attribute_definitions.append(child)
                case CParser.FunctionDefinitionContext:
                    methods.append(child)

        attributes: str = ''

        for attribute in attribute_declarations:
            attributes += self.state.tabs
            value = self.enterVariableDeclaration(attribute)
            attributes += value
            attributes += '\n'

        # attribute definition is quite tricky to handle
        # it has to be split into declaration and initialization
        # in the class constructor
        for attribute in attribute_definitions:
            attributes += self.state.tabs
            value = self.enterVariableDefinition(attribute)
            attributes += value
            attributes += '\n'

        parsed_methods: str = ''
        constructor: CParser.FunctionDefinitionContext | None = None
        for method in methods:
            if method.identifier().getText() == '__init__':
                constructor = method
                continue
            function_pointer = self.getFunctionPointer(class_name, method)
            attributes += self.state.tabs
            attributes += function_pointer
            attributes += '\n'
            self.state.exit_block_scope()
            self.state.exit_block_scope()
            value = self.enterFunctionDefinition(method)
            self.state.enter_block_scope()
            parsed_methods += value
            parsed_methods += '\n'

        parsed_constructor = self.createClassConstructor(class_name,
                                                         constructor,
                                                         methods)
        parsed_methods += parsed_constructor
        return attributes[:-1], parsed_methods

    def enterClassInstantiation(self, ctx: CParser.ClassInstantiationContext):
        type_specifier: str = self.match_type_specifier(ctx.typeSpecifier())
        class_name: str = type_specifier.split()[0]  # to remove the pointer
        identifier: str = ctx.identifier().getText()
        args: str = self.enterFunctionCallArgs(
            ctx.functionCall().functionCallArgs())
        self.objs[identifier] = {
            'class_name': class_name
        }
        result: str = f'{type_specifier} {identifier} = malloc(sizeof({class_name}));\n'
        result += f'{self.state.tabs}{class_name}___init__({identifier}, {args});'
        return result

    def enterChainedCall(self, ctx: CParser.ChainedCallContext):
        obj_name: str = ctx.identifier(0).getText()
        if obj_name not in self.objs:
            return ''
        result: str = ''
        class_name = self.objs[obj_name]['class_name']
        for child in ctx.getChildren():
            if isinstance(child, CParser.FunctionCallExpressionContext):
                method = self.clazzes[class_name][child.identifier().getText()]
                args: str = self.enterFunctionCallArgs(
                    child.functionCallArgs())
                method_alias = method['new_name']
                if args:
                    result += f'{method_alias}({obj_name}, {args})'
                else:
                    result += f'{method_alias}({obj_name})'
            else:
                result += child.getText()
        return result
