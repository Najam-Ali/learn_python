# A spam comment is define as a text containing follownig keywords:
# "Make a lot of money", "Buy Now", "Subscribe this", "Click this".Write a program to detetct spam.
p1 = "Make a lot of money"
p2 = "Buy Now"
p3 = "Subscribe this"
p4 = "Click this"

massage = input("Enter your massage here: ")
if ((p1 in massage) or (p2 in massage) or (p3 in massage) or (p4 in massage)):
    print("This is spam massage.")
else:
    print("This is not a spam massage.")