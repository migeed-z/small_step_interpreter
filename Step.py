"""
Step.py
a config is: (expr, env, cont)

config -> config

"""
from ast import Call, Lambda, Name, Num, NameConstant, Expr, IfExp, BinOp
from Earg import Earg
from Eif import Eif
from Done import Done
from Closure import Closure
from InterpreterError import InterpreterError
from Visit import OpVisitor

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
    if isinstance(expr, Num) or isinstance(expr, NameConstant):
        if not isinstance(cont, Done):
            return cont.apply(expr, env)
        else:
            return expr, env, cont

    #Var
    elif isinstance(expr, Name):
        name = expr.id
        val = env.get(name)
        if isinstance(val, Closure):
            return val.lambda_expr, val.scope, cont
        else:
            return val, env, cont

    #Lambda
    elif isinstance(expr, Lambda):
        #and if cont. has
        if not isinstance(cont, Done):
            return cont.apply(expr, env)
        else:
            return expr, env, cont

    #Call
    elif isinstance(expr, Call):
        k = Earg(expr.args[0], env, cont)
        return expr.func, env, k

    #Op (same as call)
    elif isinstance(expr, BinOp):
        visitor = OpVisitor()
        name = visitor.visit(expr.op)
        k = Earg(expr.left, env, cont)
        val = env.get(name)
        print("val %s" % val)
        return val, env, k

    #IfExpr
    elif isinstance(expr, IfExp):
        test = expr.test
        body = expr.body
        orelse = expr.orelse

        return test, env, Eif(body, orelse, env, cont)

    else:
        print("error expr %s" % expr)
        raise InterpreterError("Not a valid program")
