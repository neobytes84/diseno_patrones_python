# Structural patterns - Proxy in Python - Example 01
# Developed by Neobytes.io

from abc import ABC, abstractmethod

class Component(ABC):
    
    @abstractmethod
    def request(self) -> None:
        pass
    @abstractmethod
    def add(self, component) -> None:
        pass

class Leaf(Component):
    
    def request(self) -> None:
        print("Leaf component processed.")
        
    def add(self, component) -> None:
        print("Cannot add components to a leaf.")

class Proxy(Component):
    
    def __init__(self, real_component: Component) -> None:
        self.real_component = real_component
    
    def request(self) -> None:
        if self.check_access():
            self.real_component.request()
            self.log_access()
    
    def add(self, component) -> None:
        print("Cannot add components to the proxy.")
        if self.check_access():
            self.real_component.add(component)
            self.log_access()
    def check_access(self) -> bool:
        print("Checking access...")
        return True  # Replace with actual access control logic
    
    def log_access(self) -> None:
        print("Logging access...", end="")

def client_code(component : Component) -> None:
    component.request()
    component.add(Leaf())
    print("\n")

if __name__ == "__main__":
    print("Client: I want to use a proxy to access a complex object:")
    simple_proxy = Proxy(Leaf())
    client_code(simple_proxy)
    print("\n")
    
    print("Client: I want to use the real object directly:")
    real_object = Leaf()
    client_code(real_object)