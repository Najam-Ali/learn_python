# UNION of Sets.

s1 = {2,5,4,7,3,9}
s2 = {1,8,5,6,9,2}
# s3 = s1.union(s2) # Union is use for join two sets without repeatation
# s3 = s1 | s2 # Its symbol and method also use for the uninion of two or more sets.

#Intersection

# s3 = s1.intersection(s2) # This method use for the intersect two set and return a new set that contain on which elements that in both sets.
# s3 = s1 & s2 # Its symbol and method also use for intersection of two sets.

# DIFFERENCE

# s3 = s1.difference(s2)# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
# s3 = s1 - s2 # It symbol also use for the difference between two sets.

# Symmetric Differences 

#The symmetric_difference() method will keep only the elements that are NOT present in both sets.

# s3 = s1.symmetric_difference(s2) 
s3 = s1 ^ s2 # It Symobl also use for the symmentic diffrence of two sets.

print(s3) 
