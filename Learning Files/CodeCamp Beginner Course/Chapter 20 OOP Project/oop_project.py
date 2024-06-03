from bank_accounts import *

Dave = BankAccount(1000, "Dave")
John = BankAccount(2000, "John")

Dave.getBalace()
John.getBalace()

Dave.deposit(200)
John.deposit(500)

Dave.withdraw(10000)
Dave.withdraw(10)

Dave.transfer(120, John)

Jim = InterestRewardsAccount(1000, "Jim")
Jim.getBalace()

Jim.deposit(100)

Jim.transfer(100, Dave)

Barry = SavingsAccount(3000, "Barry")
Barry.getBalace()

Barry.deposit(100)

Barry.transfer(2000, John)

Barry.name()