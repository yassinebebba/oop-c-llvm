# Generated from core/C.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CParser import CParser
else:
    from CParser import CParser

# This class defines a complete generic visitor for a parse tree produced by CParser.

class CVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CParser#compilationUnit.
    def visitCompilationUnit(self, ctx:CParser.CompilationUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#chainedCallExpression.
    def visitChainedCallExpression(self, ctx:CParser.ChainedCallExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#ltExpression.
    def visitLtExpression(self, ctx:CParser.LtExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#gtExpression.
    def visitGtExpression(self, ctx:CParser.GtExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#constantExpression.
    def visitConstantExpression(self, ctx:CParser.ConstantExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#identifierExpression.
    def visitIdentifierExpression(self, ctx:CParser.IdentifierExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#multiplyExpression.
    def visitMultiplyExpression(self, ctx:CParser.MultiplyExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#sizeofExpression.
    def visitSizeofExpression(self, ctx:CParser.SizeofExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#gteExpression.
    def visitGteExpression(self, ctx:CParser.GteExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#funcCallExpression.
    def visitFuncCallExpression(self, ctx:CParser.FuncCallExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#divideExpression.
    def visitDivideExpression(self, ctx:CParser.DivideExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#eqExpression.
    def visitEqExpression(self, ctx:CParser.EqExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#addExpression.
    def visitAddExpression(self, ctx:CParser.AddExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#subtractExpression.
    def visitSubtractExpression(self, ctx:CParser.SubtractExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#lteExpression.
    def visitLteExpression(self, ctx:CParser.LteExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#chainedCall.
    def visitChainedCall(self, ctx:CParser.ChainedCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#constant.
    def visitConstant(self, ctx:CParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#unaryPlus.
    def visitUnaryPlus(self, ctx:CParser.UnaryPlusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#unaryMinus.
    def visitUnaryMinus(self, ctx:CParser.UnaryMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#unarySign.
    def visitUnarySign(self, ctx:CParser.UnarySignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#functionCallExpression.
    def visitFunctionCallExpression(self, ctx:CParser.FunctionCallExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#functionCall.
    def visitFunctionCall(self, ctx:CParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#functionCallArgs.
    def visitFunctionCallArgs(self, ctx:CParser.FunctionCallArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#statementList.
    def visitStatementList(self, ctx:CParser.StatementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#declarationList.
    def visitDeclarationList(self, ctx:CParser.DeclarationListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#definitionList.
    def visitDefinitionList(self, ctx:CParser.DefinitionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:CParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#variableDefinition.
    def visitVariableDefinition(self, ctx:CParser.VariableDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#arrayCell.
    def visitArrayCell(self, ctx:CParser.ArrayCellContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:CParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#functionDefinition.
    def visitFunctionDefinition(self, ctx:CParser.FunctionDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#functionReturn.
    def visitFunctionReturn(self, ctx:CParser.FunctionReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#functionArgs.
    def visitFunctionArgs(self, ctx:CParser.FunctionArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#arg.
    def visitArg(self, ctx:CParser.ArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#structDeclaration.
    def visitStructDeclaration(self, ctx:CParser.StructDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#structDefinition.
    def visitStructDefinition(self, ctx:CParser.StructDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#structBlock.
    def visitStructBlock(self, ctx:CParser.StructBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#field.
    def visitField(self, ctx:CParser.FieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#bitField.
    def visitBitField(self, ctx:CParser.BitFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#assignment.
    def visitAssignment(self, ctx:CParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#inplaceAssignment.
    def visitInplaceAssignment(self, ctx:CParser.InplaceAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#typeSpecifier.
    def visitTypeSpecifier(self, ctx:CParser.TypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#ifStatementStructure.
    def visitIfStatementStructure(self, ctx:CParser.IfStatementStructureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#ifStatement.
    def visitIfStatement(self, ctx:CParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#elseIfStatement.
    def visitElseIfStatement(self, ctx:CParser.ElseIfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#elseStatement.
    def visitElseStatement(self, ctx:CParser.ElseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#whileStatement.
    def visitWhileStatement(self, ctx:CParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#doWhileStatement.
    def visitDoWhileStatement(self, ctx:CParser.DoWhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#condition.
    def visitCondition(self, ctx:CParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#classDefinition.
    def visitClassDefinition(self, ctx:CParser.ClassDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#classBlock.
    def visitClassBlock(self, ctx:CParser.ClassBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#classInstantiation.
    def visitClassInstantiation(self, ctx:CParser.ClassInstantiationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#block.
    def visitBlock(self, ctx:CParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#identifier.
    def visitIdentifier(self, ctx:CParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#includeDirective.
    def visitIncludeDirective(self, ctx:CParser.IncludeDirectiveContext):
        return self.visitChildren(ctx)



del CParser