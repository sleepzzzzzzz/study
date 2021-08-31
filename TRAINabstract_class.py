'''Создать абстрактный класс BaseFigure и унаследовать от него классы Square и Triangle.
Сделать так, чтобы дочерние классы должны были создать у себя методы get_square()
(посчитать площадь) и get_perimeter (посчитать периметр)'''
from abc import ABC, abstractmethod


class BaseFigure(ABC):
    # общий метод, который будут использовать все наследники этого класса
    def print_hello(self):
        print("Hello!")

    # абстрактный метод, который будет необходимо переопределять для каждого подкласса
    @abstractmethod
    def get_square(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass


class Square(BaseFigure):
    def __init__(self, side):
        self.side = side


    def get_square(self):
           # pass
        print(f'у квадрата со стороной {self.side} площадь равна {self.side**2} ')

    def get_perimeter(self):
       # pass
        print(f'у квадрата со стороной {self.side} площадь равна {self.side *4} ')



class Triangle(BaseFigure):
    def __init__(self, side):
        self.side = side


    def get_square(self):
           # pass
        print(f'у правильного треугольника со стороной {self.side} площадь равна {self.side**2*3**0.5/4} ')

    def get_perimeter(self):
       # pass
        print(f'у правильного треугольника со стороной {self.side} площадь равна {self.side *3} ')

sq = Square(4)
tr = Triangle(3)
sq.get_square()
sq.get_perimeter()
tr.get_square()
tr.get_perimeter()