from Continuation import Continuation
from Ebinop import Ebinop

class Eoparg(Continuation):

    def __init__(self, expr, env, k):
        """
        :param expr: a length 2 list, position 0 is the operation, position 1 is the right side of the operation
        :type expr: python list
        :type env: Scope
        :type k: Continuation
        """
        super().__init__()

        self.k = k
        self.expr = expr
        self.env = env

    def apply(self, val, scope):
        """
        :param val: the evaluated value of the left side
        :return: Configuration
        """
        ret = self.expr[1]
        self.expr[1] = val
        return ret, self.env, Ebinop(self.expr, scope, self.k)

