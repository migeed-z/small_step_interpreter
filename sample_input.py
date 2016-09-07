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

y = lambda x: x
y(3)


[Assign(targets=[Name(id='y', ctx=Store())], value=Lambda(args=arguments(args=[arg(arg='x', annotation=None)],
vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=Name(id='x', ctx=Load()))),

 Expr(value=Call(func=Name(id='y', ctx=Load()), args=[Num(n=3)], keywords=[], starargs=None, kwargs=None))]


