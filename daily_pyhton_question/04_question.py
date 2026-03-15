# Print the user input number and the sum of all numbers from 1 to that number.
user_input = int(input("Enter your number:"))
for i in range(1, user_input):
    user_input += i
    result = user_input
print(result)

# Other way to do the same thing: 

# User se number input lo
user_input = int(input("Enter a number: "))

# Sum store karne ke liye alag variable
total = 0

# # Loop 1 se user_input tak
for i in range(1, user_input + 1):
    total += i  #     total = total + i
# Final sum print karo
print(f"The sum of numbers from 1 to {user_input} is: {total}")
