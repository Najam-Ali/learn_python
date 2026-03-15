# Print the sum of Even numbers from 1 to a user input number.

def is_even( number):
    total = 0
    for i in range(1, number + 1):
        if i % 2 == 0:
            print(f"{i} is even")
            total += i 
    print(f"The Sum of the given number is = {total} ")
number = int(input("Enter a number: "))
is_even( number)