# WAP python fuction to print first n lines of the following pattern:
'''
***
**
*
'''

def print_pattern(n):
    for i in range(n,0,-1):
        pattern = "*" * i 
        print(pattern)
n = int(input("Enter the number: "))
print_pattern(n)