from math import pi, sqrt
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        self.radius = radius

    def area(self):
        return pi * self.radius**2

class Triangle(Shape):
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Стороны должны быть положительным числом")
        if a >= c + b or b >= a + c or c >= a + b:
            raise ValueError("Треугольник не существует. Одна сторона больше сумму других")
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        half_p = (self.a+self.b+self.c)/2
        return sqrt(half_p*(half_p-self.a)*(half_p-self.b)*(half_p-self.c))

    def is_rectangular(self):
        if self.a**2 == self.b**2 + self.c**2 or self.b**2 == self.a**2 + self.c**2 or self.c**2 == self.b**2 + self.a**2:
            return True
        else: return False
