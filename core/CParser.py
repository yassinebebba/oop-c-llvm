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
        4,1,90,302,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        1,0,1,0,1,0,1,0,1,0,1,0,5,0,61,8,0,10,0,12,0,64,9,0,1,0,1,0,1,1,
        1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,83,8,
        2,3,2,85,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,
        99,8,2,10,2,12,2,102,9,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,
        1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,4,7,124,8,7,11,7,12,7,125,
        3,7,128,8,7,1,8,1,8,1,8,3,8,133,8,8,1,8,1,8,1,9,1,9,1,9,3,9,140,
        8,9,1,9,1,9,1,9,1,10,1,10,1,10,3,10,148,8,10,1,10,1,10,1,10,5,10,
        153,8,10,10,10,12,10,156,9,10,1,11,1,11,1,12,1,12,1,12,1,12,1,12,
        5,12,165,8,12,10,12,12,12,168,9,12,1,13,1,13,1,13,1,13,3,13,174,
        8,13,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,16,3,16,186,
        8,16,1,16,1,16,1,16,3,16,191,8,16,1,16,1,16,1,16,1,17,1,17,1,18,
        3,18,199,8,18,1,18,1,18,1,18,3,18,204,8,18,1,18,1,18,1,18,1,19,1,
        19,3,19,211,8,19,1,19,1,19,1,20,1,20,1,21,1,21,1,21,3,21,220,8,21,
        1,21,3,21,223,8,21,1,21,1,21,1,21,5,21,228,8,21,10,21,12,21,231,
        9,21,1,22,3,22,234,8,22,1,22,1,22,3,22,238,8,22,1,22,1,22,1,22,3,
        22,243,8,22,1,22,1,22,1,22,1,22,3,22,249,8,22,1,22,1,22,3,22,253,
        8,22,1,22,3,22,256,8,22,1,22,5,22,259,8,22,10,22,12,22,262,9,22,
        1,23,1,23,1,23,3,23,267,8,23,1,23,1,23,1,23,1,24,1,24,3,24,274,8,
        24,1,24,1,24,1,24,1,24,3,24,280,8,24,1,25,1,25,1,25,1,25,1,25,1,
        25,1,25,1,25,1,25,1,25,1,25,5,25,293,8,25,10,25,12,25,296,9,25,1,
        25,1,25,1,26,1,26,1,26,0,4,4,20,24,42,27,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,0,1,1,0,31,32,
        332,0,62,1,0,0,0,2,67,1,0,0,0,4,84,1,0,0,0,6,103,1,0,0,0,8,107,1,
        0,0,0,10,111,1,0,0,0,12,115,1,0,0,0,14,127,1,0,0,0,16,129,1,0,0,
        0,18,136,1,0,0,0,20,144,1,0,0,0,22,157,1,0,0,0,24,159,1,0,0,0,26,
        173,1,0,0,0,28,175,1,0,0,0,30,178,1,0,0,0,32,185,1,0,0,0,34,195,
        1,0,0,0,36,198,1,0,0,0,38,208,1,0,0,0,40,214,1,0,0,0,42,216,1,0,
        0,0,44,233,1,0,0,0,46,263,1,0,0,0,48,279,1,0,0,0,50,281,1,0,0,0,
        52,299,1,0,0,0,54,61,3,2,1,0,55,61,3,30,15,0,56,61,3,28,14,0,57,
        61,3,18,9,0,58,61,3,24,12,0,59,61,3,34,17,0,60,54,1,0,0,0,60,55,
        1,0,0,0,60,56,1,0,0,0,60,57,1,0,0,0,60,58,1,0,0,0,60,59,1,0,0,0,
        61,64,1,0,0,0,62,60,1,0,0,0,62,63,1,0,0,0,63,65,1,0,0,0,64,62,1,
        0,0,0,65,66,5,0,0,1,66,1,1,0,0,0,67,68,3,52,26,0,68,69,5,70,0,0,
        69,70,3,4,2,0,70,71,5,68,0,0,71,3,1,0,0,0,72,73,6,2,-1,0,73,85,3,
        14,7,0,74,85,3,16,8,0,75,85,3,52,26,0,76,82,5,22,0,0,77,83,3,4,2,
        0,78,79,5,47,0,0,79,80,3,4,2,0,80,81,5,48,0,0,81,83,1,0,0,0,82,77,
        1,0,0,0,82,78,1,0,0,0,83,85,1,0,0,0,84,72,1,0,0,0,84,74,1,0,0,0,
        84,75,1,0,0,0,84,76,1,0,0,0,85,100,1,0,0,0,86,87,10,4,0,0,87,88,
        5,44,0,0,88,99,3,4,2,5,89,90,10,3,0,0,90,91,5,45,0,0,91,99,3,4,2,
        4,92,93,10,2,0,0,93,94,5,40,0,0,94,99,3,4,2,3,95,96,10,1,0,0,96,
        97,5,42,0,0,97,99,3,4,2,2,98,86,1,0,0,0,98,89,1,0,0,0,98,92,1,0,
        0,0,98,95,1,0,0,0,99,102,1,0,0,0,100,98,1,0,0,0,100,101,1,0,0,0,
        101,5,1,0,0,0,102,100,1,0,0,0,103,104,3,4,2,0,104,105,5,44,0,0,105,
        106,3,4,2,0,106,7,1,0,0,0,107,108,3,4,2,0,108,109,5,45,0,0,109,110,
        3,4,2,0,110,9,1,0,0,0,111,112,3,4,2,0,112,113,5,40,0,0,113,114,3,
        4,2,0,114,11,1,0,0,0,115,116,3,4,2,0,116,117,5,42,0,0,117,118,3,
        4,2,0,118,13,1,0,0,0,119,128,5,3,0,0,120,128,5,4,0,0,121,128,5,2,
        0,0,122,124,5,1,0,0,123,122,1,0,0,0,124,125,1,0,0,0,125,123,1,0,
        0,0,125,126,1,0,0,0,126,128,1,0,0,0,127,119,1,0,0,0,127,120,1,0,
        0,0,127,121,1,0,0,0,127,123,1,0,0,0,128,15,1,0,0,0,129,130,3,52,
        26,0,130,132,5,47,0,0,131,133,3,20,10,0,132,131,1,0,0,0,132,133,
        1,0,0,0,133,134,1,0,0,0,134,135,5,48,0,0,135,17,1,0,0,0,136,137,
        3,52,26,0,137,139,5,47,0,0,138,140,3,20,10,0,139,138,1,0,0,0,139,
        140,1,0,0,0,140,141,1,0,0,0,141,142,5,48,0,0,142,143,5,68,0,0,143,
        19,1,0,0,0,144,145,6,10,-1,0,145,147,3,4,2,0,146,148,5,69,0,0,147,
        146,1,0,0,0,147,148,1,0,0,0,148,154,1,0,0,0,149,150,10,1,0,0,150,
        151,5,69,0,0,151,153,3,20,10,2,152,149,1,0,0,0,153,156,1,0,0,0,154,
        152,1,0,0,0,154,155,1,0,0,0,155,21,1,0,0,0,156,154,1,0,0,0,157,158,
        1,0,0,0,158,23,1,0,0,0,159,160,6,12,-1,0,160,161,3,26,13,0,161,166,
        1,0,0,0,162,163,10,1,0,0,163,165,3,26,13,0,164,162,1,0,0,0,165,168,
        1,0,0,0,166,164,1,0,0,0,166,167,1,0,0,0,167,25,1,0,0,0,168,166,1,
        0,0,0,169,174,3,32,16,0,170,171,3,28,14,0,171,172,5,68,0,0,172,174,
        1,0,0,0,173,169,1,0,0,0,173,170,1,0,0,0,174,27,1,0,0,0,175,176,3,
        44,22,0,176,177,3,52,26,0,177,29,1,0,0,0,178,179,3,44,22,0,179,180,
        3,52,26,0,180,181,5,70,0,0,181,182,3,4,2,0,182,183,5,68,0,0,183,
        31,1,0,0,0,184,186,3,44,22,0,185,184,1,0,0,0,185,186,1,0,0,0,186,
        187,1,0,0,0,187,188,3,40,20,0,188,190,5,47,0,0,189,191,3,42,21,0,
        190,189,1,0,0,0,190,191,1,0,0,0,191,192,1,0,0,0,192,193,5,48,0,0,
        193,194,5,68,0,0,194,33,1,0,0,0,195,196,3,36,18,0,196,35,1,0,0,0,
        197,199,3,44,22,0,198,197,1,0,0,0,198,199,1,0,0,0,199,200,1,0,0,
        0,200,201,3,40,20,0,201,203,5,47,0,0,202,204,3,42,21,0,203,202,1,
        0,0,0,203,204,1,0,0,0,204,205,1,0,0,0,205,206,5,48,0,0,206,207,3,
        50,25,0,207,37,1,0,0,0,208,210,5,21,0,0,209,211,3,4,2,0,210,209,
        1,0,0,0,210,211,1,0,0,0,211,212,1,0,0,0,212,213,5,68,0,0,213,39,
        1,0,0,0,214,215,3,52,26,0,215,41,1,0,0,0,216,217,6,21,-1,0,217,219,
        3,44,22,0,218,220,3,52,26,0,219,218,1,0,0,0,219,220,1,0,0,0,220,
        222,1,0,0,0,221,223,5,69,0,0,222,221,1,0,0,0,222,223,1,0,0,0,223,
        229,1,0,0,0,224,225,10,1,0,0,225,226,5,69,0,0,226,228,3,42,21,2,
        227,224,1,0,0,0,228,231,1,0,0,0,229,227,1,0,0,0,229,230,1,0,0,0,
        230,43,1,0,0,0,231,229,1,0,0,0,232,234,5,30,0,0,233,232,1,0,0,0,
        233,234,1,0,0,0,234,255,1,0,0,0,235,256,5,33,0,0,236,238,7,0,0,0,
        237,236,1,0,0,0,237,238,1,0,0,0,238,252,1,0,0,0,239,253,5,34,0,0,
        240,253,5,35,0,0,241,243,5,35,0,0,242,241,1,0,0,0,242,243,1,0,0,
        0,243,244,1,0,0,0,244,253,5,36,0,0,245,253,5,37,0,0,246,253,5,38,
        0,0,247,249,5,37,0,0,248,247,1,0,0,0,248,249,1,0,0,0,249,250,1,0,
        0,0,250,253,5,39,0,0,251,253,5,36,0,0,252,239,1,0,0,0,252,240,1,
        0,0,0,252,242,1,0,0,0,252,245,1,0,0,0,252,246,1,0,0,0,252,248,1,
        0,0,0,252,251,1,0,0,0,253,256,1,0,0,0,254,256,3,52,26,0,255,235,
        1,0,0,0,255,237,1,0,0,0,255,254,1,0,0,0,256,260,1,0,0,0,257,259,
        5,44,0,0,258,257,1,0,0,0,259,262,1,0,0,0,260,258,1,0,0,0,260,261,
        1,0,0,0,261,45,1,0,0,0,262,260,1,0,0,0,263,264,5,17,0,0,264,266,
        5,47,0,0,265,267,3,48,24,0,266,265,1,0,0,0,266,267,1,0,0,0,267,268,
        1,0,0,0,268,269,5,48,0,0,269,270,3,50,25,0,270,47,1,0,0,0,271,273,
        3,4,2,0,272,274,5,69,0,0,273,272,1,0,0,0,273,274,1,0,0,0,274,280,
        1,0,0,0,275,276,3,4,2,0,276,277,5,69,0,0,277,278,3,4,2,0,278,280,
        1,0,0,0,279,271,1,0,0,0,279,275,1,0,0,0,280,49,1,0,0,0,281,294,5,
        49,0,0,282,293,3,4,2,0,283,293,3,46,23,0,284,293,3,30,15,0,285,293,
        3,28,14,0,286,293,3,34,17,0,287,293,3,24,12,0,288,293,3,18,9,0,289,
        293,3,2,1,0,290,293,3,2,1,0,291,293,3,38,19,0,292,282,1,0,0,0,292,
        283,1,0,0,0,292,284,1,0,0,0,292,285,1,0,0,0,292,286,1,0,0,0,292,
        287,1,0,0,0,292,288,1,0,0,0,292,289,1,0,0,0,292,290,1,0,0,0,292,
        291,1,0,0,0,293,296,1,0,0,0,294,292,1,0,0,0,294,295,1,0,0,0,295,
        297,1,0,0,0,296,294,1,0,0,0,297,298,5,50,0,0,298,51,1,0,0,0,299,
        300,5,86,0,0,300,53,1,0,0,0,34,60,62,82,84,98,100,125,127,132,139,
        147,154,166,173,185,190,198,203,210,219,222,229,233,237,242,248,
        252,255,260,266,273,279,292,294
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
    RULE_assignment = 1
    RULE_expression = 2
    RULE_multiplyExpression = 3
    RULE_divideExpression = 4
    RULE_addExpression = 5
    RULE_subtractExpression = 6
    RULE_constant = 7
    RULE_functionCallExpression = 8
    RULE_functionCall = 9
    RULE_functionCallArgs = 10
    RULE_statementList = 11
    RULE_declarationList = 12
    RULE_declaration = 13
    RULE_variableDeclaration = 14
    RULE_variableInitialization = 15
    RULE_functionDeclaration = 16
    RULE_definitionList = 17
    RULE_functionDefinition = 18
    RULE_functionReturn = 19
    RULE_functionName = 20
    RULE_functionArgs = 21
    RULE_typeSpecifier = 22
    RULE_ifStatement = 23
    RULE_condition = 24
    RULE_block = 25
    RULE_identifier = 26

    ruleNames =  [ "compilationUnit", "assignment", "expression", "multiplyExpression", 
                   "divideExpression", "addExpression", "subtractExpression", 
                   "constant", "functionCallExpression", "functionCall", 
                   "functionCallArgs", "statementList", "declarationList", 
                   "declaration", "variableDeclaration", "variableInitialization", 
                   "functionDeclaration", "definitionList", "functionDefinition", 
                   "functionReturn", "functionName", "functionArgs", "typeSpecifier", 
                   "ifStatement", "condition", "block", "identifier" ]

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
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la - 30)) & ~0x3f) == 0 and ((1 << (_la - 30)) & 72057594037928959) != 0:
                self.state = 60
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 54
                    self.assignment()
                    pass

                elif la_ == 2:
                    self.state = 55
                    self.variableInitialization()
                    pass

                elif la_ == 3:
                    self.state = 56
                    self.variableDeclaration()
                    pass

                elif la_ == 4:
                    self.state = 57
                    self.functionCall()
                    pass

                elif la_ == 5:
                    self.state = 58
                    self.declarationList(0)
                    pass

                elif la_ == 6:
                    self.state = 59
                    self.definitionList()
                    pass


                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 65
            self.match(CParser.EOF)
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
        self.enterRule(localctx, 2, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.identifier()
            self.state = 68
            self.match(CParser.ASSIGN)
            self.state = 69
            self.expression(0)
            self.state = 70
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
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 73
                self.constant()
                pass

            elif la_ == 2:
                self.state = 74
                self.functionCallExpression()
                pass

            elif la_ == 3:
                self.state = 75
                self.identifier()
                pass

            elif la_ == 4:
                self.state = 76
                self.match(CParser.SIZEOF)
                self.state = 82
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 2, 3, 4, 22, 86]:
                    self.state = 77
                    self.expression(0)
                    pass
                elif token in [47]:
                    self.state = 78
                    self.match(CParser.LP)
                    self.state = 79
                    self.expression(0)
                    self.state = 80
                    self.match(CParser.RP)
                    pass
                else:
                    raise NoViableAltException(self)

                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 100
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 98
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = CParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 86
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 87
                        self.match(CParser.STAR)
                        self.state = 88
                        self.expression(5)
                        pass

                    elif la_ == 2:
                        localctx = CParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 89
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 90
                        self.match(CParser.DIV)
                        self.state = 91
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
                        self.match(CParser.PLUS)
                        self.state = 94
                        self.expression(3)
                        pass

                    elif la_ == 4:
                        localctx = CParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 95
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 96
                        self.match(CParser.MINUS)
                        self.state = 97
                        self.expression(2)
                        pass

             
                self.state = 102
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

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
        self.enterRule(localctx, 6, self.RULE_multiplyExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.expression(0)
            self.state = 104
            self.match(CParser.STAR)
            self.state = 105
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
        self.enterRule(localctx, 8, self.RULE_divideExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.expression(0)
            self.state = 108
            self.match(CParser.DIV)
            self.state = 109
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
        self.enterRule(localctx, 10, self.RULE_addExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.expression(0)
            self.state = 112
            self.match(CParser.PLUS)
            self.state = 113
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
        self.enterRule(localctx, 12, self.RULE_subtractExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.expression(0)
            self.state = 116
            self.match(CParser.MINUS)
            self.state = 117
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
        self.enterRule(localctx, 14, self.RULE_constant)
        try:
            self.state = 127
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.match(CParser.INTEGER_CONSTANT)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 120
                self.match(CParser.FLOAT_CONSTANT)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 121
                self.match(CParser.CHAR_CONSTANT)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 4)
                self.state = 123 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 122
                        self.match(CParser.STRING_LITERAL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 125 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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
        self.enterRule(localctx, 16, self.RULE_functionCallExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.identifier()
            self.state = 130
            self.match(CParser.LP)
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 4194334) != 0 or _la==86:
                self.state = 131
                self.functionCallArgs(0)


            self.state = 134
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
        self.enterRule(localctx, 18, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.identifier()
            self.state = 137
            self.match(CParser.LP)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 4194334) != 0 or _la==86:
                self.state = 138
                self.functionCallArgs(0)


            self.state = 141
            self.match(CParser.RP)
            self.state = 142
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
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_functionCallArgs, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.expression(0)
            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 146
                self.match(CParser.COMMA)


            self._ctx.stop = self._input.LT(-1)
            self.state = 154
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CParser.FunctionCallArgsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_functionCallArgs)
                    self.state = 149
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 150
                    self.match(CParser.COMMA)
                    self.state = 151
                    self.functionCallArgs(2) 
                self.state = 156
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
        self.enterRule(localctx, 22, self.RULE_statementList)
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
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_declarationList, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.declaration()
            self._ctx.stop = self._input.LT(-1)
            self.state = 166
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CParser.DeclarationListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_declarationList)
                    self.state = 162
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 163
                    self.declaration() 
                self.state = 168
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
        self.enterRule(localctx, 26, self.RULE_declaration)
        try:
            self.state = 173
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.functionDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
                self.variableDeclaration()
                self.state = 171
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
        self.enterRule(localctx, 28, self.RULE_variableDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.typeSpecifier()
            self.state = 176
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
        self.enterRule(localctx, 30, self.RULE_variableInitialization)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.typeSpecifier()
            self.state = 179
            self.identifier()
            self.state = 180
            self.match(CParser.ASSIGN)
            self.state = 181
            self.expression(0)
            self.state = 182
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
        self.enterRule(localctx, 32, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 184
                self.typeSpecifier()


            self.state = 187
            self.functionName()
            self.state = 188
            self.match(CParser.LP)
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la - 30)) & ~0x3f) == 0 and ((1 << (_la - 30)) & 72057594037928959) != 0:
                self.state = 189
                self.functionArgs(0)


            self.state = 192
            self.match(CParser.RP)
            self.state = 193
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
        self.enterRule(localctx, 34, self.RULE_definitionList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
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

        def block(self):
            return self.getTypedRuleContext(CParser.BlockContext,0)


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
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 197
                self.typeSpecifier()


            self.state = 200
            self.functionName()
            self.state = 201
            self.match(CParser.LP)
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la - 30)) & ~0x3f) == 0 and ((1 << (_la - 30)) & 72057594037928959) != 0:
                self.state = 202
                self.functionArgs(0)


            self.state = 205
            self.match(CParser.RP)
            self.state = 206
            self.block()
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
        self.enterRule(localctx, 38, self.RULE_functionReturn)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(CParser.RETURN)
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 4194334) != 0 or _la==86:
                self.state = 209
                self.expression(0)


            self.state = 212
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
        self.enterRule(localctx, 40, self.RULE_functionName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
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
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_functionArgs, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.typeSpecifier()
            self.state = 219
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 218
                self.identifier()


            self.state = 222
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 221
                self.match(CParser.COMMA)


            self._ctx.stop = self._input.LT(-1)
            self.state = 229
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CParser.FunctionArgsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_functionArgs)
                    self.state = 224
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 225
                    self.match(CParser.COMMA)
                    self.state = 226
                    self.functionArgs(2) 
                self.state = 231
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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
        self.enterRule(localctx, 44, self.RULE_typeSpecifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 232
                self.match(CParser.CONST)


            self.state = 255
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                self.state = 235
                self.match(CParser.VOID)
                pass
            elif token in [31, 32, 34, 35, 36, 37, 38, 39]:
                self.state = 237
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31 or _la==32:
                    self.state = 236
                    _la = self._input.LA(1)
                    if not(_la==31 or _la==32):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 252
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                if la_ == 1:
                    self.state = 239
                    self.match(CParser.CHAR)
                    pass

                elif la_ == 2:
                    self.state = 240
                    self.match(CParser.SHORT)
                    pass

                elif la_ == 3:
                    self.state = 242
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==35:
                        self.state = 241
                        self.match(CParser.SHORT)


                    self.state = 244
                    self.match(CParser.INT)
                    pass

                elif la_ == 4:
                    self.state = 245
                    self.match(CParser.LONG)
                    pass

                elif la_ == 5:
                    self.state = 246
                    self.match(CParser.FLOAT)
                    pass

                elif la_ == 6:
                    self.state = 248
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==37:
                        self.state = 247
                        self.match(CParser.LONG)


                    self.state = 250
                    self.match(CParser.DOUBLE)
                    pass

                elif la_ == 7:
                    self.state = 251
                    self.match(CParser.INT)
                    pass


                pass
            elif token in [86]:
                self.state = 254
                self.identifier()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 260
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 257
                    self.match(CParser.STAR) 
                self.state = 262
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(CParser.IF, 0)

        def LP(self):
            return self.getToken(CParser.LP, 0)

        def RP(self):
            return self.getToken(CParser.RP, 0)

        def block(self):
            return self.getTypedRuleContext(CParser.BlockContext,0)


        def condition(self):
            return self.getTypedRuleContext(CParser.ConditionContext,0)


        def getRuleIndex(self):
            return CParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)




    def ifStatement(self):

        localctx = CParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.match(CParser.IF)
            self.state = 264
            self.match(CParser.LP)
            self.state = 266
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 4194334) != 0 or _la==86:
                self.state = 265
                self.condition()


            self.state = 268
            self.match(CParser.RP)
            self.state = 269
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CParser.ExpressionContext,i)


        def COMMA(self):
            return self.getToken(CParser.COMMA, 0)

        def getRuleIndex(self):
            return CParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = CParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.state = 279
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 271
                self.expression(0)
                self.state = 273
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==69:
                    self.state = 272
                    self.match(CParser.COMMA)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 275
                self.expression(0)
                self.state = 276
                self.match(CParser.COMMA)
                self.state = 277
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
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


        def ifStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.IfStatementContext)
            else:
                return self.getTypedRuleContext(CParser.IfStatementContext,i)


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
            return CParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = CParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(CParser.LC)
            self.state = 294
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 1098444308510) != 0 or _la==86:
                self.state = 292
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                if la_ == 1:
                    self.state = 282
                    self.expression(0)
                    pass

                elif la_ == 2:
                    self.state = 283
                    self.ifStatement()
                    pass

                elif la_ == 3:
                    self.state = 284
                    self.variableInitialization()
                    pass

                elif la_ == 4:
                    self.state = 285
                    self.variableDeclaration()
                    pass

                elif la_ == 5:
                    self.state = 286
                    self.definitionList()
                    pass

                elif la_ == 6:
                    self.state = 287
                    self.declarationList(0)
                    pass

                elif la_ == 7:
                    self.state = 288
                    self.functionCall()
                    pass

                elif la_ == 8:
                    self.state = 289
                    self.assignment()
                    pass

                elif la_ == 9:
                    self.state = 290
                    self.assignment()
                    pass

                elif la_ == 10:
                    self.state = 291
                    self.functionReturn()
                    pass


                self.state = 296
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 297
            self.match(CParser.RC)
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
        self.enterRule(localctx, 52, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
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
        self._predicates[2] = self.expression_sempred
        self._predicates[10] = self.functionCallArgs_sempred
        self._predicates[12] = self.declarationList_sempred
        self._predicates[21] = self.functionArgs_sempred
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
         




