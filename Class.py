class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    	self.account_balance += amount	# the specific user's account increases by the amount of the value received
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount # the specific user's account decreases by the amount of the value received

    def display_user_balance(self):
        print("User:",self.name, "Balance : $",self.account_balance)

Mike = User("Mike", "Mike@python.com")
Clem = User("Clem", "Clem@python.com")
Jada = User("Jada", "Jada@python.com")

Mike.make_deposit(200)
Mike.make_deposit(100)
Mike.make_deposit(1000)
Mike.make_withdrawal(500)
Mike.display_user_balance()
Clem.make_deposit(200)
Clem.make_deposit(100)
Clem.make_withdrawal(1000)
Clem.make_withdrawal(70)
Clem.display_user_balance()
Jada.make_deposit(700)
Jada.make_withdrawal(1000)
Jada.make_withdrawal(1000)
Jada.make_withdrawal(70)
Jada.display_user_balance()