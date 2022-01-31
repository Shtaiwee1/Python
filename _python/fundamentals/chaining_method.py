

class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account_balance = 300

    def make_deposit(self,amount):
        self.account_balance += amount
        print(self.account_balance)
        return self

    def make_withdrawal(self,withdrawal):
        self.account_balance-= withdrawal
        return self

    def display_user_balance(self):
      print(self.account_balance)
      return self

    def transfer_money(self,other_self,transfer):
        self.account_balance-=transfer
        print(self.account_balance)
        other_self.account_balance+=transfer
        print(other_self.account_balance)


      

Mohammad = User('mussab','imairmohd@hotmail.com')
John = User('John','John@yahoo.com')
Mussab = User('John','John@yahoo.com')
#  *************************************************************** 
Mohammad.make_deposit(100).make_deposit(300).make_deposit(400).make_withdrawal(1000).display_user_balance()


# *********************************************************************
John.make_deposit(100).make_deposit(300).make_withdrawal(1000).make_withdrawal(1000).display_user_balance()

# **********************************************************************
Mussab.make_deposit(100).make_withdrawal(1000).make_withdrawal(1000).make_withdrawal(1000).display_user_balance()

# ************************************************************************
# Mussab.transfer_money(Mohammad,300)
# Mohammad.display_user_balance()
# Mussab.display_user_balance()








  
  





 
 

