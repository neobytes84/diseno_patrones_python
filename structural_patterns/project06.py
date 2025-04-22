# Structural patterns - Flyweight in Python - Example 02
# Developed by Neobytes.io

import json
from typing import Dict

class VehicleFactory:
    def __init__(self, shared_state: str) -> None:
        self.shared_state = shared_state
        self.load_vehicles = None
        self.create_vehicles = None
        self.buy_vehicles = None
        self.display_vehicles = None
        self.display_shared_state = None
        self.display_expensive_state = None
        self.display_change_state = None
        self.display_update_state = None
    
    def operation(self, unique_state: Dict) -> str:
        s = json.dumps(self.shared_state)
        u = json.dumps(unique_state)
        print(f"VehicleFactory: Displaying shared state {s} and unique state {u}", end="")
        
    def set_load_vehicles(self, state: Dict) -> None:
        self.load_vehicles = state
        print(f", and load vehicles {json.dumps(state)}")
    
    def set_create_vehicles(self, state: Dict) -> None:
        self.create_vehicles = state
        print(f", and create vehicles {json.dumps(state)}")
    
    def set_buy_vehicles(self, state: Dict) -> None:
        self.buy_vehicles = state
        print(f", and buy vehicles {json.dumps(state)}")
    
    def set_display_vehicles(self, state: Dict) -> None:    
        self.display_vehicles = state
        print(f", and display vehicles {json.dumps(state)}")
    
    def set_display_shared_state(self, state: Dict) -> None:
        self.display_shared_state = state
        print(f", and display shared state {json.dumps(state)}")
    
    def set_display_expensive_state(self, state: Dict) -> None:
        self.display_expensive_state = state
        print(f", and display expensive state {json.dumps(state)}")
    
    def set_display_change_state(self, state: Dict) -> None:
        self.display_change_state = state
        print(f", and display change state {json.dumps(state)}")
    
    def set_display_update_state(self, state: Dict) -> None:
        self.display_update_state = state
        print(f", and display update state {json.dumps(state)}")

class FlyweightFactory():
    _flyweights: Dict[str, VehicleFactory] = {}
    

    def __init__(self, initial_flyweights: Dict) -> None:
        for state in initial_flyweights:
            self._flyweights[self.get_key(state)] = VehicleFactory(state)
    
    def get_key(self, state: Dict) -> str:
        return "_".join(sorted(state))
    
    def get_flyweight(self, shared_state: Dict) -> VehicleFactory:
        key = self.get_key(shared_state)
        
        if key not in self._flyweights:
            print("FlyweightFactory: Can't find a flyweight, creating new one.")
            self._flyweights[key] = VehicleFactory(shared_state)
        else:
            print("FlyweightFactory: Reusing existing flyweight.")
        return self._flyweights[key]
    
    def list_flyweights(self) -> None:
        count = len(self._flyweights)
        print(f"FlyweightFactory: I have {count} flyweights.")
        print("\n".join(map(str, self._flyweights.keys())), end="")

def add_database_to_factory(
    factory: FlyweightFactory, price: str, owner: str, brand: str, model: str, color: str, 
    year: str, fuel_type: str, capacity: str,cruise_speed: str
    ) -> None:
    print("\n\Client: Adding vehicle to database system: ...")
    flyweight = factory.get_flyweight([ price, owner, brand,  model,  color, year, fuel_type, capacity, cruise_speed])
    flyweight.set_load_vehicles({"fuel_type": fuel_type, "capacity": capacity, "cruise_speed": cruise_speed})
    flyweight.set_create_vehicles({"brand": brand, "model": model, "color": color, "year": year})
    flyweight.set_buy_vehicles({"price": price, "owner": owner})
    flyweight.set_display_vehicles({"brand": brand, "model": model, "color": color, "year": year})
    flyweight.set_display_shared_state({"price": price, "owner": owner, "brand": brand, "model": model, "color": color, "year": year})
    flyweight.set_display_expensive_state({"price": price})
    flyweight.set_display_change_state({"color": color})
    flyweight.set_display_update_state({"year": "2020"})
    flyweight.operation({"brand": brand, "owner": "John Doe"})
    print("\n")
            
if __name__ == "__main__":
    initial_flyweights = [
        {"price": "10000", "owner": "John Doe", "brand": "Toyota", "model": "Camry", "color": "Red", "year": "2018", "fuel_type": "Gasoline", "capacity": "50", "cruise_speed": "120"},
        {"price": "20000", "owner": "Jane Doe", "brand": "Honda", "model": "Civic", "color": "Blue", "year": "2020", "fuel_type": "Electric", "capacity": "60", "cruise_speed": "150"},
        {"price": "30000", "owner": "David Johnson", "brand": "Ford", "model": "Mustang", "color": "Black", "year":"2023", "fuel_type": "Gasoline", "capacity": "55", "cruise_speed": "130"},
        {"price": "10000", "owner": "John Doe", "brand": "Toyota", "model": "Camry", "color": "Red", "year": "2018", "fuel_type": "Gasoline", "capacity": "50", "cruise_speed": "120"},
        {"price": "20000", "owner": "Jane Doe", "brand": "Honda", "model": "Civic", "color": "Blue", "year": "2020", "fuel_type": "Electric", "capacity": "60", "cruise_speed": "150"},
        {"price": "30000", "owner": "David Johnson", "brand": "Ford", "model": "Mustang", "color": "Black", "year":"2023", "fuel_type": "Gasoline", "capacity": "55", "cruise_speed": "130"},
        #... more vehicles...
    ]
    
    factory = FlyweightFactory(initial_flyweights)
    factory.list_flyweights()
    add_database_to_factory(factory, "10000", "John Doe", "Toyota", "Camry", "Red", "2018", "Gasoline", "50", "120")
    add_database_to_factory(factory, "20000", "Jane Doe", "Honda", "Civic", "Blue", "2020", "Electric", "60", "150")
    factory.list_flyweights()
    print("\n")
    
        