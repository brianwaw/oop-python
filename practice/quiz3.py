# Write a Python program to create a calculator class. Include methods for basic arithmetic operations.
class Calculator:
    def add(self,*numbers):
        return sum(numbers)
    
    def multiplication(self, *numbers):
        product = 1
        for number in numbers:
            product = product * number

        return product
# i made a calculator webapp using django. check it out on:

calculator = Calculator()

print(calculator.add(1,2,3))
print(calculator.multiplication(1,2,3))