from Visitor import visitor
from ast import Add, Sub, Mult, Div

class OpVisitor:
    @visitor(Add)
    def visit(self, op):
        return '+'

    @visitor(Sub)
    def visit(self, op):
        return '-'

    @visitor(Div)
    def visit(self, op):
        return '/'


    @visitor(Mult)
    def visit(self, op):
        return '*'

