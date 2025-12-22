# Write a program  to find a greatest of four numbers entered by user

user_num1 = int(input("Enter your first number: "))
user_num2 = int(input("Enter your second number: "))
user_num3 = int(input("Enter your third number: "))
user_num4 = int(input("Enter your four number: "))

if(user_num1 > user_num2 and user_num1 > user_num3 and user_num1 > user_num4 ):
    print("User1 Number is greater: ",user_num1)
elif(user_num2 > user_num1 and user_num2 > user_num3 and user_num2 > user_num4):
    print("User2 number is greater: ",user_num2)
elif(user_num3 > user_num1 and user_num3 > user_num2 and user_num3 > user_num4):
    print("User3 number is greater: ",user_num3)
elif(user_num4 > user_num1 and user_num4 > user_num2 and user_num4 > user_num3):
    print("User4 number is greater: ",user_num4)