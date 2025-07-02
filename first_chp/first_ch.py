                            # Problem 1

# print("hello world")

                            #Problem 2
                        # this module(pyttsx3) give us a voice.

# import pyttsx3
# engine = pyttsx3.init()
# engine.say("I love u")
# engine.runAndWait()

                            # Problem 3

import os

# Set the path of the directory you want to list
# You can use '.' to list the current directory
directory_path = '/'

# Get the list of files and directories
try:
    contents = os.listdir(directory_path)
    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print("Directory not found.")
except PermissionError:
    print("Permission denied.")
