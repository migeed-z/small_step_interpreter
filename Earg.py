from Continuation import Continuation
from Ecall import Ecall
from Closure import Closure

class Earg(Continuation):

    def __init__(self, expr, env, k):
        """
        :param expr: Argument to the function/ val
        :param env:
        :param k:
        :return:
        """
        super().__init__()

        self.k = k
        self.expr = expr
        self.env = env

    def apply(self, val):
        """
        :param val: Closure
        :return:
        """
        return expr, env, Ecall(val.lambda_expr, val.scope, k)



