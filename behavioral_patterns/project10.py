# Behavioral patterns - Command in Python -example 01
# Developed by Neobytes.io

from abc import ABC, abstractmethod
import pandas as pd

class Command(ABC):
    
    def __init__(self, receiver):
        self.receiver = receiver
    
    def process(self):
        pass
    
    def saving_changes(self):
        pass
    
    def restore_changes(self):
        pass
    
    def notify_changes(self):
        pass

class CommandImplementation(Command):
    
    def __init__(self, receiver):
        self.receiver = receiver
    
    def process(self):
        self.receiver.perform_action()
    
    def saving_changes(self):
        print("Saving changes...")
        self.receiver.save_state()
    
    def restore_changes(self):
        print("Restoring changes...")
        self.receiver.restore_state()
    
    def notify_changes(self):
        print("Notifying changes...")
        self.receiver.notify_changes()

class Receiver:
    
    def perform_action(self):
        print("Performing action...")
    
    def save_state(self):
        print("Saving state...")
    
    def restore_state(self):
        print("Restoring state...")
    
    def notify_changes(self):
        print("Notifying changes...")

class Invoker:
    
    def command(self,cmd):
        self.cmd = cmd
    
    def execute(self):
        self.cmd.process()
        self.cmd.saving_changes()
        self.cmd.notify_changes()
        self.cmd.restore_changes()

if __name__ == "__main__":
    receiver = Receiver()
    cmd = CommandImplementation(receiver)
    invoker = Invoker()
    invoker.command(cmd)
    invoker.execute()

