# WAP to find the sum of first n natural numbers using while loop
num = int(input("Enter a positive integer: "))
i = 0
sum = 0
while(i <= num):
    sum = sum + i
    i = i + 1
print("The sum of first n natural numbers is:", sum)
    