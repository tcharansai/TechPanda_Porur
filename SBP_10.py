#a program that will take user input of cost price and selling price and determines whether its a loss or a profit
cp=int(input("Enter the cost price: "))
sp=int(input("Enter the selling price: "))
if cp>sp:
    print("The Trade is a loss")
elif cp==sp:
    print("There is no loss nor a Profit")
else:
    print("The Trade is a Profit")