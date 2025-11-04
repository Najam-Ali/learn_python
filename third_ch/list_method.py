
# Note In string when we aplly a function on a string it return a new value in result but In list change the original string with change means old list make a new list.

# fruite = ["Apple", "Peach", 45, 78.7, False, "Ali", "Ahmed",45,79,43,45]
# fruite.append("ahmad") # Append() => add the latter at the end of the list. 
# lists = fruite.copy() # This method will use for create a copy of a list.
# fruite.clear() # clear() method use for clear all the elements of the list.
# counter = fruite.count(45) # count(value) use for count how much time repeate an element in a list.
# fruite.extend(["shah","Malik"]) # extend() use for the list by adding elements from another list
# fruite.insert(2,"mango") # insert()use for the  insert an element at a specific position in the list with the help of indux.
# fruite.pop() # pop() use for the  remove the last element from the list.
# fruite.remove("Peach") # remove() use for the  remove the first occurrence of a specified element from the list without the indux.
# fruite.reverse() # reverse() use for the  reverse the order of the elements in the list
list_of_number = [6,3,8,3,2,7,5,3,1,9,5,6,4,0]
list_of_number.sort() # sort() sort the elements of the list in ascending order
print(list_of_number)