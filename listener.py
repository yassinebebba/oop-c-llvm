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

    def enterDeclaration(self, ctx: CParser.DeclarationContext):
        pass

    def enterVariableDeclaration(self,
                                 ctx: CParser.VariableDeclarationContext):
        if self.state == State.FUNC_BLOCK:
            self.output.write('\t')

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

    def enterFunctionDefinition(self, ctx: CParser.FunctionDefinitionContext):
        for child in ctx.getChildren():
            if isinstance(child, CParser.TypeSpecifierContext):
                self.output.write(child.getText() + ' ')
            if isinstance(child, CParser.FunctionNameContext):
                self.output.write(child.getText())
            if isinstance(child, CParser.FunctionArgsContext):
                self.output.write(child.getText())

    def enterAssignment(self, ctx: CParser.AssignmentContext):
        if self.state == State.FUNC_BLOCK:
            self.output.write('\t')
        for child in ctx.getChildren():
            if isinstance(child, TerminalNodeImpl):
                self.output.write(child.getText() + ' ')
            if isinstance(child, CParser.TypeSpecifierContext):
                chunks: list[str] = []
                for terminal_node in child.children:
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
