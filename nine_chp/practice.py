# Create a car with atribute like brand and model. Then create an instance of this class.
# class Car:
#     def __init__(self,brand,model):
#        self.__brand = brand
#        self.model = model
#     def get_brand(self):
#         return self.__brand + "!"
#     def get_info(self):
#         return f"Brand: {self.brand}, Model: {self.model}"
# class ElectricCar(Car):
#     def __init__(self,brand,model,battery):
#         super().__init__(brand,model)
#         self.battery = battery
# EC1 = ElectricCar("Tesla","Model S","100KWH")
# print(EC1.brand)
# print(EC1.get_brand())
# print(f"Battery: {EC1.battery}")

# => Encapsulation in python:

# Now we learn about the Encapsulation in python. Its like a capsule means which hide the data inside the capsule but capsule access for anyone but the data inside the capsule is hidden and we can access the data inside the capsule with the help of method like getter and setter method. And we can also use the property decorator to access the data inside the capsule without calling the method with parenthesis.Here we learn about it from above example:

# Modify the Car Class to Encapsulae the brand attribute,making is private and provide a getter method for it.

class Car:
    def __init__(self,brand,model):
       self.__brand = brand  # Private: No one can access directly
       self.model = model
    def get_brand(self):    # Get data by the get method
        return self.__brand + "!"
    # def get_info(self):
    #     return f"Brand: {self.brand}, Model: {self.model}"
class ElectricCar(Car):
    def __init__(self,brand,model,battery):
        super().__init__(brand,model)
        self.battery = battery
EC1 = ElectricCar("Tesla","Model S","100KWH")
# print(EC1.brand)
print(EC1.get_brand())

# Let take another example and learn the concept of getter & setter:


