
# ********************************************************************************

class BankAccount:
		def __init__(self, int_rate=0.01, balance=0):
			self.int_rate = int_rate
			self.balance = balance


		def deposit(self, amount):
			self.balance+=amount
			return self

		def withdraw(self, amount):
			if amount<self.balance:
				self.balance-=amount
			elif amount > self.balance:
				print('"Insufficient funds: Charging a $5 fee"')
				self.balance-=5
			return self

		def display_account_info(self):
			print(self.balance)
			return self

		def yield_interest(self):
			self.balance+(self.balance*self.int_rate)
			return self



firstaccount=BankAccount(0.02,2000)
secondaccount=BankAccount(0.03,4000)

# firstaccount.deposit(300).deposit(400).deposit(500).withdraw(5000).yield_interest().display_account_info()

# secondaccount.deposit(300).deposit(400).withdraw(500).withdraw(500).withdraw(500).withdraw(500).yield_interest().display_account_info()


class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account = [BankAccount(int_rate=0.01, balance=0),BankAccount(int_rate=0.01, balance=0)]

    def make_deposit(self,amount,i):
        if i==0:
            self.account[i].deposit(amount) 
        elif i==1:
            self.account[i].deposit(amount)
        return self

    def make_withdrawal(self,amount,i):
        if i==0:
            self.account[i].withdraw(amount)
        elif i==1:
            self.account[i].withdraw(amount)
        return self

    def display_user_balance(self,i):
        if i==0:
            print(self.name ,self.account[i].balance)
        elif i==1:
            print(self.name ,self.account[i].balance)
        return self
            


Mohammad = User('Mohammad','imairmohd@hotmail.com')
John = User('John','John@yahoo.com')
Mussab = User('Mussab','mussab@yahoo.com')
#  *************************************************************** 
Mohammad.make_deposit(100,0).display_user_balance(0)
Mohammad.make_deposit(100,1).display_user_balance(1)

# Mohammad.make_withdrawal(1000)
# Mohammad.display_user_balance()
# Mohammad.account.display_account_info()









  
  





 
 

