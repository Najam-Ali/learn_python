# While loop(Condition-based)
# i = 1
# while( i<=5 ):
#     print(i)
#     if i == 3:
#         break   # With the break statement we can stop the loop even if the while condition is true
#     i += 1 

# i = 0
# while( i<5 ):
#     i += 1 
#     if i == 3:
#         continue # With the continue statement we can stop the current iteration, and continue with the next and skip the number that is matched with the condition.
#     print(i)   
# else:
#     print("i is no longer less than 5")

# i = 1
# while (i <= 5):
#     print(i) 
#     i += 1
                        # <--while Loop practice -->
        # <Example 1: Print numbers from 1 to 100>
# num = 1
# while num <= 100:
#     print(num)
#     num += 1

        # <Example 2: Print numbers from 100 to 1>                       
# num = 100
# while num >= 1:
#     print(num)
#     num -= 1
        # <Example 3: Print table of a number entered by user>
# num = int(input("Enter your number: "))
# i = 1
# while i <= 10:
#     print(f"{num} x {i} = {num * i}") # Formatted string literals means f-strings like a f"string {var}" use veriable inside string.
#     i += 1

        # <Example 4: Print all elements of a list using while loop>

# li = [1,4,9,16,25,36,49,64,81,100]
# i = 0
# while i < len(li):
#     print(li[i])
#     i += 1

        # <Example 5: Search for an element in a tuple using while loop>
# tup = (1,4,9,16,25,36,49,64,81,100)
# x = int(input("Enter a number: "))
# i = 0
# found = False
# while i < len(tup):
#     if tup[i] == x:
#         found = True
#         print(f"{x} is found at index {i}")
#         break
#     else:
#         found = False
#         print(f"{x} is not found at index {i}")
#     i += 1
# if not found:
#     print(f"{x} is not found in the tuple")

        # <Example 6: Calculate the factorial of a number using while loop>
# num = int(input("Enter a number: "))
# factorial = 1
# i = 1
# while i <= num:
#     factorial *= i
#     i += 1
# print(f"The factorial of {num} is {factorial}")

        # Concept of continue statement in while loop
# i = 0
# while i < 10:
#     i += 1
#     if i % 2 == 0:
#         continue
#     print(i) # This will print only odd numbers from 1 to 9 and skip even numbers.  
#     
                                                # Concept of for loop
# for i in range(5):  # range(5) means 0 to 4   
#     print(i)


# str = "Hello my friend."
# for new_str in str:
#     if(new_str == ' '):
#         continue
#     print(new_str)

                     # Print the elemets of a list using for loop
# li = [1,4,9,16,25,36,49,64,81,100]
# for i in li:
#     print(i)

#                          # Search for an element in a tuple using for loop
# tup = (1,4,9,16,25,36,49,64,81,100)
# num = int(input("Enter a number: "))
# for i in tup:
#     if i == num:
#         print(f"{num} is found in the tuple")
#     else:
#         print(f"{num} is not found in the tuple")
                                # Range function in for loop
# for i in range(1, 11,2):  # range(start, stop) or a step size can be added as range(start, stop, step) but the step size is optional.
#     print(i)

                         # Print number from 1 to 100 use for and range()
# for num in range(1, 101):
#     print(num)
                        # Print number from 100 to 1 use for and range()
# for num in range(100, 0, -1):
#     print(num)
                        # Print table of a number entered by user use for and range()
# num = int(input("Enter your number: "))
# for table in range(1, 11):
#     print(f"{num} x {table} = {num * table}")

                        # Concept of the pass statement in loops
# Use the pass statement when a statement is required syntactically but you do not want any command or code to execute.

# for i in range(5):
#     pass  # Placeholder for future code

