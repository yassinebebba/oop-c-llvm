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
        4,0,21,136,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,5,
        5,5,57,8,5,10,5,12,5,60,9,5,3,5,62,8,5,1,6,1,6,1,6,1,6,1,6,1,7,1,
        7,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,11,1,12,1,12,1,13,1,13,
        1,14,1,14,1,15,1,15,1,16,1,16,5,16,91,8,16,10,16,12,16,94,9,16,1,
        17,4,17,97,8,17,11,17,12,17,98,1,17,1,17,1,18,1,18,3,18,105,8,18,
        1,18,3,18,108,8,18,1,18,1,18,1,19,1,19,1,19,1,19,5,19,116,8,19,10,
        19,12,19,119,9,19,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,5,
        20,130,8,20,10,20,12,20,133,9,20,1,20,1,20,1,117,0,21,1,1,3,2,5,
        3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,15,
        31,16,33,17,35,18,37,19,39,20,41,21,1,0,5,1,0,49,57,1,0,48,57,3,
        0,65,90,95,95,97,122,3,0,9,10,13,13,32,32,2,0,10,10,13,13,143,0,
        1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,
        0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,
        0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,
        0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,
        0,0,0,1,43,1,0,0,0,3,45,1,0,0,0,5,47,1,0,0,0,7,49,1,0,0,0,9,51,1,
        0,0,0,11,61,1,0,0,0,13,63,1,0,0,0,15,68,1,0,0,0,17,72,1,0,0,0,19,
        74,1,0,0,0,21,76,1,0,0,0,23,78,1,0,0,0,25,80,1,0,0,0,27,82,1,0,0,
        0,29,84,1,0,0,0,31,86,1,0,0,0,33,88,1,0,0,0,35,96,1,0,0,0,37,107,
        1,0,0,0,39,111,1,0,0,0,41,125,1,0,0,0,43,44,5,61,0,0,44,2,1,0,0,
        0,45,46,5,47,0,0,46,4,1,0,0,0,47,48,5,43,0,0,48,6,1,0,0,0,49,50,
        5,45,0,0,50,8,1,0,0,0,51,52,5,34,0,0,52,10,1,0,0,0,53,62,5,48,0,
        0,54,58,7,0,0,0,55,57,7,1,0,0,56,55,1,0,0,0,57,60,1,0,0,0,58,56,
        1,0,0,0,58,59,1,0,0,0,59,62,1,0,0,0,60,58,1,0,0,0,61,53,1,0,0,0,
        61,54,1,0,0,0,62,12,1,0,0,0,63,64,5,118,0,0,64,65,5,111,0,0,65,66,
        5,105,0,0,66,67,5,100,0,0,67,14,1,0,0,0,68,69,5,105,0,0,69,70,5,
        110,0,0,70,71,5,116,0,0,71,16,1,0,0,0,72,73,5,42,0,0,73,18,1,0,0,
        0,74,75,5,40,0,0,75,20,1,0,0,0,76,77,5,41,0,0,77,22,1,0,0,0,78,79,
        5,123,0,0,79,24,1,0,0,0,80,81,5,125,0,0,81,26,1,0,0,0,82,83,5,91,
        0,0,83,28,1,0,0,0,84,85,5,93,0,0,85,30,1,0,0,0,86,87,5,59,0,0,87,
        32,1,0,0,0,88,92,7,2,0,0,89,91,7,2,0,0,90,89,1,0,0,0,91,94,1,0,0,
        0,92,90,1,0,0,0,92,93,1,0,0,0,93,34,1,0,0,0,94,92,1,0,0,0,95,97,
        7,3,0,0,96,95,1,0,0,0,97,98,1,0,0,0,98,96,1,0,0,0,98,99,1,0,0,0,
        99,100,1,0,0,0,100,101,6,17,0,0,101,36,1,0,0,0,102,104,5,13,0,0,
        103,105,5,10,0,0,104,103,1,0,0,0,104,105,1,0,0,0,105,108,1,0,0,0,
        106,108,5,10,0,0,107,102,1,0,0,0,107,106,1,0,0,0,108,109,1,0,0,0,
        109,110,6,18,0,0,110,38,1,0,0,0,111,112,5,47,0,0,112,113,5,42,0,
        0,113,117,1,0,0,0,114,116,9,0,0,0,115,114,1,0,0,0,116,119,1,0,0,
        0,117,118,1,0,0,0,117,115,1,0,0,0,118,120,1,0,0,0,119,117,1,0,0,
        0,120,121,5,42,0,0,121,122,5,47,0,0,122,123,1,0,0,0,123,124,6,19,
        0,0,124,40,1,0,0,0,125,126,5,47,0,0,126,127,5,47,0,0,127,131,1,0,
        0,0,128,130,8,4,0,0,129,128,1,0,0,0,130,133,1,0,0,0,131,129,1,0,
        0,0,131,132,1,0,0,0,132,134,1,0,0,0,133,131,1,0,0,0,134,135,6,20,
        0,0,135,42,1,0,0,0,9,0,58,61,92,98,104,107,117,131,1,6,0,0
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
    VOID = 7
    INT = 8
    STAR = 9
    LP = 10
    RP = 11
    LC = 12
    RC = 13
    LSQRB = 14
    RSQRB = 15
    SEMICOLON = 16
    IDENTIFIER = 17
    WS = 18
    NEWLINE = 19
    BLOCK_COMMENT = 20
    LINE_COMMENT = 21

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'/'", "'+'", "'-'", "'\"'", "'void'", "'int'", "'*'", 
            "'('", "')'", "'{'", "'}'", "'['", "']'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "INTEGER", "VOID", "INT", "STAR", "LP", "RP", "LC", "RC", "LSQRB", 
            "RSQRB", "SEMICOLON", "IDENTIFIER", "WS", "NEWLINE", "BLOCK_COMMENT", 
            "LINE_COMMENT" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "INTEGER", "VOID", 
                  "INT", "STAR", "LP", "RP", "LC", "RC", "LSQRB", "RSQRB", 
                  "SEMICOLON", "IDENTIFIER", "WS", "NEWLINE", "BLOCK_COMMENT", 
                  "LINE_COMMENT" ]

    grammarFileName = "C.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


