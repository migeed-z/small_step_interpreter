import unittest
import ast
from Step import *
from Scope import Scope
from Done import Done
from Eif import Eif


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

if __name__ == '__main__':
    unittest.main()