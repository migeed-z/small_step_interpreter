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
from InterpreterError import InterpreterError

def interpret(expr):
    """
    Interprets a python AST with small-step sementics
    :param expr: ast.AST
    :return: Value
    """

    node = expr.body[0]
    env = Scope(())
    cont = Done()

    if isinstance(node, Expr):
        val = node.value
    else:
        raise InterpreterError('Not a valid python program')

    while not is_value(val) or not isinstance(cont, Done):
        print(val)
        val, env, cont = step(val, env, cont)
        if is_value(val):
            val, env, cont = cont.apply(val)
    return val

def is_value(node):
    return  isinstance(node, Num)\
            or isinstance(node, NameConstant) \
            or isinstance(node, Closure)


