"""
Interpret.py
ast.AST -> Value

A Value is one of:
 - ast.expr where value field is a python boolean
 - ast.expr where value field is a python number
 - ast.expr where value field is a Closure

Receives a file name from and produces a python AST.
"""
from ast import Num, NameConstant, Lambda
from Scope import Scope
from Step import step
from ast import ImportFrom, Expr, dump
from Done import Done
from InterpreterError import InterpreterError
from Transform import transform

def interpret(expr):
    """
    Interprets a python AST with small-step sementics
    :param expr: ast.AST
    :return: Value
    """

    nodes = transform(expr.body)
    env = Scope(())
    cont = Done()

    final_val = None

    for node in nodes:
        if isinstance(node, Expr):
            val = node.value
            while not is_value(val) or not isinstance(cont, Done):
                val, env, cont = step(val, env, cont)

            final_val = val

        else:
            raise InterpreterError('Not a valid python program')

    return final_val

def is_value(node):
    return  isinstance(node, Num)\
            or isinstance(node, NameConstant) \
            or isinstance(node, Lambda)


