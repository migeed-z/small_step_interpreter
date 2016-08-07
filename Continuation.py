from abc import abstractclassmethod

class Continuation(list):
    def __init__(self, k):
        super().__init__(k)

    def apply(self, val):
        """
        Evaluate term under env.
        :param env the current env
        :param val thing that's supposed to be in the hole
        :return: Config
        """
        pass





