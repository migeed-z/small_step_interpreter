from abc import abstractclassmethod

class Continuation:

    def __init__(self):
        pass

    def apply(self, val, scope):
        """
        Evaluate term under env.
        :param scope the current Scope
        :param val thing that's supposed to be in the hole
        :return: Config
        """
        pass





