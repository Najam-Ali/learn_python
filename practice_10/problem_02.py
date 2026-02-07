# Write a class "Calculater" capable of finding the square, cube, and square root of a number.

class Calculater:
    def __init__(self, num):
        self.num = num
    def square(self):
        print(f"The sqaure of given number is {self.num*self.num}")
    def cube(self):
        print(f"The cube of given number is {self.num*self.num*self.num}")
    def square_root(self):
        print(f"The square root of given number is {self.num**0.5}")
num = int(input("Enter a number: "))
calc = Calculater(num)
calc.cube()
# print(calc.square(),calc.cube(),calc.square_root())
