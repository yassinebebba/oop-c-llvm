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
        4,1,90,322,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,1,0,1,0,1,0,1,0,1,0,1,0,5,0,63,8,0,10,0,12,0,66,9,0,1,
        0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,80,8,1,3,1,82,
        8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,96,8,1,10,
        1,12,1,99,9,1,1,2,1,2,1,2,1,2,4,2,105,8,2,11,2,12,2,106,3,2,109,
        8,2,1,3,1,3,1,3,3,3,114,8,3,1,3,1,3,1,4,1,4,1,4,3,4,121,8,4,1,4,
        1,4,1,4,1,5,1,5,1,5,3,5,129,8,5,1,5,1,5,1,5,5,5,134,8,5,10,5,12,
        5,137,9,5,1,6,1,6,1,7,1,7,1,7,1,7,1,7,5,7,146,8,7,10,7,12,7,149,
        9,7,1,8,1,8,1,8,1,8,3,8,155,8,8,1,9,1,9,1,9,1,10,1,10,1,10,1,10,
        1,10,1,10,1,11,3,11,167,8,11,1,11,1,11,1,11,3,11,172,8,11,1,11,1,
        11,1,11,1,12,1,12,1,13,3,13,180,8,13,1,13,1,13,1,13,3,13,185,8,13,
        1,13,1,13,1,13,1,14,1,14,3,14,192,8,14,1,14,1,14,1,15,1,15,1,16,
        1,16,1,16,3,16,201,8,16,1,16,3,16,204,8,16,1,16,1,16,1,16,5,16,209,
        8,16,10,16,12,16,212,9,16,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,
        1,18,1,18,1,19,3,19,225,8,19,1,19,1,19,3,19,229,8,19,1,19,1,19,1,
        19,3,19,234,8,19,1,19,1,19,1,19,1,19,3,19,240,8,19,1,19,1,19,3,19,
        244,8,19,1,19,3,19,247,8,19,1,19,5,19,250,8,19,10,19,12,19,253,9,
        19,1,20,1,20,5,20,257,8,20,10,20,12,20,260,9,20,1,20,3,20,263,8,
        20,1,21,1,21,1,21,4,21,268,8,21,11,21,12,21,269,1,21,1,21,1,21,1,
        22,1,22,1,22,1,23,1,23,1,23,1,24,1,24,1,24,4,24,284,8,24,11,24,12,
        24,285,1,24,1,24,1,24,1,25,1,25,3,25,293,8,25,1,25,1,25,1,25,1,25,
        3,25,299,8,25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,
        1,26,1,26,5,26,313,8,26,10,26,12,26,316,9,26,1,26,1,26,1,27,1,27,
        1,27,0,4,2,10,14,32,28,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,
        32,34,36,38,40,42,44,46,48,50,52,54,0,2,1,0,71,80,1,0,31,32,355,
        0,64,1,0,0,0,2,81,1,0,0,0,4,108,1,0,0,0,6,110,1,0,0,0,8,117,1,0,
        0,0,10,125,1,0,0,0,12,138,1,0,0,0,14,140,1,0,0,0,16,154,1,0,0,0,
        18,156,1,0,0,0,20,159,1,0,0,0,22,166,1,0,0,0,24,176,1,0,0,0,26,179,
        1,0,0,0,28,189,1,0,0,0,30,195,1,0,0,0,32,197,1,0,0,0,34,213,1,0,
        0,0,36,218,1,0,0,0,38,224,1,0,0,0,40,254,1,0,0,0,42,264,1,0,0,0,
        44,274,1,0,0,0,46,277,1,0,0,0,48,280,1,0,0,0,50,298,1,0,0,0,52,300,
        1,0,0,0,54,319,1,0,0,0,56,63,3,34,17,0,57,63,3,20,10,0,58,63,3,18,
        9,0,59,63,3,8,4,0,60,63,3,14,7,0,61,63,3,24,12,0,62,56,1,0,0,0,62,
        57,1,0,0,0,62,58,1,0,0,0,62,59,1,0,0,0,62,60,1,0,0,0,62,61,1,0,0,
        0,63,66,1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,65,67,1,0,0,0,66,64,
        1,0,0,0,67,68,5,0,0,1,68,1,1,0,0,0,69,70,6,1,-1,0,70,82,3,4,2,0,
        71,82,3,6,3,0,72,82,3,54,27,0,73,79,5,22,0,0,74,80,3,2,1,0,75,76,
        5,47,0,0,76,77,3,2,1,0,77,78,5,48,0,0,78,80,1,0,0,0,79,74,1,0,0,
        0,79,75,1,0,0,0,80,82,1,0,0,0,81,69,1,0,0,0,81,71,1,0,0,0,81,72,
        1,0,0,0,81,73,1,0,0,0,82,97,1,0,0,0,83,84,10,4,0,0,84,85,5,44,0,
        0,85,96,3,2,1,5,86,87,10,3,0,0,87,88,5,45,0,0,88,96,3,2,1,4,89,90,
        10,2,0,0,90,91,5,40,0,0,91,96,3,2,1,3,92,93,10,1,0,0,93,94,5,42,
        0,0,94,96,3,2,1,2,95,83,1,0,0,0,95,86,1,0,0,0,95,89,1,0,0,0,95,92,
        1,0,0,0,96,99,1,0,0,0,97,95,1,0,0,0,97,98,1,0,0,0,98,3,1,0,0,0,99,
        97,1,0,0,0,100,109,5,3,0,0,101,109,5,4,0,0,102,109,5,2,0,0,103,105,
        5,1,0,0,104,103,1,0,0,0,105,106,1,0,0,0,106,104,1,0,0,0,106,107,
        1,0,0,0,107,109,1,0,0,0,108,100,1,0,0,0,108,101,1,0,0,0,108,102,
        1,0,0,0,108,104,1,0,0,0,109,5,1,0,0,0,110,111,3,54,27,0,111,113,
        5,47,0,0,112,114,3,10,5,0,113,112,1,0,0,0,113,114,1,0,0,0,114,115,
        1,0,0,0,115,116,5,48,0,0,116,7,1,0,0,0,117,118,3,54,27,0,118,120,
        5,47,0,0,119,121,3,10,5,0,120,119,1,0,0,0,120,121,1,0,0,0,121,122,
        1,0,0,0,122,123,5,48,0,0,123,124,5,68,0,0,124,9,1,0,0,0,125,126,
        6,5,-1,0,126,128,3,2,1,0,127,129,5,69,0,0,128,127,1,0,0,0,128,129,
        1,0,0,0,129,135,1,0,0,0,130,131,10,1,0,0,131,132,5,69,0,0,132,134,
        3,10,5,2,133,130,1,0,0,0,134,137,1,0,0,0,135,133,1,0,0,0,135,136,
        1,0,0,0,136,11,1,0,0,0,137,135,1,0,0,0,138,139,1,0,0,0,139,13,1,
        0,0,0,140,141,6,7,-1,0,141,142,3,16,8,0,142,147,1,0,0,0,143,144,
        10,1,0,0,144,146,3,16,8,0,145,143,1,0,0,0,146,149,1,0,0,0,147,145,
        1,0,0,0,147,148,1,0,0,0,148,15,1,0,0,0,149,147,1,0,0,0,150,155,3,
        22,11,0,151,152,3,18,9,0,152,153,5,68,0,0,153,155,1,0,0,0,154,150,
        1,0,0,0,154,151,1,0,0,0,155,17,1,0,0,0,156,157,3,38,19,0,157,158,
        3,54,27,0,158,19,1,0,0,0,159,160,3,38,19,0,160,161,3,54,27,0,161,
        162,5,70,0,0,162,163,3,2,1,0,163,164,5,68,0,0,164,21,1,0,0,0,165,
        167,3,38,19,0,166,165,1,0,0,0,166,167,1,0,0,0,167,168,1,0,0,0,168,
        169,3,30,15,0,169,171,5,47,0,0,170,172,3,32,16,0,171,170,1,0,0,0,
        171,172,1,0,0,0,172,173,1,0,0,0,173,174,5,48,0,0,174,175,5,68,0,
        0,175,23,1,0,0,0,176,177,3,26,13,0,177,25,1,0,0,0,178,180,3,38,19,
        0,179,178,1,0,0,0,179,180,1,0,0,0,180,181,1,0,0,0,181,182,3,30,15,
        0,182,184,5,47,0,0,183,185,3,32,16,0,184,183,1,0,0,0,184,185,1,0,
        0,0,185,186,1,0,0,0,186,187,5,48,0,0,187,188,3,52,26,0,188,27,1,
        0,0,0,189,191,5,21,0,0,190,192,3,2,1,0,191,190,1,0,0,0,191,192,1,
        0,0,0,192,193,1,0,0,0,193,194,5,68,0,0,194,29,1,0,0,0,195,196,3,
        54,27,0,196,31,1,0,0,0,197,198,6,16,-1,0,198,200,3,38,19,0,199,201,
        3,54,27,0,200,199,1,0,0,0,200,201,1,0,0,0,201,203,1,0,0,0,202,204,
        5,69,0,0,203,202,1,0,0,0,203,204,1,0,0,0,204,210,1,0,0,0,205,206,
        10,1,0,0,206,207,5,69,0,0,207,209,3,32,16,2,208,205,1,0,0,0,209,
        212,1,0,0,0,210,208,1,0,0,0,210,211,1,0,0,0,211,33,1,0,0,0,212,210,
        1,0,0,0,213,214,3,54,27,0,214,215,5,70,0,0,215,216,3,2,1,0,216,217,
        5,68,0,0,217,35,1,0,0,0,218,219,3,54,27,0,219,220,7,0,0,0,220,221,
        3,2,1,0,221,222,5,68,0,0,222,37,1,0,0,0,223,225,5,30,0,0,224,223,
        1,0,0,0,224,225,1,0,0,0,225,246,1,0,0,0,226,247,5,33,0,0,227,229,
        7,1,0,0,228,227,1,0,0,0,228,229,1,0,0,0,229,243,1,0,0,0,230,244,
        5,34,0,0,231,244,5,35,0,0,232,234,5,35,0,0,233,232,1,0,0,0,233,234,
        1,0,0,0,234,235,1,0,0,0,235,244,5,36,0,0,236,244,5,37,0,0,237,244,
        5,38,0,0,238,240,5,37,0,0,239,238,1,0,0,0,239,240,1,0,0,0,240,241,
        1,0,0,0,241,244,5,39,0,0,242,244,5,36,0,0,243,230,1,0,0,0,243,231,
        1,0,0,0,243,233,1,0,0,0,243,236,1,0,0,0,243,237,1,0,0,0,243,239,
        1,0,0,0,243,242,1,0,0,0,244,247,1,0,0,0,245,247,3,54,27,0,246,226,
        1,0,0,0,246,228,1,0,0,0,246,245,1,0,0,0,247,251,1,0,0,0,248,250,
        5,44,0,0,249,248,1,0,0,0,250,253,1,0,0,0,251,249,1,0,0,0,251,252,
        1,0,0,0,252,39,1,0,0,0,253,251,1,0,0,0,254,258,3,42,21,0,255,257,
        3,44,22,0,256,255,1,0,0,0,257,260,1,0,0,0,258,256,1,0,0,0,258,259,
        1,0,0,0,259,262,1,0,0,0,260,258,1,0,0,0,261,263,3,46,23,0,262,261,
        1,0,0,0,262,263,1,0,0,0,263,41,1,0,0,0,264,265,5,17,0,0,265,267,
        5,47,0,0,266,268,3,50,25,0,267,266,1,0,0,0,268,269,1,0,0,0,269,267,
        1,0,0,0,269,270,1,0,0,0,270,271,1,0,0,0,271,272,5,48,0,0,272,273,
        3,52,26,0,273,43,1,0,0,0,274,275,5,12,0,0,275,276,3,42,21,0,276,
        45,1,0,0,0,277,278,5,12,0,0,278,279,3,52,26,0,279,47,1,0,0,0,280,
        281,5,29,0,0,281,283,5,47,0,0,282,284,3,50,25,0,283,282,1,0,0,0,
        284,285,1,0,0,0,285,283,1,0,0,0,285,286,1,0,0,0,286,287,1,0,0,0,
        287,288,5,48,0,0,288,289,3,52,26,0,289,49,1,0,0,0,290,292,3,2,1,
        0,291,293,5,69,0,0,292,291,1,0,0,0,292,293,1,0,0,0,293,299,1,0,0,
        0,294,295,3,2,1,0,295,296,5,69,0,0,296,297,3,2,1,0,297,299,1,0,0,
        0,298,290,1,0,0,0,298,294,1,0,0,0,299,51,1,0,0,0,300,314,5,49,0,
        0,301,313,3,2,1,0,302,313,3,40,20,0,303,313,3,48,24,0,304,313,3,
        20,10,0,305,313,3,18,9,0,306,313,3,24,12,0,307,313,3,14,7,0,308,
        313,3,8,4,0,309,313,3,34,17,0,310,313,3,36,18,0,311,313,3,28,14,
        0,312,301,1,0,0,0,312,302,1,0,0,0,312,303,1,0,0,0,312,304,1,0,0,
        0,312,305,1,0,0,0,312,306,1,0,0,0,312,307,1,0,0,0,312,308,1,0,0,
        0,312,309,1,0,0,0,312,310,1,0,0,0,312,311,1,0,0,0,313,316,1,0,0,
        0,314,312,1,0,0,0,314,315,1,0,0,0,315,317,1,0,0,0,316,314,1,0,0,
        0,317,318,5,50,0,0,318,53,1,0,0,0,319,320,5,86,0,0,320,55,1,0,0,
        0,37,62,64,79,81,95,97,106,108,113,120,128,135,147,154,166,171,179,
        184,191,200,203,210,224,228,233,239,243,246,251,258,262,269,285,
        292,298,312,314
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
    RULE_expression = 1
    RULE_constant = 2
    RULE_functionCallExpression = 3
    RULE_functionCall = 4
    RULE_functionCallArgs = 5
    RULE_statementList = 6
    RULE_declarationList = 7
    RULE_declaration = 8
    RULE_variableDeclaration = 9
    RULE_variableInitialization = 10
    RULE_functionDeclaration = 11
    RULE_definitionList = 12
    RULE_functionDefinition = 13
    RULE_functionReturn = 14
    RULE_functionName = 15
    RULE_functionArgs = 16
    RULE_assignment = 17
    RULE_inplaceAssignment = 18
    RULE_typeSpecifier = 19
    RULE_ifStatementStructure = 20
    RULE_ifStatement = 21
    RULE_elseIfStatement = 22
    RULE_elseStatement = 23
    RULE_whileStatement = 24
    RULE_condition = 25
    RULE_block = 26
    RULE_identifier = 27

    ruleNames =  [ "compilationUnit", "expression", "constant", "functionCallExpression", 
                   "functionCall", "functionCallArgs", "statementList", 
                   "declarationList", "declaration", "variableDeclaration", 
                   "variableInitialization", "functionDeclaration", "definitionList", 
                   "functionDefinition", "functionReturn", "functionName", 
                   "functionArgs", "assignment", "inplaceAssignment", "typeSpecifier", 
                   "ifStatementStructure", "ifStatement", "elseIfStatement", 
                   "elseStatement", "whileStatement", "condition", "block", 
                   "identifier" ]

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
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la - 30)) & ~0x3f) == 0 and ((1 << (_la - 30)) & 72057594037928959) != 0:
                self.state = 62
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 56
                    self.assignment()
                    pass

                elif la_ == 2:
                    self.state = 57
                    self.variableInitialization()
                    pass

                elif la_ == 3:
                    self.state = 58
                    self.variableDeclaration()
                    pass

                elif la_ == 4:
                    self.state = 59
                    self.functionCall()
                    pass

                elif la_ == 5:
                    self.state = 60
                    self.declarationList(0)
                    pass

                elif la_ == 6:
                    self.state = 61
                    self.definitionList()
                    pass


                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 67
            self.match(CParser.EOF)
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


        def getRuleIndex(self):
            return CParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ConstantExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def constant(self):
            return self.getTypedRuleContext(CParser.ConstantContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstantExpression" ):
                listener.enterConstantExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstantExpression" ):
                listener.exitConstantExpression(self)


    class AddExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CParser.ExpressionContext,i)

        def PLUS(self):
            return self.getToken(CParser.PLUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddExpression" ):
                listener.enterAddExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddExpression" ):
                listener.exitAddExpression(self)


    class SubtractExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CParser.ExpressionContext,i)

        def MINUS(self):
            return self.getToken(CParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubtractExpression" ):
                listener.enterSubtractExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubtractExpression" ):
                listener.exitSubtractExpression(self)


    class IdentiferExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(CParser.IdentifierContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentiferExpression" ):
                listener.enterIdentiferExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentiferExpression" ):
                listener.exitIdentiferExpression(self)


    class MultiplyExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CParser.ExpressionContext,i)

        def STAR(self):
            return self.getToken(CParser.STAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplyExpression" ):
                listener.enterMultiplyExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplyExpression" ):
                listener.exitMultiplyExpression(self)


    class SizeofExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SIZEOF(self):
            return self.getToken(CParser.SIZEOF, 0)
        def expression(self):
            return self.getTypedRuleContext(CParser.ExpressionContext,0)

        def LP(self):
            return self.getToken(CParser.LP, 0)
        def RP(self):
            return self.getToken(CParser.RP, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSizeofExpression" ):
                listener.enterSizeofExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSizeofExpression" ):
                listener.exitSizeofExpression(self)


    class FuncCallExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def functionCallExpression(self):
            return self.getTypedRuleContext(CParser.FunctionCallExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncCallExpression" ):
                listener.enterFuncCallExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncCallExpression" ):
                listener.exitFuncCallExpression(self)


    class DivideExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CParser.ExpressionContext,i)

        def DIV(self):
            return self.getToken(CParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivideExpression" ):
                listener.enterDivideExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivideExpression" ):
                listener.exitDivideExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = CParser.ConstantExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 70
                self.constant()
                pass

            elif la_ == 2:
                localctx = CParser.FuncCallExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 71
                self.functionCallExpression()
                pass

            elif la_ == 3:
                localctx = CParser.IdentiferExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 72
                self.identifier()
                pass

            elif la_ == 4:
                localctx = CParser.SizeofExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 73
                self.match(CParser.SIZEOF)
                self.state = 79
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 2, 3, 4, 22, 86]:
                    self.state = 74
                    self.expression(0)
                    pass
                elif token in [47]:
                    self.state = 75
                    self.match(CParser.LP)
                    self.state = 76
                    self.expression(0)
                    self.state = 77
                    self.match(CParser.RP)
                    pass
                else:
                    raise NoViableAltException(self)

                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 97
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 95
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = CParser.MultiplyExpressionContext(self, CParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 83
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 84
                        self.match(CParser.STAR)
                        self.state = 85
                        self.expression(5)
                        pass

                    elif la_ == 2:
                        localctx = CParser.DivideExpressionContext(self, CParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 86
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 87
                        self.match(CParser.DIV)
                        self.state = 88
                        self.expression(4)
                        pass

                    elif la_ == 3:
                        localctx = CParser.AddExpressionContext(self, CParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 89
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 90
                        self.match(CParser.PLUS)
                        self.state = 91
                        self.expression(3)
                        pass

                    elif la_ == 4:
                        localctx = CParser.SubtractExpressionContext(self, CParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 92
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 93
                        self.match(CParser.MINUS)
                        self.state = 94
                        self.expression(2)
                        pass

             
                self.state = 99
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 4, self.RULE_constant)
        try:
            self.state = 108
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 100
                self.match(CParser.INTEGER_CONSTANT)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 101
                self.match(CParser.FLOAT_CONSTANT)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 102
                self.match(CParser.CHAR_CONSTANT)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 4)
                self.state = 104 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 103
                        self.match(CParser.STRING_LITERAL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 106 
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
        self.enterRule(localctx, 6, self.RULE_functionCallExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.identifier()
            self.state = 111
            self.match(CParser.LP)
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 4194334) != 0 or _la==86:
                self.state = 112
                self.functionCallArgs(0)


            self.state = 115
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
        self.enterRule(localctx, 8, self.RULE_functionCall)
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
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 4194334) != 0 or _la==86:
                self.state = 119
                self.functionCallArgs(0)


            self.state = 122
            self.match(CParser.RP)
            self.state = 123
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
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_functionCallArgs, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.expression(0)
            self.state = 128
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 127
                self.match(CParser.COMMA)


            self._ctx.stop = self._input.LT(-1)
            self.state = 135
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CParser.FunctionCallArgsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_functionCallArgs)
                    self.state = 130
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 131
                    self.match(CParser.COMMA)
                    self.state = 132
                    self.functionCallArgs(2) 
                self.state = 137
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
        self.enterRule(localctx, 12, self.RULE_statementList)
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
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_declarationList, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.declaration()
            self._ctx.stop = self._input.LT(-1)
            self.state = 147
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CParser.DeclarationListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_declarationList)
                    self.state = 143
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 144
                    self.declaration() 
                self.state = 149
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
        self.enterRule(localctx, 16, self.RULE_declaration)
        try:
            self.state = 154
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.functionDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 151
                self.variableDeclaration()
                self.state = 152
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
        self.enterRule(localctx, 18, self.RULE_variableDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.typeSpecifier()
            self.state = 157
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
        self.enterRule(localctx, 20, self.RULE_variableInitialization)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.typeSpecifier()
            self.state = 160
            self.identifier()
            self.state = 161
            self.match(CParser.ASSIGN)
            self.state = 162
            self.expression(0)
            self.state = 163
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
        self.enterRule(localctx, 22, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 165
                self.typeSpecifier()


            self.state = 168
            self.functionName()
            self.state = 169
            self.match(CParser.LP)
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la - 30)) & ~0x3f) == 0 and ((1 << (_la - 30)) & 72057594037928959) != 0:
                self.state = 170
                self.functionArgs(0)


            self.state = 173
            self.match(CParser.RP)
            self.state = 174
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
        self.enterRule(localctx, 24, self.RULE_definitionList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
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
        self.enterRule(localctx, 26, self.RULE_functionDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 178
                self.typeSpecifier()


            self.state = 181
            self.functionName()
            self.state = 182
            self.match(CParser.LP)
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la - 30)) & ~0x3f) == 0 and ((1 << (_la - 30)) & 72057594037928959) != 0:
                self.state = 183
                self.functionArgs(0)


            self.state = 186
            self.match(CParser.RP)
            self.state = 187
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
        self.enterRule(localctx, 28, self.RULE_functionReturn)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(CParser.RETURN)
            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 4194334) != 0 or _la==86:
                self.state = 190
                self.expression(0)


            self.state = 193
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
        self.enterRule(localctx, 30, self.RULE_functionName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
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
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_functionArgs, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.typeSpecifier()
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 199
                self.identifier()


            self.state = 203
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 202
                self.match(CParser.COMMA)


            self._ctx.stop = self._input.LT(-1)
            self.state = 210
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CParser.FunctionArgsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_functionArgs)
                    self.state = 205
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 206
                    self.match(CParser.COMMA)
                    self.state = 207
                    self.functionArgs(2) 
                self.state = 212
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 34, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.identifier()
            self.state = 214
            self.match(CParser.ASSIGN)
            self.state = 215
            self.expression(0)
            self.state = 216
            self.match(CParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InplaceAssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(CParser.IdentifierContext,0)


        def expression(self):
            return self.getTypedRuleContext(CParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(CParser.SEMI, 0)

        def STAR_ASSIGN(self):
            return self.getToken(CParser.STAR_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(CParser.DIV_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(CParser.MOD_ASSIGN, 0)

        def PLUS_ASSIGN(self):
            return self.getToken(CParser.PLUS_ASSIGN, 0)

        def MINUS_ASSIGN(self):
            return self.getToken(CParser.MINUS_ASSIGN, 0)

        def LEFT_SHIFT_ASSIGN(self):
            return self.getToken(CParser.LEFT_SHIFT_ASSIGN, 0)

        def RIGHT_SHIFT_ASSIGN(self):
            return self.getToken(CParser.RIGHT_SHIFT_ASSIGN, 0)

        def BITWISE_AND_ASSIGN(self):
            return self.getToken(CParser.BITWISE_AND_ASSIGN, 0)

        def BITWISE_XOR_ASSIGN(self):
            return self.getToken(CParser.BITWISE_XOR_ASSIGN, 0)

        def BITWISE_OR_ASSIGN(self):
            return self.getToken(CParser.BITWISE_OR_ASSIGN, 0)

        def getRuleIndex(self):
            return CParser.RULE_inplaceAssignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInplaceAssignment" ):
                listener.enterInplaceAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInplaceAssignment" ):
                listener.exitInplaceAssignment(self)




    def inplaceAssignment(self):

        localctx = CParser.InplaceAssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_inplaceAssignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.identifier()
            self.state = 219
            _la = self._input.LA(1)
            if not((((_la - 71)) & ~0x3f) == 0 and ((1 << (_la - 71)) & 1023) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 220
            self.expression(0)
            self.state = 221
            self.match(CParser.SEMI)
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
        self.enterRule(localctx, 38, self.RULE_typeSpecifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 223
                self.match(CParser.CONST)


            self.state = 246
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                self.state = 226
                self.match(CParser.VOID)
                pass
            elif token in [31, 32, 34, 35, 36, 37, 38, 39]:
                self.state = 228
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31 or _la==32:
                    self.state = 227
                    _la = self._input.LA(1)
                    if not(_la==31 or _la==32):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 243
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                if la_ == 1:
                    self.state = 230
                    self.match(CParser.CHAR)
                    pass

                elif la_ == 2:
                    self.state = 231
                    self.match(CParser.SHORT)
                    pass

                elif la_ == 3:
                    self.state = 233
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==35:
                        self.state = 232
                        self.match(CParser.SHORT)


                    self.state = 235
                    self.match(CParser.INT)
                    pass

                elif la_ == 4:
                    self.state = 236
                    self.match(CParser.LONG)
                    pass

                elif la_ == 5:
                    self.state = 237
                    self.match(CParser.FLOAT)
                    pass

                elif la_ == 6:
                    self.state = 239
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==37:
                        self.state = 238
                        self.match(CParser.LONG)


                    self.state = 241
                    self.match(CParser.DOUBLE)
                    pass

                elif la_ == 7:
                    self.state = 242
                    self.match(CParser.INT)
                    pass


                pass
            elif token in [86]:
                self.state = 245
                self.identifier()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 251
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 248
                    self.match(CParser.STAR) 
                self.state = 253
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementStructureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifStatement(self):
            return self.getTypedRuleContext(CParser.IfStatementContext,0)


        def elseIfStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.ElseIfStatementContext)
            else:
                return self.getTypedRuleContext(CParser.ElseIfStatementContext,i)


        def elseStatement(self):
            return self.getTypedRuleContext(CParser.ElseStatementContext,0)


        def getRuleIndex(self):
            return CParser.RULE_ifStatementStructure

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatementStructure" ):
                listener.enterIfStatementStructure(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatementStructure" ):
                listener.exitIfStatementStructure(self)




    def ifStatementStructure(self):

        localctx = CParser.IfStatementStructureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_ifStatementStructure)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.ifStatement()
            self.state = 258
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 255
                    self.elseIfStatement() 
                self.state = 260
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

            self.state = 262
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 261
                self.elseStatement()


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


        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.ConditionContext)
            else:
                return self.getTypedRuleContext(CParser.ConditionContext,i)


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
        self.enterRule(localctx, 42, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.match(CParser.IF)
            self.state = 265
            self.match(CParser.LP)
            self.state = 267 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 266
                self.condition()
                self.state = 269 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 4194334) != 0 or _la==86):
                    break

            self.state = 271
            self.match(CParser.RP)
            self.state = 272
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseIfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(CParser.ELSE, 0)

        def ifStatement(self):
            return self.getTypedRuleContext(CParser.IfStatementContext,0)


        def getRuleIndex(self):
            return CParser.RULE_elseIfStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseIfStatement" ):
                listener.enterElseIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseIfStatement" ):
                listener.exitElseIfStatement(self)




    def elseIfStatement(self):

        localctx = CParser.ElseIfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_elseIfStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(CParser.ELSE)
            self.state = 275
            self.ifStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(CParser.ELSE, 0)

        def block(self):
            return self.getTypedRuleContext(CParser.BlockContext,0)


        def getRuleIndex(self):
            return CParser.RULE_elseStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseStatement" ):
                listener.enterElseStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseStatement" ):
                listener.exitElseStatement(self)




    def elseStatement(self):

        localctx = CParser.ElseStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_elseStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.match(CParser.ELSE)
            self.state = 278
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(CParser.WHILE, 0)

        def LP(self):
            return self.getToken(CParser.LP, 0)

        def RP(self):
            return self.getToken(CParser.RP, 0)

        def block(self):
            return self.getTypedRuleContext(CParser.BlockContext,0)


        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.ConditionContext)
            else:
                return self.getTypedRuleContext(CParser.ConditionContext,i)


        def getRuleIndex(self):
            return CParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)




    def whileStatement(self):

        localctx = CParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_whileStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.match(CParser.WHILE)
            self.state = 281
            self.match(CParser.LP)
            self.state = 283 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 282
                self.condition()
                self.state = 285 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 4194334) != 0 or _la==86):
                    break

            self.state = 287
            self.match(CParser.RP)
            self.state = 288
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
        self.enterRule(localctx, 50, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.state = 298
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 290
                self.expression(0)
                self.state = 292
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==69:
                    self.state = 291
                    self.match(CParser.COMMA)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 294
                self.expression(0)
                self.state = 295
                self.match(CParser.COMMA)
                self.state = 296
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


        def ifStatementStructure(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.IfStatementStructureContext)
            else:
                return self.getTypedRuleContext(CParser.IfStatementStructureContext,i)


        def whileStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.WhileStatementContext)
            else:
                return self.getTypedRuleContext(CParser.WhileStatementContext,i)


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


        def inplaceAssignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.InplaceAssignmentContext)
            else:
                return self.getTypedRuleContext(CParser.InplaceAssignmentContext,i)


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
        self.enterRule(localctx, 52, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(CParser.LC)
            self.state = 314
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 1098981179422) != 0 or _la==86:
                self.state = 312
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
                if la_ == 1:
                    self.state = 301
                    self.expression(0)
                    pass

                elif la_ == 2:
                    self.state = 302
                    self.ifStatementStructure()
                    pass

                elif la_ == 3:
                    self.state = 303
                    self.whileStatement()
                    pass

                elif la_ == 4:
                    self.state = 304
                    self.variableInitialization()
                    pass

                elif la_ == 5:
                    self.state = 305
                    self.variableDeclaration()
                    pass

                elif la_ == 6:
                    self.state = 306
                    self.definitionList()
                    pass

                elif la_ == 7:
                    self.state = 307
                    self.declarationList(0)
                    pass

                elif la_ == 8:
                    self.state = 308
                    self.functionCall()
                    pass

                elif la_ == 9:
                    self.state = 309
                    self.assignment()
                    pass

                elif la_ == 10:
                    self.state = 310
                    self.inplaceAssignment()
                    pass

                elif la_ == 11:
                    self.state = 311
                    self.functionReturn()
                    pass


                self.state = 316
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 317
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
        self.enterRule(localctx, 54, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
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
        self._predicates[1] = self.expression_sempred
        self._predicates[5] = self.functionCallArgs_sempred
        self._predicates[7] = self.declarationList_sempred
        self._predicates[16] = self.functionArgs_sempred
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
         




