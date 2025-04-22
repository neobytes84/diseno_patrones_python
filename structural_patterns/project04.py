# Structural patterns - Bridge in Python - Example 02
# Developed by Neobytes.io

class ProducingAPI1:
    def produce_item(self, price, quantity, quality, location):
        # Implementation for producing item using API 1
        print(f"Producing item with price: {price}, quantity: {quantity}, quality: {quality}, location: {location}")

class ProducingAPI2:
    
    def produce_item(self, price, quantity, quality, location):
        # Implementation for producing item using API 2
        print(f"Producing item with price: {price}, quantity: {quantity}, quality: {quality}, location: {location}")

class ProducingAPIBridge:
    def __init__(self, api, price, quantity, quality, location):
        
        self._api = api
        self._price = price
        self._quantity = quantity
        self._quality = quality
        self._location = location
        
    def produce_item(self):
        self._api.produce_item(self._price, self._quantity, self._quality, self._location)
    
    def view_api(self, new_api):
        self._api = new_api
        self.produce_item()
        print("Expanded API has been used")
    
    def change_api_version(self, new_api_class):
        self._api = new_api_class()
        self.produce_item()
        print("API version has been changed")
    
    def expand(self, times):
        
        self._price = self._price * times
        self._quantity = self._quantity * times
        self._quality = self._quality * times
        self._location = self._location + f" ({times} times expanded)"

# Example usage:

api1 = ProducingAPI1()
api2 = ProducingAPI2()

bridge = ProducingAPIBridge(api1, 10, 5, 90, "New York")
bridge.produce_item()

bridge.view_api(api2)

bridge.change_api_version(ProducingAPI1)

bridge.expand(3)

bridge2 = ProducingAPIBridge(api1, 20, 10, 80, "Los Angeles")

bridge2.produce_item()

bridge2.view_api(api2)

bridge2.change_api_version(ProducingAPI2)

bridge2.expand(2)
