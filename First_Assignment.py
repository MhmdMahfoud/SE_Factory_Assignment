Balance=1000
Choices=0
password=123
user_password=int(input("enter password"))
if user_password==password:
   while Choices !=4:
    print("""Welcome to the ATM
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit""")
    Choices =int(input("your choice is "))
    if Choices==1:
        print("Your current balance is " + str(Balance) +"$")
    elif Choices == 2:
        amount=float(input("how much to deposit ?"))
        if amount >0:
            Balance=Balance+amount
        else:
            print("amount should be greater then 0")
    elif Choices == 3:
        amount=float(input("how much to witdraw  "))
        if Balance > amount:
            Balance=Balance-amount
            print("the new balance is  " +str(Balance))
        else:
            print("no enough balance ")
    elif Choices == 4:
        print("exit")
    else:
        print("Invalid")
else:
    print("password incorrect")
    