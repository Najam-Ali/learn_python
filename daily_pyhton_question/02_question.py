# Print the smallest number in the list
num = [int(input("Enter a number: ")) for i in range(6)]
smallest = num[0]
for i in num[1:]:
    if i < smallest:
        smallest = i
print("The smallest number is:", smallest)