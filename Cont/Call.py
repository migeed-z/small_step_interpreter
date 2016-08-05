from Cont.Continuation import Continuation

class Call(Continuation):
    def __init__(self, control, env, cont):
        super(Call, self).__init__(control, env, cont)

