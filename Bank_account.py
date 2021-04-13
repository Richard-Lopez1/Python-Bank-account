class Bankaccount:        
    def __init__(self, int_rate, balance):
        self.int_rate = .01
        self.balance = 1000

    # deposit method
    def deposit(self, amount):    # takes an argument that is the amount of the deposit
        self.balance += amount    # the specific user's account increases by the amount of the value received
    
    # withdrawal method
    def withdrawal(self, amount):
        self.balance -= amount

    # interest rate
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + self.balance * self.int_rate
        else:
            
            print("Insufficient Funds: Charging a $5 fee")
        
    
    # display balance
    def display_account_info(self):
        print(f"Balance + interest: ${self.balance}, Interest rate: {self.int_rate}")
    
    
    
accnt1 = Bankaccount("rick", "rick@dojo.com")
accnt2 = Bankaccount("zaur", "zaur@dojo.com")

accnt1.deposit(50)
accnt1.deposit(50)
accnt1.deposit(100)
accnt1.withdrawal(120)
accnt1.yield_interest()
accnt1.display_account_info()

accnt2.deposit(50)
accnt2.deposit(1000)
accnt2.withdrawal(500)
accnt2.withdrawal(100)
accnt2.yield_interest()
accnt2.display_account_info()