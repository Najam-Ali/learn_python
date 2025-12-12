# Can we have a set with 18(int) and "18" (str) as an value in it.  

# s = {18,"18"}
# print(s,type(s))
# Other way

s = set()
s.add(18)
s.add("18")
print(s,type(s))
