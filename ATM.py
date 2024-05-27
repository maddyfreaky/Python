class BankAccount:
    def __init__(self):
        self.account_number=1234567890
        self.balance=10000
        print("------"*5,"Welcome","------"*5)
        print()
        print("Account number:\t",self.account_number)
        print("Balance:\t\t",self.balance)
        print()
    def decide(self):
        print("-------"*4,"Choose any one:","-------"*4)
        print()
        print("Deposit/Withdraw","\t"*7,"Close")
        print()
        self.key=input("Pick any one:").lower()
    def deposit(self):
        print()
        self.damount=int(input("Enter the deposit amount:"))
        self.balance=self.balance+self.damount
        print("------"*5,"Deposit","------"*5)
        print("Account number:\t",self.account_number)
        print("Deposit amount:\t",self.damount)
        print("Balance:\t\t",self.balance)
        print()
        print("Amount Deposited!")
        print()
        
    def withdraw(self):
        print()
        self.wamount=int(input("Enter the withdraw amount:"))
        if self.wamount<=self.balance:
            self.balance=self.balance-self.wamount
            print("------"*5,"Withdraw","------"*5)
            print("Account number:\t",self.account_number)
            print("Withdraw amount:\t",self.wamount)
            print("Balance:\t\t",self.balance)
            print()
            print("Amount withdrawn!")
            print()
        else:
            print("Insufficient balance...")
            print("Please try again!!")
            print()
entry=BankAccount()
def atm():
    entry.decide()
    if entry.key=="deposit":
        entry.deposit()
        atm()
    elif entry.key=="withdraw":
        entry.withdraw()
        atm()
    elif entry.key=="close":
        print("---------------"*5)
        print("Thank you! Come again!!")
        exit()
    else:
        print("---------------"*5)
        print("Invalid entry")
        print("Please try again!!")
        atm()
    
atm()