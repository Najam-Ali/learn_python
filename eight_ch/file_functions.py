# Here we learn more about the file functions.

# f = open("file_functions.txt", "r")
# lines = f.readlines() # Readlines return a list.
# print(lines, type(lines))
# f.close()
 

# Readline() function:

# f = open("file_functions.txt")

# lines1 = f.readline()
# print(lines1, type(lines1))

# If we print more then one line 
# lines2 = f.readline()
# print(lines2, type(lines2))
# lines3 = f.readline()
# print(lines3, type(lines3))
# lines4 = f.readline()
# print(lines4, type(lines4))
# For avoide this type of repetation we use loop.
# lines = f.readline()
# while(lines != ""):
#     print(lines)
#     lines = f.readline()

# Same with for loop.

# for lines in f:
#     print(lines)
# f.close()


# Here we see the mode of add/write anything in a last of the file then use append mode.
# Let's take example.

# st = "Here! we take the example of append mode."
# f = open("random_file.txt", "a")
# print(f.write(st)) # if we run code multiple time then add this thing accordingly.
# f.close()

# We can do it with the help of he with statment.

with open("random_file.txt", "r") as f:
    content = f.read()
    print(content)