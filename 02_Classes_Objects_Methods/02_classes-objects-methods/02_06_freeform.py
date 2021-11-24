# Write a script with three classes that model everyday objects.
# - Each class should have an `__init__()` method that sets at least 3 attributes
# - Include a `__str__()` method in each class that prints out the attributes
#     in a nicely formatted string.
# - Overload the `__add__()` method in one of the classes so that it's possible
#     to add attributes of two instances of that class using the `+` operator.
# - Create at least two instances of each class.
# - Once the objects are created, change some of their attribute values.
#
# Be creative. Have some fun. :)
# Using objects you can model anything you want:
# Animals, paintings, card games, sports teams, trees, people etc...

# create 3 classes
class Plant:
# 3 attributes
    def __init__(self,name, indoor_outdoor,water_need,amount) -> None:
        self.name = name
        self.indoor_outdoor = indoor_outdoor
        self.water_need = water_need
        self.amount = amount

# str
    def __str__(self) -> str:
        return f"""
Plant Details:  {self.indoor_outdoor}
Water Need:     {self.water_need}
Amount:           {self.amount}    
"""

# add
    def __add__(self):  
        pass

class Record:
# 3 attributes
    def __init__(self,artist,type,genre,) -> None:
        self.artist = artist
        self.type=type
        self.genre=genre
        
# str
    def __str__(self) -> str:
        return f"""
Artist:     {self.artist}
Type:       {self.type}
Genre:      {self.genre}   
"""
# add
    def __add__(self, other):  
        self_artist = self.artist.split(" ")
        other_artist = other.artist.split(" ")
        new_artist = f"{self_artist[0]} {other_artist[1]}"
        new_genre = f"{self.genre}/{other.genre}"
        new_record=Record(artist=new_artist,type="Compilation",genre=new_genre)
        return new_record

class Home:
# 3 attributes
    def __init__(self,type,location,year_built) -> None:
        self.type=type
        self.location=location
        self.year_built=year_built
# str
    def __str__(self) -> str:
        return f"""
Type:           {self.type}
Location:       {self.location}
Year Built:     {self.year_built} 
"""
# add
    def __add__(self):  
        pass


# - Create at least two instances of each class.

# plants
aloe = Plant(name="Aloe",indoor_outdoor="Outdoor", water_need="Low", amount= 3)
spider = Plant(name="Spider Plant",indoor_outdoor="Indoor", water_need="Medium", amount= 10)
plant_list = [aloe,spider]
# records
george = Record(artist="George Strait",type="LP",genre="Country/Pop")
mos = Record(artist="Mos Def",type="EP",genre="Hip Hop")
new_record = george + mos
record_list = [george,mos]
# homes
apart = Home(type="Apartment", location="Venice, Ca", year_built=1983)
mansion = Home(type="Mansion", location="Malibu, Ca", year_built=1946)
home_list = [apart,mansion]

if __name__ == "__main__":
    print(f"\n    Homes:\n{aloe}{spider}")
    print(f"\n    Records:\n{george}{mos}{new_record}")
    print(f"\n    Homes:\n{apart}{mansion}")
    