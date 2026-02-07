# Add a atatic method in problem 2 to greet the user with "Hello"

class Calculater:
    def __init__(self, num):
        self.num = num
    def square(self):
        print(f"The sqaure of given number is {self.num*self.num}")
    def cube(self):
        print(f"The cube of given number is {self.num*self.num*self.num}")
    def square_root(self):
        print(f"The square root of given number is {self.num**0.5}")
    @staticmethod
    def greet():
        print("Hello")
num = int(input("Enter a number: "))
calc = Calculater(num)
calc.square()
calc.cube()
calc.square_root()
Calculater.greet() # Static method called using class name and not any relation with self method.
