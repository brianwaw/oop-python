# Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square.

from abc import ABC, abstractmethod

class Shape(ABC):
    """The main class defining the methods to be availed in each class"""

    pi = 3.142

    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width


    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width

    def area(self):
        return (self.length * self.width)
    
    def perimeter(self):
        return  ((self.length + self.width) * 2 )
    
class Circle(Shape):
    def __init__(self, radius) -> None:
        self.radius = radius

    def area(self):
        return (self.pi * self.radius ** 2)
    
    def perimeter(self):
        return (self.radius * self.pi * 2)
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return (0.5 * self.base * self.height)
    
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return (self.side ** 2)
    
    def perimeter(self):
        return (self.side * 4)
    


square = Square(7)
print(square.area())