"""
Step.py
a config is: (expr, env, cont)

config -> config

"""
from ast import Call, Lambda, Name, Num, NameConstant, Expr, IfExp, BinOp, dump, Compare, Assign
from Earg import Earg
from Eif import Eif
from Done import Done
from Closure import Closure
from InterpreterError import InterpreterError
from Visit import OpVisitor
from Eoparg import Eoparg
from Ecomp import Ecomp
from Ecomparg import Ecomparg
from EAssign import EAssign
from copy import copy

def step(expr, env, cont):
    """
    recieves an expr and performs
    one step of computation on it.
    If no further computation is
    possible, step returns the
     expression
    :param expr: Expr.value
    :param env: Scope
    :param cont: Continuation
    :return: (Expr, Scope, Continuation)
    """

    #Num & Bool
    if isinstance(expr, Num) or isinstance(expr, NameConstant) or isinstance(expr, Lambda):
        if not isinstance(cont, Done):
            return cont.apply(expr, env)
        else:
            return expr, env, cont

    #Var
    elif isinstance(expr, Name):
        name = expr.id
        (val,scope) = env.get(name)
        if isinstance(val, Lambda):
            return val, scope, cont
        else:
            return val, env, cont

    #Call
    elif isinstance(expr, Call):
        k = Earg(expr.args[0], env, cont)
        return expr.func, env, k

    #BinOp
    elif isinstance(expr, BinOp):
        k = Eoparg(expr.right, expr.op, env, cont)
        return expr.left, env, k

    #Comparator
    elif isinstance(expr, Compare):
        k = Ecomparg(expr.ops, expr.comparators, env, cont)
        return expr.left, env, k

    #IfExpr
    elif isinstance(expr, IfExp):
        test = expr.test
        body = expr.body
        orelse = expr.orelse

        return test, env, Eif(body, orelse, env, cont)

    #Assign
    elif isinstance(expr, Assign):
        val = expr.value
        target = expr.targets[0]
        return val, env, EAssign(target, env, cont)

    else:
        raise InterpreterError("Not a valid program")

