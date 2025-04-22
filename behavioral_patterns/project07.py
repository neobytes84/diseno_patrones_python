# Behavioral patterns - Iterator in Python -example 01
# Developed by Neobytes.io

import pandas as pd
import random
import itertools
import datetime
import csv

def creator_iterato1():
    
    microservices = [chr(random.randint(97, 122)) for _ in range(10)] 
    
    for i, microservice in enumerate(microservices):
        yield f"Microservice {i+1}: {microservice}"
        if i % 3 == 2:
            yield "---"

# Create an instance of the iterator
def create_iterator2():
    
    microfrontends = [chr(random.randint(97, 122)) for _ in range(10)]
    for i, microfrontend in enumerate(microfrontends):
        yield f"Microfrontend {i+1}: {microfrontend}"
        if i % 3 == 2:
            yield "---"

# Create an instance of the iterator

def create_iterator3():
    
    databases = [chr(random.randint(97, 122)) for _ in range(10)]
    for i, database in enumerate(databases):
        yield f"Database {i+1}: {database}"

# Example usage

if __name__ == "__main__":
    
    # Create an instance of the iterator
    iterator1 = creator_iterato1()
    iterator2 = create_iterator2()
    iterator3 = create_iterator3()
    # Print the elements of the iterator
    for item in itertools.chain(iterator1, iterator2, iterator3):
        print(item)
        if item == "---":
            print("\n")
            
    # Write the elements of the iterator to a CSV file
    with open("output.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Type", "Name"])
        for item in itertools.chain(iterator1, iterator2, iterator3):
            writer.writerow(["Iterator", item])
            
    # Print the current date and time
    print(f"\nCurrent date and time: {datetime.datetime.now()}")
    
