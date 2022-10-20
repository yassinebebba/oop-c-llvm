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
        4,1,90,278,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,1,0,1,0,1,0,1,0,1,0,
        1,0,5,0,57,8,0,10,0,12,0,60,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,5,1,73,8,1,10,1,12,1,76,9,1,1,1,1,1,1,2,1,2,1,2,1,2,
        1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,95,8,3,3,3,97,8,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,111,8,3,10,
        3,12,3,114,9,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,
        7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,4,8,136,8,8,11,8,12,8,137,3,8,140,
        8,8,1,9,1,9,1,9,3,9,145,8,9,1,9,1,9,1,10,1,10,1,10,3,10,152,8,10,
        1,10,1,10,1,10,1,11,1,11,1,11,3,11,160,8,11,1,11,1,11,1,11,5,11,
        165,8,11,10,11,12,11,168,9,11,1,12,1,12,1,13,1,13,1,13,1,13,1,13,
        5,13,177,8,13,10,13,12,13,180,9,13,1,14,1,14,1,14,1,14,3,14,186,
        8,14,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,17,3,17,198,
        8,17,1,17,1,17,1,17,3,17,203,8,17,1,17,1,17,1,17,1,18,1,18,1,19,
        3,19,211,8,19,1,19,1,19,1,19,3,19,216,8,19,1,19,1,19,1,19,1,20,1,
        20,3,20,223,8,20,1,20,1,20,1,21,1,21,1,22,1,22,1,22,3,22,232,8,22,
        1,22,3,22,235,8,22,1,22,1,22,1,22,5,22,240,8,22,10,22,12,22,243,
        9,22,1,23,3,23,246,8,23,1,23,1,23,3,23,250,8,23,1,23,1,23,1,23,3,
        23,255,8,23,1,23,1,23,1,23,1,23,3,23,261,8,23,1,23,1,23,3,23,265,
        8,23,1,23,3,23,268,8,23,1,23,5,23,271,8,23,10,23,12,23,274,9,23,
        1,24,1,24,1,24,0,4,6,22,26,44,25,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,30,32,34,36,38,40,42,44,46,48,0,1,1,0,31,32,305,0,58,1,
        0,0,0,2,63,1,0,0,0,4,79,1,0,0,0,6,96,1,0,0,0,8,115,1,0,0,0,10,119,
        1,0,0,0,12,123,1,0,0,0,14,127,1,0,0,0,16,139,1,0,0,0,18,141,1,0,
        0,0,20,148,1,0,0,0,22,156,1,0,0,0,24,169,1,0,0,0,26,171,1,0,0,0,
        28,185,1,0,0,0,30,187,1,0,0,0,32,190,1,0,0,0,34,197,1,0,0,0,36,207,
        1,0,0,0,38,210,1,0,0,0,40,220,1,0,0,0,42,226,1,0,0,0,44,228,1,0,
        0,0,46,245,1,0,0,0,48,275,1,0,0,0,50,57,3,4,2,0,51,57,3,32,16,0,
        52,57,3,30,15,0,53,57,3,20,10,0,54,57,3,26,13,0,55,57,3,36,18,0,
        56,50,1,0,0,0,56,51,1,0,0,0,56,52,1,0,0,0,56,53,1,0,0,0,56,54,1,
        0,0,0,56,55,1,0,0,0,57,60,1,0,0,0,58,56,1,0,0,0,58,59,1,0,0,0,59,
        61,1,0,0,0,60,58,1,0,0,0,61,62,5,0,0,1,62,1,1,0,0,0,63,74,5,49,0,
        0,64,73,3,6,3,0,65,73,3,32,16,0,66,73,3,30,15,0,67,73,3,36,18,0,
        68,73,3,26,13,0,69,73,3,20,10,0,70,73,3,4,2,0,71,73,3,40,20,0,72,
        64,1,0,0,0,72,65,1,0,0,0,72,66,1,0,0,0,72,67,1,0,0,0,72,68,1,0,0,
        0,72,69,1,0,0,0,72,70,1,0,0,0,72,71,1,0,0,0,73,76,1,0,0,0,74,72,
        1,0,0,0,74,75,1,0,0,0,75,77,1,0,0,0,76,74,1,0,0,0,77,78,5,50,0,0,
        78,3,1,0,0,0,79,80,3,48,24,0,80,81,5,70,0,0,81,82,3,6,3,0,82,83,
        5,68,0,0,83,5,1,0,0,0,84,85,6,3,-1,0,85,97,3,16,8,0,86,97,3,18,9,
        0,87,97,3,48,24,0,88,94,5,22,0,0,89,95,3,6,3,0,90,91,5,47,0,0,91,
        92,3,6,3,0,92,93,5,48,0,0,93,95,1,0,0,0,94,89,1,0,0,0,94,90,1,0,
        0,0,95,97,1,0,0,0,96,84,1,0,0,0,96,86,1,0,0,0,96,87,1,0,0,0,96,88,
        1,0,0,0,97,112,1,0,0,0,98,99,10,4,0,0,99,100,5,44,0,0,100,111,3,
        6,3,5,101,102,10,3,0,0,102,103,5,45,0,0,103,111,3,6,3,4,104,105,
        10,2,0,0,105,106,5,40,0,0,106,111,3,6,3,3,107,108,10,1,0,0,108,109,
        5,42,0,0,109,111,3,6,3,2,110,98,1,0,0,0,110,101,1,0,0,0,110,104,
        1,0,0,0,110,107,1,0,0,0,111,114,1,0,0,0,112,110,1,0,0,0,112,113,
        1,0,0,0,113,7,1,0,0,0,114,112,1,0,0,0,115,116,3,6,3,0,116,117,5,
        44,0,0,117,118,3,6,3,0,118,9,1,0,0,0,119,120,3,6,3,0,120,121,5,45,
        0,0,121,122,3,6,3,0,122,11,1,0,0,0,123,124,3,6,3,0,124,125,5,40,
        0,0,125,126,3,6,3,0,126,13,1,0,0,0,127,128,3,6,3,0,128,129,5,42,
        0,0,129,130,3,6,3,0,130,15,1,0,0,0,131,140,5,3,0,0,132,140,5,4,0,
        0,133,140,5,2,0,0,134,136,5,1,0,0,135,134,1,0,0,0,136,137,1,0,0,
        0,137,135,1,0,0,0,137,138,1,0,0,0,138,140,1,0,0,0,139,131,1,0,0,
        0,139,132,1,0,0,0,139,133,1,0,0,0,139,135,1,0,0,0,140,17,1,0,0,0,
        141,142,3,48,24,0,142,144,5,47,0,0,143,145,3,22,11,0,144,143,1,0,
        0,0,144,145,1,0,0,0,145,146,1,0,0,0,146,147,5,48,0,0,147,19,1,0,
        0,0,148,149,3,48,24,0,149,151,5,47,0,0,150,152,3,22,11,0,151,150,
        1,0,0,0,151,152,1,0,0,0,152,153,1,0,0,0,153,154,5,48,0,0,154,155,
        5,68,0,0,155,21,1,0,0,0,156,157,6,11,-1,0,157,159,3,6,3,0,158,160,
        5,69,0,0,159,158,1,0,0,0,159,160,1,0,0,0,160,166,1,0,0,0,161,162,
        10,1,0,0,162,163,5,69,0,0,163,165,3,22,11,2,164,161,1,0,0,0,165,
        168,1,0,0,0,166,164,1,0,0,0,166,167,1,0,0,0,167,23,1,0,0,0,168,166,
        1,0,0,0,169,170,1,0,0,0,170,25,1,0,0,0,171,172,6,13,-1,0,172,173,
        3,28,14,0,173,178,1,0,0,0,174,175,10,1,0,0,175,177,3,28,14,0,176,
        174,1,0,0,0,177,180,1,0,0,0,178,176,1,0,0,0,178,179,1,0,0,0,179,
        27,1,0,0,0,180,178,1,0,0,0,181,186,3,34,17,0,182,183,3,30,15,0,183,
        184,5,68,0,0,184,186,1,0,0,0,185,181,1,0,0,0,185,182,1,0,0,0,186,
        29,1,0,0,0,187,188,3,46,23,0,188,189,3,48,24,0,189,31,1,0,0,0,190,
        191,3,46,23,0,191,192,3,48,24,0,192,193,5,70,0,0,193,194,3,6,3,0,
        194,195,5,68,0,0,195,33,1,0,0,0,196,198,3,46,23,0,197,196,1,0,0,
        0,197,198,1,0,0,0,198,199,1,0,0,0,199,200,3,42,21,0,200,202,5,47,
        0,0,201,203,3,44,22,0,202,201,1,0,0,0,202,203,1,0,0,0,203,204,1,
        0,0,0,204,205,5,48,0,0,205,206,5,68,0,0,206,35,1,0,0,0,207,208,3,
        38,19,0,208,37,1,0,0,0,209,211,3,46,23,0,210,209,1,0,0,0,210,211,
        1,0,0,0,211,212,1,0,0,0,212,213,3,42,21,0,213,215,5,47,0,0,214,216,
        3,44,22,0,215,214,1,0,0,0,215,216,1,0,0,0,216,217,1,0,0,0,217,218,
        5,48,0,0,218,219,3,2,1,0,219,39,1,0,0,0,220,222,5,21,0,0,221,223,
        3,6,3,0,222,221,1,0,0,0,222,223,1,0,0,0,223,224,1,0,0,0,224,225,
        5,68,0,0,225,41,1,0,0,0,226,227,3,48,24,0,227,43,1,0,0,0,228,229,
        6,22,-1,0,229,231,3,46,23,0,230,232,3,48,24,0,231,230,1,0,0,0,231,
        232,1,0,0,0,232,234,1,0,0,0,233,235,5,69,0,0,234,233,1,0,0,0,234,
        235,1,0,0,0,235,241,1,0,0,0,236,237,10,1,0,0,237,238,5,69,0,0,238,
        240,3,44,22,2,239,236,1,0,0,0,240,243,1,0,0,0,241,239,1,0,0,0,241,
        242,1,0,0,0,242,45,1,0,0,0,243,241,1,0,0,0,244,246,5,30,0,0,245,
        244,1,0,0,0,245,246,1,0,0,0,246,267,1,0,0,0,247,268,5,33,0,0,248,
        250,7,0,0,0,249,248,1,0,0,0,249,250,1,0,0,0,250,264,1,0,0,0,251,
        265,5,34,0,0,252,265,5,35,0,0,253,255,5,35,0,0,254,253,1,0,0,0,254,
        255,1,0,0,0,255,256,1,0,0,0,256,265,5,36,0,0,257,265,5,37,0,0,258,
        265,5,38,0,0,259,261,5,37,0,0,260,259,1,0,0,0,260,261,1,0,0,0,261,
        262,1,0,0,0,262,265,5,39,0,0,263,265,5,36,0,0,264,251,1,0,0,0,264,
        252,1,0,0,0,264,254,1,0,0,0,264,257,1,0,0,0,264,258,1,0,0,0,264,
        260,1,0,0,0,264,263,1,0,0,0,265,268,1,0,0,0,266,268,3,48,24,0,267,
        247,1,0,0,0,267,249,1,0,0,0,267,266,1,0,0,0,268,272,1,0,0,0,269,
        271,5,44,0,0,270,269,1,0,0,0,271,274,1,0,0,0,272,270,1,0,0,0,272,
        273,1,0,0,0,273,47,1,0,0,0,274,272,1,0,0,0,275,276,5,86,0,0,276,
        49,1,0,0,0,31,56,58,72,74,94,96,110,112,137,139,144,151,159,166,
        178,185,197,202,210,215,222,231,234,241,245,249,254,260,264,267,
        272
    ]

class CParser ( Parser ):

    grammarFileName = "C.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'auto'", "'break'", "'case'", 
                     "'continue'", "'default'", "'do'", "'else'", "'enum'", 
                     "'extern'", "'for'", "'goto'", "'if'", "'inline'", 
                     "'register'", "'restrict'", "'return'", "'sizeof'", 
                     "'static'", "'struct'", "'switch'", "'typedef'", "'union'", 
                     "'volatile'", "'while'", "'const'", "'signed'", "'unsigned'", 
                     "'void'", "'char'", "'short'", "'int'", "'long'", "'float'", 
                     "'double'", "'+'", "'++'", "'-'", "'--'", "'*'", "'/'", 
                     "'%'", "'('", "')'", "'{'", "'}'", "'['", "']'", "'<'", 
                     "'<='", "'>'", "'>='", "'<<'", "'>>'", "'&'", "'|'", 
                     "'&&'", "'||'", "'^'", "'!'", "'~'", "'?'", "':'", 
                     "';'", "','", "'='", "'*='", "'/='", "'%='", "'+='", 
                     "'-='", "'<<='", "'>>='", "'&='", "'^='", "'|='", "'=='", 
                     "'!='", "'->'", "'.'", "'...'" ]

    symbolicNames = [ "<INVALID>", "STRING_LITERAL", "CHAR_CONSTANT", "INTEGER_CONSTANT", 
                      "FLOAT_CONSTANT", "EXPONENT", "AUTO", "BREAK", "CASE", 
                      "CONTINUE", "DEFAULT", "DO", "ELSE", "ENUM", "EXTERN", 
                      "FOR", "GOTO", "IF", "INLINE", "REGISTER", "RESTRICT", 
                      "RETURN", "SIZEOF", "STATIC", "STRUCT", "SWITCH", 
                      "TYPEDEF", "UNION", "VOLATILE", "WHILE", "CONST", 
                      "SIGNED", "UNSIGNED", "VOID", "CHAR", "SHORT", "INT", 
                      "LONG", "FLOAT", "DOUBLE", "PLUS", "PLUS_PLUS", "MINUS", 
                      "MINUS_MINUS", "STAR", "DIV", "MOD", "LP", "RP", "LC", 
                      "RC", "LSQRB", "RSQRB", "LT", "LTE", "GT", "GTE", 
                      "LEFT_SHIFT", "RIGHT_SHIFT", "AND", "OR", "AND_AND", 
                      "OR_OR", "CARET", "NOT", "TILDE", "QUESTION", "COLON", 
                      "SEMI", "COMMA", "ASSIGN", "STAR_ASSIGN", "DIV_ASSIGN", 
                      "MOD_ASSIGN", "PLUS_ASSIGN", "MINUS_ASSIGN", "LEFT_SHIFT_ASSIGN", 
                      "RIGHT_SHIFT_ASSIGN", "BITWISE_AND_ASSIGN", "BITWISE_XOR_ASSIGN", 
                      "BITWISE_OR_ASSIGN", "EQ", "NEQ", "ARROW", "DOT", 
                      "ELLIPSIS", "IDENTIFIER", "WS", "NEWLINE", "BLOCK_COMMENT", 
                      "LINE_COMMENT" ]

    RULE_compilationUnit = 0
    RULE_functionBlock = 1
    RULE_assignment = 2
    RULE_expression = 3
    RULE_multiplyExpression = 4
    RULE_divideExpression = 5
    RULE_addExpression = 6
    RULE_subtractExpression = 7
    RULE_constant = 8
    RULE_functionCallExpression = 9
    RULE_functionCall = 10
    RULE_functionCallArgs = 11
    RULE_statementList = 12
    RULE_declarationList = 13
    RULE_declaration = 14
    RULE_variableDeclaration = 15
    RULE_variableInitialization = 16
    RULE_functionDeclaration = 17
    RULE_definitionList = 18
    RULE_functionDefinition = 19
    RULE_functionReturn = 20
    RULE_functionName = 21
    RULE_functionArgs = 22
    RULE_typeSpecifier = 23
    RULE_identifier = 24

    ruleNames =  [ "compilationUnit", "functionBlock", "assignment", "expression", 
                   "multiplyExpression", "divideExpression", "addExpression", 
                   "subtractExpression", "constant", "functionCallExpression", 
                   "functionCall", "functionCallArgs", "statementList", 
                   "declarationList", "declaration", "variableDeclaration", 
                   "variableInitialization", "functionDeclaration", "definitionList", 
                   "functionDefinition", "functionReturn", "functionName", 
                   "functionArgs", "typeSpecifier", "identifier" ]

    EOF = Token.EOF
    STRING_LITERAL=1
    CHAR_CONSTANT=2
    INTEGER_CONSTANT=3
    FLOAT_CONSTANT=4
    EXPONENT=5
    AUTO=6
    BREAK=7
    CASE=8
    CONTINUE=9
    DEFAULT=10
    DO=11
    ELSE=12
    ENUM=13
    EXTERN=14
    FOR=15
    GOTO=16
    IF=17
    INLINE=18
    REGISTER=19
    RESTRICT=20
    RETURN=21
    SIZEOF=22
    STATIC=23
    STRUCT=24
    SWITCH=25
    TYPEDEF=26
    UNION=27
    VOLATILE=28
    WHILE=29
    CONST=30
    SIGNED=31
    UNSIGNED=32
    VOID=33
    CHAR=34
    SHORT=35
    INT=36
    LONG=37
    FLOAT=38
    DOUBLE=39
    PLUS=40
    PLUS_PLUS=41
    MINUS=42
    MINUS_MINUS=43
    STAR=44
    DIV=45
    MOD=46
    LP=47
    RP=48
    LC=49
    RC=50
    LSQRB=51
    RSQRB=52
    LT=53
    LTE=54
    GT=55
    GTE=56
    LEFT_SHIFT=57
    RIGHT_SHIFT=58
    AND=59
    OR=60
    AND_AND=61
    OR_OR=62
    CARET=63
    NOT=64
    TILDE=65
    QUESTION=66
    COLON=67
    SEMI=68
    COMMA=69
    ASSIGN=70
    STAR_ASSIGN=71
    DIV_ASSIGN=72
    MOD_ASSIGN=73
    PLUS_ASSIGN=74
    MINUS_ASSIGN=75
    LEFT_SHIFT_ASSIGN=76
    RIGHT_SHIFT_ASSIGN=77
    BITWISE_AND_ASSIGN=78
    BITWISE_XOR_ASSIGN=79
    BITWISE_OR_ASSIGN=80
    EQ=81
    NEQ=82
    ARROW=83
    DOT=84
    ELLIPSIS=85
    IDENTIFIER=86
    WS=87
    NEWLINE=88
    BLOCK_COMMENT=89
    LINE_COMMENT=90

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


        def variableInitialization(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.VariableInitializationContext)
            else:
                return self.getTypedRuleContext(CParser.VariableInitializationContext,i)


        def variableDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.VariableDeclarationContext)
            else:
                return self.getTypedRuleContext(CParser.VariableDeclarationContext,i)


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
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la - 30)) & ~0x3f) == 0 and ((1 << (_la - 30)) & 72057594037928959) != 0:
                self.state = 56
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 50
                    self.assignment()
                    pass

                elif la_ == 2:
                    self.state = 51
                    self.variableInitialization()
                    pass

                elif la_ == 3:
                    self.state = 52
                    self.variableDeclaration()
                    pass

                elif la_ == 4:
                    self.state = 53
                    self.functionCall()
                    pass

                elif la_ == 5:
                    self.state = 54
                    self.declarationList(0)
                    pass

                elif la_ == 6:
                    self.state = 55
                    self.definitionList()
                    pass


                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 61
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


        def variableInitialization(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.VariableInitializationContext)
            else:
                return self.getTypedRuleContext(CParser.VariableInitializationContext,i)


        def variableDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.VariableDeclarationContext)
            else:
                return self.getTypedRuleContext(CParser.VariableDeclarationContext,i)


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


        def functionReturn(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.FunctionReturnContext)
            else:
                return self.getTypedRuleContext(CParser.FunctionReturnContext,i)


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
            self.state = 63
            self.match(CParser.LC)
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 1098444177438) != 0 or _la==86:
                self.state = 72
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 64
                    self.expression(0)
                    pass

                elif la_ == 2:
                    self.state = 65
                    self.variableInitialization()
                    pass

                elif la_ == 3:
                    self.state = 66
                    self.variableDeclaration()
                    pass

                elif la_ == 4:
                    self.state = 67
                    self.definitionList()
                    pass

                elif la_ == 5:
                    self.state = 68
                    self.declarationList(0)
                    pass

                elif la_ == 6:
                    self.state = 69
                    self.functionCall()
                    pass

                elif la_ == 7:
                    self.state = 70
                    self.assignment()
                    pass

                elif la_ == 8:
                    self.state = 71
                    self.functionReturn()
                    pass


                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 77
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

        def identifier(self):
            return self.getTypedRuleContext(CParser.IdentifierContext,0)


        def ASSIGN(self):
            return self.getToken(CParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(CParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(CParser.SEMI, 0)

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
            self.state = 79
            self.identifier()
            self.state = 80
            self.match(CParser.ASSIGN)
            self.state = 81
            self.expression(0)
            self.state = 82
            self.match(CParser.SEMI)
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


        def SIZEOF(self):
            return self.getToken(CParser.SIZEOF, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CParser.ExpressionContext,i)


        def LP(self):
            return self.getToken(CParser.LP, 0)

        def RP(self):
            return self.getToken(CParser.RP, 0)

        def STAR(self):
            return self.getToken(CParser.STAR, 0)

        def DIV(self):
            return self.getToken(CParser.DIV, 0)

        def PLUS(self):
            return self.getToken(CParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(CParser.MINUS, 0)

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
            self.state = 96
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 85
                self.constant()
                pass

            elif la_ == 2:
                self.state = 86
                self.functionCallExpression()
                pass

            elif la_ == 3:
                self.state = 87
                self.identifier()
                pass

            elif la_ == 4:
                self.state = 88
                self.match(CParser.SIZEOF)
                self.state = 94
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 2, 3, 4, 22, 86]:
                    self.state = 89
                    self.expression(0)
                    pass
                elif token in [47]:
                    self.state = 90
                    self.match(CParser.LP)
                    self.state = 91
                    self.expression(0)
                    self.state = 92
                    self.match(CParser.RP)
                    pass
                else:
                    raise NoViableAltException(self)

                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 112
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 110
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = CParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 98
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 99
                        self.match(CParser.STAR)
                        self.state = 100
                        self.expression(5)
                        pass

                    elif la_ == 2:
                        localctx = CParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 101
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 102
                        self.match(CParser.DIV)
                        self.state = 103
                        self.expression(4)
                        pass

                    elif la_ == 3:
                        localctx = CParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 104
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 105
                        self.match(CParser.PLUS)
                        self.state = 106
                        self.expression(3)
                        pass

                    elif la_ == 4:
                        localctx = CParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 107
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 108
                        self.match(CParser.MINUS)
                        self.state = 109
                        self.expression(2)
                        pass

             
                self.state = 114
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MultiplyExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CParser.ExpressionContext,i)


        def STAR(self):
            return self.getToken(CParser.STAR, 0)

        def getRuleIndex(self):
            return CParser.RULE_multiplyExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplyExpression" ):
                listener.enterMultiplyExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplyExpression" ):
                listener.exitMultiplyExpression(self)




    def multiplyExpression(self):

        localctx = CParser.MultiplyExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_multiplyExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.expression(0)
            self.state = 116
            self.match(CParser.STAR)
            self.state = 117
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DivideExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CParser.ExpressionContext,i)


        def DIV(self):
            return self.getToken(CParser.DIV, 0)

        def getRuleIndex(self):
            return CParser.RULE_divideExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivideExpression" ):
                listener.enterDivideExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivideExpression" ):
                listener.exitDivideExpression(self)




    def divideExpression(self):

        localctx = CParser.DivideExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_divideExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.expression(0)
            self.state = 120
            self.match(CParser.DIV)
            self.state = 121
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CParser.ExpressionContext,i)


        def PLUS(self):
            return self.getToken(CParser.PLUS, 0)

        def getRuleIndex(self):
            return CParser.RULE_addExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddExpression" ):
                listener.enterAddExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddExpression" ):
                listener.exitAddExpression(self)




    def addExpression(self):

        localctx = CParser.AddExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_addExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.expression(0)
            self.state = 124
            self.match(CParser.PLUS)
            self.state = 125
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubtractExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CParser.ExpressionContext,i)


        def MINUS(self):
            return self.getToken(CParser.MINUS, 0)

        def getRuleIndex(self):
            return CParser.RULE_subtractExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubtractExpression" ):
                listener.enterSubtractExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubtractExpression" ):
                listener.exitSubtractExpression(self)




    def subtractExpression(self):

        localctx = CParser.SubtractExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_subtractExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.expression(0)
            self.state = 128
            self.match(CParser.MINUS)
            self.state = 129
            self.expression(0)
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

        def INTEGER_CONSTANT(self):
            return self.getToken(CParser.INTEGER_CONSTANT, 0)

        def FLOAT_CONSTANT(self):
            return self.getToken(CParser.FLOAT_CONSTANT, 0)

        def CHAR_CONSTANT(self):
            return self.getToken(CParser.CHAR_CONSTANT, 0)

        def STRING_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(CParser.STRING_LITERAL)
            else:
                return self.getToken(CParser.STRING_LITERAL, i)

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
            self.state = 139
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.match(CParser.INTEGER_CONSTANT)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self.match(CParser.FLOAT_CONSTANT)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 133
                self.match(CParser.CHAR_CONSTANT)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 4)
                self.state = 135 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 134
                        self.match(CParser.STRING_LITERAL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 137 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

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
            self.state = 141
            self.identifier()
            self.state = 142
            self.match(CParser.LP)
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 4194334) != 0 or _la==86:
                self.state = 143
                self.functionCallArgs(0)


            self.state = 146
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

        def SEMI(self):
            return self.getToken(CParser.SEMI, 0)

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
            self.state = 148
            self.identifier()
            self.state = 149
            self.match(CParser.LP)
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 4194334) != 0 or _la==86:
                self.state = 150
                self.functionCallArgs(0)


            self.state = 153
            self.match(CParser.RP)
            self.state = 154
            self.match(CParser.SEMI)
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
            self.state = 157
            self.expression(0)
            self.state = 159
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 158
                self.match(CParser.COMMA)


            self._ctx.stop = self._input.LT(-1)
            self.state = 166
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CParser.FunctionCallArgsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_functionCallArgs)
                    self.state = 161
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 162
                    self.match(CParser.COMMA)
                    self.state = 163
                    self.functionCallArgs(2) 
                self.state = 168
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

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
            self.state = 172
            self.declaration()
            self._ctx.stop = self._input.LT(-1)
            self.state = 178
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CParser.DeclarationListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_declarationList)
                    self.state = 174
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 175
                    self.declaration() 
                self.state = 180
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

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


        def SEMI(self):
            return self.getToken(CParser.SEMI, 0)

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
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.functionDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 182
                self.variableDeclaration()
                self.state = 183
                self.match(CParser.SEMI)
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
            self.state = 187
            self.typeSpecifier()
            self.state = 188
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableInitializationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeSpecifier(self):
            return self.getTypedRuleContext(CParser.TypeSpecifierContext,0)


        def identifier(self):
            return self.getTypedRuleContext(CParser.IdentifierContext,0)


        def ASSIGN(self):
            return self.getToken(CParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(CParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(CParser.SEMI, 0)

        def getRuleIndex(self):
            return CParser.RULE_variableInitialization

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableInitialization" ):
                listener.enterVariableInitialization(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableInitialization" ):
                listener.exitVariableInitialization(self)




    def variableInitialization(self):

        localctx = CParser.VariableInitializationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_variableInitialization)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.typeSpecifier()
            self.state = 191
            self.identifier()
            self.state = 192
            self.match(CParser.ASSIGN)
            self.state = 193
            self.expression(0)
            self.state = 194
            self.match(CParser.SEMI)
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

        def SEMI(self):
            return self.getToken(CParser.SEMI, 0)

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
        self.enterRule(localctx, 34, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 196
                self.typeSpecifier()


            self.state = 199
            self.functionName()
            self.state = 200
            self.match(CParser.LP)
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la - 30)) & ~0x3f) == 0 and ((1 << (_la - 30)) & 72057594037928959) != 0:
                self.state = 201
                self.functionArgs(0)


            self.state = 204
            self.match(CParser.RP)
            self.state = 205
            self.match(CParser.SEMI)
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
        self.enterRule(localctx, 36, self.RULE_definitionList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
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
        self.enterRule(localctx, 38, self.RULE_functionDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 209
                self.typeSpecifier()


            self.state = 212
            self.functionName()
            self.state = 213
            self.match(CParser.LP)
            self.state = 215
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la - 30)) & ~0x3f) == 0 and ((1 << (_la - 30)) & 72057594037928959) != 0:
                self.state = 214
                self.functionArgs(0)


            self.state = 217
            self.match(CParser.RP)
            self.state = 218
            self.functionBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionReturnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(CParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(CParser.SEMI, 0)

        def expression(self):
            return self.getTypedRuleContext(CParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CParser.RULE_functionReturn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionReturn" ):
                listener.enterFunctionReturn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionReturn" ):
                listener.exitFunctionReturn(self)




    def functionReturn(self):

        localctx = CParser.FunctionReturnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_functionReturn)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(CParser.RETURN)
            self.state = 222
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 4194334) != 0 or _la==86:
                self.state = 221
                self.expression(0)


            self.state = 224
            self.match(CParser.SEMI)
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
        self.enterRule(localctx, 42, self.RULE_functionName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
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
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_functionArgs, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.typeSpecifier()
            self.state = 231
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 230
                self.identifier()


            self.state = 234
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 233
                self.match(CParser.COMMA)


            self._ctx.stop = self._input.LT(-1)
            self.state = 241
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CParser.FunctionArgsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_functionArgs)
                    self.state = 236
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 237
                    self.match(CParser.COMMA)
                    self.state = 238
                    self.functionArgs(2) 
                self.state = 243
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

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


        def CONST(self):
            return self.getToken(CParser.CONST, 0)

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
        self.enterRule(localctx, 46, self.RULE_typeSpecifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 244
                self.match(CParser.CONST)


            self.state = 267
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                self.state = 247
                self.match(CParser.VOID)
                pass
            elif token in [31, 32, 34, 35, 36, 37, 38, 39]:
                self.state = 249
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31 or _la==32:
                    self.state = 248
                    _la = self._input.LA(1)
                    if not(_la==31 or _la==32):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 264
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                if la_ == 1:
                    self.state = 251
                    self.match(CParser.CHAR)
                    pass

                elif la_ == 2:
                    self.state = 252
                    self.match(CParser.SHORT)
                    pass

                elif la_ == 3:
                    self.state = 254
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==35:
                        self.state = 253
                        self.match(CParser.SHORT)


                    self.state = 256
                    self.match(CParser.INT)
                    pass

                elif la_ == 4:
                    self.state = 257
                    self.match(CParser.LONG)
                    pass

                elif la_ == 5:
                    self.state = 258
                    self.match(CParser.FLOAT)
                    pass

                elif la_ == 6:
                    self.state = 260
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==37:
                        self.state = 259
                        self.match(CParser.LONG)


                    self.state = 262
                    self.match(CParser.DOUBLE)
                    pass

                elif la_ == 7:
                    self.state = 263
                    self.match(CParser.INT)
                    pass


                pass
            elif token in [86]:
                self.state = 266
                self.identifier()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 272
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 269
                    self.match(CParser.STAR) 
                self.state = 274
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

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
        self.enterRule(localctx, 48, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.match(CParser.IDENTIFIER)
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
        self._predicates[22] = self.functionArgs_sempred
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
         




