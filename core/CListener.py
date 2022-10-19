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


    # Enter a parse tree produced by CParser#functionBlock.
    def enterFunctionBlock(self, ctx:CParser.FunctionBlockContext):
        pass

    # Exit a parse tree produced by CParser#functionBlock.
    def exitFunctionBlock(self, ctx:CParser.FunctionBlockContext):
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


    # Enter a parse tree produced by CParser#functionReturn.
    def enterFunctionReturn(self, ctx:CParser.FunctionReturnContext):
        pass

    # Exit a parse tree produced by CParser#functionReturn.
    def exitFunctionReturn(self, ctx:CParser.FunctionReturnContext):
        pass


    # Enter a parse tree produced by CParser#multiplyExpression.
    def enterMultiplyExpression(self, ctx:CParser.MultiplyExpressionContext):
        pass

    # Exit a parse tree produced by CParser#multiplyExpression.
    def exitMultiplyExpression(self, ctx:CParser.MultiplyExpressionContext):
        pass


    # Enter a parse tree produced by CParser#divideExpression.
    def enterDivideExpression(self, ctx:CParser.DivideExpressionContext):
        pass

    # Exit a parse tree produced by CParser#divideExpression.
    def exitDivideExpression(self, ctx:CParser.DivideExpressionContext):
        pass


    # Enter a parse tree produced by CParser#addExpression.
    def enterAddExpression(self, ctx:CParser.AddExpressionContext):
        pass

    # Exit a parse tree produced by CParser#addExpression.
    def exitAddExpression(self, ctx:CParser.AddExpressionContext):
        pass


    # Enter a parse tree produced by CParser#subtractExpression.
    def enterSubtractExpression(self, ctx:CParser.SubtractExpressionContext):
        pass

    # Exit a parse tree produced by CParser#subtractExpression.
    def exitSubtractExpression(self, ctx:CParser.SubtractExpressionContext):
        pass


    # Enter a parse tree produced by CParser#constant.
    def enterConstant(self, ctx:CParser.ConstantContext):
        pass

    # Exit a parse tree produced by CParser#constant.
    def exitConstant(self, ctx:CParser.ConstantContext):
        pass


    # Enter a parse tree produced by CParser#functionCallExpression.
    def enterFunctionCallExpression(self, ctx:CParser.FunctionCallExpressionContext):
        pass

    # Exit a parse tree produced by CParser#functionCallExpression.
    def exitFunctionCallExpression(self, ctx:CParser.FunctionCallExpressionContext):
        pass


    # Enter a parse tree produced by CParser#functionCall.
    def enterFunctionCall(self, ctx:CParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by CParser#functionCall.
    def exitFunctionCall(self, ctx:CParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by CParser#functionCallArgs.
    def enterFunctionCallArgs(self, ctx:CParser.FunctionCallArgsContext):
        pass

    # Exit a parse tree produced by CParser#functionCallArgs.
    def exitFunctionCallArgs(self, ctx:CParser.FunctionCallArgsContext):
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


    # Enter a parse tree produced by CParser#typeSpecifier.
    def enterTypeSpecifier(self, ctx:CParser.TypeSpecifierContext):
        pass

    # Exit a parse tree produced by CParser#typeSpecifier.
    def exitTypeSpecifier(self, ctx:CParser.TypeSpecifierContext):
        pass


    # Enter a parse tree produced by CParser#identifier.
    def enterIdentifier(self, ctx:CParser.IdentifierContext):
        pass

    # Exit a parse tree produced by CParser#identifier.
    def exitIdentifier(self, ctx:CParser.IdentifierContext):
        pass



del CParser