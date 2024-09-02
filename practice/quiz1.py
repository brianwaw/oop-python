# Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.

class Circle:

    pi = 3.14159265359

    def __init__(self,radius) -> None:
        self.radius = radius

    def perimeter(self):
        per = 2*(self.pi * self.radius)
        return per
    
    def area(self):
        Area = self.pi * self.radius * self.radius
        return Area


unclean_radius = input("Enter the radius: ")
# converting the string from input to float

radius = float(unclean_radius)

# Creating circle object

circle = Circle(radius)

circle.perimeter()

print (circle.perimeter())

print(circle.area())