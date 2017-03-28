class DiffiHellmann(object):

    def __init__(self, a, g, p, b):
        self._a = a
        self.g = g
        self.p = p
        self._b = b

    def first_to_second(self):
        return self.g ** self._a % self.p

    def second_to_first(self):
        return self.g ** self._a % self.p

    def _get_keys(self):
        if self.first_to_second()**self._b % self.p == self.second_to_first()**self._a % self.p:
            return True
        else:
            return False
