# Here in this chp we will discuss how a user wanted value input in a python program.

# a = input("Enter your name: ")
# print("Hello, " + a + "!"), # The out is (Hello, Your name!) why is it because the + operator concatinate the the string and the variable together.An other exapmle to see something differents

# a = input("Enter your first number: ") # This will ask the user to enter a number like first input num,
# b = input("Enter your second number: ") # This will ask the user to enter a number like second input num.
# print(type(a)) # That is use for the type of the variable and verification
# print(type(b)) # That is use for the type of the variable and verification
# print("The sum of your two numbers is: ", a + b) # The out is (e.g: 1+2 = 12) its due to a + b is a string operation not a math operation and it concatinate the both number.

# To solve this problem we can use int() function to convert the input to integer and then we can do the math operation.

a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
print("The sum of your two numbers is: ", a + b) # This output is gives you the sum of the two number.
# print ("The sum of your two numbers is: ", int(a) + int(b)) Its an other way write if you want to convert the input to integer that are already string.Mean both operation perform in one line like conversion and sum operaton.
