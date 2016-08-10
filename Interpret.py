"""
Interpret.py
ast.AST -> Value

A Value is one of:
 - ast.expr where value field is a python boolean
 - ast.expr where value field is a python number
 - ast.expr where value field is a Closure

Receives a file name from and produces a python AST.
"""
from ast import Num, NameConstant
from Scope import Scope
from Step import step
from ast import ImportFrom, Expr, dump
from Done import Done
from Closure import Closure

def interpret(expr):
    """
    Interprets a python AST with small-step sementics
    :param expr: ast.AST
    :return: Value
    """

    node = expr.body[0]
    env = Scope(())
    cont = Done()
    print(dump(node))

    while not is_value(node) or not isinstance(cont, Done):
        node, env, cont = step(node, env, cont)
        if is_value(node):
            cont.apply(node)
    return node

def is_value(node):
    return isinstance(node, Expr) and \
           (isinstance(node.value, Num) or
            isinstance(node.value, NameConstant) or
            isinstance(node.value, Closure))


