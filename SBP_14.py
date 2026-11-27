#a string s representing time in 24-hour format "HH:MM", compute the smallest angle in degrees between the hour and minute hands of an analog clock.
H=int(input("Enter the hour in 12-hour format: "))
M=int(input("Enter the minutes: "))
angle=abs((30*H+M/2)-(6*M))
if angle>180:  
    angle=360-angle
print("The angle between the hour and minute hands is:", angle, "degrees")