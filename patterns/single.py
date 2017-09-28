class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        import pdb
        pdb.set_trace()
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MyClass(object):

    def __init__(self, value):
        self.value = value

    __metaclass__ = Singleton


if __name__ == '__main__':
    cls1 = MyClass('test')
    print str(cls1) + cls1.value
    cls1 = MyClass('another_test')
    print str(cls1) + cls1.value