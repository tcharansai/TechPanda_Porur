# a program to find the euclidean distance between two coordinates.
x1=int(input("Enter the First x1 Coordinate: "))
y1=int(input("Enter the First y1 Coordinate: "))
x2=int(input("Enter the Second x2 Coordinate: "))
y2=int(input("Enter the Second y2 Coordinate: "))
d=((x2-x1)**2+(y2-y1)**2)**0.5
print("The euclidean distance between the two coordinates is:", d)