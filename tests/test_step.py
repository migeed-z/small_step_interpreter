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
        self.assert_(isinstance(val, Closure))
        expr = val.lambda_expr
        self.assertEqual(expr.args.args[0].arg, 'x')
        self.assertEqual(expr.body.n, 3)

    def test_call(self):
        call_expr = ast.Expr(value=Call(func=Lambda(args=ast.arguments(args=[ast.arg(arg='x')]), body=Name(id='x')), args=[Num(n=3)]))
        env = Scope([])
        k = Done()
        val = step(call_expr, env, k)[0]
        earg = step(call_expr, env, k)[2]
        self.assertEqual(val.args.args[0].arg, 'x')
        self.assertEqual(val.body.id, 'x')
        self.assert_(isinstance(earg, Earg))
        self.assertEqual(earg.expr.n, 3)

    def test_if(self):
        if_expr = ast.Expr(value=IfExp(test=Num(n=2), body=Num(n=1), orelse=Num(n=3)))
        env = Scope([])
        k = Done()
        val = step(if_expr, env, k)[0]
        eif = step(if_expr, env, k)[2]
        self.assert_(isinstance(eif, Eif))
        self.assertEqual(val.value.n, 2)
        self.assertEqual(eif.then.value.n, 1)
        self.assertEqual(eif.el.value.n, 3)

    def test_earg_apply(self):
        lamb_expr = ast.Expr(value=Lambda(args=ast.arguments(args=[ast.arg(arg='x')]), body=Name(id='x')))
        env = Scope([])
        earg = Earg(ast.Expr(value=Num(n=3)), env, Done())
        val = step(lamb_expr, env, earg)[0]
        cont = step(lamb_expr, env, earg)[2]
        self.assertEqual(val.value.n, 3)
        self.assert_(isinstance(cont, Ecall))
        self.assert_(isinstance(cont.k, Done))

    def test_ecall_apply(self):
        num_expr = ast.Expr(value=Num(n=3))
        env = Scope([])
        k = Ecall(ast.Expr(value=Lambda(args=ast.arguments(args=[ast.arg(arg='x')]), body=Name(id='x'))), env, Done())
        scope = step(num_expr, env, k)[1]
        self.assertEqual(scope.get('x').n, 3)


if __name__ == '__main__':
    unittest.main()