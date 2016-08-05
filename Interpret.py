"""
Interpret.py
ast.AST -> Value

A Value is one of:
 - ast.expr where value field is a python boolean
 - ast.expr where value field is a python number
 - ast.expr where value field is a Closure

Receives a file name from and produces a python AST.
"""
from Scope import Scope
from Step import step
from ast import ImportFrom, Expr, dump
from Cont.Done import Done

def interpret(expr):
    """
    Interprets a python AST with small-step sementics
    :param expr: ast.AST
    :return: Value
    """

    node = expr.body[0]
    print(dump(node))

    env = Scope(())
    cont = Done

    return step(node, env, cont)

    # while not is_value(node):
    #     node, env = step(node, env)
    # return node



