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


    #Problem here (we are not using a closure)!!!!!!!!!!!!!!!
    def apply(self, val, scope):
        """
        :param val: arg
        """
        new_scope = self.env.extend(self.expr.args.args[0].arg, (val,scope))
        return self.expr.body, new_scope, self.k

