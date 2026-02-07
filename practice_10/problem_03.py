# Create a class with a class attribute a; Create and object from it and set "a" directly using object.a = o . Does this change the class attribute.
class character:
    a = 4
o = character()
o.a = 0 # We set the intance attribute 'a' for object 'o', this does not change the class attribute 'a'.
print(o.a)
print(character.a) # The class attribute remains unchanged.