# The classic OOP example: Write a class to model a car. The class should:
#
# 1. Set the attributes model, year, and max_speed in the `__init__()` method.
# 2. Have a method that increases the `max_speed` of the car by 5 when called.
# 3. Have a method that prints the details of the car.
#
# Create at least two different objects of this `Car()` class and demonstrate
# changing the objects' attributes.






class Car:
# 1. Set the attributes model, year, and max_speed in the `__init__()` method.
    def __init__(self, model, year, max_speed) -> None:
        self.model = model
        self.year = year
        self.max_speed = max_speed

# 2. Have a method that increases the `max_speed` of the car by 5 when called.
    def increase_max_speed(self, amount=5):
        self.max_speed += amount
        return print(f"Max speed increased by {amount} mph.")
    
# 3. Have a method that prints the details of the car.
    def __str__(self) -> None:
        return f"""
Details: 

    Model:      {self.model}
    Year:       {self.year}
    Max Speed:  {self.max_speed} mph
"""

# Create at least two different objects of this `Car()` class and demonstrate
# changing the objects' attributes.

flag = " <| <| <| <| <|  flag  |> |> |> |> |>\n"

if __name__ == "__main__":
    civic = Car(model="Honda Civic",year=1991,max_speed=120)
    taurus= Car(model="Ford Taurus",year=2001,max_speed=95)
    print(civic)
    print(taurus)
    print(flag)
    civic.increase_max_speed()
    taurus.increase_max_speed(30)
    print(civic, taurus)



