# множественное наследование
# MRO - method resolution order порядок выполнения методов

class A:
    def __init__(self, a):
        self.a = a

    def c(self):
        print(self,'это метод А')


class A2(A):
    def c(self):
        print(self,'это метод А2')



class C:
    def __init__(self, с):
        self.с = с

    def c1(self):
        print(self,'это метод C')



class B(A2,C,A):
    def __init__(self,a,c):
        A.__init__(self,a)
        C.__init__(self,c)




b=B('a','c')
b.c()
print(B.mro())