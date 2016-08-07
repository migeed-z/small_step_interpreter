from Continuation import Continuation

class Ecall(Continuation):
    
    def __init__(self, expr, env, k):
        
        super().__init__(k)
        self.expr = expr
        self.env = env

    def apply(self, val):
        """
        :param val: Closure
        :return: Config?
        """
        pass

