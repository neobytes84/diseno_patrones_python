# Behavioral patterns - Templates in Python - Example 01
# Developed by Neobytes.io


from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional

class AbstractClassTemplate(ABC):
    
    
    def template_method(self) -> None:
        
        self.base_operation1()
        self.required_operations1()
        self.removed_operation1()
        self.base_operation2()
        self.hook_operation1()
        self.removed_operation2()
        self.required_operations2()
        self.base_operation3()
        self.hook_operation2()
    
    def base_operation1(self) -> None:
        print("AbstractClass says: I am doing the base operation 1.")
    
    def base_operation2(self) -> None:
        print("AbstractClass says: I am doing the base operation 2.")
    
    def base_operation3(self) -> None:
        print("AbstractClass says: I am doing the base operation 3.")
    
    # These operations can be replaced by subclasses
    @abstractmethod
    def required_operations1(self) -> None:
        pass
    
    @abstractmethod
    def required_operations2(self) -> None:
        pass
    
    # These are "hooks". Subclasses can override them. But it's not mandatory to implement them
    # since the hooks already have default implementations. Hooks can also be used to add new operations without breaking the existing code
    # provided additional extensions points in some crucial  places of the algorithm.
    
    def hook_operation1(self) -> Optional[Any]:
        pass
    
    def hook_operation2(self) -> Optional[Any]:
        pass
    
    def removed_operation1(self) -> None:
        print("AbstractClass says: I am doing the removed operation 1.")
        print("This operation is not implemented in the base class.")
    def removed_operation2(self) -> None:
        print("AbstractClass says: I am doing the removed operation 2.")
        print("This operation is not implemented in the base class.")
        print("This operation has been removed.")

class ConcreteClass1(AbstractClassTemplate):
    
    def required_operations1(self) -> None:
        print("ConcreteClass1 says: I am doing required operation 1.")
        
    def required_operations2(self):
        print("ConcreteClass1 says: I am doing required operation 2.")
        
    def hook_operation1(self):
        print("ConcreteClass1 says: I am doing hook operation 1.")
    
    def removed_operation1(self):
        print("ConcreteClass1 says: I am doing removed operation 1.")
        print("This operation is not implemented in the base class.")
    
    def removed_operation2(self):
        print("ConcreteClass1 says: I am doing removed operation 2.")
        print("This operation is not implemented in the base class.")

class ConcreteClass2(AbstractClassTemplate):
    def required_operations1(self) -> None:
        print("ConcreteClass2 says: I am doing required operation 1.")
        
    def required_operations2(self) -> None:
        print("ConcreteClass2 says: I am doing required operation 2.")
        
    def hook_operation1(self) -> Optional[Any]:
        print("ConcreteClass2 says: I am doing hook operation 1.")

def client_code(abst_class: AbstractClassTemplate) -> None:
    abst_class.template_method()

if __name__ == "__main__":
    print("Client: Let's create an instance of ConcreteClass1 and call the template method:")
    client_code(ConcreteClass1())
    print("\n")
    
    print("Client: Let's create an instance of ConcreteClass2 and call the template method:")
    client_code(ConcreteClass2())
    print("\n")
