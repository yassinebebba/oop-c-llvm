from core.CParser import CParser
from core.CListener import CListener
from io import FileIO
from antlr4.tree.Tree import TerminalNodeImpl


class Listener(CListener):
    def __init__(self, output):
        self.output: FileIO = output

    def add_newline(self):
        self.output.write('\n')

    def enterDeclaration(self, ctx: CParser.DeclarationContext):
        pass

    def enterVariableDeclaration(self, ctx:CParser.VariableDeclarationContext):
        for child in ctx.getChildren():
            if isinstance(child, CParser.TypeSpecifierContext):
                self.output.write(child.getText() + ' ')
            if isinstance(child, CParser.IdentifierContext):
                self.output.write(child.getText())
        self.output.write(';')
        self.add_newline()

    def enterFunctionDeclaration(self,
                                 ctx: CParser.FunctionDeclarationContext):
        for child in ctx.getChildren():
            if isinstance(child, CParser.TypeSpecifierContext):
                self.output.write(child.getText() + ' ')
            if isinstance(child, CParser.FunctionNameContext):
                self.output.write(child.getText())
            if isinstance(child, CParser.FunctionArgsContext):
                self.output.write(child.getText())

        self.output.write(';')
        self.add_newline()

    def enterAssignment(self, ctx: CParser.AssignmentContext):
        for child in ctx.getChildren():
            if isinstance(child, TerminalNodeImpl):
                self.output.write(child.getText() + ' ')
            if isinstance(child, CParser.TypeSpecifierContext):
                self.output.write(child.getText() + ' ')
            if isinstance(child, CParser.IdentifierContext):
                self.output.write(child.getText() + ' ')
            if isinstance(child, CParser.ExpressionContext):
                self.output.write(child.getText())
        self.add_newline()

    def enterBlock(self, ctx: CParser.BlockContext):
        print(ctx.getText())
