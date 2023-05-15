from tests.base import compile
from tests.base import run_script

def test_1():
    """
    test short definition and assignment separately
    """
    print(__file__)
    compile('./sourcecode/short/test_1.c')
    stdout, stderr, return_code = run_script()
    expected = """a = 10
a = 20
a = 30
"""
    assert return_code == 0
    assert stdout == expected

def test_2():
    """
    test short declaration and declaration with addition expression;
    """
    compile('./sourcecode/short/test_2.c')
    stdout, stderr, return_code = run_script()
    expected = """a = 2
b = 5
"""
    assert return_code == 0
    assert stdout == expected


