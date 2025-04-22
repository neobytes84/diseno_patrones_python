# Structural patterns - Composite in Python - Example 01
# Developed by Neobytes.io


class Developer:
    def __init__(self, *args):
        self.position = args[0]

    def ShowDetails(self):
        print("\t",end="")
        print(self.position)

class SoftwareComposite:
    def __init__(self, *args):
        self.position = args[0]
        self.children = []
    
    def add(self, child):
        self.children.append(child)
    
    def remove(self, child):
        self.children.remove(child)
    
    def ShowDetails(self):
        print(self.position)
        for child in self.children:
            print("\t",end="")
            child.ShowDetails()

class Salary:
    def __init__(self, *args):
        self.position = args[0]
        self.children = []
    def add_salary(self, child):
        self.children.append(child)
    
    def remove(self, child):
        self.children.remove(child)
    
    def ShowDetails(self):
        print(self.position)
        for child in self.children:
            print("\t",end="")
            child.ShowDetails()
        
# Test the code
if __name__ == "__main__":
    # Create a software composite object
    TopLevelDeveloper = SoftwareComposite("Top Level Developer")
    MiddleLevelDeveloper = SoftwareComposite("Middle Level Developer")
    SeniorDeveloper = SoftwareComposite("Senior Developer")
    JuniorDeveloper = SoftwareComposite("Junior Developer")
    JuniorDeveloper1 = Developer("Junior Developer 1")
    JuniorDeveloper2 = Developer("Junior Developer 2")
    MiddleLevelDeveloper1 = Developer("Middle Level Developer 1")
    MiddleLevelDeveloper2 = Developer("Middle Level Developer 2")
    SeniorDeveloper1 = Developer("Senior Developer 1")
    SeniorDeveloper2 = Developer("Senior Developer 2")
    SeniorDeveloper3 = Developer("Senior Developer 3")
    
    # Add developers to the composite structure
    TopLevelDeveloper.add(MiddleLevelDeveloper)
    TopLevelDeveloper.add(SeniorDeveloper)
    MiddleLevelDeveloper.add(JuniorDeveloper)
    MiddleLevelDeveloper.add(MiddleLevelDeveloper1)
    MiddleLevelDeveloper.add(MiddleLevelDeveloper2)
    SeniorDeveloper.add(SeniorDeveloper1)
    SeniorDeveloper.add(SeniorDeveloper2)
    SeniorDeveloper.add(SeniorDeveloper3)
    
    # Show the details of the composite structure
    print("Composite Structure:")
    TopLevelDeveloper.ShowDetails()
    print("\n")
    
    # Add salaries to the composite structure
    SalaryStructure = Salary("Salary Structure")
    MiddleSalary = Salary("Middle Salary")
    JuniorSalary = Salary("Junior Salary")
    SeniorSalary = Salary("Senior Salary")
    JuniorSalary1 = Developer("Junior Developer 1")
    JuniorSalary2 = Developer("Junior Developer 2")
    MiddleSalary1 = Developer("Middle Level Developer 1")
    MiddleSalary2 = Developer("Middle Level Developer 2")
    
    # Add developers to the salary structure

    MiddleSalary.add_salary(MiddleSalary1)
    MiddleSalary.add_salary(MiddleSalary2)
    JuniorSalary.add_salary(JuniorSalary1)
    JuniorSalary.add_salary(JuniorSalary2)
    SeniorSalary.add_salary(SeniorDeveloper1)
    SeniorSalary.add_salary(SeniorDeveloper2)
    SeniorSalary.add_salary(SeniorDeveloper3)
    
    # Show the details of the salary structure
    print("Salary Structure:")
    SalaryStructure.ShowDetails()
    print("\n")
    
    # Remove a developer from the composite structure
    TopLevelDeveloper.remove(MiddleLevelDeveloper)
    print("Composite Structure after removing Middle Level Developer:")
    TopLevelDeveloper.ShowDetails()
    print("\n")
    
    # Show the details of the salary structure
    print("Salary Structure:")
    SalaryStructure.ShowDetails()
    print("\n")
