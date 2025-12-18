# Here we write the conditonal statement practice; In which we know about some time we need condition mean if user fulfil the requirement then program run other it create error or else.

# user_age = int(input("Enter your are age for test your eligibilty: "))
# if(user_age>=18):
#     print("You are an adult")
#     print("You can vote")
#     print("You have full legal rights")
# else:
#     print("You are't an adult")
#     print("You can't vote")
#     print("You have't full legal rights")

# marks = int(input("Enter your marks: "))

# if marks >= 90:
#     print("A+")
# elif marks >= 80:
#     print("A")
# elif marks >= 70:
#     print("B")
# else:
#     print("Fail")

rider_age = int(input("Enter the age for check the eligibility of ride: "))
has_licence = input("Do you have a driving licence? (yes/no): ").lower()
if(rider_age >= 18):
    if(has_licence == "yes" ):
        print("You can Drive")
    else:
        print("You have not licence.So, You can't drive")
else:
    print("You can't drive because you are blow the age of driving.")