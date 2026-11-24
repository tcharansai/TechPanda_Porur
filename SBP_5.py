# program that will reverse a four digit number.Also it checks whether the reverse is true.
num=int(input("Enter a four digit number: "))
num1=num
reverse=0
while(num>0):
    digit=num%10
    reverse=reverse*10+digit
    num=num//10
print("The reverse of the number is: ", reverse)
print("The original number is: ", num1)
if reverse==num1:
    print("The reverse is true")
else:
    print("The reverse is not true")