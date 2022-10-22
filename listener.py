import os
from core.CParser import CParser
from core.CListener import CListener
from io import FileIO
from antlr4.tree.Tree import TerminalNodeImpl


class State:
    def __init__(self):
        self.global_scope = True
        self.block_scope = False
        self.indentation_count = 0

    def enter_block_scope(self):
        self.indentation_count += 1
        self.global_scope = False
        self.block_scope = True

    def exit_block_scope(self):
        self.indentation_count -= 1
        if self.indentation_count == 0:
            self.global_scope = True
            self.block_scope = False


class Listener(CListener):
    def __init__(self, output):
        self.output: FileIO = output
        self.state = State()

    def add_newline(self) -> None:
        self.output.write('\n')

    def add_indentation(self):
        if self.state.block_scope:
            self.output.write('\t' * self.state.indentation_count)

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

        self.output.write(' '.join(chunks) + ' ')

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

    def enterDeclaration(self, ctx: CParser.DeclarationContext):
        pass

    def enterVariableInitialization(self,
                                    ctx: CParser.VariableInitializationContext):
        self.add_indentation()
        for child in ctx.typeSpecifier().getChildren():
            self.output.write(f'{child.getText()} ')
        self.output.write(
            f'{ctx.identifier().getText()} = {self.enterExpression(ctx.expression())};')
        self.add_newline()

    def enterVariableDeclaration(self,
                                 ctx: CParser.VariableDeclarationContext):
        self.add_indentation()
        for child in ctx.getChildren():
            if isinstance(child, CParser.TypeSpecifierContext):
                self.match_type_specifier(child)
            if isinstance(child, CParser.IdentifierContext):
                self.output.write(child.getText())
        self.output.write(';')
        self.add_newline()

    def enterFunctionDeclaration(self,
                                 ctx: CParser.FunctionDeclarationContext):
        for child in ctx.getChildren():
            if isinstance(child, CParser.TypeSpecifierContext):
                self.match_type_specifier(child)
            if isinstance(child, CParser.FunctionNameContext):
                self.output.write(child.getText())

            if (x := child.getText()) in '()':
                self.output.write(x)
            if isinstance(child, CParser.FunctionArgsContext):
                func_args = []
                # recursive func to visit nodes
                self.get_args(child, func_args)
                self.output.write(', '.join(func_args))

        self.output.write(';')
        self.add_newline()

    def enterFunctionDefinition(self, ctx: CParser.FunctionDefinitionContext):
        for child in ctx.getChildren():
            if isinstance(child, CParser.TypeSpecifierContext):
                self.match_type_specifier(child)
            if isinstance(child, CParser.FunctionNameContext):
                self.output.write(child.getText())
            if isinstance(child, TerminalNodeImpl):
                # TODO: this should probably be changed to enter FunctionArgs
                match child.getText():
                    case '(':
                        self.output.write('(')
                    case ')':
                        self.output.write(') ')

            if isinstance(child, CParser.FunctionArgsContext):
                func_args = []
                # recursive func to visit nodes
                self.get_args(child, func_args)
                self.output.write(', '.join(func_args))

    def exitFunctionDefinition(self, ctx: CParser.FunctionDefinitionContext):
        # overriding this method just for styling purpose
        self.add_newline()

    def enterAssignment(self, ctx: CParser.AssignmentContext):
        self.add_indentation()
        for child in ctx.getChildren():
            if isinstance(child, TerminalNodeImpl):
                self.output.write(child.getText() + ' ')
            if isinstance(child, CParser.TypeSpecifierContext):
                self.match_type_specifier(child)
            if isinstance(child, CParser.IdentifierContext):
                self.output.write(child.getText() + ' ')
            if isinstance(child, CParser.ExpressionContext):
                self.output.write(self.enterExpression(child))
        self.add_newline()

    def enterInplaceAssignment(self, ctx: CParser.InplaceAssignmentContext):
        self.add_indentation()
        for child in ctx.getChildren():
            if isinstance(child, TerminalNodeImpl):
                self.output.write(child.getText() + ' ')
            if isinstance(child, CParser.IdentifierContext):
                self.output.write(child.getText() + ' ')
            if isinstance(child, CParser.ExpressionContext):
                self.output.write(self.enterExpression(child))
        self.add_newline()

    def enterFunctionCall(self, ctx: CParser.FunctionCallContext):
        self.add_indentation()
        self.output.write(ctx.getText())
        self.add_newline()

    def enterFunctionReturn(self, ctx: CParser.FunctionReturnContext):
        self.add_indentation()
        if ctx.expression():
            self.output.write(f'return {ctx.expression().getText()};')
        else:
            self.output.write('return;')
        self.add_newline()

    def enterIfStatementStructure(self,
                                  ctx: CParser.IfStatementStructureContext):
        self.add_newline()
        self.add_indentation()
        for child in ctx.getChildren():
            if isinstance(child, CParser.IfStatementContext):
                self.output.write(self.enterIfStatement(child))

    def enterIfStatement(self, ctx: CParser.IfStatementContext):
        conditions: list[CParser.ConditionContext] = [
            condition for condition in ctx.getChildren()
            if isinstance(condition, CParser.ConditionContext)
        ]
        values = list(map(self.enterCondition, conditions))
        return f'if ({", ".join(values)}) '

    def enterElseIfStatement(self, ctx: CParser.ElseIfStatementContext):
        self.output.write(f' else {self.enterIfStatement(ctx.ifStatement())} ')

    def exitElseIfStatement(self, ctx: CParser.ElseIfStatementContext):
        self.add_newline()

    def enterElseStatement(self, ctx: CParser.ElseStatementContext):
        self.ungetch()
        self.output.write(f' else ')

    def exitElseStatement(self, ctx: CParser.ElseIfStatementContext):
        self.add_newline()

    def enterWhileStatement(self, ctx: CParser.WhileStatementContext):
        self.add_indentation()
        conditions: list[CParser.ConditionContext] = [
            condition for condition in ctx.getChildren()
            if isinstance(condition, CParser.ConditionContext)
        ]
        values = list(map(self.enterCondition, conditions))
        self.output.write(f'while ({", ".join(values)}) ')

    def exitWhileStatement(self, ctx: CParser.WhileStatementContext):
        # overriding this method just for styling purpose
        self.add_newline()

    def enterDoWhileStatement(self, ctx: CParser.DoWhileStatementContext):
        self.add_indentation()
        self.output.write(f'do ')

    def exitDoWhileStatement(self, ctx: CParser.DoWhileStatementContext):
        conditions: list[CParser.ConditionContext] = [
            condition for condition in ctx.getChildren()
            if isinstance(condition, CParser.ConditionContext)
        ]
        values = list(map(self.enterCondition, conditions))
        self.output.write(f' while ({", ".join(values)});')
        self.add_newline()

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
        self.state.enter_block_scope()
        self.output.write('{')
        self.add_newline()

    def exitBlock(self, ctx: CParser.BlockContext):
        self.state.exit_block_scope()
        self.add_indentation()
        self.output.write('}')
