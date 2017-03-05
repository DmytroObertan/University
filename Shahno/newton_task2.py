from __future__ import division
from copy import deepcopy

class Newton(object):

    def __init__(self, n):
        self.n = n
        self.h = 0.3/(self.n + 1)
        self.A = [[0 for i in range(self.n + 2)] for j in range(self.n + 2)]
        self.A[0][0] = -1
        self.A[0][1] = 1
        self.A[self.n + 1][self.n] = 1
        self.A[self.n + 1][self.n + 1] = -1 - 2*self.h
        for i in range(1, self.n + 1):
            self.A[i][i] = 2
            self.A[i][i - 1] = -1 - 1.5*self.h
            self.A[i][i + 1] = -1 + 1.5*self.h
        self.X = [i*self.h for i in range(self.n + 2)]
        self.V = [0.1 for i in range(self.n + 2)]
        self.B = deepcopy(self.A)
        for i in range(1, self.n + 1):
            self.B[i][i] += -self.X[i]/self.V[i]**2

    def write(self):
        for i in range(self.n + 2):
            print self.A[i]
        print 'X = ' + str(self.X)

if __name__ == '__main__':
    n = int(raw_input('n = '))
    new = Newton(n)
    new.write()