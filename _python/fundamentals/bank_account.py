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

secondaccount.deposit(300).deposit(400).withdraw(500).withdraw(500).withdraw(500).withdraw(500).yield_interest().display_account_info()