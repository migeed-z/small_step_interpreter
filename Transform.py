from ast import Expr, Assign

def transform(ast_list):
    """
    Transforms an AST list into a single expression
    :param ast_list: List of AST
    :return: List of AST
    """
    res_exprs = []
    for ast in ast_list:
        res_exprs.append(transform_expr(ast))

    return res_exprs


def transform_expr(ast):
    """
    Transforms a single ast expression
    :param ast: AST
    :return: AST
    """
    if isinstance(ast, Expr):
        ast.value = transform_expr(ast.value)
        return ast
    elif isinstance(ast, Assign):
        return Expr(value=ast)
    else:
        return ast