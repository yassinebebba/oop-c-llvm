# Generated from core/C.g4 by ANTLR 4.11.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,29,199,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,
        1,4,1,5,1,5,1,5,5,5,73,8,5,10,5,12,5,76,9,5,3,5,78,8,5,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,
        8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,11,
        1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,
        1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,16,1,16,1,17,
        1,17,1,18,1,18,1,19,1,19,1,20,1,20,1,21,1,21,1,22,1,22,1,23,1,23,
        1,24,1,24,5,24,154,8,24,10,24,12,24,157,9,24,1,25,4,25,160,8,25,
        11,25,12,25,161,1,25,1,25,1,26,1,26,3,26,168,8,26,1,26,3,26,171,
        8,26,1,26,1,26,1,27,1,27,1,27,1,27,5,27,179,8,27,10,27,12,27,182,
        9,27,1,27,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,5,28,193,8,28,
        10,28,12,28,196,9,28,1,28,1,28,1,180,0,29,1,1,3,2,5,3,7,4,9,5,11,
        6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,15,31,16,33,17,
        35,18,37,19,39,20,41,21,43,22,45,23,47,24,49,25,51,26,53,27,55,28,
        57,29,1,0,5,1,0,49,57,1,0,48,57,3,0,65,90,95,95,97,122,3,0,9,10,
        13,13,32,32,2,0,10,10,13,13,206,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,
        0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,
        0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,
        0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,
        0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,
        0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,0,
        0,0,57,1,0,0,0,1,59,1,0,0,0,3,61,1,0,0,0,5,63,1,0,0,0,7,65,1,0,0,
        0,9,67,1,0,0,0,11,77,1,0,0,0,13,79,1,0,0,0,15,86,1,0,0,0,17,95,1,
        0,0,0,19,100,1,0,0,0,21,105,1,0,0,0,23,111,1,0,0,0,25,115,1,0,0,
        0,27,120,1,0,0,0,29,126,1,0,0,0,31,133,1,0,0,0,33,135,1,0,0,0,35,
        137,1,0,0,0,37,139,1,0,0,0,39,141,1,0,0,0,41,143,1,0,0,0,43,145,
        1,0,0,0,45,147,1,0,0,0,47,149,1,0,0,0,49,151,1,0,0,0,51,159,1,0,
        0,0,53,170,1,0,0,0,55,174,1,0,0,0,57,188,1,0,0,0,59,60,5,61,0,0,
        60,2,1,0,0,0,61,62,5,47,0,0,62,4,1,0,0,0,63,64,5,43,0,0,64,6,1,0,
        0,0,65,66,5,45,0,0,66,8,1,0,0,0,67,68,5,34,0,0,68,10,1,0,0,0,69,
        78,5,48,0,0,70,74,7,0,0,0,71,73,7,1,0,0,72,71,1,0,0,0,73,76,1,0,
        0,0,74,72,1,0,0,0,74,75,1,0,0,0,75,78,1,0,0,0,76,74,1,0,0,0,77,69,
        1,0,0,0,77,70,1,0,0,0,78,12,1,0,0,0,79,80,5,115,0,0,80,81,5,105,
        0,0,81,82,5,103,0,0,82,83,5,110,0,0,83,84,5,101,0,0,84,85,5,100,
        0,0,85,14,1,0,0,0,86,87,5,117,0,0,87,88,5,110,0,0,88,89,5,115,0,
        0,89,90,5,105,0,0,90,91,5,103,0,0,91,92,5,110,0,0,92,93,5,101,0,
        0,93,94,5,100,0,0,94,16,1,0,0,0,95,96,5,118,0,0,96,97,5,111,0,0,
        97,98,5,105,0,0,98,99,5,100,0,0,99,18,1,0,0,0,100,101,5,99,0,0,101,
        102,5,104,0,0,102,103,5,97,0,0,103,104,5,114,0,0,104,20,1,0,0,0,
        105,106,5,115,0,0,106,107,5,104,0,0,107,108,5,111,0,0,108,109,5,
        114,0,0,109,110,5,116,0,0,110,22,1,0,0,0,111,112,5,105,0,0,112,113,
        5,110,0,0,113,114,5,116,0,0,114,24,1,0,0,0,115,116,5,108,0,0,116,
        117,5,111,0,0,117,118,5,110,0,0,118,119,5,103,0,0,119,26,1,0,0,0,
        120,121,5,102,0,0,121,122,5,108,0,0,122,123,5,111,0,0,123,124,5,
        97,0,0,124,125,5,116,0,0,125,28,1,0,0,0,126,127,5,100,0,0,127,128,
        5,111,0,0,128,129,5,117,0,0,129,130,5,98,0,0,130,131,5,108,0,0,131,
        132,5,101,0,0,132,30,1,0,0,0,133,134,5,42,0,0,134,32,1,0,0,0,135,
        136,5,40,0,0,136,34,1,0,0,0,137,138,5,41,0,0,138,36,1,0,0,0,139,
        140,5,123,0,0,140,38,1,0,0,0,141,142,5,125,0,0,142,40,1,0,0,0,143,
        144,5,91,0,0,144,42,1,0,0,0,145,146,5,93,0,0,146,44,1,0,0,0,147,
        148,5,59,0,0,148,46,1,0,0,0,149,150,5,44,0,0,150,48,1,0,0,0,151,
        155,7,2,0,0,152,154,7,2,0,0,153,152,1,0,0,0,154,157,1,0,0,0,155,
        153,1,0,0,0,155,156,1,0,0,0,156,50,1,0,0,0,157,155,1,0,0,0,158,160,
        7,3,0,0,159,158,1,0,0,0,160,161,1,0,0,0,161,159,1,0,0,0,161,162,
        1,0,0,0,162,163,1,0,0,0,163,164,6,25,0,0,164,52,1,0,0,0,165,167,
        5,13,0,0,166,168,5,10,0,0,167,166,1,0,0,0,167,168,1,0,0,0,168,171,
        1,0,0,0,169,171,5,10,0,0,170,165,1,0,0,0,170,169,1,0,0,0,171,172,
        1,0,0,0,172,173,6,26,0,0,173,54,1,0,0,0,174,175,5,47,0,0,175,176,
        5,42,0,0,176,180,1,0,0,0,177,179,9,0,0,0,178,177,1,0,0,0,179,182,
        1,0,0,0,180,181,1,0,0,0,180,178,1,0,0,0,181,183,1,0,0,0,182,180,
        1,0,0,0,183,184,5,42,0,0,184,185,5,47,0,0,185,186,1,0,0,0,186,187,
        6,27,0,0,187,56,1,0,0,0,188,189,5,47,0,0,189,190,5,47,0,0,190,194,
        1,0,0,0,191,193,8,4,0,0,192,191,1,0,0,0,193,196,1,0,0,0,194,192,
        1,0,0,0,194,195,1,0,0,0,195,197,1,0,0,0,196,194,1,0,0,0,197,198,
        6,28,0,0,198,58,1,0,0,0,9,0,74,77,155,161,167,170,180,194,1,6,0,
        0
    ]

class CLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    INTEGER = 6
    SIGNED = 7
    UNSIGNED = 8
    VOID = 9
    CHAR = 10
    SHORT = 11
    INT = 12
    LONG = 13
    FLOAT = 14
    DOUBLE = 15
    STAR = 16
    LP = 17
    RP = 18
    LC = 19
    RC = 20
    LSQRB = 21
    RSQRB = 22
    SEMICOLON = 23
    COMMA = 24
    IDENTIFIER = 25
    WS = 26
    NEWLINE = 27
    BLOCK_COMMENT = 28
    LINE_COMMENT = 29

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'/'", "'+'", "'-'", "'\"'", "'signed'", "'unsigned'", 
            "'void'", "'char'", "'short'", "'int'", "'long'", "'float'", 
            "'double'", "'*'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
            "';'", "','" ]

    symbolicNames = [ "<INVALID>",
            "INTEGER", "SIGNED", "UNSIGNED", "VOID", "CHAR", "SHORT", "INT", 
            "LONG", "FLOAT", "DOUBLE", "STAR", "LP", "RP", "LC", "RC", "LSQRB", 
            "RSQRB", "SEMICOLON", "COMMA", "IDENTIFIER", "WS", "NEWLINE", 
            "BLOCK_COMMENT", "LINE_COMMENT" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "INTEGER", "SIGNED", 
                  "UNSIGNED", "VOID", "CHAR", "SHORT", "INT", "LONG", "FLOAT", 
                  "DOUBLE", "STAR", "LP", "RP", "LC", "RC", "LSQRB", "RSQRB", 
                  "SEMICOLON", "COMMA", "IDENTIFIER", "WS", "NEWLINE", "BLOCK_COMMENT", 
                  "LINE_COMMENT" ]

    grammarFileName = "C.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


