# These dict methods follow in the python.


student = {
    "name" : "Ahmed",
    "marks" : "50%",
    "status" : "pass",
    "class" : "Matric"
}

# print(student.items()) # It gives us the list of the key pair values in the form of list and key value pair in the form of the tuple.It is very helpful with the for loop.
# print(student.keys()) # It print the keys of the dict.
# print(student.values()) # It print the values of the dict.
# student.update({"class": "Inter"}) # It help us to update the perivouse dict and if we want add a some value in a that not include in current dict the also add the update method.
# print(student.get("gender")) # It provide me "NONE" because i have no value againts the key "Gender". It return non not error.
# print(student.get("grnder","Please add the gender")) # Its the ways to write anything that show an answer against the key that by default.
# st = student.pop("status") # It remove the key but print the value that you store in the variable that name is "st".
# print(st)
# print(student.popitem()) # Removes last inserted key–value pair and Returns (key, value) tuple
# st = student.copy() # Returns shallow copy (not deep copy)
# student.clear() # Clear whole dictionary
