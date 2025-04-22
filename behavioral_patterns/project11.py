# Behavioral patterns - Interpreter in Python -example 01
# Developed by Neobytes.io

import math
import random
from abc import ABC, abstractmethod

class AbstractExpression(ABC):
    @abstractmethod
    def interpret(self, context):
        pass

class TerminalExpression(AbstractExpression):
    def __init__(self, price, quantity, discount):
        self._price = price
        self._quantity = quantity
        self._discount = discount
    
    def interpret(self, context):
        return self._price * self._quantity * (1 - self._discount)

class Calculator(AbstractExpression):
    def __init__(self, left, operator, right):
        self._left = left
        self._operator = operator
        self._right = right
    
    def interpret(self, context):
        if self._operator == '+':
            return self._left.interpret(context) + self._right.interpret(context)
        elif self._operator == '-':
            return self._left.interpret(context) - self._right.interpret(context)
        elif self._operator == '*':
            return self._left.interpret(context) * self._right.interpret(context)
        elif self._operator == '/':
            if self._right.interpret(context) == 0:
                raise ZeroDivisionError('Division by zero is not allowed')
            return self._left.interpret(context) / self._right.interpret(context)
    
    def evaluate(self, context):
        return self.interpret(context)

class Finance(AbstractExpression):
    def __init__(self, price, discount):
        self._price = price
        self._discount = discount
        self._calculator = Calculator(TerminalExpression(price, 1, discount), '*', TerminalExpression(price, 1, 1 - discount))
    
    def interpret(self, context):
        return self._calculator.interpret(context)

class Productivity(AbstractExpression):
    def __init__(self, price, discount):
        self._price = price
        self._discount = discount
        self._calculator = Calculator(TerminalExpression(price, 1, discount), '*', TerminalExpression(price, 1, 1 - discount))
        self._finance_expression = Finance(price, discount)
        self._productivity_score = Calculator(self._finance_expression, '+', self._calculator)
        self._performance_trends = [random.choice(['Good', 'Average', 'Bad']) for _ in range(10)]
    
    def interpret(self, context):
        context['productivity_score'] = self._productivity_score.interpret(context)
        context['performance_trends'] = self._performance_trends
        return context['productivity_score']

def main():
    context = {}

    expre = Productivity(100, 0.1)
    print(expre.interpret(context))
    print(context)
    print(f'Productivity Score: {context["productivity_score"]}')
    print(f'Performance Trends: {context["performance_trends"]}')
    print('---')
    
    expre = Calculator(TerminalExpression(100, 1, 0.1), '+', TerminalExpression(200, 1, 0.2))
    print(expre.interpret(context))
    print(context)
    
    expre = Finance(100, 0.1)
    print(expre.interpret(context))
    print(context)
    print('---')

if __name__ == '__main__':
    main()