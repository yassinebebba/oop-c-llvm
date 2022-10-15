import sys
from antlr4 import *
from core.CLexer import CLexer
from core.CParser import CParser
from listener import Listener


def main(argv):
    input = FileStream(argv[1])
    lexer = CLexer(input)
    stream = CommonTokenStream(lexer)
    parser = CParser(stream)
    tree = parser.compilationUnit()
    with open('output.c', 'w') as file:
        listener = Listener(file)
        walker = ParseTreeWalker()
        walker.walk(listener, tree)


if __name__ == '__main__':
    main(sys.argv)
