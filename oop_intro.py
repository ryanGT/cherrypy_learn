class myclass(object):
    def __init__(self, a, b=7):
        print('calling myclass.__init__')
        self.a = a
        self.b = b


    def calc_c(self):
        print('in myclass.calc_c')
        self.c = self.a + self.b
        return self.c


    def calc_d(self):
        print('in myclass.calc_d')
        self.d = self.a * self.b
        return self.d
    

class derived_class(myclass):
    def __init__(self, a, b=10):
        print('calling derived_class.__init__')
        myclass.__init__(self, a, b=b)


    def calc_d(self):
        print('in derived_class.calc_d')
        self.d = float(self.a) / float(self.b)
        return self.d



jeff = myclass(3,8)
jeff.calc_c()
jeff.calc_d()
print('='*20)
bob = derived_class(4)
bob.calc_c()
bob.calc_d()
