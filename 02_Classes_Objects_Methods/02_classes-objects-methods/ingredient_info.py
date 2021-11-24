from ingredients import Ingredient

search_name = input(f"\nWhat ingredient would you like to research?\n --> ")


i = Ingredient(search_name)

Ingredient.get_info(i)

i.get_info()
