# Inheritance in python is a fundamental object-oriented programming concept that allows a new class (called a child or subclass) to inherit attributes and methods from an existing class (called a parent or superclass). This promotes code reusability and establishes a natural hierarchical relationship between classes.

class employee:
    company = "ABC Corporation"
    def __init__(self,name,age,salary,designation):
        self.name = name
        self.age = age
        self.salary = salary
        self.designation = designation        
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Company: {self.company}, Designation: {self.designation}")
    

class manager(employee): # Here we are inheriting the employee class in manager class
    def __init__(self,name,age,salary,designation,department):
        super().__init__(name,age,salary,designation) # Here we are calling the constructor of the parent class using super() function to initialize the attributes of the parent class.
        # Beacuse we are inheriting the employee class in manager class so we can use the attributes of the employee class in manager class. And we are also adding new attribute department in manager class.And If we used the init method/constructor it will override the constructor of the parent class so we need to call the constructor of the parent class using super() function to initialize the attributes of the parent class.
        self.department = department
    def display_manager_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Company: {self.company}, Designation: {self.designation}, Department: {self.department}")
m1 = manager("Alice", 35, 80000, "Manager", "Sales")
m1.display_info() # This method is inherited from the employee class
m1.display_manager_info() # This method is defined in the manager class
