# WAP using a funcion to find the greatest 3 numbers.
def greatest_of_three(a, b, c):
    if a > b and a > c:
        return f"{a} is the greatest number"
    elif b > a and b > c:
        return f"{b} is the greatest number"
    else:
        return f"{c} is the greatest number"

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

result = greatest_of_three(a, b, c)
print(result)

# Other way to resolve this problem help of AI.
def greatest_of_three(a, b, c):
    return max(a, b, c) # Here we use the built-in max() function to find the greatest number among the three.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print(greatest_of_three(a, b, c))

# If i want user put the number and program find the greatest number among them.

def greatest_of_three(a, b, c):
    return max(a, b, c)

while True:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))

    print(greatest_of_three(a, b, c))

    choice = input("Again? (y/n): ")
    if choice == 'n':
        break
