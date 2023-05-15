import subprocess
import antlr4
from antlr4 import CommonTokenStream
from core.CLexer import CLexer
from core.CParser import CParser
from visitor import Visitor

def compile(file_path: str):
    with open(file_path) as input, open('tests/output.ll', 'w') as output:
        input_str = input.read()
        input_stream = antlr4.InputStream(input_str)
        lexer = CLexer(input_stream)
        token_stream = antlr4.CommonTokenStream(lexer)
        parser = CParser(token_stream)
        tree = parser.compilationUnit()
        stream = CommonTokenStream(lexer)
        visitor = Visitor(stream, output)
        visitor.visit(tree)


def run_script():
    process = subprocess.Popen(['bash', 'tests/make.sh'], stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    stdout = stdout.decode('utf-8')
    stderr = stderr.decode('utf-8')
    return_code = process.returncode

    return stdout, stderr, return_code

def test_1():
    """
    This test has one method main and test all
    operations that can be done on 'short'
    :return:
    """
    compile('tests/sourcecode/test_1.c')
    stdout, stderr, return_code = run_script()
    expected = """a = 0
a = 10
"""
    assert return_code == 0
    assert stdout == expected

