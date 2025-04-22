# Creational patterns - Singleton in Python - Example 02
# Developed by Neobytes.io

import json
import os

class Singleton:
    _instance = {}
    
    def __new__(cls, *args, **kwargs):
        
        if cls not in cls._instance:
            cls._instance[cls] = super().__new__(cls)
            cls._instance[cls].data = {}
        return cls._instance[cls]
    
    def load_data(self, filename: str) -> None:
        filepath = os.path.join(os.path.dirname(__file__), filename)
        
        if os.path.isfile(filepath):
            with open(filepath, 'r') as file:
                self.data = json.load(file)
                print(f"Data loaded from {filepath}")
                print(f"Current data: {json.dumps(self.data, indent=4)}")
                print("---")
    def save_data(self, filename: str) -> None:
        filepath = os.path.join(os.path.dirname(__file__), filename)
        
        with open(filepath, 'w') as file:
            json.dump(self.data, file, indent=4)
            print(f"Data saved to {filepath}")
            print("---")
            print(f"Current data: {json.dumps(self.data, indent=4)}")
            print("---")

class SingletonOperations(Singleton):
    def some_operation(self) -> None:
        print("Singleton operations are performed...")
        print(f"Current data: {json.dumps(self.data, indent=4)}")
        print("---")
    def add_data(self, key: str, value: str) -> None:
        self.data[key] = value
        print(f"Data updated: {key} -> {value}")
        print(f"Current data: {json.dumps(self.data, indent=4)}")
        print("---")
    
    def delete_data(self, key: str) -> None:
        if key in self.data:
            del self.data[key]
            print(f"Data deleted: {key}")
            print(f"Current data: {json.dumps(self.data, indent=4)}")
            print("---")
        else:
            print(f"Key '{key}' not found.")
            print("---")
    
    def create_report(self) -> None:
        print("Creating report...")
        print(f"Current data: {json.dumps(self.data, indent=4)}")
        print("---")
        print("Report created.")
        print("---")

# Example usage

if __name__ == "__main__":
    # Create singleton instances
    singleton1 = SingletonOperations()
    singleton2 = SingletonOperations()
    
    # Load and save data
    singleton1.load_data("data.json")
    singleton1.save_data("data_updated.json")
    print("---")
    
    # Perform operations
    singleton1.some_operation()
    singleton1.add_data("key1", "value1")
    singleton1.delete_data("key1")
    singleton2.add_data("key2", "value2")
    singleton2.create_report()
    print("---")
    
    # Check data consistency
    print(f"singleton1 data: {json.dumps(singleton1.data, indent=4)}")
    print(f"singleton2 data: {json.dumps(singleton2.data, indent=4)}")
    print("---")
    print("Data consistency checked.")
    print("---")