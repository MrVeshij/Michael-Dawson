class Test1():
    def __init__(self,egg,spam):
        self.egg = egg
        self.spam = spam

    def print_text(self):
        print(self.egg, self.spam, sep='\n')

#t = Test1(12,'spam',(1,2,3))

class Test2(Test1):
    def __init__(self, a = None, b = None):
        Test1.__init__(self, a, b)


t2 = Test2(a = 1, b = 2)
t2.print_text()