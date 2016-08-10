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

    def test_call(self):
        call_expr = ast.Module(body=[Expr(value=Call(
            func=Lambda(args=ast.arguments(args=[ast.arg(arg='x')]), body=Name(id='x')), args=[Num(n=3)]))])
        val = interpret(call_expr)
        self.assertEqual(val.n, 3)


if __name__ == '__main__':
    unittest.main()