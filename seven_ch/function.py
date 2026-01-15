
# def avg(): # Its the defination of the function.
#     sub1_mark = int (input ("Enter the marks of subject 1: "))
#     sub2_mark = int (input ("Enter the marks of subject 2: ")) 
#     sub3_mark = int (input ("Enter the marks of subject 3: "))
#     avg = (sub1_mark + sub2_mark + sub3_mark) / 3
#     print ("The average marks is: ", avg)
# avg() # Here we call the function.And we can call it multiple times.

# WAP a simple prgram greet a user with "Good Day" using function.
# def greet(): # Its the defination of the function.
#     print ("Good Day") # The body of the function.
# greet() 
# Here we call the function.And we can call it multiple times.

# Types of functions
      # => Built-in functions (Python make this type of functions like: print(), length(),rang()  etc.)
      # => User-defined functions (Developer make\write this type of functions)
# Function with arguments
# def greet_user(name): # Here name is the parameter.
#     print(f"Good Day, {name}")
# greet_user("Alice") # Here "Alice" is the argument.

# Function with return statement
# def add(a, b): # Here a and b are parameters.
#     result = a + b
#     return result
# sum = add(5, 10) # Here 5 and 10 are arguments.
# print(sum) 

# Default parameter value

# def greet_user(name, greeting = "Good Day"):  # Here i will not pass any value for greeting parameter so it will take the default value.
#     print(f"{greeting}, {name}")
# greet_user("Alice")
# greet_user("Bob", "Hello")  # Here i am passing a value for greeting parameter so it will take this value.

# Concept of recursion in function
# Recursion is a process in which a function calls itself directly or indirectly.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n *factorial(n-1)
# print(factorial(3))
n = int (input("Enter a number to find its factorial: "))
print(f"The factorial of {n} is {factorial(n)}") # It also work to print(factorial(5)) directly but in which user defined number.