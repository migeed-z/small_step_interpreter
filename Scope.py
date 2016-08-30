import ast

class Scope:
    """
    To represent the definitions as a tuple T, where t[0] is a key, t[1] is a value and t[2] is
    the old scope
    """

    def __init__(self, defs):
        """
        Initialises the scope from a tuple with three elements
        :param defs: Tuple containing three elements. If no definitions exist, we may use an empty tuple
        """
        self.defs = defs

    def extend(self, name, val):
        """
        Expends this Scope with name and val
        :param name: String
        :param val: Value corresponding to name
        :return: New scope with extended definitions
        """
        if not isinstance(name, str) :
            raise BSLError('name field must be a string')
        return Scope((name, val, self))

    def get(self, key):
        """
        Gets the first value having key
        :param key: String
        :return: Val U None
        """
        if self.defs:
            name = self.defs[0]
            # print("key & name %s %s" % (key, name))
            val = self.defs[1]
            old_self = self.defs[2]
            if key == name:
                return val
            else:
                return old_self.get(key)

    def __eq__(self, other):
        return isinstance(other, Scope) and self.defs == other.defs


