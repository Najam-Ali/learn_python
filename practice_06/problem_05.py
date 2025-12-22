# Write a program to calculate the grade of a student from his mars from the following secheme:

# st_marks = int(input("Enter your marks:"))
# if(st_marks > 90 ):
#     print("You secore is excillent")
# elif(st_marks < 90 and st_marks > 80):
#     print("Your secore grade is: A")
# elif(st_marks < 80 and st_marks > 70):
#     print("Your secore grade is: B")
# elif(st_marks < 70 and st_marks > 60):
#     print("Your secore grade is: C")
# elif(st_marks < 60 and st_marks > 50):
#     print("Your secore grade is: D")
# else:
#     print("You Secore grade is F")
# I try other method for it

st_marks = int(input("Enter your marks: "))

if st_marks >= 90:
    print("Your score is Excellent")
elif st_marks >= 80:
    print("Your score grade is: A")
elif st_marks >= 70:
    print("Your score grade is: B")
elif st_marks >= 60:
    print("Your score grade is: C")
elif st_marks >= 50:
    print("Your score grade is: D")
else:
    print("Your score grade is: F")
