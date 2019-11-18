class Threadingclass(object):

    def longFunction(self, a, b):
        for i in range (10000000):
            a = a + b
            print(a)
