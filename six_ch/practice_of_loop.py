# WAP to find the sum of "n" natural numbers using while loop

# n = int(input("Enter a number: "))
# sum = 0
# i = 1

# while i <= n:
#     sum = sum + i
#     i = i + 1
# print("Sum of first", n, "natural numbers is:", sum)

# This above program also write with for loop
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n+1):
    sum = sum + i
print("Sum of first", n, "natural numbers is:", sum)


# WAP to find the factorial of a number using for loop
num = int(input("Enter a number: "))
factorial = 1
i = 1
for i in range(1,num+1):
    factorial *= i
print(f"The factorial of {num} is {factorial}")
