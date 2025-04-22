# Behavioral patterns - Observer in Python
# Developed by Neobytes.io

from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List

class Subject(ABC):
    
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass
    
    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass
    
    @abstractmethod
    def notify(self) -> None:
        pass
    
class ConcreteSubject(Subject):
    
    _state: int = 0
    
    _observers: List[Observer] = []
    
    def attach(self, observer: Observer) -> None:
        print("Subject attaching observer.")
        self._observers.append(observer)
    
    def detach(self, observer: Observer) -> None:
        print("Subject detaching observer.")
        self._observers.remove(observer)
    
    def notify(self) -> None:
        
        print("Subject notifying observers...")
        for observer in self._observers:
            observer.update(self)
    
    def send_message(self, message: str) -> None:
        
        print(f"Subject: Message received: {message}")
        for observer in self._observers:
            observer.update(self)
    
    
    def some_business_logic(self) -> None:
        
        print("Subject: I'm doing something important...")
        self._state = randrange(0, 10)
        print("\n")
        
        print(f"Subject: My state has changed to: {self._state}")
        self.notify()
        print("\n")
        
        print("Subject: I've just sent a message: 'Hello, World!'")
        self.send_message("Hello, World!")
        print("\n")
  

class Observer(ABC):
    
    @abstractmethod
    def update(self, subject: Subject) -> None:
        
        pass

class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state < 3:
            print("ConcreteObserverA: Reacted to the event.")

class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 0 or subject._state >= 2:
            print("ConcreteObserverB: Reacted to the event.")

if __name__ == "__main__":
    # The client code
    subject = ConcreteSubject()
    
    observer_a = ConcreteObserverA()
    subject.attach(observer_a)
    
    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    
    subject.some_business_logic()
    subject.some_business_logic()

    subject.detach(observer_a)
    
    subject.some_business_logic()
    
    subject.send_message("Goodbye, World!")
