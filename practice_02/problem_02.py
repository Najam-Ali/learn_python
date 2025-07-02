# Write a program  to fill in a letter template given below with name and date:
latter = '''Dear < |Name| >, 
you are selected!
< |Date| > '''
# letter = "Dear Najam Ali|>\nYou are selected!\n<|02-07-2025|>"
# print (letter)

# Try another method to print this.

print(latter.replace("< |Name| >","Najam Ali").replace("< |Date| >","07 july 2025")) # its an other way to print this latter formate and its important for the best practice to use of the string function of python.