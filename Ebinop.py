import ast
from Continuation import Continuation


class Ebinop(Continuation):
    def __init__(self, expr, env, k):
        """

        :param expr: length 2 list, position 0 is the operation, position 1 is the evaluated value of left side
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
        :param val: evaluated value of right side
        """
        self.expr.append(val)
        return self.expr, scope, self.k

