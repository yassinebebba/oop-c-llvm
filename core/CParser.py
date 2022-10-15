# Generated from core/C.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,22,180,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,1,0,1,0,1,0,5,0,48,8,0,10,0,12,0,51,9,0,1,0,1,0,1,
        1,1,1,1,1,1,1,1,1,5,1,60,8,1,10,1,12,1,63,9,1,1,1,1,1,1,2,1,2,1,
        2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,3,3,77,8,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,95,8,3,10,3,12,3,98,
        9,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,3,8,110,8,8,1,9,1,9,
        1,9,1,9,3,9,116,8,9,5,9,118,8,9,10,9,12,9,121,9,9,1,9,1,9,1,10,1,
        10,1,11,1,11,1,11,1,11,1,11,5,11,132,8,11,10,11,12,11,135,9,11,1,
        12,1,12,1,12,1,12,3,12,141,8,12,1,13,1,13,1,13,1,14,3,14,147,8,14,
        1,14,1,14,1,14,1,14,1,15,1,15,1,16,3,16,156,8,16,1,16,1,16,1,16,
        1,16,1,17,1,17,1,18,1,18,1,18,1,19,1,19,1,20,1,20,1,21,1,21,5,21,
        173,8,21,10,21,12,21,176,9,21,1,21,1,21,1,21,0,2,6,22,22,0,2,4,6,
        8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,0,2,1,0,7,8,
        1,0,5,5,178,0,49,1,0,0,0,2,54,1,0,0,0,4,66,1,0,0,0,6,76,1,0,0,0,
        8,99,1,0,0,0,10,101,1,0,0,0,12,103,1,0,0,0,14,105,1,0,0,0,16,109,
        1,0,0,0,18,111,1,0,0,0,20,124,1,0,0,0,22,126,1,0,0,0,24,140,1,0,
        0,0,26,142,1,0,0,0,28,146,1,0,0,0,30,152,1,0,0,0,32,155,1,0,0,0,
        34,161,1,0,0,0,36,163,1,0,0,0,38,166,1,0,0,0,40,168,1,0,0,0,42,170,
        1,0,0,0,44,48,3,4,2,0,45,48,3,22,11,0,46,48,3,30,15,0,47,44,1,0,
        0,0,47,45,1,0,0,0,47,46,1,0,0,0,48,51,1,0,0,0,49,47,1,0,0,0,49,50,
        1,0,0,0,50,52,1,0,0,0,51,49,1,0,0,0,52,53,5,0,0,1,53,1,1,0,0,0,54,
        61,5,12,0,0,55,60,3,6,3,0,56,60,3,30,15,0,57,60,3,22,11,0,58,60,
        3,4,2,0,59,55,1,0,0,0,59,56,1,0,0,0,59,57,1,0,0,0,59,58,1,0,0,0,
        60,63,1,0,0,0,61,59,1,0,0,0,61,62,1,0,0,0,62,64,1,0,0,0,63,61,1,
        0,0,0,64,65,5,13,0,0,65,3,1,0,0,0,66,67,3,40,20,0,67,68,3,38,19,
        0,68,69,5,1,0,0,69,70,3,6,3,0,70,71,5,16,0,0,71,5,1,0,0,0,72,73,
        6,3,-1,0,73,77,3,16,8,0,74,77,3,18,9,0,75,77,3,38,19,0,76,72,1,0,
        0,0,76,74,1,0,0,0,76,75,1,0,0,0,77,96,1,0,0,0,78,79,10,4,0,0,79,
        80,3,8,4,0,80,81,3,6,3,5,81,95,1,0,0,0,82,83,10,3,0,0,83,84,3,10,
        5,0,84,85,3,6,3,4,85,95,1,0,0,0,86,87,10,2,0,0,87,88,3,12,6,0,88,
        89,3,6,3,3,89,95,1,0,0,0,90,91,10,1,0,0,91,92,3,14,7,0,92,93,3,6,
        3,2,93,95,1,0,0,0,94,78,1,0,0,0,94,82,1,0,0,0,94,86,1,0,0,0,94,90,
        1,0,0,0,95,98,1,0,0,0,96,94,1,0,0,0,96,97,1,0,0,0,97,7,1,0,0,0,98,
        96,1,0,0,0,99,100,5,9,0,0,100,9,1,0,0,0,101,102,5,2,0,0,102,11,1,
        0,0,0,103,104,5,3,0,0,104,13,1,0,0,0,105,106,5,4,0,0,106,15,1,0,
        0,0,107,110,5,6,0,0,108,110,3,42,21,0,109,107,1,0,0,0,109,108,1,
        0,0,0,110,17,1,0,0,0,111,112,3,38,19,0,112,119,5,10,0,0,113,115,
        3,6,3,0,114,116,5,17,0,0,115,114,1,0,0,0,115,116,1,0,0,0,116,118,
        1,0,0,0,117,113,1,0,0,0,118,121,1,0,0,0,119,117,1,0,0,0,119,120,
        1,0,0,0,120,122,1,0,0,0,121,119,1,0,0,0,122,123,5,11,0,0,123,19,
        1,0,0,0,124,125,1,0,0,0,125,21,1,0,0,0,126,127,6,11,-1,0,127,128,
        3,24,12,0,128,133,1,0,0,0,129,130,10,1,0,0,130,132,3,24,12,0,131,
        129,1,0,0,0,132,135,1,0,0,0,133,131,1,0,0,0,133,134,1,0,0,0,134,
        23,1,0,0,0,135,133,1,0,0,0,136,141,3,28,14,0,137,138,3,26,13,0,138,
        139,5,16,0,0,139,141,1,0,0,0,140,136,1,0,0,0,140,137,1,0,0,0,141,
        25,1,0,0,0,142,143,3,40,20,0,143,144,3,38,19,0,144,27,1,0,0,0,145,
        147,3,40,20,0,146,145,1,0,0,0,146,147,1,0,0,0,147,148,1,0,0,0,148,
        149,3,34,17,0,149,150,3,36,18,0,150,151,5,16,0,0,151,29,1,0,0,0,
        152,153,3,32,16,0,153,31,1,0,0,0,154,156,3,40,20,0,155,154,1,0,0,
        0,155,156,1,0,0,0,156,157,1,0,0,0,157,158,3,34,17,0,158,159,3,36,
        18,0,159,160,3,2,1,0,160,33,1,0,0,0,161,162,3,38,19,0,162,35,1,0,
        0,0,163,164,5,10,0,0,164,165,5,11,0,0,165,37,1,0,0,0,166,167,5,18,
        0,0,167,39,1,0,0,0,168,169,7,0,0,0,169,41,1,0,0,0,170,174,5,5,0,
        0,171,173,8,1,0,0,172,171,1,0,0,0,173,176,1,0,0,0,174,172,1,0,0,
        0,174,175,1,0,0,0,175,177,1,0,0,0,176,174,1,0,0,0,177,178,5,5,0,
        0,178,43,1,0,0,0,15,47,49,59,61,76,94,96,109,115,119,133,140,146,
        155,174
    ]

class CParser ( Parser ):

    grammarFileName = "C.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'/'", "'+'", "'-'", "'\"'", "<INVALID>", 
                     "'void'", "'int'", "'*'", "'('", "')'", "'{'", "'}'", 
                     "'['", "']'", "';'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "INTEGER", "VOID", "INT", 
                      "STAR", "LP", "RP", "LC", "RC", "LSQRB", "RSQRB", 
                      "SEMICOLON", "COMMA", "IDENTIFIER", "WS", "NEWLINE", 
                      "BLOCK_COMMENT", "LINE_COMMENT" ]

    RULE_compilationUnit = 0
    RULE_functionBlock = 1
    RULE_assignment = 2
    RULE_expression = 3
    RULE_multiplyOp = 4
    RULE_divideOp = 5
    RULE_addOp = 6
    RULE_subtractOp = 7
    RULE_constant = 8
    RULE_functionCall = 9
    RULE_statementList = 10
    RULE_declarationList = 11
    RULE_declaration = 12
    RULE_variableDeclaration = 13
    RULE_functionDeclaration = 14
    RULE_definitionList = 15
    RULE_functionDefinition = 16
    RULE_functionName = 17
    RULE_functionArgs = 18
    RULE_identifier = 19
    RULE_typeSpecifier = 20
    RULE_stringLiteral = 21

    ruleNames =  [ "compilationUnit", "functionBlock", "assignment", "expression", 
                   "multiplyOp", "divideOp", "addOp", "subtractOp", "constant", 
                   "functionCall", "statementList", "declarationList", "declaration", 
                   "variableDeclaration", "functionDeclaration", "definitionList", 
                   "functionDefinition", "functionName", "functionArgs", 
                   "identifier", "typeSpecifier", "stringLiteral" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    INTEGER=6
    VOID=7
    INT=8
    STAR=9
    LP=10
    RP=11
    LC=12
    RC=13
    LSQRB=14
    RSQRB=15
    SEMICOLON=16
    COMMA=17
    IDENTIFIER=18
    WS=19
    NEWLINE=20
    BLOCK_COMMENT=21
    LINE_COMMENT=22

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CompilationUnitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CParser.EOF, 0)

        def assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.AssignmentContext)
            else:
                return self.getTypedRuleContext(CParser.AssignmentContext,i)


        def declarationList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.DeclarationListContext)
            else:
                return self.getTypedRuleContext(CParser.DeclarationListContext,i)


        def definitionList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.DefinitionListContext)
            else:
                return self.getTypedRuleContext(CParser.DefinitionListContext,i)


        def getRuleIndex(self):
            return CParser.RULE_compilationUnit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompilationUnit" ):
                listener.enterCompilationUnit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompilationUnit" ):
                listener.exitCompilationUnit(self)




    def compilationUnit(self):

        localctx = CParser.CompilationUnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_compilationUnit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 262528) != 0:
                self.state = 47
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 44
                    self.assignment()
                    pass

                elif la_ == 2:
                    self.state = 45
                    self.declarationList(0)
                    pass

                elif la_ == 3:
                    self.state = 46
                    self.definitionList()
                    pass


                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 52
            self.match(CParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LC(self):
            return self.getToken(CParser.LC, 0)

        def RC(self):
            return self.getToken(CParser.RC, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CParser.ExpressionContext,i)


        def definitionList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.DefinitionListContext)
            else:
                return self.getTypedRuleContext(CParser.DefinitionListContext,i)


        def declarationList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.DeclarationListContext)
            else:
                return self.getTypedRuleContext(CParser.DeclarationListContext,i)


        def assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.AssignmentContext)
            else:
                return self.getTypedRuleContext(CParser.AssignmentContext,i)


        def getRuleIndex(self):
            return CParser.RULE_functionBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionBlock" ):
                listener.enterFunctionBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionBlock" ):
                listener.exitFunctionBlock(self)




    def functionBlock(self):

        localctx = CParser.FunctionBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_functionBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(CParser.LC)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 262624) != 0:
                self.state = 59
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 55
                    self.expression(0)
                    pass

                elif la_ == 2:
                    self.state = 56
                    self.definitionList()
                    pass

                elif la_ == 3:
                    self.state = 57
                    self.declarationList(0)
                    pass

                elif la_ == 4:
                    self.state = 58
                    self.assignment()
                    pass


                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 64
            self.match(CParser.RC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeSpecifier(self):
            return self.getTypedRuleContext(CParser.TypeSpecifierContext,0)


        def identifier(self):
            return self.getTypedRuleContext(CParser.IdentifierContext,0)


        def expression(self):
            return self.getTypedRuleContext(CParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(CParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = CParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.typeSpecifier()
            self.state = 67
            self.identifier()
            self.state = 68
            self.match(CParser.T__0)
            self.state = 69
            self.expression(0)
            self.state = 70
            self.match(CParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constant(self):
            return self.getTypedRuleContext(CParser.ConstantContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(CParser.FunctionCallContext,0)


        def identifier(self):
            return self.getTypedRuleContext(CParser.IdentifierContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CParser.ExpressionContext,i)


        def multiplyOp(self):
            return self.getTypedRuleContext(CParser.MultiplyOpContext,0)


        def divideOp(self):
            return self.getTypedRuleContext(CParser.DivideOpContext,0)


        def addOp(self):
            return self.getTypedRuleContext(CParser.AddOpContext,0)


        def subtractOp(self):
            return self.getTypedRuleContext(CParser.SubtractOpContext,0)


        def getRuleIndex(self):
            return CParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 73
                self.constant()
                pass

            elif la_ == 2:
                self.state = 74
                self.functionCall()
                pass

            elif la_ == 3:
                self.state = 75
                self.identifier()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 96
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 94
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = CParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 78
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 79
                        self.multiplyOp()
                        self.state = 80
                        self.expression(5)
                        pass

                    elif la_ == 2:
                        localctx = CParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 82
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 83
                        self.divideOp()
                        self.state = 84
                        self.expression(4)
                        pass

                    elif la_ == 3:
                        localctx = CParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 86
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 87
                        self.addOp()
                        self.state = 88
                        self.expression(3)
                        pass

                    elif la_ == 4:
                        localctx = CParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 90
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 91
                        self.subtractOp()
                        self.state = 92
                        self.expression(2)
                        pass

             
                self.state = 98
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MultiplyOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(CParser.STAR, 0)

        def getRuleIndex(self):
            return CParser.RULE_multiplyOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplyOp" ):
                listener.enterMultiplyOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplyOp" ):
                listener.exitMultiplyOp(self)




    def multiplyOp(self):

        localctx = CParser.MultiplyOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_multiplyOp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(CParser.STAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DivideOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CParser.RULE_divideOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivideOp" ):
                listener.enterDivideOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivideOp" ):
                listener.exitDivideOp(self)




    def divideOp(self):

        localctx = CParser.DivideOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_divideOp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(CParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CParser.RULE_addOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddOp" ):
                listener.enterAddOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddOp" ):
                listener.exitAddOp(self)




    def addOp(self):

        localctx = CParser.AddOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_addOp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(CParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubtractOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CParser.RULE_subtractOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubtractOp" ):
                listener.enterSubtractOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubtractOp" ):
                listener.exitSubtractOp(self)




    def subtractOp(self):

        localctx = CParser.SubtractOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_subtractOp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(CParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(CParser.INTEGER, 0)

        def stringLiteral(self):
            return self.getTypedRuleContext(CParser.StringLiteralContext,0)


        def getRuleIndex(self):
            return CParser.RULE_constant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant" ):
                listener.enterConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant" ):
                listener.exitConstant(self)




    def constant(self):

        localctx = CParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_constant)
        try:
            self.state = 109
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.match(CParser.INTEGER)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 108
                self.stringLiteral()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(CParser.IdentifierContext,0)


        def LP(self):
            return self.getToken(CParser.LP, 0)

        def RP(self):
            return self.getToken(CParser.RP, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CParser.COMMA)
            else:
                return self.getToken(CParser.COMMA, i)

        def getRuleIndex(self):
            return CParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)




    def functionCall(self):

        localctx = CParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.identifier()
            self.state = 112
            self.match(CParser.LP)
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 262240) != 0:
                self.state = 113
                self.expression(0)
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==17:
                    self.state = 114
                    self.match(CParser.COMMA)


                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 122
            self.match(CParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CParser.RULE_statementList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementList" ):
                listener.enterStatementList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementList" ):
                listener.exitStatementList(self)




    def statementList(self):

        localctx = CParser.StatementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_statementList)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(CParser.DeclarationContext,0)


        def declarationList(self):
            return self.getTypedRuleContext(CParser.DeclarationListContext,0)


        def getRuleIndex(self):
            return CParser.RULE_declarationList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclarationList" ):
                listener.enterDeclarationList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclarationList" ):
                listener.exitDeclarationList(self)



    def declarationList(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CParser.DeclarationListContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_declarationList, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.declaration()
            self._ctx.stop = self._input.LT(-1)
            self.state = 133
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CParser.DeclarationListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_declarationList)
                    self.state = 129
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 130
                    self.declaration() 
                self.state = 135
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionDeclaration(self):
            return self.getTypedRuleContext(CParser.FunctionDeclarationContext,0)


        def variableDeclaration(self):
            return self.getTypedRuleContext(CParser.VariableDeclarationContext,0)


        def SEMICOLON(self):
            return self.getToken(CParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)




    def declaration(self):

        localctx = CParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_declaration)
        try:
            self.state = 140
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.functionDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.variableDeclaration()
                self.state = 138
                self.match(CParser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeSpecifier(self):
            return self.getTypedRuleContext(CParser.TypeSpecifierContext,0)


        def identifier(self):
            return self.getTypedRuleContext(CParser.IdentifierContext,0)


        def getRuleIndex(self):
            return CParser.RULE_variableDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclaration" ):
                listener.enterVariableDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclaration" ):
                listener.exitVariableDeclaration(self)




    def variableDeclaration(self):

        localctx = CParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_variableDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.typeSpecifier()
            self.state = 143
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionName(self):
            return self.getTypedRuleContext(CParser.FunctionNameContext,0)


        def functionArgs(self):
            return self.getTypedRuleContext(CParser.FunctionArgsContext,0)


        def SEMICOLON(self):
            return self.getToken(CParser.SEMICOLON, 0)

        def typeSpecifier(self):
            return self.getTypedRuleContext(CParser.TypeSpecifierContext,0)


        def getRuleIndex(self):
            return CParser.RULE_functionDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDeclaration" ):
                listener.enterFunctionDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDeclaration" ):
                listener.exitFunctionDeclaration(self)




    def functionDeclaration(self):

        localctx = CParser.FunctionDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7 or _la==8:
                self.state = 145
                self.typeSpecifier()


            self.state = 148
            self.functionName()
            self.state = 149
            self.functionArgs()
            self.state = 150
            self.match(CParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefinitionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionDefinition(self):
            return self.getTypedRuleContext(CParser.FunctionDefinitionContext,0)


        def getRuleIndex(self):
            return CParser.RULE_definitionList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefinitionList" ):
                listener.enterDefinitionList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefinitionList" ):
                listener.exitDefinitionList(self)




    def definitionList(self):

        localctx = CParser.DefinitionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_definitionList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.functionDefinition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionName(self):
            return self.getTypedRuleContext(CParser.FunctionNameContext,0)


        def functionArgs(self):
            return self.getTypedRuleContext(CParser.FunctionArgsContext,0)


        def functionBlock(self):
            return self.getTypedRuleContext(CParser.FunctionBlockContext,0)


        def typeSpecifier(self):
            return self.getTypedRuleContext(CParser.TypeSpecifierContext,0)


        def getRuleIndex(self):
            return CParser.RULE_functionDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDefinition" ):
                listener.enterFunctionDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDefinition" ):
                listener.exitFunctionDefinition(self)




    def functionDefinition(self):

        localctx = CParser.FunctionDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_functionDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7 or _la==8:
                self.state = 154
                self.typeSpecifier()


            self.state = 157
            self.functionName()
            self.state = 158
            self.functionArgs()
            self.state = 159
            self.functionBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(CParser.IdentifierContext,0)


        def getRuleIndex(self):
            return CParser.RULE_functionName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionName" ):
                listener.enterFunctionName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionName" ):
                listener.exitFunctionName(self)




    def functionName(self):

        localctx = CParser.FunctionNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_functionName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(CParser.LP, 0)

        def RP(self):
            return self.getToken(CParser.RP, 0)

        def getRuleIndex(self):
            return CParser.RULE_functionArgs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionArgs" ):
                listener.enterFunctionArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionArgs" ):
                listener.exitFunctionArgs(self)




    def functionArgs(self):

        localctx = CParser.FunctionArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_functionArgs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(CParser.LP)
            self.state = 164
            self.match(CParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(CParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return CParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)




    def identifier(self):

        localctx = CParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(CParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeSpecifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VOID(self):
            return self.getToken(CParser.VOID, 0)

        def INT(self):
            return self.getToken(CParser.INT, 0)

        def getRuleIndex(self):
            return CParser.RULE_typeSpecifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeSpecifier" ):
                listener.enterTypeSpecifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeSpecifier" ):
                listener.exitTypeSpecifier(self)




    def typeSpecifier(self):

        localctx = CParser.TypeSpecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_typeSpecifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            _la = self._input.LA(1)
            if not(_la==7 or _la==8):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CParser.RULE_stringLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringLiteral" ):
                listener.enterStringLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringLiteral" ):
                listener.exitStringLiteral(self)




    def stringLiteral(self):

        localctx = CParser.StringLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_stringLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(CParser.T__4)
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 8388574) != 0:
                self.state = 171
                _la = self._input.LA(1)
                if _la <= 0 or _la==5:
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 176
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 177
            self.match(CParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expression_sempred
        self._predicates[11] = self.declarationList_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         

    def declarationList_sempred(self, localctx:DeclarationListContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 1)
         




