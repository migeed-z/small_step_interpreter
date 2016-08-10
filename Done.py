from Continuation import Continuation

class Done(Continuation):
    pass


    def __eq__(self, other):
        return isinstance(other, Done)