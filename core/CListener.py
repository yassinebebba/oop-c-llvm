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


    # Enter a parse tree produced by CParser#chainedCallExpression.
    def enterChainedCallExpression(self, ctx:CParser.ChainedCallExpressionContext):
        pass

    # Exit a parse tree produced by CParser#chainedCallExpression.
    def exitChainedCallExpression(self, ctx:CParser.ChainedCallExpressionContext):
        pass


    # Enter a parse tree produced by CParser#ltExpression.
    def enterLtExpression(self, ctx:CParser.LtExpressionContext):
        pass

    # Exit a parse tree produced by CParser#ltExpression.
    def exitLtExpression(self, ctx:CParser.LtExpressionContext):
        pass


    # Enter a parse tree produced by CParser#gtExpression.
    def enterGtExpression(self, ctx:CParser.GtExpressionContext):
        pass

    # Exit a parse tree produced by CParser#gtExpression.
    def exitGtExpression(self, ctx:CParser.GtExpressionContext):
        pass


    # Enter a parse tree produced by CParser#constantExpression.
    def enterConstantExpression(self, ctx:CParser.ConstantExpressionContext):
        pass

    # Exit a parse tree produced by CParser#constantExpression.
    def exitConstantExpression(self, ctx:CParser.ConstantExpressionContext):
        pass


    # Enter a parse tree produced by CParser#identifierExpression.
    def enterIdentifierExpression(self, ctx:CParser.IdentifierExpressionContext):
        pass

    # Exit a parse tree produced by CParser#identifierExpression.
    def exitIdentifierExpression(self, ctx:CParser.IdentifierExpressionContext):
        pass


    # Enter a parse tree produced by CParser#multiplyExpression.
    def enterMultiplyExpression(self, ctx:CParser.MultiplyExpressionContext):
        pass

    # Exit a parse tree produced by CParser#multiplyExpression.
    def exitMultiplyExpression(self, ctx:CParser.MultiplyExpressionContext):
        pass


    # Enter a parse tree produced by CParser#sizeofExpression.
    def enterSizeofExpression(self, ctx:CParser.SizeofExpressionContext):
        pass

    # Exit a parse tree produced by CParser#sizeofExpression.
    def exitSizeofExpression(self, ctx:CParser.SizeofExpressionContext):
        pass


    # Enter a parse tree produced by CParser#gteExpression.
    def enterGteExpression(self, ctx:CParser.GteExpressionContext):
        pass

    # Exit a parse tree produced by CParser#gteExpression.
    def exitGteExpression(self, ctx:CParser.GteExpressionContext):
        pass


    # Enter a parse tree produced by CParser#funcCallExpression.
    def enterFuncCallExpression(self, ctx:CParser.FuncCallExpressionContext):
        pass

    # Exit a parse tree produced by CParser#funcCallExpression.
    def exitFuncCallExpression(self, ctx:CParser.FuncCallExpressionContext):
        pass


    # Enter a parse tree produced by CParser#divideExpression.
    def enterDivideExpression(self, ctx:CParser.DivideExpressionContext):
        pass

    # Exit a parse tree produced by CParser#divideExpression.
    def exitDivideExpression(self, ctx:CParser.DivideExpressionContext):
        pass


    # Enter a parse tree produced by CParser#eqExpression.
    def enterEqExpression(self, ctx:CParser.EqExpressionContext):
        pass

    # Exit a parse tree produced by CParser#eqExpression.
    def exitEqExpression(self, ctx:CParser.EqExpressionContext):
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


    # Enter a parse tree produced by CParser#lteExpression.
    def enterLteExpression(self, ctx:CParser.LteExpressionContext):
        pass

    # Exit a parse tree produced by CParser#lteExpression.
    def exitLteExpression(self, ctx:CParser.LteExpressionContext):
        pass


    # Enter a parse tree produced by CParser#chainedCall.
    def enterChainedCall(self, ctx:CParser.ChainedCallContext):
        pass

    # Exit a parse tree produced by CParser#chainedCall.
    def exitChainedCall(self, ctx:CParser.ChainedCallContext):
        pass


    # Enter a parse tree produced by CParser#constant.
    def enterConstant(self, ctx:CParser.ConstantContext):
        pass

    # Exit a parse tree produced by CParser#constant.
    def exitConstant(self, ctx:CParser.ConstantContext):
        pass


    # Enter a parse tree produced by CParser#unaryPlus.
    def enterUnaryPlus(self, ctx:CParser.UnaryPlusContext):
        pass

    # Exit a parse tree produced by CParser#unaryPlus.
    def exitUnaryPlus(self, ctx:CParser.UnaryPlusContext):
        pass


    # Enter a parse tree produced by CParser#unaryMinus.
    def enterUnaryMinus(self, ctx:CParser.UnaryMinusContext):
        pass

    # Exit a parse tree produced by CParser#unaryMinus.
    def exitUnaryMinus(self, ctx:CParser.UnaryMinusContext):
        pass


    # Enter a parse tree produced by CParser#unarySign.
    def enterUnarySign(self, ctx:CParser.UnarySignContext):
        pass

    # Exit a parse tree produced by CParser#unarySign.
    def exitUnarySign(self, ctx:CParser.UnarySignContext):
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


    # Enter a parse tree produced by CParser#definitionList.
    def enterDefinitionList(self, ctx:CParser.DefinitionListContext):
        pass

    # Exit a parse tree produced by CParser#definitionList.
    def exitDefinitionList(self, ctx:CParser.DefinitionListContext):
        pass


    # Enter a parse tree produced by CParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:CParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by CParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:CParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by CParser#variableDefinition.
    def enterVariableDefinition(self, ctx:CParser.VariableDefinitionContext):
        pass

    # Exit a parse tree produced by CParser#variableDefinition.
    def exitVariableDefinition(self, ctx:CParser.VariableDefinitionContext):
        pass


    # Enter a parse tree produced by CParser#arrayCell.
    def enterArrayCell(self, ctx:CParser.ArrayCellContext):
        pass

    # Exit a parse tree produced by CParser#arrayCell.
    def exitArrayCell(self, ctx:CParser.ArrayCellContext):
        pass


    # Enter a parse tree produced by CParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:CParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by CParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:CParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by CParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:CParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by CParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:CParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by CParser#functionReturn.
    def enterFunctionReturn(self, ctx:CParser.FunctionReturnContext):
        pass

    # Exit a parse tree produced by CParser#functionReturn.
    def exitFunctionReturn(self, ctx:CParser.FunctionReturnContext):
        pass


    # Enter a parse tree produced by CParser#functionArgs.
    def enterFunctionArgs(self, ctx:CParser.FunctionArgsContext):
        pass

    # Exit a parse tree produced by CParser#functionArgs.
    def exitFunctionArgs(self, ctx:CParser.FunctionArgsContext):
        pass


    # Enter a parse tree produced by CParser#arg.
    def enterArg(self, ctx:CParser.ArgContext):
        pass

    # Exit a parse tree produced by CParser#arg.
    def exitArg(self, ctx:CParser.ArgContext):
        pass


    # Enter a parse tree produced by CParser#structDeclaration.
    def enterStructDeclaration(self, ctx:CParser.StructDeclarationContext):
        pass

    # Exit a parse tree produced by CParser#structDeclaration.
    def exitStructDeclaration(self, ctx:CParser.StructDeclarationContext):
        pass


    # Enter a parse tree produced by CParser#structDefinition.
    def enterStructDefinition(self, ctx:CParser.StructDefinitionContext):
        pass

    # Exit a parse tree produced by CParser#structDefinition.
    def exitStructDefinition(self, ctx:CParser.StructDefinitionContext):
        pass


    # Enter a parse tree produced by CParser#structBlock.
    def enterStructBlock(self, ctx:CParser.StructBlockContext):
        pass

    # Exit a parse tree produced by CParser#structBlock.
    def exitStructBlock(self, ctx:CParser.StructBlockContext):
        pass


    # Enter a parse tree produced by CParser#field.
    def enterField(self, ctx:CParser.FieldContext):
        pass

    # Exit a parse tree produced by CParser#field.
    def exitField(self, ctx:CParser.FieldContext):
        pass


    # Enter a parse tree produced by CParser#bitField.
    def enterBitField(self, ctx:CParser.BitFieldContext):
        pass

    # Exit a parse tree produced by CParser#bitField.
    def exitBitField(self, ctx:CParser.BitFieldContext):
        pass


    # Enter a parse tree produced by CParser#assignment.
    def enterAssignment(self, ctx:CParser.AssignmentContext):
        pass

    # Exit a parse tree produced by CParser#assignment.
    def exitAssignment(self, ctx:CParser.AssignmentContext):
        pass


    # Enter a parse tree produced by CParser#inplaceAssignment.
    def enterInplaceAssignment(self, ctx:CParser.InplaceAssignmentContext):
        pass

    # Exit a parse tree produced by CParser#inplaceAssignment.
    def exitInplaceAssignment(self, ctx:CParser.InplaceAssignmentContext):
        pass


    # Enter a parse tree produced by CParser#typeSpecifier.
    def enterTypeSpecifier(self, ctx:CParser.TypeSpecifierContext):
        pass

    # Exit a parse tree produced by CParser#typeSpecifier.
    def exitTypeSpecifier(self, ctx:CParser.TypeSpecifierContext):
        pass


    # Enter a parse tree produced by CParser#ifStatementStructure.
    def enterIfStatementStructure(self, ctx:CParser.IfStatementStructureContext):
        pass

    # Exit a parse tree produced by CParser#ifStatementStructure.
    def exitIfStatementStructure(self, ctx:CParser.IfStatementStructureContext):
        pass


    # Enter a parse tree produced by CParser#ifStatement.
    def enterIfStatement(self, ctx:CParser.IfStatementContext):
        pass

    # Exit a parse tree produced by CParser#ifStatement.
    def exitIfStatement(self, ctx:CParser.IfStatementContext):
        pass


    # Enter a parse tree produced by CParser#elseIfStatement.
    def enterElseIfStatement(self, ctx:CParser.ElseIfStatementContext):
        pass

    # Exit a parse tree produced by CParser#elseIfStatement.
    def exitElseIfStatement(self, ctx:CParser.ElseIfStatementContext):
        pass


    # Enter a parse tree produced by CParser#elseStatement.
    def enterElseStatement(self, ctx:CParser.ElseStatementContext):
        pass

    # Exit a parse tree produced by CParser#elseStatement.
    def exitElseStatement(self, ctx:CParser.ElseStatementContext):
        pass


    # Enter a parse tree produced by CParser#whileStatement.
    def enterWhileStatement(self, ctx:CParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by CParser#whileStatement.
    def exitWhileStatement(self, ctx:CParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by CParser#doWhileStatement.
    def enterDoWhileStatement(self, ctx:CParser.DoWhileStatementContext):
        pass

    # Exit a parse tree produced by CParser#doWhileStatement.
    def exitDoWhileStatement(self, ctx:CParser.DoWhileStatementContext):
        pass


    # Enter a parse tree produced by CParser#condition.
    def enterCondition(self, ctx:CParser.ConditionContext):
        pass

    # Exit a parse tree produced by CParser#condition.
    def exitCondition(self, ctx:CParser.ConditionContext):
        pass


    # Enter a parse tree produced by CParser#classDefinition.
    def enterClassDefinition(self, ctx:CParser.ClassDefinitionContext):
        pass

    # Exit a parse tree produced by CParser#classDefinition.
    def exitClassDefinition(self, ctx:CParser.ClassDefinitionContext):
        pass


    # Enter a parse tree produced by CParser#classBlock.
    def enterClassBlock(self, ctx:CParser.ClassBlockContext):
        pass

    # Exit a parse tree produced by CParser#classBlock.
    def exitClassBlock(self, ctx:CParser.ClassBlockContext):
        pass


    # Enter a parse tree produced by CParser#classMethod.
    def enterClassMethod(self, ctx:CParser.ClassMethodContext):
        pass

    # Exit a parse tree produced by CParser#classMethod.
    def exitClassMethod(self, ctx:CParser.ClassMethodContext):
        pass


    # Enter a parse tree produced by CParser#classInstantiation.
    def enterClassInstantiation(self, ctx:CParser.ClassInstantiationContext):
        pass

    # Exit a parse tree produced by CParser#classInstantiation.
    def exitClassInstantiation(self, ctx:CParser.ClassInstantiationContext):
        pass


    # Enter a parse tree produced by CParser#block.
    def enterBlock(self, ctx:CParser.BlockContext):
        pass

    # Exit a parse tree produced by CParser#block.
    def exitBlock(self, ctx:CParser.BlockContext):
        pass


    # Enter a parse tree produced by CParser#identifier.
    def enterIdentifier(self, ctx:CParser.IdentifierContext):
        pass

    # Exit a parse tree produced by CParser#identifier.
    def exitIdentifier(self, ctx:CParser.IdentifierContext):
        pass


    # Enter a parse tree produced by CParser#includeDirective.
    def enterIncludeDirective(self, ctx:CParser.IncludeDirectiveContext):
        pass

    # Exit a parse tree produced by CParser#includeDirective.
    def exitIncludeDirective(self, ctx:CParser.IncludeDirectiveContext):
        pass



del CParser