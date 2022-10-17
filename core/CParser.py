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
        4,1,29,248,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,1,0,1,0,1,0,1,0,5,0,53,8,0,10,
        0,12,0,56,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,5,1,66,8,1,10,1,12,
        1,69,9,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,3,3,83,
        8,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,5,3,101,8,3,10,3,12,3,104,9,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,
        7,1,8,1,8,3,8,116,8,8,1,9,1,9,1,9,3,9,121,8,9,1,9,1,9,1,10,1,10,
        1,10,3,10,128,8,10,1,10,1,10,1,10,1,11,1,11,1,11,3,11,136,8,11,1,
        11,1,11,1,11,5,11,141,8,11,10,11,12,11,144,9,11,1,12,1,12,1,13,1,
        13,1,13,1,13,1,13,5,13,153,8,13,10,13,12,13,156,9,13,1,14,1,14,1,
        14,1,14,3,14,162,8,14,1,15,1,15,1,15,1,16,3,16,168,8,16,1,16,1,16,
        1,16,3,16,173,8,16,1,16,1,16,1,16,1,17,1,17,1,18,3,18,181,8,18,1,
        18,1,18,1,18,3,18,186,8,18,1,18,1,18,1,18,1,19,1,19,1,20,1,20,1,
        20,3,20,196,8,20,1,20,3,20,199,8,20,1,20,1,20,1,20,5,20,204,8,20,
        10,20,12,20,207,9,20,1,21,1,21,3,21,211,8,21,1,21,1,21,1,21,3,21,
        216,8,21,1,21,1,21,1,21,1,21,3,21,222,8,21,1,21,1,21,3,21,226,8,
        21,1,21,3,21,229,8,21,1,21,5,21,232,8,21,10,21,12,21,235,9,21,1,
        22,1,22,1,23,1,23,5,23,241,8,23,10,23,12,23,244,9,23,1,23,1,23,1,
        23,0,4,6,22,26,40,24,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,
        32,34,36,38,40,42,44,46,0,2,1,0,7,8,1,0,5,5,265,0,54,1,0,0,0,2,59,
        1,0,0,0,4,72,1,0,0,0,6,82,1,0,0,0,8,105,1,0,0,0,10,107,1,0,0,0,12,
        109,1,0,0,0,14,111,1,0,0,0,16,115,1,0,0,0,18,117,1,0,0,0,20,124,
        1,0,0,0,22,132,1,0,0,0,24,145,1,0,0,0,26,147,1,0,0,0,28,161,1,0,
        0,0,30,163,1,0,0,0,32,167,1,0,0,0,34,177,1,0,0,0,36,180,1,0,0,0,
        38,190,1,0,0,0,40,192,1,0,0,0,42,228,1,0,0,0,44,236,1,0,0,0,46,238,
        1,0,0,0,48,53,3,4,2,0,49,53,3,20,10,0,50,53,3,26,13,0,51,53,3,34,
        17,0,52,48,1,0,0,0,52,49,1,0,0,0,52,50,1,0,0,0,52,51,1,0,0,0,53,
        56,1,0,0,0,54,52,1,0,0,0,54,55,1,0,0,0,55,57,1,0,0,0,56,54,1,0,0,
        0,57,58,5,0,0,1,58,1,1,0,0,0,59,67,5,19,0,0,60,66,3,6,3,0,61,66,
        3,34,17,0,62,66,3,26,13,0,63,66,3,20,10,0,64,66,3,4,2,0,65,60,1,
        0,0,0,65,61,1,0,0,0,65,62,1,0,0,0,65,63,1,0,0,0,65,64,1,0,0,0,66,
        69,1,0,0,0,67,65,1,0,0,0,67,68,1,0,0,0,68,70,1,0,0,0,69,67,1,0,0,
        0,70,71,5,20,0,0,71,3,1,0,0,0,72,73,3,42,21,0,73,74,3,44,22,0,74,
        75,5,1,0,0,75,76,3,6,3,0,76,77,5,23,0,0,77,5,1,0,0,0,78,79,6,3,-1,
        0,79,83,3,16,8,0,80,83,3,18,9,0,81,83,3,44,22,0,82,78,1,0,0,0,82,
        80,1,0,0,0,82,81,1,0,0,0,83,102,1,0,0,0,84,85,10,4,0,0,85,86,3,8,
        4,0,86,87,3,6,3,5,87,101,1,0,0,0,88,89,10,3,0,0,89,90,3,10,5,0,90,
        91,3,6,3,4,91,101,1,0,0,0,92,93,10,2,0,0,93,94,3,12,6,0,94,95,3,
        6,3,3,95,101,1,0,0,0,96,97,10,1,0,0,97,98,3,14,7,0,98,99,3,6,3,2,
        99,101,1,0,0,0,100,84,1,0,0,0,100,88,1,0,0,0,100,92,1,0,0,0,100,
        96,1,0,0,0,101,104,1,0,0,0,102,100,1,0,0,0,102,103,1,0,0,0,103,7,
        1,0,0,0,104,102,1,0,0,0,105,106,5,16,0,0,106,9,1,0,0,0,107,108,5,
        2,0,0,108,11,1,0,0,0,109,110,5,3,0,0,110,13,1,0,0,0,111,112,5,4,
        0,0,112,15,1,0,0,0,113,116,5,6,0,0,114,116,3,46,23,0,115,113,1,0,
        0,0,115,114,1,0,0,0,116,17,1,0,0,0,117,118,3,44,22,0,118,120,5,17,
        0,0,119,121,3,22,11,0,120,119,1,0,0,0,120,121,1,0,0,0,121,122,1,
        0,0,0,122,123,5,18,0,0,123,19,1,0,0,0,124,125,3,44,22,0,125,127,
        5,17,0,0,126,128,3,22,11,0,127,126,1,0,0,0,127,128,1,0,0,0,128,129,
        1,0,0,0,129,130,5,18,0,0,130,131,5,23,0,0,131,21,1,0,0,0,132,133,
        6,11,-1,0,133,135,3,6,3,0,134,136,5,24,0,0,135,134,1,0,0,0,135,136,
        1,0,0,0,136,142,1,0,0,0,137,138,10,1,0,0,138,139,5,24,0,0,139,141,
        3,22,11,2,140,137,1,0,0,0,141,144,1,0,0,0,142,140,1,0,0,0,142,143,
        1,0,0,0,143,23,1,0,0,0,144,142,1,0,0,0,145,146,1,0,0,0,146,25,1,
        0,0,0,147,148,6,13,-1,0,148,149,3,28,14,0,149,154,1,0,0,0,150,151,
        10,1,0,0,151,153,3,28,14,0,152,150,1,0,0,0,153,156,1,0,0,0,154,152,
        1,0,0,0,154,155,1,0,0,0,155,27,1,0,0,0,156,154,1,0,0,0,157,162,3,
        32,16,0,158,159,3,30,15,0,159,160,5,23,0,0,160,162,1,0,0,0,161,157,
        1,0,0,0,161,158,1,0,0,0,162,29,1,0,0,0,163,164,3,42,21,0,164,165,
        3,44,22,0,165,31,1,0,0,0,166,168,3,42,21,0,167,166,1,0,0,0,167,168,
        1,0,0,0,168,169,1,0,0,0,169,170,3,38,19,0,170,172,5,17,0,0,171,173,
        3,40,20,0,172,171,1,0,0,0,172,173,1,0,0,0,173,174,1,0,0,0,174,175,
        5,18,0,0,175,176,5,23,0,0,176,33,1,0,0,0,177,178,3,36,18,0,178,35,
        1,0,0,0,179,181,3,42,21,0,180,179,1,0,0,0,180,181,1,0,0,0,181,182,
        1,0,0,0,182,183,3,38,19,0,183,185,5,17,0,0,184,186,3,40,20,0,185,
        184,1,0,0,0,185,186,1,0,0,0,186,187,1,0,0,0,187,188,5,18,0,0,188,
        189,3,2,1,0,189,37,1,0,0,0,190,191,3,44,22,0,191,39,1,0,0,0,192,
        193,6,20,-1,0,193,195,3,42,21,0,194,196,3,44,22,0,195,194,1,0,0,
        0,195,196,1,0,0,0,196,198,1,0,0,0,197,199,5,24,0,0,198,197,1,0,0,
        0,198,199,1,0,0,0,199,205,1,0,0,0,200,201,10,1,0,0,201,202,5,24,
        0,0,202,204,3,40,20,2,203,200,1,0,0,0,204,207,1,0,0,0,205,203,1,
        0,0,0,205,206,1,0,0,0,206,41,1,0,0,0,207,205,1,0,0,0,208,229,5,9,
        0,0,209,211,7,0,0,0,210,209,1,0,0,0,210,211,1,0,0,0,211,225,1,0,
        0,0,212,226,5,10,0,0,213,226,5,11,0,0,214,216,5,11,0,0,215,214,1,
        0,0,0,215,216,1,0,0,0,216,217,1,0,0,0,217,226,5,12,0,0,218,226,5,
        13,0,0,219,226,5,14,0,0,220,222,5,13,0,0,221,220,1,0,0,0,221,222,
        1,0,0,0,222,223,1,0,0,0,223,226,5,15,0,0,224,226,5,12,0,0,225,212,
        1,0,0,0,225,213,1,0,0,0,225,215,1,0,0,0,225,218,1,0,0,0,225,219,
        1,0,0,0,225,221,1,0,0,0,225,224,1,0,0,0,226,229,1,0,0,0,227,229,
        3,44,22,0,228,208,1,0,0,0,228,210,1,0,0,0,228,227,1,0,0,0,229,233,
        1,0,0,0,230,232,5,16,0,0,231,230,1,0,0,0,232,235,1,0,0,0,233,231,
        1,0,0,0,233,234,1,0,0,0,234,43,1,0,0,0,235,233,1,0,0,0,236,237,5,
        25,0,0,237,45,1,0,0,0,238,242,5,5,0,0,239,241,8,1,0,0,240,239,1,
        0,0,0,241,244,1,0,0,0,242,240,1,0,0,0,242,243,1,0,0,0,243,245,1,
        0,0,0,244,242,1,0,0,0,245,246,5,5,0,0,246,47,1,0,0,0,28,52,54,65,
        67,82,100,102,115,120,127,135,142,154,161,167,172,180,185,195,198,
        205,210,215,221,225,228,233,242
    ]

class CParser ( Parser ):

    grammarFileName = "C.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'/'", "'+'", "'-'", "'\"'", "<INVALID>", 
                     "'signed'", "'unsigned'", "'void'", "'char'", "'short'", 
                     "'int'", "'long'", "'float'", "'double'", "'*'", "'('", 
                     "')'", "'{'", "'}'", "'['", "']'", "';'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "INTEGER", "SIGNED", "UNSIGNED", 
                      "VOID", "CHAR", "SHORT", "INT", "LONG", "FLOAT", "DOUBLE", 
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
    RULE_functionCallExpression = 9
    RULE_functionCall = 10
    RULE_functionCallArgs = 11
    RULE_statementList = 12
    RULE_declarationList = 13
    RULE_declaration = 14
    RULE_variableDeclaration = 15
    RULE_functionDeclaration = 16
    RULE_definitionList = 17
    RULE_functionDefinition = 18
    RULE_functionName = 19
    RULE_functionArgs = 20
    RULE_typeSpecifier = 21
    RULE_identifier = 22
    RULE_stringLiteral = 23

    ruleNames =  [ "compilationUnit", "functionBlock", "assignment", "expression", 
                   "multiplyOp", "divideOp", "addOp", "subtractOp", "constant", 
                   "functionCallExpression", "functionCall", "functionCallArgs", 
                   "statementList", "declarationList", "declaration", "variableDeclaration", 
                   "functionDeclaration", "definitionList", "functionDefinition", 
                   "functionName", "functionArgs", "typeSpecifier", "identifier", 
                   "stringLiteral" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    INTEGER=6
    SIGNED=7
    UNSIGNED=8
    VOID=9
    CHAR=10
    SHORT=11
    INT=12
    LONG=13
    FLOAT=14
    DOUBLE=15
    STAR=16
    LP=17
    RP=18
    LC=19
    RC=20
    LSQRB=21
    RSQRB=22
    SEMICOLON=23
    COMMA=24
    IDENTIFIER=25
    WS=26
    NEWLINE=27
    BLOCK_COMMENT=28
    LINE_COMMENT=29

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


        def functionCall(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.FunctionCallContext)
            else:
                return self.getTypedRuleContext(CParser.FunctionCallContext,i)


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
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 33619840) != 0:
                self.state = 52
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 48
                    self.assignment()
                    pass

                elif la_ == 2:
                    self.state = 49
                    self.functionCall()
                    pass

                elif la_ == 3:
                    self.state = 50
                    self.declarationList(0)
                    pass

                elif la_ == 4:
                    self.state = 51
                    self.definitionList()
                    pass


                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 57
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


        def functionCall(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.FunctionCallContext)
            else:
                return self.getTypedRuleContext(CParser.FunctionCallContext,i)


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
            self.state = 59
            self.match(CParser.LC)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 33619936) != 0:
                self.state = 65
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 60
                    self.expression(0)
                    pass

                elif la_ == 2:
                    self.state = 61
                    self.definitionList()
                    pass

                elif la_ == 3:
                    self.state = 62
                    self.declarationList(0)
                    pass

                elif la_ == 4:
                    self.state = 63
                    self.functionCall()
                    pass

                elif la_ == 5:
                    self.state = 64
                    self.assignment()
                    pass


                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 70
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
            self.state = 72
            self.typeSpecifier()
            self.state = 73
            self.identifier()
            self.state = 74
            self.match(CParser.T__0)
            self.state = 75
            self.expression(0)
            self.state = 76
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


        def functionCallExpression(self):
            return self.getTypedRuleContext(CParser.FunctionCallExpressionContext,0)


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
            self.state = 82
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 79
                self.constant()
                pass

            elif la_ == 2:
                self.state = 80
                self.functionCallExpression()
                pass

            elif la_ == 3:
                self.state = 81
                self.identifier()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 102
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 100
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = CParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 84
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 85
                        self.multiplyOp()
                        self.state = 86
                        self.expression(5)
                        pass

                    elif la_ == 2:
                        localctx = CParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 88
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 89
                        self.divideOp()
                        self.state = 90
                        self.expression(4)
                        pass

                    elif la_ == 3:
                        localctx = CParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 92
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 93
                        self.addOp()
                        self.state = 94
                        self.expression(3)
                        pass

                    elif la_ == 4:
                        localctx = CParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 96
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 97
                        self.subtractOp()
                        self.state = 98
                        self.expression(2)
                        pass

             
                self.state = 104
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
            self.state = 105
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
            self.state = 107
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
            self.state = 109
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
            self.state = 111
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
            self.state = 115
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.match(CParser.INTEGER)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 114
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


    class FunctionCallExpressionContext(ParserRuleContext):
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

        def functionCallArgs(self):
            return self.getTypedRuleContext(CParser.FunctionCallArgsContext,0)


        def getRuleIndex(self):
            return CParser.RULE_functionCallExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCallExpression" ):
                listener.enterFunctionCallExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCallExpression" ):
                listener.exitFunctionCallExpression(self)




    def functionCallExpression(self):

        localctx = CParser.FunctionCallExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_functionCallExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.identifier()
            self.state = 118
            self.match(CParser.LP)
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 33554528) != 0:
                self.state = 119
                self.functionCallArgs(0)


            self.state = 122
            self.match(CParser.RP)
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

        def SEMICOLON(self):
            return self.getToken(CParser.SEMICOLON, 0)

        def functionCallArgs(self):
            return self.getTypedRuleContext(CParser.FunctionCallArgsContext,0)


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
        self.enterRule(localctx, 20, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.identifier()
            self.state = 125
            self.match(CParser.LP)
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 33554528) != 0:
                self.state = 126
                self.functionCallArgs(0)


            self.state = 129
            self.match(CParser.RP)
            self.state = 130
            self.match(CParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(CParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(CParser.COMMA, 0)

        def functionCallArgs(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.FunctionCallArgsContext)
            else:
                return self.getTypedRuleContext(CParser.FunctionCallArgsContext,i)


        def getRuleIndex(self):
            return CParser.RULE_functionCallArgs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCallArgs" ):
                listener.enterFunctionCallArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCallArgs" ):
                listener.exitFunctionCallArgs(self)



    def functionCallArgs(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CParser.FunctionCallArgsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_functionCallArgs, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.expression(0)
            self.state = 135
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 134
                self.match(CParser.COMMA)


            self._ctx.stop = self._input.LT(-1)
            self.state = 142
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CParser.FunctionCallArgsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_functionCallArgs)
                    self.state = 137
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 138
                    self.match(CParser.COMMA)
                    self.state = 139
                    self.functionCallArgs(2) 
                self.state = 144
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 24, self.RULE_statementList)
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
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_declarationList, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.declaration()
            self._ctx.stop = self._input.LT(-1)
            self.state = 154
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CParser.DeclarationListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_declarationList)
                    self.state = 150
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 151
                    self.declaration() 
                self.state = 156
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

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
        self.enterRule(localctx, 28, self.RULE_declaration)
        try:
            self.state = 161
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                self.functionDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 158
                self.variableDeclaration()
                self.state = 159
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
        self.enterRule(localctx, 30, self.RULE_variableDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.typeSpecifier()
            self.state = 164
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


        def LP(self):
            return self.getToken(CParser.LP, 0)

        def RP(self):
            return self.getToken(CParser.RP, 0)

        def SEMICOLON(self):
            return self.getToken(CParser.SEMICOLON, 0)

        def typeSpecifier(self):
            return self.getTypedRuleContext(CParser.TypeSpecifierContext,0)


        def functionArgs(self):
            return self.getTypedRuleContext(CParser.FunctionArgsContext,0)


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
        self.enterRule(localctx, 32, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 166
                self.typeSpecifier()


            self.state = 169
            self.functionName()
            self.state = 170
            self.match(CParser.LP)
            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 33619840) != 0:
                self.state = 171
                self.functionArgs(0)


            self.state = 174
            self.match(CParser.RP)
            self.state = 175
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
        self.enterRule(localctx, 34, self.RULE_definitionList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
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


        def LP(self):
            return self.getToken(CParser.LP, 0)

        def RP(self):
            return self.getToken(CParser.RP, 0)

        def functionBlock(self):
            return self.getTypedRuleContext(CParser.FunctionBlockContext,0)


        def typeSpecifier(self):
            return self.getTypedRuleContext(CParser.TypeSpecifierContext,0)


        def functionArgs(self):
            return self.getTypedRuleContext(CParser.FunctionArgsContext,0)


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
        self.enterRule(localctx, 36, self.RULE_functionDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 179
                self.typeSpecifier()


            self.state = 182
            self.functionName()
            self.state = 183
            self.match(CParser.LP)
            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 33619840) != 0:
                self.state = 184
                self.functionArgs(0)


            self.state = 187
            self.match(CParser.RP)
            self.state = 188
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
        self.enterRule(localctx, 38, self.RULE_functionName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
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

        def typeSpecifier(self):
            return self.getTypedRuleContext(CParser.TypeSpecifierContext,0)


        def identifier(self):
            return self.getTypedRuleContext(CParser.IdentifierContext,0)


        def COMMA(self):
            return self.getToken(CParser.COMMA, 0)

        def functionArgs(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.FunctionArgsContext)
            else:
                return self.getTypedRuleContext(CParser.FunctionArgsContext,i)


        def getRuleIndex(self):
            return CParser.RULE_functionArgs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionArgs" ):
                listener.enterFunctionArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionArgs" ):
                listener.exitFunctionArgs(self)



    def functionArgs(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CParser.FunctionArgsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_functionArgs, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.typeSpecifier()
            self.state = 195
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 194
                self.identifier()


            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 197
                self.match(CParser.COMMA)


            self._ctx.stop = self._input.LT(-1)
            self.state = 205
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CParser.FunctionArgsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_functionArgs)
                    self.state = 200
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 201
                    self.match(CParser.COMMA)
                    self.state = 202
                    self.functionArgs(2) 
                self.state = 207
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TypeSpecifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VOID(self):
            return self.getToken(CParser.VOID, 0)

        def identifier(self):
            return self.getTypedRuleContext(CParser.IdentifierContext,0)


        def STAR(self, i:int=None):
            if i is None:
                return self.getTokens(CParser.STAR)
            else:
                return self.getToken(CParser.STAR, i)

        def CHAR(self):
            return self.getToken(CParser.CHAR, 0)

        def SHORT(self):
            return self.getToken(CParser.SHORT, 0)

        def INT(self):
            return self.getToken(CParser.INT, 0)

        def LONG(self):
            return self.getToken(CParser.LONG, 0)

        def FLOAT(self):
            return self.getToken(CParser.FLOAT, 0)

        def DOUBLE(self):
            return self.getToken(CParser.DOUBLE, 0)

        def SIGNED(self):
            return self.getToken(CParser.SIGNED, 0)

        def UNSIGNED(self):
            return self.getToken(CParser.UNSIGNED, 0)

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
        self.enterRule(localctx, 42, self.RULE_typeSpecifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.state = 208
                self.match(CParser.VOID)
                pass
            elif token in [7, 8, 10, 11, 12, 13, 14, 15]:
                self.state = 210
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==7 or _la==8:
                    self.state = 209
                    _la = self._input.LA(1)
                    if not(_la==7 or _la==8):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 225
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                if la_ == 1:
                    self.state = 212
                    self.match(CParser.CHAR)
                    pass

                elif la_ == 2:
                    self.state = 213
                    self.match(CParser.SHORT)
                    pass

                elif la_ == 3:
                    self.state = 215
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==11:
                        self.state = 214
                        self.match(CParser.SHORT)


                    self.state = 217
                    self.match(CParser.INT)
                    pass

                elif la_ == 4:
                    self.state = 218
                    self.match(CParser.LONG)
                    pass

                elif la_ == 5:
                    self.state = 219
                    self.match(CParser.FLOAT)
                    pass

                elif la_ == 6:
                    self.state = 221
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==13:
                        self.state = 220
                        self.match(CParser.LONG)


                    self.state = 223
                    self.match(CParser.DOUBLE)
                    pass

                elif la_ == 7:
                    self.state = 224
                    self.match(CParser.INT)
                    pass


                pass
            elif token in [25]:
                self.state = 227
                self.identifier()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 233
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 230
                    self.match(CParser.STAR) 
                self.state = 235
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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
        self.enterRule(localctx, 44, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.match(CParser.IDENTIFIER)
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
        self.enterRule(localctx, 46, self.RULE_stringLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(CParser.T__4)
            self.state = 242
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 1073741790) != 0:
                self.state = 239
                _la = self._input.LA(1)
                if _la <= 0 or _la==5:
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 244
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 245
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
        self._predicates[11] = self.functionCallArgs_sempred
        self._predicates[13] = self.declarationList_sempred
        self._predicates[20] = self.functionArgs_sempred
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
         

    def functionCallArgs_sempred(self, localctx:FunctionCallArgsContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 1)
         

    def declarationList_sempred(self, localctx:DeclarationListContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 1)
         

    def functionArgs_sempred(self, localctx:FunctionArgsContext, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 1)
         




