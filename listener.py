from core.CParser import CParser
from core.CListener import CListener
from io import FileIO
from antlr4.tree.Tree import TerminalNodeImpl
from enum import Enum


class State(Enum):
    NOTHING = 0
    FUNC_BLOCK = 1


class Listener(CListener):
    def __init__(self, output):
        self.output: FileIO = output
        self.state = State.NOTHING

    def add_newline(self):
        self.output.write('\n')

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

    def enterVariableDeclaration(self,
                                 ctx: CParser.VariableDeclarationContext):
        if self.state == State.FUNC_BLOCK:
            self.output.write('\t')

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
                if (x := child.getText()) in '()':
                    self.output.write(x)
            if isinstance(child, CParser.FunctionArgsContext):
                func_args = []
                # recursive func to visit nodes
                self.get_args(child, func_args)
                self.output.write(', '.join(func_args))

    def enterAssignment(self, ctx: CParser.AssignmentContext):
        if self.state == State.FUNC_BLOCK:
            self.output.write('\t')
        for child in ctx.getChildren():
            if isinstance(child, TerminalNodeImpl):
                self.output.write(child.getText() + ' ')
            if isinstance(child, CParser.TypeSpecifierContext):
                self.match_type_specifier(child)
            if isinstance(child, CParser.IdentifierContext):
                self.output.write(child.getText() + ' ')
            if isinstance(child, CParser.ExpressionContext):
                self.output.write(child.getText())
        self.add_newline()

    def enterFunctionCall(self, ctx: CParser.FunctionCallContext):
        if self.state == State.FUNC_BLOCK:
            self.output.write('\t')
        self.output.write(ctx.getText())
        self.add_newline()

    def enterFunctionBlock(self, ctx: CParser.FunctionBlockContext):
        self.state = State.FUNC_BLOCK
        self.output.write('{')
        self.add_newline()

    def exitFunctionBlock(self, ctx: CParser.FunctionBlockContext):
        self.state = State.NOTHING
        self.output.write('}')
        self.add_newline()
