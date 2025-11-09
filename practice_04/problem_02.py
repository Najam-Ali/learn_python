# write a program to accept marks of 6 students and display them in a sorted number.

marks_list = []
st1 = int(input("Enter first marks: "))
marks_list.append(st1)
st2 = int(input("Enter second marks: "))
marks_list.append(st2)
st3 = int(input("Enter third marks: "))
marks_list.append(st3)
st4 = int(input("Enter four marks: "))
marks_list.append(st4)
st5 = int(input("Enter five marks: "))
marks_list.append(st5)
st6 = int(input("Enter six marks: "))
marks_list.append(st6)
marks_list.sort()
print(marks_list)
