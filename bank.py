class BankAccount:
    def __init__(self,balance):
        self.balance=balance
        self.deposit=0
        self.withdrawl=0
    
    def deposit_amount(self):
        self.deposit=int(input("Enter the amount of money to deposit: "))
        print(f"You have deposited {self.deposit}")
        self.balance=self.balance+self.deposit
        print(f"Your current balance is {self.balance}")
    
    def withdrawl_amount(self):
        self.withdrawl=int(input("Enter the amount of money to withdraw: "))
        if self.withdrawl>self.balance:
            print("Cannot withdraw the amount")
        else:
            self.balance=self.balance-self.withdrawl
            print(f"You have withdrawn {self.withdrawl}")

        print(f"Your current balance is {self.balance}")

bank1=BankAccount(200)
bank1.deposit_amount()
bank1.withdrawl_amount()

