# Project: RPG Game

# Tasks:
# Build a text-based role-playing game that has at least two classes:

# 1. Hero(): the protagonist of your game that the player controls 
# and identifies with. There should be only one hero.

# 2. Opponent(): the challengers that the player meets throughout the gameplay. 
# There should be multiple opponents.

# The hero should encounter multiple opponents 
# of different strengths or levels. 
# They should be able to perform different 
# actions when meeting an opponent. 
# These actions should be at a minimum:

#     - attack
#     - or run away



import random

# make hero class 
class Hero:

    def __init__(self, name, strength, max_hp, berries):
        self.name = name
        self.strength = strength
        self.max_hp = max_hp
        self.hp = max_hp
        self.berries = berries    

    def __repr__(self):
        return f"Hero (name={self.name}, strength={self.strength}, HP={self.hp}/{self.max_hp})"
    
    def __str__(self):
        return self.status

    def dice_throw(self):
        d_20 = random.randint(1,20)     # throw d20
        attack = d_20 + self.strength   # d20 + strength
        return int(attack)

    def eat_berries(self, amount = 1):
        
        if self.hp < self.max_hp:
            if self.max_hp - self.hp == 1:
                self.berries -= amount
                self.hp += 1
                print(f"+1 HP. Full HP!       HP={self.hp}/{self.max_hp}")
            else:
                self.hp += 2
                if self.hp == self.max_hp:
                    self.berries -= amount
                    print(f"+2 HP. Full HP!       HP={self.hp}/{self.max_hp}")
                else:
                    self.berries -= amount
                    print(f"+2 HP.       HP={self.hp}/{self.max_hp}")
        else:
            print(f"You have full health!       HP={self.hp}/{self.max_hp}")\

    def lose_hp(self, amount=2):
        self.hp -= amount
        return print(f"{self.name} -{amount} HP :(")

    def status(self):
        stat = f"{self.name}: strength={self.strength}, HP={self.hp}/{self.max_hp}, Berries={self.berries}"
        return stat

# make opponent class 
class Opponent:
    
    def __init__(self, name, strength, max_hp):
        self.name = name
        self.strength = strength
        self.max_hp = max_hp
        self.hp = max_hp

    def __repr__(self) -> str:
        return f"Opponent (name={self.name}, strength={self.strength}, HP={self.hp}/{self.max_hp})"
        
    def __str__(self):
        return self.status
        
    def dice_throw(self):
        d_20 = random.randint(1,20)     # throw d20
        attack = d_20 + self.strength   # d20 + strength
        return attack

    def lose_hp(self, amount=2):
        self.hp -= amount
        return print(f"{self.name} -{amount} HP")
    
    def status(self):
        stat = f"{self.name}: strength={self.strength}, HP={self.hp}/{self.max_hp}"
        return stat

class Turn:
    def __init__(turn, count) -> None:
        turn.count = count
    def __str__(turn) -> str:
        return f"Turn Count: {turn.count}"
    def __repr__(turn) -> str:
        return f"Turn {turn.count}"  
    
    def add_turn(turn):
        turn.count += 1
        return turn.count



# multiple opponents, defferent strengths or levels

# player character
pc = Hero(name="Jet Jones", strength=2, max_hp=10, berries=5)
# names only placeholders, 1stw initial corresponds to their opponent number
opp_1 = Opponent(name="Adam", strength=2, max_hp=4)
opp_2 = Opponent(name="Brandon", strength=3, max_hp=6)
opp_3 = Opponent(name="Carson", strength=4, max_hp=8)
opp_4 = Opponent(name="Derek", strength=5, max_hp=10)   
opponent_list= [opp_1, opp_2, opp_3, opp_4]

boss = Opponent(name="Mr.Manager", strength=7, max_hp=14) 

# keeps track of turn
turn = Turn(count=1)

# take a look at it        
if __name__ == '__main__':
    # pc.lose_hp()
    # opp_2.lose_hp()
    # hero.eat_berries()
    # print(hero)
    # pc.lose_hp(1)
    print(pc.status)
    print(opp_4.status)

