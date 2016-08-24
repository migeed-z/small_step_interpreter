from Visitor import visitor
from ast import Add, Sub, Mult, Div
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

