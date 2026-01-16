# WAP to print the table of multiplication of a given number by using function.
def mulitiplication_num(num):
    for i in range(1,11):
        mult = num*i
        print(f"{num} * {i} = {mult}")
    return mult
num = int(input("Enter the number: "))
mulitiplication_num(num)

