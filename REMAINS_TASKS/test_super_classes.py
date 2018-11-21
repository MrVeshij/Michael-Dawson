class Test1():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        print(a,b,c,sep='\n')

#t = Test1(12,'spam',(1,2,3))

class Test2(Test1):
    def __init__(self):
        super().__init__(12,13,14)


t2 = Test2(1,2,3)