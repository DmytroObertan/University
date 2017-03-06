from __future__ import division
from copy import deepcopy

class Newton(object):

    def __init__(self, n):
        self.n = n
        self.h = 0.3/(self.n + 1)
        self.A = [[0 for i in range(self.n + 2)] for j in range(self.n + 2)]
        self.A[0][0] = 1
        self.A[0][1] = -1
        self.A[self.n + 1][self.n] = 1/-1 - 2 * self.h
        self.A[self.n + 1][self.n + 1] = -1 - 2 * self.h
        for i in range(1, self.n + 1):
            self.A[i][i] = 2
            self.A[i][i - 1] = -1 - 1.5*self.h
            self.A[i][i + 1] = -1 + 1.5*self.h
        self.X = [1.2 + i*self.h for i in range(self.n + 2)]
        self.V = [0.1 for i in range(self.n + 2)]
        self.V1 = [0 for i in range(self.n + 2)]
        self.H = [0 for i in range(self.n + 2)]

    def check(self):
        b = True
        for i in range(0,self.n):
            if(abs(self.V[i] - self.V1[i]) > self.eps):
                b = False
                break
        return b

    def newton(self):
        while self.check():
            matrix = deepcopy(self.A)
            for i in range(1, self.n + 1):
                matrix += self.h**2*(-self.X[i]/self.V[i]**2)
            for i in range(self.n + 2):
                sum = 0
                for j in range(self.n + 2):
                    sum += self.A[i][j] * self.V[j]
                if i == 0:
                    self.H[i] = - sum - self.h
                elif i == self.n + 1:
                    self.H[i] = - sum - 0.5*self.h
                else:
                    self.H[i] = -(sum + self.h**2*(self.X[i] + 1 + self.X[i] / self.V[i]))

    def progonka(self):
        pass

    def write(self):
        for i in range(self.n + 2):
            print self.A[i]
        print 'X = ' + str(self.X)

if __name__ == '__main__':
    n = int(raw_input('n = '))
    new = Newton(n)
    new.write()