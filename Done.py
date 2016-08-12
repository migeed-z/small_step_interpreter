from Continuation import Continuation

class Done(Continuation):
    pass


    def __eq__(self, other, scope):
        return isinstance(other, Done)