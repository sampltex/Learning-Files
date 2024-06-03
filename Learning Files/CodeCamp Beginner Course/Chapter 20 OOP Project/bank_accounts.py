class BalanceExeption(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")

    def getBalace(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\nDeposit complete.")
        self.getBalace()

    # def withdraw(self, amount):
    #     if self.balance >= amount:
    #         self.balance = self.balance - amount
    #         print("\nWithdrawl complete.")
    #         self.getBalace()
    #     else:
    #         print("Couldn't withdrawl from balance")

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceExeption(
                f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}."
            )
        
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete.")
            self.getBalace()
        except BalanceExeption as error:
            print(f"\nWithdraw interrupted: {error}")

    def transfer(self, amount, account):
        try:
            print("\n**********\n\nBeginning transfer...")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer complete.\n\n**********")
        except BalanceExeption as error:
            print(f"\nTransfer could not be completed. {error}")

class InterestRewardsAccount(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete.")
        self.getBalace()

class SavingsAccount(InterestRewardsAccount):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw complete.")
            self.getBalace()
        except BalanceExeption as error:
            print(f"\nWithdraw interrupted: {error}")