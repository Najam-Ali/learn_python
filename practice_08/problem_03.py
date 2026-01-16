# Write a recursion function to calculate the sum of first n natural numbers.
def sum_of_natural_numbers(n):
    if n==1:
        return 1
    else: 
        return n + sum_of_natural_numbers(n-1)
n = int(input("Enter the number: "))
print(f"The sum of the {n} natural number,{(sum_of_natural_numbers(n))}")