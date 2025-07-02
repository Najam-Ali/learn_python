# Write a program to detect Double spaces in a string

str = "I am bad  boy"
print("Find the double space of the string",str.find("  ")) 

# Here we use a find method for the finding of the double spaces and it give the index of targeted char exist other it return the -1.

str = "I am bad boy"
print("Find the double space of the string",str.find("ad")) # output is "6" beacuse the "ad" at the place of the 6 index.

str = "I am bad boy"
print("Find the double space of the string",str.find("n")) # output is "-1" beacuse the "n" is not exist at any index of your string.