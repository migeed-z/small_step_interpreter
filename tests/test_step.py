import unittest
import ast
from Step import *
from Scope import Scope
from Done import Done
from Earg import Earg
from Eif import Eif
from Closure import Closure


class TestStep(unittest.TestCase):

    def test_num_no_cont(self):
        num_expr = ast.Expr(value=Num(3))
        env = Scope([])
        k = Done()
        val = step(num_expr, env, k)[0].value
        self.assertEqual(val.n, 3)

    def test_num_with_cont(self):
        num_expr = ast.Expr(value=Num(3))
        env = Scope([])
        k = Eif(Expr(value=Num(4)), Expr(value=Num(2)), env, Done())
        val_tuple = step(num_expr, env, k)
        val = val_tuple[0].value
        new_cont = val_tuple[2]
        self.assertEqual(val.n, 4)
        self.assertEqual(new_cont, Done())

    def test_bool_no_cont(self):
        bool_expr = ast.Expr(value=NameConstant(True))
        env = Scope([])
        k = Done()
        val = step(bool_expr, env, k)[0].value
        self.assertEqual(val.value, True)

    def test_bool_with_cont(self):
        bool_expr = ast.Expr(value=NameConstant(3))
        env = Scope([])
        k = Eif(Expr(value=Num(4)), Expr(value=Num(2)), env, Done())
        val_tuple = step(bool_expr, env, k)
        val = val_tuple[0].value
        new_cont = val_tuple[2]
        self.assertEqual(val.n, 4)
        self.assertEqual(new_cont, Done())

    def test_variable(self):
        var_expr = ast.Expr(value=Name(id='x'))
        env = Scope([])
        new_env = env.extend('x', Num(3))
        k = Done()
        val = step(var_expr, new_env, k)[0]
        self.assertEqual(val.n, 3)

    def test_lambda(self):
        lamb_expr = ast.Expr(value=Lambda(args=ast.arguments(args=[ast.arg(arg='x')]), body=Num(n=3)))
        env = Scope([])
        k = Done()
        val = step(lamb_expr, env, k)[0]
        clos = Closure(lamb_expr, env)
        self.assertEqual(val, clos)

if __name__ == '__main__':
    unittest.main()