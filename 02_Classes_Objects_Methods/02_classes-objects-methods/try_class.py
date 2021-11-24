class Planet:
    
    def __init__(self, name, system, size) -> None:
        self.name = name
        self.system = system
        self.size = size
        
    
    def __str__(self) -> str:
        return f"\nPlanet: {self.name}\nSystem: {self.system}\nSize: {self.size}\n"


# test:

from try_class import Planet
planet = Planet(name="Earth", system="Sol", size="Small")
print(planet)