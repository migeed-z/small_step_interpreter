import unittest
import ast
from Step import *
from Scope import Scope
from Done import Done
from Earg import Earg
from Eif import Eif
from Ecall import Ecall
from Closure import Closure
from Interpret import interpret



class TestStep(unittest.TestCase):

    def test_num(self):
        num_expr = ast.Module(body=[Expr(value=Num(n=3))])
        val = interpret(num_expr)
        self.assertEqual(val.n, 3)

    def test_call(self):
        call_expr = ast.Module(body=[Expr(value=Call(
            func=Lambda(args=ast.arguments(args=[ast.arg(arg='x')]), body=Name(id='x')), args=[Num(n=3)]))])
        val = interpret(call_expr)
        self.assertEqual(val.n, 3)

    def test_if_true(self):
        if_expr = ast.Module(body=[Expr(value=IfExp(test=Num(n=2), body=Num(n=1), orelse=Num(n=3)))])
        val = interpret(if_expr)
        self.assertEqual(val.n, 1)

    def test_if_false(self):
        if_expr = ast.Module(body=[Expr(value=IfExp(test=NameConstant(value=False), body=Num(n=1), orelse=Num(n=3)))])
        val = interpret(if_expr)
        self.assertEqual(val.n, 3)

    def test_bool(self):
        bool_expr = ast.Module(body=[Expr(value=NameConstant(value=True))])
        val = interpret(bool_expr)
        self.assertEqual(val.value, True)

    def test_if_call(self):
        if_call_expr = ast.Module(body=[Expr(value=IfExp(test=NameConstant(value=False), body=Num(n=1), orelse=Call(func=Call(
            func=Lambda(args=ast.arguments(args=[ast.arg(arg='x')]), body=Name(id='x')), args=[Lambda(
            args=ast.arguments(args=[ast.arg(arg='y')]), body=Name(id='y'))]), args=[Num(n=4)])))])
        val = interpret(if_call_expr)
        self.assertEqual(val.n, 4)

    def test_if_if(self):
        if_if_expr = ast.Module(body=[Expr(value=IfExp(test=NameConstant(value=False), body=Num(n=3), orelse=IfExp(test=NameConstant(value=True), body=Num(n=4), orelse=Num(n=1))))])
        val = interpret(if_if_expr)
        self.assertEqual(val.n, 4)


if __name__ == '__main__':
    unittest.main()