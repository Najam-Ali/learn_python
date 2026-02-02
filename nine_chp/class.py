# I pracice about the classes in python.
# I learn about the class is the blueprint of diffrent obj and with the help of classes we can create an multiple objects.

class Employee:
    name = "John"
    age = 30
    salary = 50000
    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {Employee.salary}"

    @staticmethod # This is static method which is not dependent on the object of the class.Means no reference of self is required and not any realation with object.
    def greet():
        print("Its my static method.")

emp1 = Employee()
print( emp1.get_info() )
print( Employee.greet() )
# print( emp1.name, emp1.age, emp1.salary )
# emp2 = Employee()
# emp2.name = "Doe"
# print( emp2.name, emp2.age, emp2.salary )
