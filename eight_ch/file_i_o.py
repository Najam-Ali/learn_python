# If We want to take some data from a file we learn the concept of file and safe this data in our memory permanently handling in python.
# File Handling in Python
# There are two types of files
# 1. Text File (.txt, .py, .c, .cpp)
# 2. Binary File (.jpg, .png, .pdf, .docx)
# In Python, we can handle files using built-in functions.
# Here some practice of the file handling in python.

f = open("random_file.txt", "r")  # Open a file in read mode
data = f.read()  # Read the content of the file
print(data)
f.close # If i open the file and its my responsibility to close this file.

