# SETS in pyhton define as the collection of well defined ojects.
d = {} # its create the empty dictionary.
# print(d, type(d)) # Its result is empty dictionary & type also dict.

# s = {2,4,5,8,5,4,0,7,8,45,65}
# print(s,type(s))

# Sets are UnOrdered.
# Sets are UnIndexed.
# Not any repeated value exist in sets.
# There is no way to change items in sets.
# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.Let Take an example.

thisSet = {"Apple","Grapes","Mango"}
# tropical = {"pineapple", "Mango", "papaya"}
mylist = ["kiwi", "orange"]
# print("Apple" in thisSet )

# thisSet.add("Peach") # Peach is add in set and that is very usefull method in sets.

# thisSet.update(tropical) # To add items from another set into the current set, use the update() method. And you will notice Mango is not add in this set because Duplicate value is not allowed in set.

# thisSet.update(mylist) # The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

# To remove an item in a set, use the remove(), or the discard() method.If the item to remove does not exist, remove() will raise an error.If the item to remove does not exist, discard() will NOT raise an error.Let take examples:
# thisSet.remove("orange") # "orange" not exist then give an error.
#thisSet.remove("Apple") # Its print {'Mango', 'Grapes'} 
# thisSet.discard("orange") # "orange" not exist but not give an error.
# thisSet.discard("Apple") # Its print {'Mango', 'Grapes'} 

# You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.The return value of the pop() method is the removed item.

# thisSet.pop() # Its will print the remaing values.But 
# x = thisSet.pop() # Its return the removed item.

# The clear() method empties the set but the set exist.Let take example
# thisSet.clear() # It return set(), means empty set.

# The del keyword will delete the set completely:Let take example
# del thisSet # It use for del the set completely.


print(thisSet)


