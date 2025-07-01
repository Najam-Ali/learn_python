# In this we discuse the negative order of the string.

old_string = "Najam ali"
old_sliced_string = old_string[1:4]
new_sliced_string = old_string[-4:-1] # Note the left side always the greater index in negtive and and right is small beacuse its started always form -1.
# print("The negtive slice string is ", new_sliced_string)
# print("The positive slice string is", old_sliced_string)

# print(old_string[:3]) # It same as the [0:3]
# print(old_string[1:]) # It same as the [1:5(mean where are the lenght os the string like -1 index is the end of the string)]
# Agar -1 wala bhi chahiye:
# print(old_string[-4:])    # "-4" to end of string (inclusive of -1 index)

# explicitly -4 to len(string)
# print(old_string[-4:len(old_string)])  # same output

# slice with skip value.

skiped_sliced_string = old_string[1:7:2]
print("Output after the sliced of string",skiped_sliced_string) # In this line we get the the output is => aa beacuse the old_string is => Najam Ali and the [1:6:2] mean stating from the index 1 and move forwardly toward the 6 (exclud) and 2 mean move after two values print the next value. 
