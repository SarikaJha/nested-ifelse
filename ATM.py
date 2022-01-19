print("welcome to your ATM /swipe your card")
balance=10000
language=(input("enter the language= "))
if language=="english":
    print("choose your transaction\n1.balance enquiry\n2.withdraw money\n3.deposit money\n5.transfer money\n6.Exit")
    transaction=input("enter your transaction=")
    if transaction=="balance enquiry":
        swipe=(input("do yoy want to swipe your card= "))
        if swipe=="yes":
            atm_pin=9999
            pin=int(input("enter your pin"))
            if pin==atm_pin:
                print("your balance is 10000")
                print("here is your card,thanks for using")
            else:
                print("your atm_pin is wrong")
        else:
            print("thanks for using atm")
    elif transaction=="withdraw money":
        balance=input("balance=10000")
        amount=int(input("enter your amount= "))
        total=10000-amount
        if amount>10000:
            print("you have insufficient balance to withdraw")
            
        else:
            if amount<10000:
                atm_pin=9999
                pin=int(input("enter your pin"))
                if pin==atm_pin:
                    print("your available balance is",total)
                    print("collect your cash")
                else:
                    print("wrong pin")
    elif transaction=="deposit money":
        balance=int(input("enter your balance="))
        deposit=int(input("enter your deposit amount="))
        total=balance+deposit
        if deposit>0:
            atm_pin=9999
            pin=int(input("enter your pin= "))
            if pin==atm_pin:
                print("your balance is",total)
                print("your deposit is done successsfully and thanks for using atm")
            else:
                print("wrong pin")
        else:
            print("enter a valid deposit amount")
    elif transaction=="transfer money":
        balance=int(input("enter your balance="))
        transfer_money=int(input("enter your amout to transfer money="))
        total=balance-transfer_money
        if transfer_money>0:
            atm_pin=9999
            pin=int(input("enter your pin= "))
            if pin==atm_pin:
                print("your balance is",total)
                print("your money has been transfered and thanks for using atm")
            else:
                print("wrong pin")
        else:
            print("please enter a valid amount to proceed")
    elif transaction=="Exit":
        Exit=input("enter yes if you want to Exit=")
        if Exit=="yes":
            atm_pin=9999
            pin=int(input("enter your pin"))
            if pin==atm_pin:
                print("THANK YOU FOR USING")
            else:
                print("wrong pin")
else:
    print("language not found")