"""
Read_and_Parse.py
name of python/text file -> expr

Receives a file name from and produces a python AST.
"""

import ast
from Interpret import interpret
from Closure import Closure
import sys

# sys.path.insert(0, '../programs')

def main(argv):
    if len(argv) < 1:
        print('Bye!')
        exit()
    print(read(argv[0]))

def read(file_name):
    node = parse_ast(file_name)
    res = interpret(node)
    return unwrap(res)

def unwrap(node):
    """
    Unwraps python value from given node.
    :param node: AST
    :return: U bool num
    """
    if isinstance(node, ast.NameConstant):
        return node.value
    elif isinstance(node, ast.Num):
        return node.n
    elif isinstance(node, Closure):
        return node.lambda_expr

def parse_ast(file_name):
    with open(file_name, "r") as f:
        return ast.parse(f.read(), filename='<unknown>', mode='exec')

if __name__ == "__main__":
   main(sys.argv[1:])

