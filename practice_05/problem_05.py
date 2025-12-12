# Create an empty dictonary.Allow 4 friends to enter that fvrt languages as value and use key as thier name.assume the names are unique.

this_dict = {}
name = input("Enter your name: ")
lang = input("Enter language name: ")
this_dict[name] = lang
name = input("Enter your name: ")
lang = input("Enter language name: ")
this_dict[name] = lang
name = input("Enter your name: ")
lang = input("Enter language name: ")
this_dict[name] = lang
name = input("Enter your name: ")
lang = input("Enter language name: ")
this_dict.update({
    name:lang
})
print(this_dict)

# Let take an other problem that number is 6 and in which we said: If the name of 2 friends are same: What will happento the program in problem # 5. And the answer is the pyhton update thier value and print the lastest key value that assinged in dict.

# Let take an other problem that number is 7 and in which we said:
# if the languages of two friends are same,What will happend to the  program in problem # 5. And the answer is value will be same.
