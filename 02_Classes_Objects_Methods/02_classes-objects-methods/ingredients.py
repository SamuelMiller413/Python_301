# CLASSES AND OBJECT-ORIENTED PROGRAMMING
import webbrowser
class Ingredient:
    
    """Models a food item used as an ingredient."""
    def __init__(self, name, amount=0):
        self.name = name
        self.amount = amount

    def expire(self):
        """Expires the ingredient."""
        print(f"whoops, these {self.name} went bad...")
        self.name = "expired " + self.name

    def __str__(self):
        return f"{self.name} ({self.amount})."

    def use(self, use_amount):
        self.amount -= use_amount

    def __repr__(self):
        return f"Ingredients(name={self.name}, amount={self.amount})"

    def get_info(self):
        ing_string = ''
        ing_name = self.name
        ing_string = ing_name.replace(' ', '_')
        url = f"https://en.wikipedia.org/wiki/{ing_string}"
        return webbrowser.open(url, new=1, autoraise=True)
        
        
    def search_recipe(self):
        recipe_string = self.name.replace(' ', '_')
        url = f"https://www.google.com/search?q={recipe_string}+recipe"
        return webbrowser.open(url, new=1, autoraise=True)

    # def expire(self):
    #     """Expires the ingredient."""
    #     print(f"whoops, these {self.name} went bad...")
    #     self.name = "expired " + self.name



# peas = Ingredient("peas", 3)
# tom = Ingredient("tomatoes", 5)
# pepp = Ingredient("peppers", 6)
# c = Ingredient("carrots", 5)

# print(c)
# print(repr(c))


