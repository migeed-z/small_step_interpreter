import ast
from Continuation import Continuation


class Ecall(Continuation):
    
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

    def apply(self, val):
        """
        :param val: arg
        :return: Configuration
        """
        scope = self.env.extend(self.expr.args.args[0].arg, val)
        return self.expr.body, scope, self.k

