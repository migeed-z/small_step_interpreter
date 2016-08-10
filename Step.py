"""
Step.py
a config is: (expr, env, cont)

config -> config

"""
from ast import Call, Lambda, Name, Num, NameConstant, Expr, IfExp
from Done import Done
from Earg import Earg
from Eif import Eif
from Closure import Closure
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

    if isinstance(expr, Expr):
        value = expr.value

        #Num & Bool
        if isinstance(value, Num) or isinstance(value, NameConstant):
            return expr, env, cont

        #Var
        elif isinstance(value, Name):
            name = value.id
            val = env.get(name)
            if isinstance(val, Closure):
                return val.lambda_expr, val.scope, cont
            else:
                return val, env, cont

        #Lambda
        elif isinstance(value, Lambda):
            val = Closure(value, env)
            return val, env, cont

        #Call
        elif isinstance(value, Call):
            k = Earg(value.args[0], env, cont)
            return value.func, env, k

        #IfExpr
        elif isinstance(value, IfExp):
            test = Expr(value=value.test)
            body = Expr(value=value.body)
            orelse = Expr(value=value.orelse)

            return test, env, Eif(body, orelse, env, cont)

    else:
        raise InterpreterError("Not a valid program")

