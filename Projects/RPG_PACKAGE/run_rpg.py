import random
from rpg_class_files import Hero, Opponent, Turn

# player character
pc = Hero(name="Jet Jones", strength=2, max_hp=10, berries=5)

# names only placeholders, 1st initial corresponds to their opponent number
opp_1 = Opponent(name="Adam", strength=2, max_hp=4)
opp_2 = Opponent(name="Brandon", strength=3, max_hp=6)
opp_3 = Opponent(name="Carson", strength=4, max_hp=8)
opp_4 = Opponent(name="Derek", strength=5, max_hp=10)   
opponent_list= [opp_1, opp_2, opp_3, opp_4]

# boss
boss = Opponent(name="Mr.Manager", strength=12, max_hp=14) 

# keeps track of turn
turn = Turn(count=1)

phase_1 = True
phase_2 = True
phase_3 = True
rewarding = True
congrats = True
# phase_1 = False
# phase_2 = False
# phase_3 = False
# rewarding = False
# congrats = False


while len(opponent_list) > 0 and phase_1 == True:           # 1st phase
    answer = input(f"\nWould you like to:\n   (s) search the area           \n\
        -or-                    {pc.status()}\n   (e) eat berries to gain HP\n    -> ")
    
    if answer.lower() != "s" and answer.lower() != "e":
        print(f"\nWhoops! Invalid entry. Try again ")
        continue
    if answer.lower() == "s" or answer.lower() == "e":
        if answer.lower() == "e":
            pc.eat_berries()
            turn.add_turn()    
# eat Berries        
        else:
            print(f"\nYou go out and search the area...")
            turn.add_turn()
            pass
# search 
            encountered = True    
            while encountered:    
                enemy = opponent_list[random.randint(0, (len(opponent_list) - 1))]
                answer = input(f"\nOh no, you've encountered an opponent!                 {pc.status()}\nHis name is {enemy.name}.                                      {enemy.status()}\n  Do you (f) fight or (r) run away?\n -> ")
# encounter
                if answer.lower() == 'f' or answer.lower() == 'r':
                        if answer.lower() == 'f':
                            engaged = True
# engage Battle                            
                            while engaged:
                                answer = input(f"\nIt's on!                                   {pc.status()}\nEnter (a) to attack or (r) to run away?           {enemy.status()}\n  -> ")

                                if answer.lower() == 'a':
                                    hero_roll = pc.dice_throw()
                                    opp_roll = enemy.dice_throw()
                                    
                                    if hero_roll > opp_roll:
                                        enemy.lose_hp()
                                        if enemy.hp <= 0:
                                            print(f"\nWhoa! You defeated {enemy.name}!\nMax HP +2\nHP +2\nStrength +2")
                                            pc.max_hp += 2
                                            pc.hp += 2
                                            pc.strength += 2
                                            opponent_list.remove(enemy)
                                            turn.add_turn()
                                            engaged = False
                                            encountered = False                    

                                        else:
                                            print(f"\nNice! You take 2 HP from {enemy.name}!")
                                            turn.add_turn()

                                    elif hero_roll == opp_roll:
                                        print(f"\nClash! It's a tie!")
                                        turn.add_turn()

                                    elif hero_roll < opp_roll:
                                        pc.lose_hp()
                                        if pc.hp <= 0:
                                            print(f"\nWhoa! You lost to {enemy.name}!\nBetter luck next time!")
                                            turn.add_turn()
                                            engaged = False
                                            encountered = False
                                            phase_1 = False
                                            phase_2 = False
                                            phase_3 = False
                                            congrats = False
                                            rewarding = False
                                            
                                        else:
                                            print(f"\nOuch! {enemy.name} takes 2 HP from you!")
                                            turn.add_turn()
# run Away 2
                                else:        
                                    pc.lose_hp(1)
                                    print(f"\nYou run away from {enemy.name}. You lose 1 HP!")
                                    # phase_1 = False
                                    engaged = False
                                    encountered = False                    
                                    turn.add_turn()

# run Away 1                                     
                        else:       
                            if answer.lower() == 'r': 
                                pc.lose_hp(1)
                                print(f"\nYou run away from {enemy.name}. You lose 1 HP!")
                                turn.add_turn()
                                engaged = False
                                encountered = False                    

                            else:
                                print(f"\nWhoops! Invalid entry. Try again ")
                                continue
                
                else:
                    print(f"\nWhoops! Invalid entry. Try again ")
                    continue

while congrats:
    print(f"\nWOW!!!! You've defeated all of your opponents!! Congratulations!")
    congrats = False

# rewarding phase/phase_2
while rewarding and phase_2:               
    answer = input(
f"""
You'll be wanting an reward then, eh?
(y) Yes, please! Why else am I here?!
        -or-
(n) Thanks but no. The thrill of victory
        is its own reward. 
    -> """)
    if answer.lower() != 'y':
        if answer.lower() == 'n':
            print(f"\nOkay well that's great. See ya!\n")
            rewarding = False
        else:
            print(f"\nWhoops! Invalid entry. Try again ")     
    else:
        print(f"""
Thought so. 
You're reward is...
    FIGHTING THE BOSS!!!!""")
        print(f"\nBefore the fight, you eat your remaining berries.")
        remaining_berries = pc.berries
        pc.eat_berries(remaining_berries)
        rewarding = False




while boss.hp > 0 and phase_3:                    
    answer = input(f"""
Press (a) to attack!                   {pc.status()}
                                       {boss.status()}
    --> """)
    if answer.lower() == 'a':
        hero_roll = pc.dice_throw()
        opp_roll = boss.dice_throw()
        
        if hero_roll > opp_roll:
            boss.lose_hp()
            if boss.hp <= 0:
                turn.add_turn()
                print(f"""
Whoa! You defeated {boss.name}! You are the victor!
You won the game in {turn.count} turns!
Try to beat the game in less turns???
""")    
                engaged = False
                encountered = False                    

            else:
                print(f"\nNice! You take 2 HP from {boss.name}!")
                turn.add_turn()

        elif hero_roll == opp_roll:
            if boss.hp > 1 and pc.hp > 1:
                print(f"\nClash! It's a tie! You both lose 1 HP!")
                pc.lose_hp(1)
                boss.lose_hp(1)
                turn.add_turn()
            else:
                print(f"\nClash! It's a tie!")
                turn.add_turn()
        elif hero_roll < opp_roll:
            pc.lose_hp()
            if pc.hp <= 0:
                turn.add_turn()
                print(f"""
Whoa! You've lost to {boss.name}...
and it only took you {turn.count} turns...""")
                engaged = False
                encountered = False
                

            else:
                print(f"\nOuch! {boss.name} takes 2 HP from you!")
                turn.add_turn()
    else:
        print(f"\nWhoops! Invalid entry. You stumble and lose 1 HP...")
        pc.lose_hp()
        turn.add_turn()
        continue
