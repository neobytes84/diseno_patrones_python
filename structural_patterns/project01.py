# Structural patterns - Flyweight in Python
# Developed by Neobytes.io

import json
from typing import Dict

class Flyweight():
    def __init__(self, shared_state: str) -> None:
        self.shared_state = shared_state
        self.expensive_state = None
        self.change_state = None
        self.update_state = None
        
    def operation(self, unique_state: str) -> str:
        s = json.dumps(self.shared_state)
        u = json.dumps(unique_state)
        print(f"Flyweight: Displaying shared state {s} and unique state {u}", end="")
        
    def set_expensive_state(self, state: Dict) -> None:
        self.expensive_state = state
        print(f", and expensive state {json.dumps(state)}")
        
    def set_change_state(self, state: Dict) -> None:
        self.change_state = state
        print(f", and change state {json.dumps(state)}")
    
    def set_update_state(self, state: Dict) -> None:
        self.update_state = state
        print(f", and update state {json.dumps(state)}")
        
class FlyweightFactory():
    
    _flyweights: Dict[str, Flyweight] = {}
    
    def __init__(self, initial_flyweights: Dict) -> None:
        for state in initial_flyweights:
            self._flyweights[self.get_key(state)] = Flyweight(state)
    
    def get_key(self, state: Dict) -> str:
        
        
        return "_".join(sorted(state))
    def get_flyweight(self, shared_state: Dict) -> Flyweight:
        
        key = self.get_key(shared_state)
        
        if key not in self._flyweights:
            print("FlyweightFactory: Can't find a flyweight, creating new one.")
            self._flyweights[key] = Flyweight(shared_state)
        else:
            print("FlyweightFactory: Reusing existing flyweight.")
        return self._flyweights[key]
    
    def list_flyweights(self) -> None:
        count = len(self._flyweights)
        print(f"FlyweightFactory: I have {count} flyweights.")
        print("\n".join(map(str, self._flyweights.keys())), end="")
    
def add_car_to_police_database(
        factory: FlyweightFactory, plates: str, owner: str,
        brand: str, model: str, color: str, year: str, price: str
    )-> None:
        print("\n\nClient: Adding a car to police database...")
        flyweight = factory.get_flyweight([brand, model, color, year])
        flyweight.set_expensive_state({"price": price})
        flyweight.set_change_state({"color": "Green"})  # Simulating change in color
        flyweight.set_update_state({"year": "2020"})  # Simulating update in year
        flyweight.operation({"plate": plates, "owner": owner})
        print("\n")

if __name__ == "__main__":
        
        factory = FlyweightFactory([
            ["Toyota", "Camry", "Red", "2010", "25000"],
            ["Honda", "Accord", "Blue", "2015", "30000"],
            ["Ford", "Mustang", "Black", "2018", "40000"],
            ["Toyota", "Camry", "Red", "2010", "25000"],
            ["Honda", "Accord", "Blue", "2015", "30000"],
            
        ])
        factory.list_flyweights()
        add_car_to_police_database(factory, "ABC123", "John Doe", "Toyota", "Camry", "Red", "2010", "25000")
        add_car_to_police_database(factory, "DEF456", "Jane Smith", "Honda", "Accord", "Blue", "2015", "30000")
        
        print("\n\nClient: Requesting the same car...")
        
        factory.list_flyweights()