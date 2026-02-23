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
    total_car = 0 # vriable in Class method
    def __init__(self,brand,model):
       self.__brand = brand  # Private: No one can access directly
       self.__model = model
       Car.total_car +=1
    def get_brand(self):    # Get data by the get method
        return self.__brand + "!"
    def fuel_type(self): # Here are the example of the Polymorphism
        return f"The fuel_type is Petrol or Desil."
    # def get_info(self):
    #     return f"Brand: {self.brand}, Model: {self.model}"

    @property # Its use for read only veriable,no change allowed
    def get_model(self):
        return self.__model

    @staticmethod 
    def general_discription():
        return f"Car use for Trasportional perpose."
class ElectricCar(Car):
    def __init__(self,brand,model,battery):
        super().__init__(brand,model)
        self.battery = battery
    def fuel_type(self): #  Here are the example of the Polymorphism
        return f"The fuel type is Electric Charge." 

EC1 = ElectricCar("Tesla","Model S","100KWH")
# # print(EC1.brand)
# print(EC1.fuel_type())
# C2 = Car("Tata","Safari")
# print(C2.fuel_type())
# print(Car.total_car)
# print(Car.general_discription()) # Printed as a class attribiute
# print(EC1.get_model) # Print for result of the property decorator

# Here We learn the POLYMORPHISM in python.
    # Some have multiple faces but different in behaivour.
    # Let take example in which Demonstrate polymorphism by defining a method fuel type in both Car and Electric car Class but with diffrent behaviors.

# Let take another example and learn the concept of getter & setter:

# class ATM:
#     def __init__(self, balance, pin):
#         self.set_balance(balance)   # setter use in constructor
#         self.set_pin(pin)
#         self.__attempts = 0
#         self.__blocked = False

#     # -----------------------
#     # Balance Getter
#     # -----------------------
#     def get_balance(self):
#         return self.__balance

#     # -----------------------
#     # Balance Setter
#     # -----------------------
#     def set_balance(self, balance):
#         if balance >= 0:
#             self.__balance = balance
#         else:
#             print("Balance cannot be negative.")
#             self.__balance = 0

#     # -----------------------
#     # PIN Setter
#     # -----------------------
#     def set_pin(self, pin):
#         if len(str(pin)) == 4:
#             self.__pin = pin
#         else:
#             print("PIN must be 4 digits.")
#             self.__pin = 0000

#     # -----------------------
#     # Private PIN Verification
#     # -----------------------
#     def __verify_pin(self, entered_pin):
#         if self.__blocked:
#             print("Account is blocked.")
#             return False

#         if entered_pin == self.__pin:
#             self.__attempts = 0
#             return True
#         else:
#             self.__attempts += 1
#             print("Wrong PIN.")

#             if self.__attempts >= 3:
#                 self.__blocked = True
#                 print("Account Blocked!")

#             return False

#     # -----------------------
#     # Public Methods
#     # -----------------------
#     def check_balance(self, entered_pin):
#         if self.__verify_pin(entered_pin):
#             print("Balance:", self.get_balance())

#     def deposit(self, amount):
#         if not self.__blocked:
#             if amount > 0:
#                 new_balance = self.get_balance() + amount
#                 self.set_balance(new_balance)
#                 print("Deposit successful.")
#             else:
#                 print("Invalid amount.")

#     def withdraw(self, amount, entered_pin):
#         if self.__verify_pin(entered_pin):
#             if amount <= self.get_balance():
#                 new_balance = self.get_balance() - amount
#                 self.set_balance(new_balance)
#                 print("Withdraw successful.")
#             else:
#                 print("Insufficient balance.")

        
    

#     # def check_balance(self, entered_pin):
#     #     if str(entered_pin) == self.__pin:
#     #         print(f"Balance: {self.__balance}")
#     #     else:
#     #         print("Incorrect PIN.")

# cust_1 = ATM(50000, 1234)
# # cust_1.check_balance(1234)
# cust_1.deposit(4000)
# cust_1.check_balance(1234)
# cust_1.check_balance(1234)
  