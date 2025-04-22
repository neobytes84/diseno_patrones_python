# Behavioral patterns - Memento in Python -example 01
# Developed by Neobytes.io


class OriginalDocument:
    def __init__(self, text, author, date):
        self.text = text
        self.author = author
        self.date = date
    
    def set_text(self,text):
        self.text = text
    def get_text(self):
        return self.text

    def create_memento(self):
        return Memento(self.text)
    
    def restore_memento(self, memento):
        self.text = memento.get_state()
    def __str__(self):
        return f'Original Document: Text: {self.text}'

class Memento:
    def __init__(self,state):
        self._state = state
    
    def get_state(self):
        return self._state

class CareTaker:
    def __init__(self):
        self._mementos = []
        self._current_index = -1
    
    def save(self, memento):
        
        if self._current_index + 1 < len(self._mementos):
            self._mementos = self._mementos[:self._current_index + 1]
        
        self._mementos.append(memento)
        self._current_index += 1
    
    def restore(self):
        
        if self._current_index > 0:
            self._current_index -= 1
            return self._mementos[self._current_index]
        return None
    
    def redo(self):
        if self._current_index + 1 < len(self._mementos):
            self._current_index += 1
            return self._mementos[self._current_index]
        return None

# Example usage
if __name__ == "__main__":

    editor = OriginalDocument("Initial Text", "John Doe", "2022-01-01")
    print(editor)
    
    caretaker = CareTaker()
    caretaker.save(editor.create_memento())
    
    editor.set_text("Updated Text 1")
    caretaker.save(editor.create_memento())
    
    editor.set_text("Updated Text 2")
    caretaker.save(editor.create_memento())
    
    # Perform restore and redo operations
    print("Current state:", editor)
    memento = caretaker.restore()
    if memento:
        editor.restore_memento(memento)
        print("Restored state:", editor)
    
    memento = caretaker.redo()
    if memento:
        editor.restore_memento(memento)
        print("Redone state:", editor)
    