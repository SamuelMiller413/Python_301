# design a pokemon game

#    your class should follow these specifications:

# 1. Each Pokemon should have a name, primary_type, max_hp and hp.
# 2. Primary types should be limited to water, fire and grass.
# 3. Implement a battle() method based on rock-paper-scissors that decides who wins based only on the primary_type:
# 4. water > fire > grass > water
# 5. Display messages that explain who won or lost a battle.
# 6. If a Pokemon loses a battle, they lose some of their hp.
# 7. If you call the feed() method on a Pokemon, they regain some hp.

# create a pokemon
class Pokemon:
    def __init__(self, name, primary_type, max_hp):
        self.name = name
        self.primary_type = primary_type
        self.hp = max_hp
        self.max_hp = max_hp
   
    def __str__(self) -> str:
        return f"{self.name} ({self.primary_type}: {self.hp}/{self.max_hp})"
    
    def __repr__(self) -> str:
        return f"{self.name}_({self.primary_type}: {self.hp}/{self.max_hp})"
    
        pass  

    # feed them to increase health
    def feed(self):
        if self.hp < self.max_hp:
            self.hp += 1
            print(f"{self.name} has now {self.hp} HP.")
        else:
            print(f"{self.name} is full")


    # make them battle and decide for a winner
    def battle(self, other):
        print("Battle:", self.name, other.name)
        result = self.typewheel(self.primary_type, other.primary_type)
        # depending on the result, have effects
        if result == "lose":
            self.hp -= 10
            print(f"{self.name} lost and now has {self.hp} HP.")
        # if result:
        #     pass     
        print(f"{self.name} fought {other.name} and the result is a {result} ")
        # call type wheel
    
    @staticmethod
    def typewheel(type1, type2):
        result = {0: "lose", 1: "win", -1: "tie"}
        # mapping between types and result conditions
        game_map = {"water": 0, "fire":1, "grass": 2}
        # implement win-lose matrix
        wl_matrix = [
            [-1, 1, 0],     # water
            [0, -1, 1],     # fire
            [1, 0, -1],     # grass
        ]
        # declare a winner
        # game_map["water"]
        # wl_matrix[0][1] #1
        # wl_result = wl_matrix[game_map["water"]][game_map["fire"]]
        wl_result = wl_matrix[game_map[type1]][game_map[type2]]
        return result[wl_result]


# take a look at it        
if __name__ == '__main__':
    bulbi = Pokemon(name="bulbasaur", primary_type="grass", max_hp=100)
    charm = Pokemon(name="charmander", primary_type="fire", max_hp=150)
    # bulbi.battle(charm)
    # bulbi.battle(charm)
    print(bulbi.name)