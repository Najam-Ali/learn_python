# num = []
# for i in range(1, 5):
#     n = int(input("Enter a number: "))
#     num.append(n)
# if n >= num[0] or n >= num[1] or n >= num[2] or n >= num[3]:
#     # result = num.max()
#     # print(f"The largest number is: {result}")
#     print(f"The largest number is: {max(num)}")
# else:
#     print("Invalid input. Please enter a number greater than or equal to all previous numbers.")

num = [int(input("Enter a number: ")) for i in range(5)]
largest = num[0]
for i in num[1:]:
    if i > largest:
        largest = i
print(f"The largest number is: {largest}")