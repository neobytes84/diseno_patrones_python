# Creational patterns - Builder in Python - Example 02
# Developed by Neobytes.io

class Finance:
    
    def __init__(self):
        self.id_client()
        self.account_number()
        self.balance()
        self.transactions()
    
    def id_client(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    def account_number(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    def balance(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    def transactions(self):
        raise NotImplementedError("Subclasses must implement this method")

class BankAccountBuilder(Finance):
    
    def id_client(self):
        self.id_client = "245"
    
    def account_number(self):
        self.account_number = "123456789"
        
    def balance(self):
        self.balance = 10000
    
    def transactions(self):
        self.transactions = []
    
    def __str__(self):
        return "BankAccountBuilder"

class CreditCardBuilder(Finance):
    def id_client(self):
        self.id_client= "241"
        
    def account_number(self):
        self.account_number = "987654321"
        
    def balance(self):
        self.balance = 5000
    
    def transactions(self):
        self.transactions = []

class AdministrativeBuilder(Finance):
    def id_client(self):
        self.id_client = "124"
        
    def account_number(self):
        self.account_number = "000000000"
        
    def balance(self):
        self.balance = 0
    
    def transactions(self):
        self.transactions = []

class BuilderComplex:
    
    def __repr__(self):
        return 'id client: {0.id_client} | Account Number: {0.account_number} | Balance: {0.balance}| Transactions: {0.transactions}'.format(self)

class BuilderComplexBuilder(BuilderComplex):
    
    def id_client(self):
        self.id_client= "780"
    
    def account_number(self):
        self.account_number = "1234567890"
        
    def balance(self):
        self.balance = 10000
    
    def transactions(self):
        self.transactions = []

def construct_bank_account(cls):
    
    builder = cls()
    builder.id_client()
    builder.account_number()
    builder.balance()
    builder.transactions()
    
    return builder

if __name__ == "__main__":
    
     dbs = BankAccountBuilder()
     fsl = CreditCardBuilder()
     al = AdministrativeBuilder()
     
     builder_complex = construct_bank_account(BuilderComplexBuilder)
     print(builder_complex)