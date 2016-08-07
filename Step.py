"""
Step.py
a config is: (expr, env, cont)

config -> config

"""
from ast import Call, Lambda, Name, Num, NameConstant, Expr, IfExp

# from Closure import Closure
from InterpreterError import InterpreterError


def step(expr, env, cont):
    """
    recieves an expr and performs
    one step of computation on it.
    If no further computation is
    possible, step returns the
     expression
    :param expr: Expr
    :param env: Scope
    :param cont: Continuation
    :return: (Expr, Scope, Continuation)
    """
    value = expr.value
    if isinstance(expr, Expr):

        #Num
        if isinstance(value, Num):
            print("Num")

        #Var
        elif isinstance(value, Name):
            name = value.id
            print("Variable")

        #Bool
        elif isinstance(value, NameConstant):
            print( "Bool")

        #Lambda
        elif isinstance(value, Lambda):
            print("Lambda")

        #IfExpr
        elif isinstance(value, IfExp):
            print("If Expr")

        #Call
        elif isinstance(value, Call):
            print("Call")

    else:
        raise InterpreterError("Not a valid python program")

