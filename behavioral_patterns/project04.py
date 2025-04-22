# Behavioral patterns - Strategy in Python -example 01
# Developed by Neobytes.io

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
import random

class Enterprise():
    
    def __init__(self, name: str, strategy: Strategy, system: Sytem) -> None:
        
        self.strategy = strategy
        self.system = system
    
    @property
    def strategy(self) -> Strategy:
        
        return self._strategy
    
    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy
    
    def execute_strategy(self) -> str:
        
        print("Enterprise: executing strategy for special departments...")
        result = self._strategy.do_algorithm(["a", "b", "c","d", "e"])        
        print(",".join(result))
    
    @property
    def system(self) -> Sytem:
        return self._system

    @system.setter
    def system(self, system: Sytem) -> None:
        self._system = system
    
    def execute_system(self) -> str:
        print("Enterprise: executing system...")
        result = self._system.do_algorithm(["a", "b", "c", "d", "e", 3, 2, 1, 5, 4, 6, 7, 8])
        print(",".join(result))

class Strategy(ABC):
    
    @abstractmethod
    def do_algorithm(self, data: List):
        pass

class Sytem(ABC):
    @abstractmethod
    def do_algorithm(self, data:List) -> str:
        pass

class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data: List) -> List:
        return sorted(data)

class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data: List) -> List:
        return sorted(data, reverse=True)
        
class ConcreteSystemA(Sytem):
    def do_algorithm(self, data: List) -> str:
        return "System A: " + ",".join(map(str, data))
    
class ConcreteSystemB(Sytem):
    def do_algorithm(self, data: List) -> str:
        return "System B: " + ",".join(map(str, data))
class SelectStrategy(object):
    def select_strategy(self, strategy_type: str) -> Strategy:
        if strategy_type == "A":
            return ConcreteStrategyA()
        elif strategy_type == "B":
            return ConcreteStrategyB()
        else:
            raise ValueError("Invalid strategy type")
    
    def select_system(self, system_type: str) -> Sytem:
        if system_type == "A":
            return ConcreteSystemA()
        elif system_type == "B":
            return ConcreteSystemB()
        else:
            raise ValueError("Invalid system type")
# Usage
if __name__ == "__main__":
    
    enterprise_a = Enterprise("Enterprise A", ConcreteStrategyA(), ConcreteSystemA())
    print("Enterprise A:")
    enterprise_a.execute_strategy()
    enterprise_a.execute_system()
    print()
    
    enterprise_b = Enterprise("Enterprise B", ConcreteStrategyB(), ConcreteSystemB())
    print("Enterprise B:")
    enterprise_b.execute_strategy()
    enterprise_b.execute_system()
    print()
    
    select_strategy = SelectStrategy()
    strategy_a = select_strategy.select_strategy("A")
    system_a = select_strategy.select_system("A")
    enterprise_c = Enterprise("Enterprise C", strategy_a, system_a)
    print("Enterprise C:")
    enterprise_c.execute_strategy()
    enterprise_c.execute_system()
    print()
    strategy_b = select_strategy.select_strategy("B")
    system_b = select_strategy.select_system("B")
    enterprise_d = Enterprise("Enterprise D", strategy_b, system_b)
    print("Enterprise D:")
    enterprise_d.execute_strategy()
    enterprise_d.execute_system()
    print()
