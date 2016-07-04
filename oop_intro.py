class myclass(object):
    def __init__(self, a, b=7):
        self.a = a
        self.b = b


    def calc_c(self):
        self.c = self.a + self.b
        return self.c


    def calc_d(self):
        self.d = self.a * self.b
        return self.d
    

class derived_class(myobject):
    def __init__(self, a, b=10):
        myobject.__init__(self, a, b=b)


    def calc_d(self):
        self.d = float(self.a) / float(self.b)
        return self.d



jeff = myclass(3,8)
bob = derived_class(4)
