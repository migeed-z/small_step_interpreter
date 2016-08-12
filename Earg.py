from Continuation import Continuation
from Ecall import Ecall
from Closure import Closure

class Earg(Continuation):

    def __init__(self, expr, env, k):
        """
        :param expr: Argument to the function/ val
        :type expr: Expr.value
        :type env: Scope
        :type k: Continuation
        """
        super().__init__()

        self.k = k
        self.expr = expr
        self.env = env

    def apply(self, val, scope):
        """
        :param val: Closure
        :return: Configuration
        """
        return self.expr, self.env, Ecall(val, scope, self.k)



