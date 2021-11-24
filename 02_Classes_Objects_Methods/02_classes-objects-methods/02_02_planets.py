# Create a `Planet()` class that models attributes and methods of
# a planet object.
# Use the appropriate dunder method to get informative output with `print()`

class Planet:
    
    def __init__(self, name, system, size) -> None:
        self.name = name
        self.system = system
        self.size = size
        
    
    def __str__(self) -> str:
        return f"\nPlanet: {self.name},\nSystem: {self.system}\nSize: {self.size}\n"

