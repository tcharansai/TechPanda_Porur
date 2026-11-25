#a program to find the volume of the cylinder. Also find the cost when ,when the cost of 1litre milk is 40Rs
h=int(input("Enter the height of the cylinder in cm: "))
r=int(input("Enter the radius of the cylinder in cm: "))
v=3.14*r*r*h
print("The volume of the cylinder is", v, "cm³")
c=v*40/1000
print("The cost of the milk is", c, "Rs")