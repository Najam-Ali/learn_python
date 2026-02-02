# Here we learn about constructors in Python classes 
class Person:
    # name = "John"
    # age = 30 
    # city = "New York" # We remove these attributes to use constructor and noe we will initialize these attributes using constructor. Because not every time every object will have same attributes values.
    def __init__(self, name, age, city): # Its also called dunder method that call automatically when we create an object of the class.
        self.name = name
        self.age = age
        self.city = city
        # print("i am constructor method.")
    # def __str__(self):
        # return f"Name: {self.name}, Age: {self.age}, City: {self.city}"
    
    # Here are the method to get the details of the person.
    def get_details(self):
        print(f"Name: {self.name}, Age: {self.age}, City: {self.city}")
p1 = Person("Alice", 25, "Los Angeles")
p2 = Person("Bob", 28, "Chicago")
# print(p1)
# print(p2)
p1.get_details()
p2.get_details()