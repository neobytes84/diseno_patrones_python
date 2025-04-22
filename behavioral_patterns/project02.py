# Behavioral patterns - Chain of responsability in Python - Example 01
# Developed by Neobytes.io


from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional

class Handler(ABC):
    
    @abstractmethod
    def set_next(self, handler: Handler) -> None:
        pass
    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass
    
class AbstractHandler(Handler):
    
    _next_handler: Handler = None
    
    def set_next(self, handler: Handler) -> None:
        self._next_handler = handler
        return handler
    
    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

class CreateSoftwareRequest(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "API development":
            return "Developer assigned to API development"
        else:
            return super().handle(request)

class DesignSoftwareRequest(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "UI/UX design":
            return f"Designer assigned to UI/UX design{request}"
        else:
            return super().handle(request)

class TestSoftwareRequest(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Test automation":
            return f"Tester assigned to test automation{request}"
        else:
            return super().handle(request)

class ReleaseSoftwareRequest(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Release management":
            return f"Release manager assigned to release management{request}"
        else:
            return super().handle(request)

def client_code(handler: Handler, developer: str) -> None:
    
    for request in ["API development", "UI/UX design", "Test automation", "Release management"]:
        print(f"Request: {developer}")
        result = handler.handle(developer)
        if result:
            print(f"Assigned to: {result}", end="")
        else:
            print("{developer} cannot be handled", end="")

if __name__ == "__main__":
    # Set up the chain of handlers
    handler1 = CreateSoftwareRequest()
    handler2 = DesignSoftwareRequest()
    handler3 = TestSoftwareRequest()
    handler4 = ReleaseSoftwareRequest()
    
    # Connect the handlers
    handler1.set_next(handler2)
    handler2.set_next(handler3)
    handler3.set_next(handler4)
    
    # Test the chain
    client_code(handler1, "John Doe")
    print("\n")
    client_code(handler1, "Jane Smith")
    print("\n")
    client_code(handler1, "David Johnson")
    print("\n")
    client_code(handler1, "Emily Davis")
    print("\n")
    client_code(handler1, "Michael Wilson")
    print("\n")
    client_code(handler1, "Sarah Thompson")
    print("\n")