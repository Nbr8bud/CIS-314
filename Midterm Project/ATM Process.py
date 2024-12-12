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

    def transfer(self, destination_account, Amount):
        if Amount <= 0:
            return "Your transfer must be more than 0"
        elif Amount > self.amount:
            return "Sorry you have insufficient funds."
        else:
            self.amount -= Amount
            destination_account.amount += Amount
            return f" Yay: Your ${Amount:.2f} has been transferred to its destination."
        
    def show_account_balance(checking_balance, savings_balance):
        while True:
            try:
                account = input("Type 'checking' for checking account balance or 'savings' for savings account balance? ")

                if account == "checking":
                    print(f"Your Checking Account Balance is ${checking_balance.amount:.2f}")
                    return

                elif account == "savings":
                    print(f"Your Savings Account Balance is ${savings_balance.amount:.2f}")
                    return

            except ValueError:
                print("Incorrect. Please try again, type 'checking' for Checking Account Balance or 'savings' for Savings Account Balance. ")



Check=bank_account()
Save=bank_account()

print("Welcome to SecuriBank. Insert Card")
password=1234
pin=int(input("Enter Your Four Digit Pin:"))
while pin==password:
    print("1-Deposit\n2-Withdraw\n3-Check Balance\n4-Transfer\n5-Exit")
    x=int(input("Enter Choice:"))
    if(x==5):
        exit()
    y=int(input("Choose Account: 1-Checkings 2-Savings\n"))
    if(y==1):
        if x == 1:
            amount = float(input("Enter Deposit Amount: "))
            Check.deposit(amount)
        elif x == 2:
            amount = float(input("Enter Withdraw Amount: "))
            print(Check.withdraw(amount))
        elif x == 3:
            Check.balance()
        elif x == 4:
            amount = float(input("Enter Transfer Amount: "))
            destination_account = Save
            print(Check.transfer(destination_account, amount))
        else:
            print("You Have Chosen an Invalid Choice")
    elif(y==2):
        if x == 1:
            amount = float(input("Enter Deposit Amount: "))
            Save.deposit(amount)
        elif x == 2:
            amount = float(input("Enter Withdraw Amount: "))
            print(Save.withdraw(amount))
        elif x == 3:
            Save.balance()
        elif x == 4:
            amount = float(input("Enter Transfer Amount: "))
            destination_account = Check
            print(Check.transfer(destination_account, amount))
        else:
            print("You Have Chosen an Invalid Choice")
    else:
        print("You Have Chosen an Invalid Choice")
else:
    print("Wrong Pin Number Entered. Try Again")
    