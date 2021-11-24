from ingredients import Ingredient


search_recipe = input(f"\nwhat is the first ingredient in your recipe?\n     -> ")

flag = True
while flag == True: 
    next_ing = input(f"\nAlright. What else?           (or type 's' to search)\n   -> ")
    if next_ing.lower() == 's':
        flag = False
    else:
        search_recipe += f"+{next_ing}"

r = Ingredient(search_recipe)
r.search_recipe()