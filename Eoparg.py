from Continuation import Continuation
from Ebinop import Ebinop

class Eoparg(Continuation):

    def __init__(self, expr, op, env, k):
        """
        :param expr: right side of the expression
        :type expr: Expr.value
        :param op: operation
        :type op: operator
        :type env: Scope
        :type k: Continuation
        """
        super().__init__()

        self.op = op
        self.k = k
        self.expr = expr
        self.env = env

    def apply(self, val, scope):
        """
        :param val: the evaluated value of the left side
        :type val: Num
        :return: Configuration
        """
        return self.expr, self.env, Ebinop(val, self.op, scope, self.k)

