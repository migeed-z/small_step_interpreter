import ast
from Continuation import Continuation


class Ecall(Continuation):
    
    def __init__(self, expr, env, k):
        """

        :param expr: Lambda expression
        :param env: the env. of the lambda expr.
        :param k:
        :return:
        """
        super().__init__()

        self.k = k
        self.expr = expr
        self.env = env

    def apply(self, val):
        """
        :param val: arg
        :return: Config?
        """
        print(ast.dump(self.expr))
        scope = self.env.extend(self.expr.value.args.args[0].arg, val)
        return self.expr.value.body, scope, self.k

