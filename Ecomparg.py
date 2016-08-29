from Ecomp import Ecomp
from copy import copy

class Ecomparg:

    def __init__(self, ops, rs, env, k):
        """
        :param ops: Operations for comparisons
        :type ops: List
        :param rs: Right sides of the comparision
        :type rs: List
        :param env: the environment
        :param k: the continuation
        """
        self.ops = ops
        self.rs = rs
        self.env = env
        self.k = k

    def apply(self, val, scope):
        rs = copy(self.rs)
        expr = rs.pop()

        return expr, self.env, Ecomp(val, self.ops, rs, scope, self.k)

