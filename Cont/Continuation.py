class Continuation:
    def __init__(self, control, env, cont):
        """
        :param control: expr
        :param env: Scope
        :param k: Continuation
        :return:
        """
        self.control = control
        self.env = env
        self.cont = cont




