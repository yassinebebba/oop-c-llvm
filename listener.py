from core.CParser import CParser
from core.CListener import CListener
from io import FileIO


class Listener(CListener):
    def __init__(self, output):
        self.output: FileIO = output

    def enterProgram(self, ctx: CParser.CompilationUnitContext):
        pass

    def enterDeclaration(self, ctx: CParser.DeclarationContext):
        # print(ctx.getChild(0))
        # print(ctx.getChild(1))
        # print(ctx.getChild(2))
        ...

    def enterFunctionDeclaration(self, ctx: CParser.FunctionDeclarationContext):
        func_rt = ctx.getChild(0)
        func_name = ctx.getChild(1)
        func_args = ctx.getChild(2)
        func_rt = func_rt.getText() if func_rt else None
        func_name = func_name.getText() if func_name else None
        func_args = func_args.getText() if func_args else None
        print(f'{func_rt=}, {func_name=}, {func_args=}')
        self.output.write(f'{func_rt} {func_name}{func_args};')
        self.output.write('\n')

    def enterFunctionName(self, ctx: CParser.FunctionNameContext):
        pass

    def enterBlock(self, ctx:CParser.BlockContext):
        print(ctx.getText())

    def enterTypeSpecifier(self, ctx:CParser.TypeSpecifierContext):
        print(ctx.getText())
