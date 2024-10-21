class bank_account():
    def __init__(self):
        self.amount=0

    def deposit(self,Amount):
            self.amount+=Amount
            print("Amount Deposited Successfully")
            print("New Bank Balance: ",self.amount)

    def withdraw(self,Amount):
            if(self.amount-Amount>=0):
                self.amount-=Amount
                print("Amount Withdrawn Successfully")
                print("New Bank Balance: ",self.amount)
            else:
                print("Insufficient Balance")

    def balance(self):
        print("Your Balance Is: ",self.amount)


Check=bank_account()
Save=bank_account()

while True:
    print("1-Deposit\n2-Withdraw\n3-Check Balance\n4-Transfer\n5-Exit")
    x=int(input("Enter Choice:"))
    y=int(input("Choose Account: 1-Checkings 2-Savings\n"))
    if(y==1):
        if(x==1):
            AmountC=float(input("Enter Deposit Amount:"))
            Check.deposit(AmountC)
        elif(x==2):
            AmountC=float(input("Enter Withdraw Amount:"))
            Check.withdraw(AmountC)
        elif(x==3):
            Check.balance()
        elif(x==5):
            exit()
        else:
            print("You Have Chosen an Invalid Choice")
    elif(y==2):
        if(x==1):
            AmountS=float(input("Enter Deposit Amount:"))
            Save.deposit(AmountS)
        elif(x==2):
            AmountS=float(input("Enter Withdraw Amount:"))
            Save.withdraw(AmountS)
        elif(x==3):
            Save.balance()
        elif(x==5):
            exit()
        else:
            print("You Have Chosen an Invalid Choice")
    else:
        print("You Have Chosen an Invalid Choice")

    
        