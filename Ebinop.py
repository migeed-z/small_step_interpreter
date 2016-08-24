import ast
from Continuation import Continuation


class Ebinop(Continuation):
    def __init__(self, expr, env, k):
        """

        :param expr: Lambda expression
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
        :param val: arg
        """
        self.expr.append(val)
        return self.expr, scope, self.k

