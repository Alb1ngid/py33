# инкапсуляция



# 1 капсула
# 2 уровни защиты
# 3 публичный,приватный,скрытый

class Bank:
    def __init__(self, name, age, money, password):
        self.name = name
        self.age = age
        self._money = money
        self.__passw = password

    def setpass(self, n):
        if len(self.__passw) < 10:
            print('слишком маленький ')
        else:
            self.__passw = n

    def getpass(self):
        print(self.__passw)

    def pname(self):
        print(self.name, self._money)

    def __ppas(self):
        print(self.__passw)

    def pasww(self):
        self.__ppas()


beka = Bank('бека', 20, 0, '12345678987543')
beka.getpass()
beka.setpass('qwerdwvfsd')
beka.getpass()

# beka._money = 123456789
#
# print(beka._money)
# beka.pname()
#
# beka.__passw = '0'
# print(beka.__passw)
# beka._Bank__passw = '23'
# beka.pasww()
# beka.pasww()
print(dir(beka))
