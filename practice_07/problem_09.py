# WAP to print the user definded number table in reverse order.

# num = int(input("Enter a number to print its table in reverse order: "))
# for i in range(10 ,0, -1):
#     print(f"{num} x {i} = {num * i}")

# Other Method
num = int(input("Enter a number to print its table in reverse order: "))
for i in range(1, 11):
    print(f"{num} x {11 - i} = {num * (11 - i)}")