#Corey Henry & Natalie Morrison              #Date Assigned: 10Feb15
#                                            #
#Course CSE 1384 Sec 06                      #Date Due: 07Oct2014
#File name: Banking.py
#
#Program description - creates a banking program for a bank account and college
#savings bond.

class Account:
    def __init__(self,name,bank):
        
        #set all the variabels for the class of the inported information
        self.user = name
        self.bank_name = bank

        #set the orginial bank ammount at 0
        self.ammount = 0

        #set orginial interest rate
        
        self.interest_rate = 2


# create a function that will take the deposit and add the ammount to it
    def deposit(self,ammount):
        self.ammount += ammount

# function to find out the interest ammount and return the interest.
    def calculateInterest(self):
        self.interest = self.ammount * self.interest_rate / 100
        return(self.interest)

# create a string that will display the status of thier account and return it
    def getStatus(self):
        Status = (self.user + ' has a net deposit of ' + str(self.ammount) + ' dollars in '+ self.bank_name +'.')
        return(Status)




    
#create a account and a function that can withdrawl
class BankAccount(Account):
    def withdraw(self, ammount):
        self.ammount -= ammount
        
# print that they have overdrawn thier account if bank foes under 0 dollars
        if self.ammount < 0:
            print('You have overdrawn your Account')

#Create a class that will be for the college bond
class CollegeBond(Account):
    
    #intialize the class and add a basic length of 8 if not given.
    def __init__(self,name, bank, length = 8):
        
#set all the variables and class rewrites
        self.user = name
        self.bank_name = bank
        self.ammount = 0
        self.length = length
        self.interest_rate = 10
        
#function that will return the length
    def getBondLength(self):
        return(self.length)
        
        

    
       
        
        
