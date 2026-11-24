#User will input (3ages).Find the oldest one
age1=int(input("Enter the age of first person: "))
age2=int(input("Enter the age of second person: "))
age3=int(input("Enter the age of third person: "))
if age1>age2 and age1>age3:
    print("First person is the oldest")
elif age2>age1 and age2>age3:
    print("Second person is the oldest")
else:
    print("Third person is the oldest")
