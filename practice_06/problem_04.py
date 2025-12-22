# Write a program to find whether a given user name contain less then 10 characters or not.

user_name = input("Enter your user name: ")
# lenght_of_user_name = len(user_name)
# if (lenght_of_user_name < 10):
#     print("User name length is valid: ",user_name)
# else:
#     print("user name length is not valid: ",user_name)
# I want to learn in other way
# Username:
# Must not be empty
# Minimum 5 characters
# Space not allowed
# only letters, numbers, underscore (_) aur dot (.) allowed
# Not only start with number.

if(len(user_name) == 0 ):
    print("Username cannot be empty")
elif(len(user_name) < 5):
    print("Username must be at least 5 characters long")
elif(" " in user_name ):
    print("Username should not contain spaces")
elif(not user_name.replace("_", "").replace(".","").isalnum()):
    print("Username can contain only letters, numbers, _ and .")
elif(user_name[0].isdigit()):
    print("Username cannot start with a number") 
else:
    print("Username is valid ✅")