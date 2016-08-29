from Visitor import visitor
from ast import Add, Sub, Mult, Div, Eq, Gt, Lt, LtE
import operator

class OpVisitor:
    @visitor(Add)
    def visit(self, op):
        return operator.add

    @visitor(Sub)
    def visit(self, op):
        return operator.sub

    @visitor(Div)
    def visit(self, op):
        return operator.div


    @visitor(Mult)
    def visit(self, op):
        return operator.mul

    @visitor(Eq)
    def visit(self, op):
        return operator.eq

    @visitor(Lt)
    def visit(self, op):
        return operator.lt

    @visitor(Gt)
    def visit(self, op):
        return operator.gt

    @visitor(LtE)
    def visit(self, op):
        return operator.le