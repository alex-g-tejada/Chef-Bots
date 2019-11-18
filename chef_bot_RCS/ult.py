class Threadingclass(object):

    def longFunction(self, a, b):
        for i in range (10000000):
            a = a + b
            print(a)


        '''# Multithreading code
        This is just for the multithreading portion

        classObject = Threadingclass()
        t = Thread(target=classObject.nameoffunctionhere, args=(2, 6))
        # set daemon to true so the thread dies when app is closed
        t.daemon = True
        # start the thread
        t.start()
        '''