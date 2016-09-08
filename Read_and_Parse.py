"""
Read_and_Parse.py
name of python/text file -> expr

Receives a file name from and produces a python AST.
"""

import ast
from Interpret import interpret
import sys


# def main(argv):
#     if len(argv) < 1:
#         print('Bye!')
#         exit()
#     return (read(argv[0]))

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
    elif isinstance(node, ast.Lambda):
        return node

def parse_ast(file_name):
    with open(file_name, "r") as f:
        return ast.parse(f.read(), filename='<unknown>', mode='exec')




# print(ast.dump(parse_ast('sample_input.py')))