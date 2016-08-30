(lambda f: (lambda x: x(x))(lambda y: f(lambda args: y(y)(args))))(lambda z: lambda n: 0 if n == 0 else (1 if n == 1 else z(n-1) + z(n-2)))(7)
