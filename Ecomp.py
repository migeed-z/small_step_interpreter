from copy import copy
from ast import Compare, Num
from Visit import OpVisitor

class Ecomp:

    def __init__(self, left, ops, rs, env, k):
        """
        :param left: The evaluated left side of the comparison
        :type left: Val
        :type ops: List
        :type rs: List
        :type env: Scope
        :type k: Continuation
        """
        self.left = left
        self.ops = ops
        self.rs = rs
        self.env = env
        self.k = k

    def apply(self, val, scope):
        ops = copy(self.ops)
        op = ops.pop()

        visitor = OpVisitor()
        operation = visitor.visit(op)
        left = self.left
        res = operation(left.n, val.n)

        if len(ops) == 0:
            expr = Num(n=res)
        else:
            expr = Compare(left=Num(n=res), ops=ops, comparators=self.rs)

        return expr, self.env, self.k
