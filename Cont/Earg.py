from Cont.Continuation import Continuation

class Earg(Continuation):
    def __init__(self, control, env, cont):
        super(Earg, self).__init__(control, env, cont)
        
        