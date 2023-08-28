
from lesson2 import People

class Student(People):  #дочерний класс
    # свойства - атрибут\переменная  уровня класса
    x='gen'

    def __init__(self, name, age, view): #  атрибут класса
        People.__init__(self, name, age)
        super().__init__(name, age)
        self.view = view

    # методы
    def eating_fastfood(self):
        print(self.name, 'eating')

    def print(self):
        print('aaaaaaaaaaaa')

# экземпляр класса
student1 = Student('beka', 20, 0)

# принципы ооп
# наследование полиморфизм инкапсуляция


# _ and _Class__
#MRO
#mro()
