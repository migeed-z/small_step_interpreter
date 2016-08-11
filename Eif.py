import ast
from Continuation import Continuation

class Eif(Continuation):

    def __init__(self, then, el, env, k):
        super().__init__()
        self.k = k
        self.then = then
        self.el = el
        self.env = env


    def apply(self, cond):
        val = None
        if isinstance(cond, ast.NameConstant):
            val = cond.value
        elif isinstance(cond, ast.Num):
            val = cond.n

        return (self.then if val else self.el, self.env, self.k)