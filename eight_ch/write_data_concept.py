# Here we learn how we add in a file of python.

# st = "Hello!"
st = "Hi! I learn about the writing concept in python" # I use this line for the learn concept of overwriting of a file.

f = open("random.write_file.txt", "w") # Imp Note: If the file is not exixt in active directory then write() function auto created.But if file existed the write function overwitre the privious file and the previos data of the file is deleted and add the new data add. If i want to add the data in previous file without deleting the older data so we will learn the concept of the appen function.
count = f.write(st) 
print(count) # Here we use this because it show/give some number with this we identify and confirmation about the data store sucessfully or not.
f.close()