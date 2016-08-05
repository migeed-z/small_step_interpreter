from ast import expr
from Scope import Scope

class Closure(expr):
    def __init__(self, lambda_expr, scope):

        self.lambda_expr = lambda_expr
        self.scope = scope

    def closure_extend(self, val):
        """
        Extends the lambda body with parame
        :return: (expr, env)
        """
        body = self.lambda_expr.body
        param = self.lambda_expr.args.args[0].args
        self.scope.extend(param, val)
        return body, self.scope















