# Structural patterns - Bridge in Python - Example 01
# Developed by Neobytes.io

from __future__ import annotations
from abc import ABC, abstractmethod

class Abstraction:
    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation
    
    def operation(self) -> str:
        return(f"Abstraction: Requesting from implementation:\n"
               f"{self.implementation.operation_implementation()}")

class ExtendedAbstraction(Abstraction):
    
    def operation(self) -> str:
        return(f"ExtendedAbstraction: Requesting from implementation:\n"
               f"{self.implementation.operation_implementation()}")

class Implementation(ABC):
    @abstractmethod
    def operation_implementation(self) -> str:
        pass

class ConcreteImplementationA(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationA: Operation implemented"

class ConcreteImplementationB(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationB: Operation implemented"

class ConcreteImplementationC(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationC: Operation implemented"

class ConcreteExtendedImplementationA(ExtendedAbstraction):
    def extended_operation_implementation(self) -> str:
        return "ConcreteExtendedImplementationA: Extended operation implemented"

class ConcreteExtendedImplementationB(ExtendedAbstraction):
    def extended_operation_implementation(self) -> str:
        return "ConcreteExtendedImplementationB: Extended operation implemented"

class ConcreteExtendedImplementationC(ExtendedAbstraction):
    def extended_operation_implementation(self) -> str:
        return "ConcreteExtendedImplementationC: Extended operation implemented"

def client_code(abstraction: Abstraction, extended_abstraction: ExtendedAbstraction) -> None:
    print(abstraction.operation(), end="\n")
    print(extended_abstraction.operation(), end="")

if __name__ == "__main__":
    concrete_implementation_a = ConcreteImplementationA()
    abstraction = Abstraction(concrete_implementation_a)
    client_code(abstraction, abstraction)
    print("\n")
    
    concrete_implementation_b = ConcreteImplementationB()
    extended_abstraction = ExtendedAbstraction(concrete_implementation_b)
    client_code(abstraction, extended_abstraction)
    print("\n")
    
    concrete_implementation_c = ConcreteImplementationC()
    extended_abstraction = ExtendedAbstraction(concrete_implementation_c)
    client_code(abstraction, extended_abstraction)
    print("\n")

