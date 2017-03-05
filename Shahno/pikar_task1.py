from __future__ import division
from math import sqrt
from copy import deepcopy
import sys
n = 9


class Pikar(object):

    def __init__(self, n):
        self.eps = 0.000001
        self.n = n
        self.h = 1 / (self.n + 1)
        self.A = [[0 for x in range(n)] for y in range(n)]
        for i in range(n):
            for j in range(n):
                self.A[i][i] = 2
            try:
                self.A[i][i + 1] = -1
                self.A[i + 1][i] = -1
            except IndexError:
                pass
        self.X = [self.h + i * self.h for i in range(self.n )]
        self.V = [0.1 for x in range(self.n)]
        self.V1 = [0 for x in range(self.n)]

    def mult(self):
        return [- self.h ** 2 * h for h in self.H]

    def check(self):
        b = True
        for i in range(0,self.n):
            if(abs(self.V[i] - self.V1[i]) > self.eps):
                b = False
                break
        return b
    def seidel(self):
        self.k = 0
        while not self.check():
            self.k = self.k+1
            for i in range(0,self.n):
                self.V1[i] = self.V[i]
                self.H = [3*v + x**2 + 10*v**3 for v, x in zip(self.V, self.X)]
            converge = False
            while not converge:
                v_new = deepcopy(self.V)
                for i in range(self.n):
                    s1 = sum(self.A[i][j] * v_new[j] for j in range(i))
                    s2 = sum(self.A[i][j] * self.V[j] for j in range(i + 1, n))
                    v_new[i] = (self.mult()[i] - s1 - s2) / self.A[i][i]
                converge = (sqrt(sum((v_new[i] - self.V[i]) ** 2 for i in range(n)))) <= self.eps
                self.V = v_new
        return self.V, self.k

    def write(self):
        self.m = map(lambda x:round(x,4), self.V)
        if self.n == 99:
            for i in range(0, n + 2, 10):
                print str(self.X[i]) + '  ' + str(self.m[i])
        else:
            print 'X = ' + str(self.X)
            print 'V = ' + str(self.m)
        print 'Iter = ' + str(self.k)
        # print 'H = ' + str(self.H)
        # for i in range(self.n):
        #     print self.A[i]


pik = Pikar(n)
pik.seidel()
pik.write()
