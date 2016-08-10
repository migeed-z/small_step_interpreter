"""
Read_and_Parse.py
name of python/text file -> expr

Receives a file name from and produces a python AST.
"""

from ast import *
from Interpret import interpret


def read(file_name):
    ast = parse_ast(file_name)
    return interpret(ast)

def parse_ast(file_name):
    with open(file_name, "r") as f:
        return parse(f.read(), filename='<unknown>', mode='exec')


print(dump(parse_ast("sample_input.py")))


# read("sample_input.py")