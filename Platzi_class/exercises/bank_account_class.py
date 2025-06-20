class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True
    
    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f"You deposited {amount}. Your current balance is {self.balance} ")
        else:
            print("You can't deposit, your account is inactive")
        
    def withdraw(self, amount):
        if self.active:
            if amount <= self.balance:
                self.balance -= amount
                print(f"You have withdrew {amount}. Current balance {self.balance}")
    
    def deactivate_account(self):
        self.is_active = False
        print(f"the account has been deactivated")
   
    def activate_account(self):
        self.is_active = True
        print(f"the account has been activated")

account1 = BankAccount("Anna", 500)
account2 = BankAccount("Luis", 1000)
account3 = BankAccount("Pedro", 5300)
account4 = BankAccount("Patricia", 2200)

account1.deposit(200)
account2.deposit(100)
account1.deactivate_account()
account1.deposit(50)
account1.activate_account()
account1.deposit(50)
account3.deposit(10)
account4.deposit(1000)