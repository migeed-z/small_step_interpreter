from Continuation import Continuation
from Ebinop import Ebinop

class Eoparg(Continuation):

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
        ret = self.expr[1]
        self.expr[1] = val
        return ret, self.env, Ebinop(self.expr, scope, self.k)

