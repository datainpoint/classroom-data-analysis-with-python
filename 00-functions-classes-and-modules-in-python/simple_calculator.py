class SimpleCalculator:
    """
    This class creates a simple calculator that has 2 attributes and 1 method.
    """
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __repr__(self):
        out = "a: {}, b: {}".format(self.a, self.b)
        return out
    def add(self):
        out = self.a + self.b
        return out