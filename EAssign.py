import ast
from Continuation import Continuation

class EAssign(Continuation):
    def __init__(self, target, env, k):
        """
        :param target: expr in which we will store the value
        :param env: Scope
        :param k: Cont
        """
        super().__init__()
        self.target = target
        self.env = env
        self.k = k

    def apply(self, val, scope):
        """
        :param val: evaluated value of right side of the assignment
        """
        return ast.NameConstant(value=None), scope.extend(self.target.id, (val, scope)), self.k
