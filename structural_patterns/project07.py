# Structural patterns - Decorator in Python
# Developed by Neobytes.io
import csv
import json
import math 
import functools
import requests

class LoggingDecorator:
    def __init__(self, func):
        self.func = func
        self.log_file = open('logs.txt', 'a')
        functools.update_wrapper(self, func)
        self.log_file.write(f'Function {self.func.__name__} started.\n')
        self.log_file.flush()
        print(f'Function {self.func.__name__} started.')
        
    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        self.log_file.write(f'Function {self.func.__name__} completed with result: {json.dumps(result)}.\n')
        self.log_file.flush()
        print(f'Function {self.func.__name__} completed with result: {json.dumps(result)}.')
        return result
    
    def __del__(self):
        self.log_file.write(f'Function {self.func.__name__} ended.\n')
        self.log_file.close()
        print(f'Function {self.func.__name__} ended.')
    
    @staticmethod
    def decorator_factory(logging_level):
        def decorator(func):
            if logging_level == 'debug':
                return LoggingDecorator(func)
            elif logging_level == 'info':
                return func
            else:
                raise ValueError('Invalid logging level')
        return decorator
    @staticmethod
    def log_to_file(filename):
        def decorator(func):
            def wrapper(*args, **kwargs):
                log_file = open(filename, 'a')
                log_file.write(f'Function {func.__name__} started.\n')
                log_file.flush()
                print(f'Function {func.__name__} started.')
                result = func(*args, **kwargs)
                log_file.write(f'Function {func.__name__} completed with result: {json.dumps(result)}.\n')
                log_file.flush()
                print(f'Function {func.__name__} completed with result: {json.dumps(result)}.')
                log_file.close()
                return result
            return wrapper
        return decorator
    @staticmethod
    def log_to_api(api_url):
        def decorator(func):
            def wrapper(*args, **kwargs):
                response = requests.post(api_url, json={'function': func.__name__, 'args': args, 'kwargs': kwargs})
                if response.status_code == 200:
                    result = response.json()['result']
                    print(f'Function {func.__name__} completed with result: {json.dumps(result)}.')
                    return result
                else:
                    print(f'Error logging function {func.__name__}. Response status code: {response.status_code}')
                    return None
            return wrapper
        return decorator
    @staticmethod
    def export_csv(filename):
        def decorator(func):
            def wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                with open(filename, 'w', newline='') as csvfile:
                    fieldnames = ['Function', 'Args', 'Result']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerow({'Function': func.__name__, 'Args': args, 'Result': json.dumps(result)})
                print(f'Function {func.__name__} completed and results exported to {filename}.')
                return result
            return wrapper
        return decorator
    @staticmethod
    def export_to_json(filename):
        def decorator(func):
            def wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                with open(filename, 'w') as jsonfile:
                    json.dump(result, jsonfile)
                print(f'Function {func.__name__} completed and results exported to {filename}.')
                return result
            return wrapper
        return decorator

if __name__ == '__main__':
    @LoggingDecorator.decorator_factory('debug')
    def add(a, b):
        return a + b
    
    @LoggingDecorator.log_to_file('debug_logs.txt')
    def subtract(a, b):
        return a - b
    
    @LoggingDecorator.log_to_api('http://example.com/logging_api')
    def multiply(a, b):
        return a * b
    
    @LoggingDecorator.export_csv('results.csv')
    def divide(a, b):
        if b == 0:
            raise ZeroDivisionError('Cannot divide by zero')
        return a / b
    
    @LoggingDecorator.export_to_json('results.json')
    def square_root(n):
        if n < 0:
            raise ValueError('Cannot calculate square root of a negative number')
        return math.sqrt(n)
    
    print(add(5, 3))
    
    print(subtract(5, 3))
    print(multiply(5, 3))
    print(square_root(9))
    print(divide(10, 5))
    print(square_root(120))
    print(multiply(5, 3))
    print(divide(10, 2))