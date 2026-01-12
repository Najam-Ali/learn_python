# write a program to find a given number  is prime or not?

num = int(input("Enter a number: "))
if num <= 1:
    print("The number is not prime")
else: 
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            print("The number is not prime")
            break
    else:
        print("The number is prime")