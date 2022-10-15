# Generated from C.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CParser import CParser
else:
    from CParser import CParser

# This class defines a complete generic visitor for a parse tree produced by CParser.

class CVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CParser#program.
    def visitProgram(self, ctx:CParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#statement_list.
    def visitStatement_list(self, ctx:CParser.Statement_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#declaration_list.
    def visitDeclaration_list(self, ctx:CParser.Declaration_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#declaration.
    def visitDeclaration(self, ctx:CParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#function_declaration.
    def visitFunction_declaration(self, ctx:CParser.Function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#type_specifier.
    def visitType_specifier(self, ctx:CParser.Type_specifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#function_name.
    def visitFunction_name(self, ctx:CParser.Function_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#function_args.
    def visitFunction_args(self, ctx:CParser.Function_argsContext):
        return self.visitChildren(ctx)



del CParser