# Creational patterns - Prototype in Python - Example 01
# Developed by Neobytes.io

import copy
import json

class Prototype:
    def __init__(self):
        self.parent_state = None
    
    def set_parent_state(self, parent_state):
        self.parent_state = parent_state

class ConcretePrototype:
    
    def __init__(self,some_init, some_list_objects, some_circular_object):

        self.some_init = some_init
        self.some_list_objects = some_list_objects
        self.some_circular_object = some_circular_object
    
    def __copy__(self):
       some_list_objects = copy.copy(self.some_list_objects)
       some_circular_object = copy.copy(self.some_circular_object)
       
       new = self.__class__(
           self.some_init, some_list_objects, some_circular_object
           )
       
       new.__dict__.update(self.__dict__)
       
       return new

    def __deepcopy__(self, memo=None):
        
        if memo is None:
            memo = {}
        
        some_list_objects = copy.deepcopy(self.some_list_objects, memo)
        some_circular_object = copy.deepcopy(self.some_circular_object, memo)
        
        new = self.__class__(
            self.some_init, some_list_objects, some_circular_object
            )
        new.__dict__ = copy.deepcopy(self.__dict__, memo)
        
        return new

class TypingPrototypeComponent(Prototype):
    def __init__(self, some_init, some_list_objects, some_circular_object):
        super().__init__()
        self.some_init = some_init
        self.some_list_objects = some_list_objects
        self.some_circular_object = some_circular_object
        self.typing_info = self.get_typing_info()
        self.typing_info_as_json = json.dumps(self.typing_info)
        self.typing_info_as_json_as_dict = json.loads(self.typing_info_as_json)
        self.set_parent_state(component)
    def get_typing_info(self):
        return {
            "some_init": type(self.some_init).__name__,
            "some_list_objects": [type(x).__name__ for x in self.some_list_objects],
            "some_circular_object": type(self.some_circular_object).__name__
        }
    
    def __str__(self):
        return f"Prototype Component:\n{self.typing_info_as_json}"

if __name__ == "__main__":
    
    list_objects = [1,{1,2,3,4,5}, [1,2,3,4,5]]
    circular_object = Prototype()
    component = ConcretePrototype(10, list_objects, circular_object)
    circular_object.set_parent_state(component)
    
    shallow_copied_component = copy.copy(component)
    
    shallow_copied_component.some_list_objects.append("new_item")
    if component.some_list_objects[-1] == "new_item":
        print(
            "Addition of new item to list in shallow copy is successful"
            "some list in original component has changed too"
            "some_list_objects."
            )
    else:
        print (
            "Addition of new item to list in shallow copy has failed"
            "some list in original component has not changed"
            "some_list_objects."
    
        )
    # Let's change the set in the list of objects.
    component.some_list_objects[1].add(4)
    if 4 in shallow_copied_component.some_list_objects[1]:
        print (
            "Addition of new item to set in list in shallow copy is successful"
            "set in original component has changed too"
            "some_list_objects[1]."
    
        )
    else:
        print (
            "Addition of new item to set in list in shallow copy has failed"
            "set in original component has not changed"
            "some_list_objects[1]."
        )
    
    deep_copied_component = copy.deepcopy(component)
    
    # Let's change the list in deep_copied_component and see if it changes in
    # component.
    deep_copied_component.some_list_objects.append("one more object")
    if component.some_list_objects[-1] == "one more object":
        print(
            "Addition of new item to list in deep copy is successful"
            "some list in original component has not changed"
            "some_list_objects."
            )
    else:
        print (
            "Addition of new item to list in deep copy has failed"
            "some list in original component has changed"
            "some_list_objects."
        )
        
    # Let's change the set in deep_copied_component and see if it changes in
    component.some_list_objects[1].add(10)
    if 10 in shallow_copied_component.some_list_objects[1]:
        print (
            "Change of set in list in deep copy is successful"
            "set in original component has not changed"
            "some_list_objects."
        )
    else:
        print (
            "Change of set in list in deep copy has failed"
            "set in original component has changed"
            "some_list_objects."
        )
    
    print(
        f"id(deep_copied_component.some_circular_object): "
        f"{id(deep_copied_component.some_circular_object)}"
    )
    print(
        f"id(deep_copied_component.some_circular_object.parent_state): "
        f"{id(deep_copied_component.some_circular_object.parent_state)}"

    )
    print(
        f"id(component.some_circular_object): "
        f"{id(component.some_circular_object)}"
    )
    print(
        f"id(component.some_circular_object.parent_state): "
        f"{id(component.some_circular_object.parent_state)}"
    )
    print(
        f"Type of deep_copied_component.some_circular_object: "
        f"{type(deep_copied_component.some_circular_object).__name__}"
        f"Type of component.some_circular_object: "
        f"{type(component.some_circular_object).__name__}"
        f"Both references are pointing to the same object: "
        f"{id(deep_copied_component.some_circular_object) == id(component.some_circular_object)}"
        f"Both references are pointing to the same parent state: "
        f"{id(deep_copied_component.some_circular_object.parent_state) == id(component.some_circular_object.parent_state)}"
        f"Both references are pointing to the same parent state: "
        f"{id(deep_copied_component.some_circular_object.parent_state) == id(shallow_copied_component.some_circular_object.parent_state)}"
    )
    print(
        f"Type of deep_copied_component.some_circular_object.parent_state: "
        f"{type(deep_copied_component.some_circular_object.parent_state).__name__}"
        f"Type of component.some_circular_object.parent_state: "
        f"{type(component.some_circular_object.parent_state).__name__}"
        f"Both references are pointing to the same object: "
        f"{id(deep_copied_component.some_circular_object.parent_state) == id(component.some_circular_object.parent_state)}"
    )
    print("End of testing")