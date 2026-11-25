#a program that will tell whether the given number is divisible by 3 & 6
a=int(input("Enter a number: "))
if a%3==0 and a%6==0:
    print("The number is divisible by both 3 and 6")
else:
    print("The number is not divisible by both 3 and 6")