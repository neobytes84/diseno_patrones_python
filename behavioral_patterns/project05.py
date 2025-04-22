# Behavioral patterns - Mediator in Python -example 01
# Developed by Neobytes.io

import numpy as np
import random

class Management(object):
    """Mediator class."""
    
    def add_employee(self, user, name_employee):
        print("[{}]: {} has joined the team.".format(user, name_employee))
    
    def remove_employee(self, user, name_employee):
        print("[{}]: {} has left the team.".format(user, name_employee))
    
    def update_employee(self, user, name_employee, new_status):
        print("[{}]: {}'s status has been updated to {}.".format(user, name_employee, new_status))
        print("User {} has updated their status to {}.".format(name_employee, new_status))
        print("---")
        
class User(object):
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.management = Management()
    
    def displayUser(self, name_management, status):
        print("[{}] User {} has status: {}".format(name_management, self.name, status))
        self.management.update_employee(self.name, self.name, status)
    
    def joinTeam(self, id_team, name_management):
        self.management.add_employee(name_management, self.name)
        print("[{}] User {} has joined team {}".format(name_management, self.name, id_team))
    
    def leaveTeam(self, id_team, name_management):
        self.management.remove_employee(name_management, self.name)
        print("[{}] User {} has left team {}".format(name_management, self.name, id_team))
    
    def updateStatus(self, id_team, name_management, new_status):
        self.displayUser(name_management, new_status)
        if random.random() < 0.5:
            self.joinTeam(id_team, name_management)
            self.leaveTeam(id_team, name_management)
            self.displayUser(name_management, new_status)
            print("---")
    
    def join_user_management(self, id_team, name_management):
        self.joinTeam(id_team, name_management)
        self.displayUser(name_management, "Active")
        print("---")
        
class Sales(object):
    
    def __init__(self, sales_amount, price_hour, tax, shipments, quantity_sold):
        self.sales_amount = sales_amount
        self.price_hour = price_hour
        self.tax = tax
        self.shipments = shipments
        self.quantity_sold = quantity_sold
        self.sales = []
        self.salary = []
        self.worked_hours = []
        self.months = []
        self.salary_per_month = []
        self.tax_per_months = []
        self.salary_per_hour = []
        self.total_sales_amount = []
        self.total_sales_shipments = []
    
    def update_status(self, user, status):
        self.sales.append(self.sales_amount)
        self.total_sales_amount.append(sum(self.sales))
        self.total_sales_shipments.append(self.shipments)
        self.salary.append(self.calculate_salary(self.sales_amount, self.price_hour, self.tax))
        self.months.append(self.calculate_shipments())
        print("---")
    
    def calculate_salary(self, sales_amount, price_hour, tax):
        return sales_amount / price_hour * (1 - tax)
    
    def calculate_salary_per_hour(self, salary, worked_hours):
        return salary / worked_hours
    
    def calculate_shipments(self):
        return self.quantity_sold * self.shipments
    
class Production(object):
    def __init__(self, production_amount, efficiency, cost_per_unit, id_department, income, expenses):
        self.production_amount = production_amount
        self.efficiency = efficiency
        self.cost_per_unit = cost_per_unit
        self.id_department = id_department
        self.income = income
        self.expenses = expenses
        self.production = []
        self.revenue = []
        self.profit = []
        self.production_per_month = []
        self.revenue_per_month = []
        self.profit_per_month = []
        self.total_production_amount = []
        self.total_revenue_amount = []
        self.total_profit_amount = []
        self.total_expenses = []
    
    def update_status(self, user, status):
        self.production.append(self.production_amount)
        self.total_production_amount.append(sum(self.production))
        self.revenue.append(self.calculate_revenue(self.production_amount, self.efficiency, self.cost_per_unit))
        self.profit.append(self.calculate_profit(self.revenue[-1], self.expenses))
        self.production_per_month.append(self.calculate_production_per_month())
        self.revenue_per_month.append(self.calculate_revenue_per_month())
        self.profit_per_month.append(self.calculate_profit_per_month())
        print("---")
    
    def calculate_revenue(self, production_amount, efficiency, cost_per_unit):
        return production_amount * efficiency * cost_per_unit
    
    def calculate_profit(self, revenue, expenses):
        return revenue - expenses
    
    def calculate_production_per_month(self):
        return sum(self.production) / 12
    
    def calculate_revenue_per_month(self):
        return sum(self.revenue) / 12
    
    def calculate_profit_per_month(self):   
        return sum(self.profit) / 12
    
    def calculate_total_expenses(self):
        return sum(self.total_expenses) / 12
# Example usage
if __name__ == "__main__":
    # User management example 1
    user1 = User("Alice", 1)
    user2 = User("Bob", 2)
    user3 = User("Charlie", 3)
    user4 = User("David", 4)
    user5 = User("Eve", 5)
    
    user1.updateStatus(1, "Management 1", "Active")
    user2.updateStatus(1, "Management 1", "Inactive")
    user3.updateStatus(1, "Management 1", "Active")
    user4.updateStatus(1, "Management 1", "Inactive")
    user5.updateStatus(1, "Management 1", "Active")
    user5.join_user_management(1, "Management 1")
    user5.updateStatus(1, "Management 1", "Inactive")
    user5.updateStatus(1, "Management 1", "Active")
    user5.join_user_management(1, "Management 1")
    user5.updateStatus(1, "Management 1", "Inactive")
    user5.updateStatus(1, "Management 1", "Active")
    
    # Sales management example 1
    sales1 = Sales(10000, 20, 0.1, 5, 100)
    sales1.update_status(user5, "Active")
    sales1.update_status(user5, "Inactive")
    sales1.update_status(user5, "Active")
    sales1.update_status(user5, "Inactive")
    sales1.update_status(user5, "Active")
    sales1.update_status(user5, "Inactive")
    
    print("Total sales amount:", sales1.total_sales_amount)
    print("Total sales shipments:", sales1.total_sales_shipments)
    print("Salary per hour:", sales1.salary_per_hour)
    print("Salary per month:", sales1.salary_per_month)
    print("Tax per month:", sales1.tax_per_months)
    print("Worked hours:", sales1.worked_hours)
    print("Months:", sales1.months)
    
    # Production management example 1
    production1 = Production(10000, 0.9, 5, 1, 5000, 2000)
    production1.update_status(user5, "Active")
    production1.update_status(user5, "Inactive")
    production1.update_status(user5, "Active")
    production1.update_status(user1, "Inactive")
    production1.update_status(user2, "Active")
    production1.update_status(user3, "Inactive")
    production1.update_status(user4, "Active")
    
    print("Total production amount:", production1.total_production_amount)
    print("Total revenue amount:", production1.total_revenue_amount)
    print("Total profit amount:", production1.total_profit_amount)
    print("Production per month:", production1.production_per_month)
    print("Revenue per month:", production1.revenue_per_month)
    print("Profit per month:", production1.profit_per_month)
    print("Total expenses:", production1.calculate_total_expenses())
