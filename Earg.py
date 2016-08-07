from Continuation import Continuation
from Ecall import Ecall
from Closure import Closure

class Earg(Continuation):

    def __init__(self, expr, env, k):
        super().__init__(k)
        self.expr = expr
        self.env = env

    def apply(self, val):
        self.k.append(Ecall(val, env, k))
        return expr, env, k

