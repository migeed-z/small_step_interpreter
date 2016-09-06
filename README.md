# Small_step_interpreter

An interpreter that evaluates a small language written in python syntax.


**Valid Syntax**
 - exp if test else orelse - If Expression
 - (lambda param: body)(arg) - Function Expression
 - lambda param: body - Lambda Expression
 - R - Number
 - True/ False - Boolean

**Expr**:
- Expr if Expr else Expr
- lambda: arg Expr (Expr)
- Token
- lambda: arg Expr
- Numerical Expr
- Constant

**Token**
A token is a sequence of characters. 

**Constant**
- True
- False

**Numerical Expr**
- num
- Numerical Expr OP Numerical Expr

**OP**
- +
- -
- *
- /

**Values**:
- Bool
- Num
- Lambda




