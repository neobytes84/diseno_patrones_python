# Creational patterns - Builder in Python - Example 01
# Developed by Neobytes.io

class Computer():
    
    def price(self) -> float:
        self.price = 8550.55
        return self.price
    
    def availability(self):
        self.availability = 'Available'
        return self.availability
    
    def warranty(self):
        self.warranty = '1 year'
        return self.warranty

class ComputerBuilder:
    
    def price(self) -> float:
        self.price = 540.77
        return self.price
    
    def availability(self):
        self.availability = 'Out of stock'
        return self.availability
    
    def warranty(self):
        self.warranty = '3 years'
        return self.warranty

class ComputerDirector:
    
    def price(self) -> float:
        self.price = 802.14
        return self.price
    
    def availability(self):
        self.availability = 'Available'
        return self.availability
    
    def warranty(self):
        self.warranty = '1 year'
        return self.warranty

class DatabaseComputerBuilder(ComputerBuilder):
    def price(self) -> float:
        self.price = 750.99
        return self.price
    def availability(self):
        self.availability = 'Available'
        return self.availability
    def warranty(self):
        self.warranty = '2 years'
        return self.warranty

if __name__ == "__main__":
     fe = Computer()
     pr = ComputerBuilder()
     di = ComputerDirector()
     db = DatabaseComputerBuilder()
     
     print(f"Original Computer: Price = ${fe.price()}, Availability = {fe.availability()}, Warranty = {fe.warranty()}")
     print(f"New Computer: Price = ${pr.price()}, Availability = {pr.availability()}, Warranty = {pr.warranty()}")
     print(f"Director Computer: Price = ${di.price()}, Availability = {di.availability()}, Warranty = {di.warranty()}")
     
     print(f"Database Computer: Price = ${db.price()}, Availability = {db.availability()}, Warranty = {db.warranty()}")
     print()
