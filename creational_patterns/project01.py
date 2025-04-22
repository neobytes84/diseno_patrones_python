# Creational patterns - Abstract factory in Python - Example 01
# Developed by Neobytes.io
import random
from itertools import product, permutations, combinations


class EnterpriseSystem:
    def __init__(self, productions_factory: None):
        self.production_factory = productions_factory
    
    def show_product(self):
        products  = self.production_factory()
        
        print(f'Enterprise System:{products}')
        print(f'Product: {products.price()}')
        print(f'Description: {products.description()}')
        print(f'Vendor: {products.vendor()}')
        print(f'Shipment Date: {products.shipment_date()}')
        print(f'Quantity: {products.quantity()}')
        print()
    
    def generate_operations(self):
        operations = ['Create', 'Update', 'Delete']
        return random.choice(operations)
        
    def generate_products(self):
        product_types = [EnterpriseProductA1, EnterpriseProductA2]
        return random.choice(product_types)()
    
    def generate_product_types(self):
        product_types = [EnterpriseProductA1, EnterpriseProductA2]
        return random.choice(product_types)()
    
    def generate_product_variants(self):
        product_variants = [EnterpriseProductA1, EnterpriseProductA2]
        return random.choice(product_variants)()
    
    def generate_product_variants_combinations(self):
        product_variants = [EnterpriseProductA1, EnterpriseProductA2]
        return list(combinations(product_variants, 2))
    
    def generate_product_variants_permutations(self):
        product_variants = [EnterpriseProductA1, EnterpriseProductA2]
        return list(permutations(product_variants, 3))
    
    
class EnterpriseProductA1:
    
    def price(self):
        return 5500
    
    def description(self):
        return "Software level 1"
    
    def vendor(self):
        return "Vendor A"
    
    def shipment_date(self):
        return "10th October 2022"
    
    def quantity(self):
        return 100
    
    def __str__(self):
        return "Enterprise Product A1"

class EnterpriseProductA2:
    def price(self):
        return 6000
    
    def description(self):
        return "Software level 2"
    
    def vendor(self):
        return "Vendor B"
    
    def shipment_date(self):
        return "10th October 2023"
    
    def quantity(self):
        return 150
    
    def __str__(self):
        return "Enterprise Product A2"
    
class EnterpriseProductB1:
    def price(self):
        return 7000
    
    def description(self):
        return "Hardware level 1"
    
    def vendor(self):
        return "Vendor C"
    
    def shipment_date(self):
        return "10th October 2024"
    
    def quantity(self):
        return 200

    def __str__(self):
        return "Enterprise Product B1"

class EnterpriseProductB2:
    def price(self):
        return 7500
    
    def description(self):
        return "Hardware level 2"
    
    def vendor(self):
        return "Vendor D"
    
    def shipment_date(self):
        return "10th October 2025"
    
    def quantity(self):
        return 250
    
    def __str__(self):
        return "Enterprise Product B2"


def random_product_factory():
    return random.choice([EnterpriseProductA1, EnterpriseProductA2, EnterpriseProductB1, EnterpriseProductB2])()



if __name__ == "__main__":
    # Create a products
    products = EnterpriseSystem(random_product_factory)
    
    for i in range(10):
        products.show_product()
        print("-------------------")
    
    # Generate operations
    operations = products.generate_operations()
    print(f"Generated Operation: {operations}")
    
    # Generate product types
    product_types = products.generate_product_types()
    print(f"Generated Product Type: {product_types}")
    
    # Generate product variants
    product_variants = products.generate_product_variants()
    print(f"Generated Product Variants: {product_variants}")
    
    # Generate product variants combinations
    product_variants_combinations = products.generate_product_variants_combinations()
    print(f"Generated Product Variants Combinations: {product_variants_combinations}")
    
    # Generate product variants permutations
    product_variants_permutations = products.generate_product_variants_permutations()
    print(f"Generated Product Variants Permutations: {product_variants_permutations}")

    
