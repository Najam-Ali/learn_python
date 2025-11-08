# write a program to detect double space in a string.

string = "My name is NAJAM  ALI.I want to become a PYTHON Developer."
# print(string.find("  ")) # it print the location where double space in your string.

                    # I want to find the index and print the index and want print text after find the text.On the other hand i want not this index words in my ouput.
index = string.find("  ") 
print(index,string[index+2:])