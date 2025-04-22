# Structural Patterns - Adapter
# Conceptual Example (via inheritance)
# Developed by Neobytes.io

class TargetInterface:
    def request(self):
        return "Target: The default target's behavior"

class Adaptee:
    
    def specific_request(self) -> str:
        return "Adaptee: (Specific) I can do the work"

class Adapter(TargetInterface, Adaptee):
    
    def request(self) -> str:
        return "Adapter: (TRANSLating) I am adapting the request." + self.specific_request()
    
def client_code(target: TargetInterface) -> None:
    print(target.request(), end="")

# Create instances and use them

if __name__ == "__main__":
    print("Client: I can work with the target interface.")
    target = TargetInterface()
    client_code(target)
    print("\n")
    
    adaptee = Adaptee()
    print("Client: I can work with the adaptee interface." 
          "See what happens.")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")
    
    print("Client: I can work with the adapter interface." )
    adapter = Adapter()
    client_code(adapter)