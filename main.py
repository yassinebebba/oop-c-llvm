import sys
import antlr4
from antlr4 import *
from core.CLexer import CLexer
from core.CParser import CParser
from visitor import Visitor


def main(argv):
    with open('input.c') as input, open('output.c', 'w') as output:
        input_str = input.read()
        input_stream = antlr4.InputStream(input_str)
        lexer = CLexer(input_stream)
        token_stream = antlr4.CommonTokenStream(lexer)
        parser = CParser(token_stream)
        tree = parser.compilationUnit()
        stream = CommonTokenStream(lexer)
        visitor = Visitor(stream, output)
        visitor.visit(tree)


if __name__ == '__main__':
    main(sys.argv)
