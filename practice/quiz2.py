# Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.

from datetime import datetime

class Person:
    """This is a class to store persons details"""
    def __init__(self, name, country, dob) -> None:
        self.name = name
        self.country = country
        self.dob = datetime.strptime(dob, "%d/%m/%Y")

    def ageCalculator(self):
        today = datetime.today()

        years = today.year - self.dob.year

        if today.month < self.dob.month:
            years = years - 1
            return years
        
        elif today.month == self.dob.month and today.day < self.dob.day:
            years = years -1
            return years
        
        else:
            return years
        
# definitions

name = input("Enter your name: ")
country = input("Enter the country you are from: ")
dob = input("Enter your date of birth in the order dd/mm/year: ")


person = Person(name, country, dob)

print (person.ageCalculator())
