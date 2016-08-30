# def x(y):
#     if y:
#         return True
#     else:
#         return False
#
#
# if True:
#     5
# else:
#     6

(lambda f: (lambda x: x(x))(lambda y: f(lambda args: y(y)(args))))(lambda f: lambda n: 0 if n == 0 else (1 if n == 1 else f(n-1) + f(n-2)))(2)

Call(func=Call(func=Lambda(args=arguments(args=[arg(arg='f', annotation=None)], vararg=None, kwonlyargs=[], kw_defaults=[],
                                          kwarg=None, defaults=[]), body=Call(func=Lambda(args=arguments(args=[arg(arg='x', annotation=None)],
                                         vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=Call(func=Name(id='x', ctx=Load()), args=[Name(id='x', ctx=Load())], keywords=[], starargs=None, kwargs=None)), args=[Lambda(args=arguments(args=[arg(arg='y', annotation=None)], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=Call(func=Name(id='f', ctx=Load()), args=[Lambda(args=arguments(args=[arg(arg='args', annotation=None)], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=Call(func=Call(func=Name(id='y', ctx=Load()), args=[Name(id='y', ctx=Load())], keywords=[], starargs=None, kwargs=None), args=[Name(id='args', ctx=Load())], keywords=[], starargs=None, kwargs=None))], keywords=[], starargs=None, kwargs=None))], keywords=[], starargs=None, kwargs=None)), args=[Lambda(args=arguments(args=[arg(arg='f', annotation=None)], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=Lambda(args=arguments(args=[arg(arg='n', annotation=None)], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=IfExp(test=Compare(left=Name(id='n', ctx=Load()), ops=[Eq()], comparators=[Num(n=0)]), body=Num(n=0), orelse=IfExp(test=Compare(left=Name(id='n', ctx=Load()), ops=[Eq()], comparators=[Num(n=1)]), body=Num(n=1), orelse=BinOp(left=Call(func=Name(id='f', ctx=Load()), args=[BinOp(left=Name(id='n', ctx=Load()), op=Sub(), right=Num(n=1))], keywords=[], starargs=None, kwargs=None), op=Add(), right=Call(func=Name(id='f', ctx=Load()), args=[BinOp(left=Name(id='n', ctx=Load()), op=Sub(), right=Num(n=2))], keywords=[], starargs=None, kwargs=None))))))], keywords=[], starargs=None, kwargs=None), args=[Num(n=2)], keywords=[], starargs=None, kwargs=None)
