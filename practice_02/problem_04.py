# Write a program in which replace the double space from problem 3 with single spaces.

str = "I am bad  boy"
# print(str.replace("  ", " ")) 
# print(str.replace("  "," ",8)) # Its other method with the help pf the index.

# An other method of this:
new_str = ' '.join(str.split()) # splite method break the string in single words and join each word sepratly sepratly in a string with space.
print(new_str)
