from functools import wraps
from abc import ABCMeta, abstractmethod


class Base():
    def foo(self):
        print 'foo'

class Base1():
    @staticmethod
    def foo1():
        print 'foo1'

class Papa(Base, Base1):

    pass
if __name__ == '__main__':
    l = Papa()
    l.foo()
    l.foo1()




# class Meta(type):


#     def __new__(cls, class_name, bases, dct):
#         uppr = {}
#         for key in dct:
#             if not key.startswith('__'):
#                 uppr[key.upper()] = dct[key].upper()
#             else:
#                 uppr[key] = dct[key]
#         cls.add = 'kaka'

#         return type.__new__(cls, class_name, bases, uppr)


# class Pups(object):

#     __metaclass__ = Meta

#     foo = 'foo'


# def dec(func):
#     @wraps(func)
#     def wrap(*args):
#         num = args
#         return str(func(num)) + ' lal'
#     return wrap


# @dec
# def get_num(x):
#     return x



# def fib(n):
#     a, b = 0, 1
#     for k in range(n):
#         # while a < n:
#         b, a = a, a + b
#         yield b

# if __name__ == '__main__':
#     k = lambda n: n**2
#     print map(k, range(10))

