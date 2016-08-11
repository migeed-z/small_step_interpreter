import unittest
import ast
from Step import *
from Scope import Scope
from Done import Done
from Earg import Earg
from Eif import Eif
from Ecall import Ecall
from Closure import Closure



class TestStep(unittest.TestCase):

    def test_num_no_cont(self):
        num_expr = Num(3)
        env = Scope([])
        k = Done()
        val = step(num_expr, env, k)[0]
        self.assertEqual(val.n, 3)

    def test_bool_no_cont(self):
        bool_expr = NameConstant(True)
        env = Scope([])
        k = Done()
        val = step(bool_expr, env, k)[0]
        self.assertEqual(val.value, True)

    def test_variable(self):
        var_expr = Name(id='x')
        env = Scope([])
        new_env = env.extend('x', Num(3))
        k = Done()
        val = step(var_expr, new_env, k)[0]
        self.assertEqual(val.n, 3)

    def test_lambda(self):
        lamb_expr = Lambda(args=ast.arguments(args=[ast.arg(arg='x')]), body=Num(n=3))
        env = Scope([])
        k = Done()
        val = step(lamb_expr, env, k)[0]
        self.assert_(isinstance(val, Closure))
        expr = val.lambda_expr
        self.assertEqual(expr.args.args[0].arg, 'x')
        self.assertEqual(expr.body.n, 3)

    def test_call(self):
        call_expr = Call(func=Lambda(args=ast.arguments(args=[ast.arg(arg='x')]), body=Name(id='x')), args=[Num(n=3)])
        env = Scope([])
        k = Done()
        val = step(call_expr, env, k)[0]
        earg = step(call_expr, env, k)[2]
        self.assertEqual(val.args.args[0].arg, 'x')
        self.assertEqual(val.body.id, 'x')
        self.assert_(isinstance(earg, Earg))
        self.assertEqual(earg.expr.n, 3)

    def test_if(self):
        if_expr = IfExp(test=Num(n=2), body=Num(n=1), orelse=Num(n=3))
        env = Scope([])
        k = Done()
        val = step(if_expr, env, k)[0]
        eif = step(if_expr, env, k)[2]
        self.assert_(isinstance(eif, Eif))
        self.assertEqual(val.n, 2)
        self.assertEqual(eif.then.n, 1)
        self.assertEqual(eif.el.n, 3)


if __name__ == '__main__':
    unittest.main()