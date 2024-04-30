class Bank:
    
    country = "India"
    count = 0 
    
    def __init__(self,fn,ln,acc,bal):
        self.firstName = fn
        self.lastName = ln
        self.accNo = acc
        self.balance = bal
        self.transactions = []
        Bank.count = Bank.count + 1
        
    def deposit(self,amount):
        self.balance = self.balance + amount
        self.transactions.append(amount)
        
    def withdrawl(self,amount):
        if (self.balance > amount):
            self.balance = self.balance - amount
            self.transactions.append(amount)
            
        else:
            print("insufficient balance")
            
    def lastFiveTransaction(cls,cl):
        cls.country = cl
    
    @staticmethod
    def objCount():
        return Bank.count
    
idbi = Bank("nirnay","sangolkar",123,80000)
sbi = Bank("vedant","gaikwad",345,70000)
icici = Bank("mithilesh","badge",678,60000)
pnb = Bank("chinmay","deshpande",987,80000)
kotak = Bank("tavish","anade",476,30000)

print(Bank.objCount())
idbi.withdrawl(1000000000)
idbi.deposit(10000)
idbi.deposit(10000)
idbi.deposit(1000)
idbi.deposit(10)
idbi.deposit(1)
print(idbi.lastFiveTransaction(2))
    
            
        
        