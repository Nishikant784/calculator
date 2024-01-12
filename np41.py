class Costumer:
    '''This class is developed by nishikanta for mini bank application'''
    bankname='NISBANK'

    def __init__(self,name,balance=0.00):
        self.name=name
        self.balance=balance

    def deposite(self,amount):
        self.balance+amount
        print('After deposite balance:',self.balance)

    def withdraw(self,amount):
        if amount>self.balance:
            print('Insufficient funds....cant perform this operation')
        else:
            self.balance=self.balance+amount
            print('After withdraw balance:',self.balance)
    
print('Welcome to',Costumer.bankname)
name=input('Enter Your Name:')
c=Costumer(name)
while True:
    print('d-Deposit\nw-Withdraw\ne-Exit')
    option=input('Chose your option')
    if option.lower()=='d':
        amount= float(input('Enter amount to be deposited:'))
        c.deposit(amount)
    elif option.lower()=='w':
        amount=float('Enter amount to be withdraw')
        c.withdraw(amount)
    elif option.lower()=='e':
        print('Thanks For Using NIS bank')
        break
    else:
        print('Invalid choice.......Pls chose a valid option')
    