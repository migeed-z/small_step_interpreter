import ast
from Continuation import Continuation
from Visit import OpVisitor


class Ebinop(Continuation):
    def __init__(self, expr, op, env, k):
        """

        :param expr: value of the left side
        :type expr: Num
        :param op: expr.op
        :type op: operation
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
        :param val: evaluated value of right side
        """
        visitor = OpVisitor()
        operation = visitor.visit(self.op)
        return ast.Num(operation(self.expr.n, val.n)), self.env, self.k
