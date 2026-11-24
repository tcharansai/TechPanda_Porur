#a program that take a user inputr of three angles and will find out whether it can form a triangle or not.
a1=int(input("Enter the 1st Angle of the triangle: "))
a2=int(input("Enter the 2nd Angle of the triangle: "))
a3=int(input("Enter the 3rd Angle of the triangle: "))
if a1+a2+a3==180:
    print("The given angles form a triangle.")
else:
    print("The given angles do not form a triangle.")