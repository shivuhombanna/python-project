balance=1000
def display_menu():
    print("simpale bank system")
    print("1.Check Balance\n2.Deposit Money\n3.Withdraw Money\n4.Exit")

while True:
    display_menu()
    choice=int(input("Enter your choice {1,2,3,4}"))

    if choice==1:
        print(f"your bank balance is {balance}")
    elif choice==2:
        amount=int(input("Enter your Deposit money "))
        if amount>0:
            balance+=amount
            print(f"{amount} is Deposit success fully ")
            print(f"total amount is {balance}")
        else:
            print("transation fail")    

    elif choice==3:
        amount=int(input("Enter your Deposit money "))
        if amount<=0:
            print("invalid amount")

        elif amount>balance:
            print(f"in suffisiant balance ")
        else:
            print(f"{amount} is Deposit success fully ")
            print(f"total amount is {balance}")

    else:
        print("Thank you for visiting banking suystem")
        break