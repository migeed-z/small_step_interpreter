"""
Step.py
(expr, env, cont) -> (expr', env', cont')
"""
from ast import Call, Lambda, Name, Num, NameConstant, Expr, IfExp
from Cont.Continuation import Continuation
from Cont.Earg import Earg
from Cont.Call import Call

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
            return Continuation(value.n, env, cont)

        #restore env. work on new expr.
        #Var
        elif isinstance(value, Name):
            name = value.id
            #Closure
            val = env.get(name)
            if not val:
                raise ValueError("no value for key %s" % name)
            else:
                return Continuation(val, env, cont)


            #restore env. work on new expr.

        #Bool
        elif isinstance(value, NameConstant):
            return Continuation(value.value, env, cont)

        #Lambda
        elif isinstance(value, Lambda):
            print("Lambda")

        #IfExpr
        elif isinstance(value, IfExp):
            print("If Expr")

        #Call
        elif isinstance(value, Call):
            pass
            # return step(value, env, k.extend(None, Earg()))


    else:
        raise InterpreterError("Not a valid python program")

