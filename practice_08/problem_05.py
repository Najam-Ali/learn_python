# WAP convert inches to cms using function.
def inches_convert_cm(Inches):
    CM = Inches * 2.54 
    return CM
Inches= int(input("Enter the number: "))
measure= inches_convert_cm(Inches)
print(f"The {Inches} Inches convert is {round(measure , 2)} CM")