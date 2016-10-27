from Banking import *

#Initialize accounts.
account1 = Account("Alex Munos", "Marvelous Futures Banking and Investment")
account2 = Account("Zeke Johnson", "Marvelous Futures Banking and Investment")

#Depositing some money into the accounts.
account1.deposit(2789)
account2.deposit(230)

#This should return the account status.
print(str(account1.getStatus()))
print("This account will have a return of " + str(account1.calculateInterest()) + " this year.")
print("")
print(str(account2.getStatus()))
print("This account will have a return of " + str(account2.calculateInterest()) + " this year.")
print("")

#Start of commented out section


account3 = BankAccount("Claire Stanfield", "Marvelous Futures Banking and Investment")
account3.deposit(100)
account3.withdraw(500)

print(str(account3.getStatus()))
print("This account will have a return of " + str(account3.calculateInterest()) + " this year.")
print("")

account4 = CollegeBond("Tiffany Aching", "Marvelous Futures Banking and Investment", 4)
account4.deposit(400)

print(str(account4.getStatus()))
print("This account will mature in " + str(account4.getBondLength()) + " years.")
print("This account will have a return of " + str(account4.calculateInterest()) + " this year.")
print("")

account4.getStatus()
    

