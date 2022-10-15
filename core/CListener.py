# Generated from core/C.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CParser import CParser
else:
    from CParser import CParser

# This class defines a complete listener for a parse tree produced by CParser.
class CListener(ParseTreeListener):

    # Enter a parse tree produced by CParser#compilationUnit.
    def enterCompilationUnit(self, ctx:CParser.CompilationUnitContext):
        pass

    # Exit a parse tree produced by CParser#compilationUnit.
    def exitCompilationUnit(self, ctx:CParser.CompilationUnitContext):
        pass


    # Enter a parse tree produced by CParser#block.
    def enterBlock(self, ctx:CParser.BlockContext):
        pass

    # Exit a parse tree produced by CParser#block.
    def exitBlock(self, ctx:CParser.BlockContext):
        pass


    # Enter a parse tree produced by CParser#assignment.
    def enterAssignment(self, ctx:CParser.AssignmentContext):
        pass

    # Exit a parse tree produced by CParser#assignment.
    def exitAssignment(self, ctx:CParser.AssignmentContext):
        pass


    # Enter a parse tree produced by CParser#expression.
    def enterExpression(self, ctx:CParser.ExpressionContext):
        pass

    # Exit a parse tree produced by CParser#expression.
    def exitExpression(self, ctx:CParser.ExpressionContext):
        pass


    # Enter a parse tree produced by CParser#multiplyOp.
    def enterMultiplyOp(self, ctx:CParser.MultiplyOpContext):
        pass

    # Exit a parse tree produced by CParser#multiplyOp.
    def exitMultiplyOp(self, ctx:CParser.MultiplyOpContext):
        pass


    # Enter a parse tree produced by CParser#divideOp.
    def enterDivideOp(self, ctx:CParser.DivideOpContext):
        pass

    # Exit a parse tree produced by CParser#divideOp.
    def exitDivideOp(self, ctx:CParser.DivideOpContext):
        pass


    # Enter a parse tree produced by CParser#addOp.
    def enterAddOp(self, ctx:CParser.AddOpContext):
        pass

    # Exit a parse tree produced by CParser#addOp.
    def exitAddOp(self, ctx:CParser.AddOpContext):
        pass


    # Enter a parse tree produced by CParser#subtractOp.
    def enterSubtractOp(self, ctx:CParser.SubtractOpContext):
        pass

    # Exit a parse tree produced by CParser#subtractOp.
    def exitSubtractOp(self, ctx:CParser.SubtractOpContext):
        pass


    # Enter a parse tree produced by CParser#constant.
    def enterConstant(self, ctx:CParser.ConstantContext):
        pass

    # Exit a parse tree produced by CParser#constant.
    def exitConstant(self, ctx:CParser.ConstantContext):
        pass


    # Enter a parse tree produced by CParser#functionCall.
    def enterFunctionCall(self, ctx:CParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by CParser#functionCall.
    def exitFunctionCall(self, ctx:CParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by CParser#statementList.
    def enterStatementList(self, ctx:CParser.StatementListContext):
        pass

    # Exit a parse tree produced by CParser#statementList.
    def exitStatementList(self, ctx:CParser.StatementListContext):
        pass


    # Enter a parse tree produced by CParser#declarationList.
    def enterDeclarationList(self, ctx:CParser.DeclarationListContext):
        pass

    # Exit a parse tree produced by CParser#declarationList.
    def exitDeclarationList(self, ctx:CParser.DeclarationListContext):
        pass


    # Enter a parse tree produced by CParser#declaration.
    def enterDeclaration(self, ctx:CParser.DeclarationContext):
        pass

    # Exit a parse tree produced by CParser#declaration.
    def exitDeclaration(self, ctx:CParser.DeclarationContext):
        pass


    # Enter a parse tree produced by CParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:CParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by CParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:CParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by CParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:CParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by CParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:CParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by CParser#definitionList.
    def enterDefinitionList(self, ctx:CParser.DefinitionListContext):
        pass

    # Exit a parse tree produced by CParser#definitionList.
    def exitDefinitionList(self, ctx:CParser.DefinitionListContext):
        pass


    # Enter a parse tree produced by CParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:CParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by CParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:CParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by CParser#functionName.
    def enterFunctionName(self, ctx:CParser.FunctionNameContext):
        pass

    # Exit a parse tree produced by CParser#functionName.
    def exitFunctionName(self, ctx:CParser.FunctionNameContext):
        pass


    # Enter a parse tree produced by CParser#functionArgs.
    def enterFunctionArgs(self, ctx:CParser.FunctionArgsContext):
        pass

    # Exit a parse tree produced by CParser#functionArgs.
    def exitFunctionArgs(self, ctx:CParser.FunctionArgsContext):
        pass


    # Enter a parse tree produced by CParser#identifier.
    def enterIdentifier(self, ctx:CParser.IdentifierContext):
        pass

    # Exit a parse tree produced by CParser#identifier.
    def exitIdentifier(self, ctx:CParser.IdentifierContext):
        pass


    # Enter a parse tree produced by CParser#typeSpecifier.
    def enterTypeSpecifier(self, ctx:CParser.TypeSpecifierContext):
        pass

    # Exit a parse tree produced by CParser#typeSpecifier.
    def exitTypeSpecifier(self, ctx:CParser.TypeSpecifierContext):
        pass


    # Enter a parse tree produced by CParser#stringLiteral.
    def enterStringLiteral(self, ctx:CParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by CParser#stringLiteral.
    def exitStringLiteral(self, ctx:CParser.StringLiteralContext):
        pass



del CParser