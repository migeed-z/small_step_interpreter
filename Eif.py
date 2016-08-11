from Continuation import Continuation

class Eif(Continuation):

    def __init__(self, then, el, env, k):
        super().__init__()
        self.k = k
        self.then = then
        self.el = el
        self.env = env


    def apply(self, cond):
        return (self.then if cond else self.el, self.env, self.k)