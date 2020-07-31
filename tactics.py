#setup
import math
import random
# generate random integer values
from random import seed
from random import randint
# seed random number generator=
from datetime import datetime
random.seed(datetime.now())

#player stats
gold = 1000
platnium = 0
renown = 300
unit_exp = 0
weapon_exp = 0

week = 1
season = 1

renown_bonus = math.log((renown + 5), 5)

#classes

class Unit:
    def __init__(self, exp, affinity, blade_exp, polearm_exp, heavy_exp, range_exp, \
        elemental_exp, holy_exp, dark_exp, psychic_exp, \
        power_base, power_growth, speed_base, speed_growth, precision_base, precision_growth, \
        constitution_base, constitution_growth, defense_base, defense_growth, reflex_base, reflex_growth, \
        evasion_base, evasion_growth, resilience_base, resilience_growth):

        self.affinity = affinity
        self.exp = exp

        #character level
        if self.exp < 100:
            self.level = 0
        else:
            self.level = math.ceil(math.log2 (self.exp /100 + 0.00001))

        self.blade_exp = blade_exp
        self.polearm_exp = polearm_exp
        self.heavy_exp = heavy_exp
        self.range_exp = range_exp
        self.elemental_exp = elemental_exp
        self.holy_exp = holy_exp
        self.dark_exp = dark_exp
        self.psychic_exp = psychic_exp


        #weapon ranks
        if self.blade_exp < 100:
            self.blade_rank = 0
        else:
            self.blade_rank = math.ceil(math.log2 (self.blade_exp /100 + 0.00001))

        if self.polearm_exp < 100:
            self.polearm_rank = 0
        else:
            self.polearm_rank = math.ceil(math.log2 (self.polearm_exp /100 + 0.00001))

        if self.heavy_exp < 100:
            self.heavy_rank = 0
        else:
            self.heavy_rank = math.ceil(math.log2 (self.heavy_exp /100 + 0.00001))

        if self.range_exp < 100:
            self.range_rank = 0
        else:
            self.range_rank = math.ceil(math.log2 (self.range_exp /100 + 0.00001))

        if self.elemental_exp < 100:
            self.elemental_rank = 0
        else:
            self.elemental_rank = math.ceil(math.log2 (self.elemental_exp /100 + 0.00001))

        if self.holy_exp < 100:
            self.holy_rank = 0
        else:
            self.holy_rank = math.ceil(math.log2 (self.holy_exp /100 + 0.00001))

        if self.dark_exp < 100:
            self.dark_rank = 0
        else:
            self.dark_rank = math.ceil(math.log2 (self.dark_exp /100 + 0.00001))

        if self.psychic_exp < 100:
            self.psychic_rank = 0
        else:
            self.psychic_rank = math.ceil(math.log2 (self.psychic_exp /100 + 0.00001))



        self.power = power_base + self.level * power_growth
        self.speed = speed_base + self.level * speed_growth
        self.precision = precision_base + self.level * precision_growth
        self.constitution = constitution_base + self.level * constitution_growth
        self.defense = defense_base + self.level * defense_growth
        self.reflex = reflex_base + self.level * reflex_growth
        self.evasion = evasion_base + self.level * evasion_growth
        self.resilience = resilience_base + self.level * resilience_growth

        self.base_attack = 0

    def weapon_equip(self, weapon):
        self.base_attack = weapon.might

        if weapon.shape == 1:
            if self.blade_rank < weapon.rank:
                self.base_attack = 0

        if weapon.shape == 2:
            if self.polearm_rank < weapon.rank:
                self.base_attack = 0

        if weapon.shape == 3:
            if self.heavy_rank < weapon.rank:
                self.base_attack = 0

        if weapon.shape == 4:
            if self.range_rank < weapon.rank:
                self.base_attack = 0

        if weapon.shape == 5:
            if self.elemental_rank < weapon.rank:
                self.base_attack = 0

        if weapon.shape == 6:
            if self.holy_rank < weapon.rank:
                self.base_attack = 0

        if weapon.shape == 7:
            if self.dark_rank < weapon.rank:
                self.base_attack = 0

        if weapon.shape == 8:
            if self.psychic_rank < weapon.rank:
                self.base_attack = 0

    def attack_power(self, target):
        total = 0

        power_bonus = 1
        if self.power > target.defense:
            power_bonus += 0.1 * (self.power - target.defense)
        
        speed_bonus = 1
        if self.speed > target.reflex:
            speed_bonus += 0.1 * (self.speed - target.reflex)       
        
        precision_bonus = 1
        if self.precision > target.evasion:
            precision_bonus += 0.1 * (self.precision - target.evasion)        
        
        constitution_bonus = 1
        if self.constitution > target.resilience:
            constitution_bonus += 0.1 * (self.constitution - target.resilience)        
        
        total = self.base_attack * power_bonus * speed_bonus * precision_bonus * constitution_bonus



        if self.affinity - target.affinity == 1:
            total = total * 2
        
        if self.affinity == 1 and target.affinity == 6:
            total = total * 2
        
        return total


class Foe:
    def __init__(self, affinity, might, power, speed, precision, constitution, \
        defense, reflex, evasion, resilience):
        pass

        self.affinity = affinity

        self.might = might

        self.power = power
        self.speed = speed
        self.precision = precision
        self.constitution = constitution
        self.defense = defense
        self.reflex = reflex
        self.evasion = evasion
        self.resilience = resilience
    
    def attack_power(self, target):
        total = 0

        power_bonus = 1
        if self.power > target.defense:
            power_bonus += 0.1 * (self.power - target.defense)
        speed_bonus = 1
        if self.speed > target.reflex:
            speed_bonus += 0.1 * (self.speed - target.reflex)       
        precision_bonus = 1
        if self.precision > target.evasion:
            precision_bonus += 0.1 * (self.precision - target.evasion)        
        constitution_bonus = 1
        if self.constitution > target.resilience:
            constitution_bonus += 0.1 * (self.constitution - target.resilience)        
        
        total = self.might * power_bonus * speed_bonus * precision_bonus * constitution_bonus

        if self.affinity - target.affinity == 1:
            total = total * 2
        
        if self.affinity == 1 and target.affinity == 6:
            total = total * 2

        return total



class Weapon:
    def __init__(self, might, shape, rank):
        self.might = might
        self.shape = shape
        self.rank = rank


class Quest:
    
    def __init__(self, seed, time, difficulty):
        self.time = time

        self.setup = seed * (week + season * 12)

        renown_bonus = math.log((renown + 5), 5)

        self.gold_reward = renown_bonus * time * difficulty * \
            randint(800000 , (1200000 + self.setup)) * randint(800000 , (1200000 - self.setup)) / (1000000 * 1000000)
        self.renown_reward = renown_bonus * time * difficulty * \
            randint(800000 , (1199999 + self.setup)) * randint(800000 , (1199999 - self.setup)) / (1000000 * 1000000)
        self.unit_exp_reward = renown_bonus * time * difficulty * \
            randint(800000 , (1199998 + self.setup)) * randint(800000 , (1199998 - self.setup)) / (1000000 * 1000000)
        self.weapon_exp_reward = renown_bonus * time * difficulty * \
            randint(800000 , (1199997 + self.setup)) * randint(800000 , (1199997- self.setup)) / (1000000 * 1000000)

        self.CR = self.gold_reward + self.renown_reward + self.unit_exp_reward + self.weapon_exp_reward

        self.gold_reward = self.gold_reward * 1000
        self.renown_reward = self.renown_reward * 20
        self.unit_exp_reward = self.unit_exp_reward * 100
        self.weapon_exp_reward = self.weapon_exp_reward + 10

    def generate_new_quest():
        self.time = time

        self.setup = seed * (week + season * 12)

        renown_bonus = math.log((renown + 5), 5)

        self.gold_reward = renown_bonus * time * difficulty * \
            randint(800000 , (1200000 + self.setup)) * randint(800000 , (1200000 - self.setup)) / (1000000 * 1000000)
        self.renown_reward = renown_bonus * time * difficulty * \
            randint(800000 , (1199999 + self.setup)) * randint(800000 , (1199999 - self.setup)) / (1000000 * 1000000)
        self.unit_exp_reward = renown_bonus * time * difficulty * \
            randint(800000 , (1199998 + self.setup)) * randint(800000 , (1199998 - self.setup)) / (1000000 * 1000000)
        self.weapon_exp_reward = renown_bonus * time * difficulty * \
            randint(800000 , (1199997 + self.setup)) * randint(800000 , (1199997- self.setup)) / (1000000 * 1000000)

        self.CR = self.gold_reward + self.renown_reward + self.unit_exp_reward + self.weapon_exp_reward

        self.gold_reward = self.gold_reward * 1000
        self.renown_reward = self.renown_reward * 20
        self.unit_exp_reward = self.unit_exp_reward * 100
        self.weapon_exp_reward = self.weapon_exp_reward + 10

    def victory():
        global gold
        global renown
        global unit_exp
        global weapon_exp

        gold += self.gold_reward
        renown += self.renown_reward
        unit_exp += self.unit_exp_reward
        weapon_exp += self.weapon_exp_reward

#randint(800000 , (1200000 + self.setup)) * randint(800000 , (1200000 - self.setup)) / (1000000 * 1000000)
#randint(800000 , (1199999 + self.setup)) * randint(800000 , (1199999 - self.setup)) / (999999 * 999999)

Quest1 = Quest(1, 1, 0.5)
Quest2 = Quest(2, 1, 0.5)
Quest3 = Quest(3, 1, 1)
Quest4 = Quest(4, 1, 1)
Quest5 = Quest(5, 1, 1.5)
Quest6 = Quest(6, 1, 1.5)

Quest7 = Quest(7, 2, 0.5)
Quest8 = Quest(8, 2, 0.5)
Quest9 = Quest(9, 2, 1)
Quest10 = Quest(10, 2, 1)
Quest11 = Quest(11, 2, 1.5)
Quest12 = Quest(12, 2, 1.5)

Quest13 = Quest(13, 4, 1)

def battle_1(A, enemy):
    party_attack_power = 0
    party_attack_power += A.attack_power(enemy)
    
    enemy_attack_power = 0
    enemy_attack_power += enemy.attack_power(A)

    #return 1 for victory, 0 for defeat
    if party_attack_power > enemy_attack_power:
        return 1
    else:
        return 0

def battle_4(A, B, C, D, enemy):
    party_attack_power = 0
    party_attack_power += A.attack_power(enemy)
    party_attack_power += B.attack_power(enemy)
    party_attack_power += C.attack_power(enemy)
    party_attack_power += D.attack_power(enemy)
    
    enemy_attack_power = 0
    enemy_attack_power += enemy.attack_power(A)
    enemy_attack_power += enemy.attack_power(B)
    enemy_attack_power += enemy.attack_power(C)
    enemy_attack_power += enemy.attack_power(D)

    #return 1 for victory, 0 for defeat
    if party_attack_power > enemy_attack_power:
        return 1
    else:
        return 0

def battle_6(A, B, C, D, E, F, enemy):
    party_attack_power = 0
    party_attack_power += A.attack_power(enemy)
    party_attack_power += B.attack_power(enemy)
    party_attack_power += C.attack_power(enemy)
    party_attack_power += D.attack_power(enemy)
    party_attack_power += E.attack_power(enemy)
    party_attack_power += F.attack_power(enemy)

    enemy_attack_power = 0
    enemy_attack_power += enemy.attack_power(A)
    enemy_attack_power += enemy.attack_power(B)
    enemy_attack_power += enemy.attack_power(C)
    enemy_attack_power += enemy.attack_power(D)
    enemy_attack_power += enemy.attack_power(E)
    enemy_attack_power += enemy.attack_power(F)

    #return 1 for victory, 0 for defeat
    if party_attack_power > enemy_attack_power:
        return 1
    else:
        return 0

#enemies
# affinity, might, power, speed, precision, constitution, defense, reflex, evasion, resilience

Zombies = Foe(5, 1 * renown_bonus, 2 * renown_bonus, 2 * renown_bonus, 2 * renown_bonus, 2 * renown_bonus,\
    2 * renown_bonus, 2 * renown_bonus, 2 * renown_bonus, 2 * renown_bonus)
Soliders = Foe(4, 1 * renown_bonus, 3 * renown_bonus, 2 * renown_bonus, 2 * renown_bonus, 3 * renown_bonus,\
    3 * renown_bonus, 2 * renown_bonus, 2 * renown_bonus, 3 * renown_bonus)

#weapons
# might, shape, rank
broken_sword = Weapon(1, 1, 1)
broken_spear = Weapon(1, 2, 1)
broken_axe = Weapon(1, 3, 1)
broken_bow = Weapon(1, 4, 1)

#characters
'''
(exp, affinity, \
blade exp, polearm exp, heavy exp, range exp, \
elemental exp, holy exp, dark exp, psychic exp, \
power base, power growth, speed base, speed growth, precision base, precision growth, constitution base, constitution growth, \
defense base, defense growth, reflex base, reflex growth, evasion base, evasion growth, resilience base, resilience growth)
'''
Douglas = Unit(1000, 4, \
    0, 200, 0, 0, \
    0, 0, 0, 0, \
    12, 0.4, 5, 0.1, 6, 0.1, 8, 0.25, \
    7, 0.2, 4, 0.1, 5, 0.1, 9, 0.2)

Lyra = Unit(500, 1, \
    0, 0, 0, 150, \
    0, 0, 0, 0, \
    3, 0.2, 8, 0.8, 7, 1.1, 2, 0, \
    2, 0.1, 5, 0.9, 8, 1, 1, 0)

Martin = Unit(0, 4, \
    100, 0, 0, 0, \
    0, 0, 0, 0, \
    3, 0.35, 0, 0, 0, 0, 0, 0, \
    3, 0.35, 0, 0, 0, 0, 0, 0)

Sera = Unit(0, 4, \
    0, 100, 0, 0, \
    0, 0, 0, 0, \
    0, 0, 3, 0.35, 0, 0, 0, 0, \
    0, 0, 3, 0.35, 0, 0, 0, 0)

Issac = Unit(0, 4, \
    0, 0, 100, 0, \
    0, 0, 0, 0, \
    0, 0, 0, 0, 3, 0.35, 0, 0, \
    0, 0, 0, 0, 3, 0.35, 0, 0)

Perry = Unit(0, 4, \
    0, 0, 0, 100, \
    0, 0, 0, 0, \
    0, 0, 0, 0, 0, 0, 3, 0.35, \
    0, 0, 0, 0, 0, 0, 3, 0.35)

def background():
    print (
    '''
    So, some BBEG is invading your country / world. The current militrary tried to stop them and got their asses kicked. So now the king is like "Shit!
    Okay, if anyone can raise up a squad powerful enough to take the BBEG down there will be REALLY cool rewards and stuff I promise.
    Please someone compotent do something, I have no fucking clue what I'm doing anymore!"

    Also with no military presence, there is like chaos and baddies everywhere. Which sucks ... Buuuuut, it does give you an oppuruntity
    to train your low level units up a bit. Silver linings

    You are a retired tactian who retired early in a small sleepy village. Now it's time to get things back in shape.

    You only start with a few people in village who can actually sorta fight.
    ''')

def Douglas_join():
    print ("Douglas has joined the party!")

def Douglas_background():
    print ("An old veteran who served time in the army. Has some prior experience but will struggle to learn new skills")

def Lyra_join():
    print ("Lyra has joined the party!")

def Lyra_backgroun():
    print ("An archer from your home village. Has some potential.")

def villagers_join():
    print ("Martin, Sera, Issac and Perry have joined the party!")

def villagers_background():
    print ("A common villager.")

available_quest_list = [1,2]

Quest_choice = 0
def Pick_quest():
    global Quest_choice
    if not available_quest_list:
        print ("There are no quests available right now")

    else:
        selecting = True
        while selecting:
            print ("Pick your next quest")

            if 1 in available_quest_list:
                print ("Quest 1" , "Gold:" , Quest1.gold_reward, "Renown:" , Quest1.renown_reward, \
                    "Unit exp:" , Quest1.unit_exp_reward, "Weapon exp:" , Quest1.weapon_exp_reward , "Overall challenge rating:" , Quest1.CR)
            if 2 in available_quest_list:
                print ("Quest 2" , "Gold:" , Quest2.gold_reward, "Renown:" , Quest2.renown_reward, \
                    "Unit exp:" , Quest2.unit_exp_reward, "Weapon exp:" , Quest2.weapon_exp_reward , "Overall challenge rating:" , Quest2.CR)

            text = input()

            if text == "1":
                Quest_choice = 1
                selecting = False
            elif text == "2":
                Quest_choice = 2
                selecting = False
            
            else:
                print ("Invalid input, please try again")

def Confirm_quest():
    if Quest_choice in available_quest_list:
        
        if Quest_choice == 1:
            available_quest_list.remove(1)
            if battle_6(Unit1, Unit2, Unit3, Unit4, Unit5, Unit6, Zombies) == 1:
                print ("Quest complete!")
                Quest1.victory
            elif battle_6(Unit1, Unit2, Unit3, Unit4, Unit5, Unit6, Zombies) == 0:
                print ("Quest failed...")
        elif Quest_choice == 2:
            available_quest_list.remove(2)
            if battle_6(Unit1, Unit2, Unit3, Unit4, Unit5, Unit6, Soliders) == 1:
                print ("Quest complete!")
                Quest2.victory
            elif battle_6(Unit1, Unit2, Unit3, Unit4, Unit5, Unit6, Soliders) == 0:
                print ("Quest failed...")

    else:
        print("That quest isn't available, please select another.")

#deployed units
Unit1 = Douglas
Unit2 = Lyra
Unit3 = Martin
Unit4 = Sera
Unit5 = Issac
Unit6 = Perry

Douglas.weapon_equip(broken_spear)

game_on = True
while game_on:
    #background()

    #text = input()

    Pick_quest()
    Confirm_quest()
