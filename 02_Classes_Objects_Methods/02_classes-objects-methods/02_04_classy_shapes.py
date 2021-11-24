# Create two classes that model a rectangle and a circle.
# The rectangle class should be constructed by length and width
# while the circle class should be constructed by radius.
#
# Write methods in the appropriate class so that you can calculate
# the area of both the rectangle and the circle, the perimeter
# of the rectangle, and the circumference of the circle.

from math import pi

# create rectangle class
    # A = LW
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def get_area(self):
        # A = LW
        a = self.length * self.width
        return a
    def get_perimeter(self):
        # P = 2(L+W)
        p = 2 * (self.length + self.width)
        return p
    def __str__(self) -> str:
        return f"""
Length: {self.length}     Width:      {self.width}
Area:   {self.get_area():.2f}    Perimeter:  {self.get_perimeter():.2f}  
"""

# create circle class
    # r = C/2π
class Circle:
    def __init__(self, radius):
        self.radius= radius
    def get_area(self):
        # a = π * (r ** 2)
        a = pi * (self.radius ** 2)
        return a
    def get_cirumference(self):
        # r = c / 2 * π
        c = self.radius * (2 * pi)
        return c
    def __str__(self) -> str:
        return f"""
Radius: {self.radius}   
Area:   {self.get_area():.2f} Circumference:  {self.get_cirumference():.2f}  
"""
flag = " <| <| <| <| <|  flag  |> |> |> |> |>\n"

if __name__ == "__main__":
    rec = Rectangle(length=5, width=10)
    circ = Circle(radius=10)
    
    print(flag)
    print(rec, circ)
    print(flag)
    