# Here are some more things about the inheritance in python:
# 1. Types of Inheritance:
#    a. Single Inheritance: A child class inherits from a single parent class.Let's take an example of single inheritance:
# class parent:
#     def parent_method(self):
#         print("This is a method in the parent class.")
# class child(parent): # Here we are inheriting the parent class in child class
#     def child_method(self):
#         print("This is a method in the child class.")
# c1 = child()
# c1.child_method() # This method is inherited from the parent class

#    b. Multiple Inheritance: A child class inherits from multiple parent classes.Let's take an example of multiple inheritance:
# class father:
#     def father_skills(self):
#         print("Father has skills in Driving.")
# class mother:
#     def mother_skills(self):
#         print("Mother has skills in Cooking.")
# class child(father, mother): # Here we are inheriting the father and mother class in child class
#     def child_skills(self):
#         print("Child has skills in Programming.")
# c = child()
# c.father_skills() # This method is inherited from the father class
# c.mother_skills() # This method is inherited from the mother class
# c.child_skills() # This method is defined in the child class

# Multilevel Inheritance: A child class inherits from a parent class, and then another child class inherits from that child class.Let's take an example of multilevel inheritance:
# grandfather => father => child

# class grandfather:
#     def grandfather_method(self):
#         print("This is a method in the grandfather class.")
# class father(grandfather): # Here we are inheriting the grandfather class in father class
#     def father_method(self):
#         print("This is a method in the father class.")
# class child(father): # Here we are inheriting the father class in child class
#     def child_method(self):
#         print("This is a method in the child class.")
# c = child()
# c.grandfather_method() # This method is inherited from the grandfather class
# c.father_method() # This method is inherited from the father class

# Hierarchical Inheritance: Multiple child classes inherit from a single parent class.Let's take an example of hierarchical inheritance:
# class parent:
#     def parent_method(self):
#        return "This is a method in the parent class."
# class child1(parent): # Here we are inheriting the parent class in child1 class
#     def child1_method(self):
#         print("This is a method in the child1 class.")
# class child2(parent): # Here we are inheriting the parent class in child2 class
#     def child2_method(self):
#         print("This is a method in the child2 class.")
# c1 = child1()
# c2 = child2()
# # c1.parent_method() # This method is inherited from the parent class
# print(f"Inherent the propertities of the parent class inside the child2 output: {c2.parent_method()}") # This method is defined in the child1 class

# => Concept of the super function in python:

# class parent:
#    def __init__(self,name):
#       self.name = name
#    def parent_name(self):
#       print(f"The name of parent is: {self.name}")
# class child1(parent):
#    def __init__(self,child_name):
#       super().__init__(child_name) # Here we are calling the constructor of the parent class using super() function to initialize the attributes of the parent class. And we are also adding new attribute child_name in child1 class.And If we used the init method/constructor it will override the constructor of the parent class so we need to call the constructor of the parent class using super() function to initialize the attributes of the parent class.
#       self.child_name = child_name
#    def display(self):
#       print(f"The name of the class is: {self.child_name}")
#       print(f"The name of the class is: {self.name}")
# c = child1("Alice")
# c.parent_name()


# => Concept of the Class method:
# Directly Access the class method with attribute of the class without creating an object of the class.

# class employee:
#     company_name = "ABC Prv.Limited"
#     def __init__(self, name, age, salary, designation):
#         self.name = name
#         self.age = age
#         self.salary = salary
#         self.designation = designation
#     def display_info(self):
#         return f"The employee {self.name}, {self.age} year old that salary is {self.salary}, and the working designation in this company is {self.designation}"
#     @classmethod
#     def get_company_name(cls):
# 	    return f"The company name in which they are working is: {cls.company_name}"
# # print(employee.get_company_name())
# emp = employee("Alice", 30, 50000, "Software Engineer")
# print(emp.display_info())
# emp.company_name = "XYZ Pvt.Limited"    
# print(employee.get_company_name()) # This will print the updated company name because we are accessing the class method with the class name and we are also updating the company name using the object of the class. So when we access the class method it will print the updated company name.


# => Concept of the property decorator in python:
# This method is used as for use the method as an attribute without calling the method with parenthesis.

class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age= age
        self.salary = salary
    @property
    def display_info(self):
        return f"The employee {self.name}, {self.age} year old that salary is {self.salary}"
emp1 = Employee("Alice", 30, 50000)
# print(emp1.display_info()) # This is the normal way to call the method with parenthesis
print(emp1.display_info) # This is the way to call the method with property decorator without parenthesis. And we can also use this method as an attribute without calling the method with parenthesis. So we can access the method as an attribute without calling the method with parenthesis.