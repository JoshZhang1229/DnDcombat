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
renown = 0

week = 1
season = 1

#classes

class Unit:
    def __init__(self, exp, affinity, blade_exp, polearm_exp, heavy_exp, range_exp, \
        strength_base, strength_growth, speed_base, speed_growth, precision_base, precision_growth, \
        constitution_base, constitution_growth, defense_base, defense_growth, reflex_base, reflex_growth, \
        evasion_base, evasion_growth, resilience_base, resilience_growth):

        self.affinity = affinity

        self.level = math.floor(math.log2(exp + 2))

        self.blade_exp = blade_exp
        self.polearm_exp = polearm_exp
        self.heavy_exp = heavy_exp
        self.range_exp = range_exp


        if self.blade_exp < 1000:
            self.blade_rank = 1
        else:
            self.blade_rank = math.ceil(math.log2 (self.blade_exp / 1000))

        if self.polearm_exp < 1000:
            self.polearm_rank = 1
        else:
            self.polearm_rank = math.ceil(math.log2 (self.polearm_exp / 1000))

        if self.heavy_exp < 1000:
            self.heavy_rank = 1
        else:
            self.heavy_rank = math.ceil(math.log2 (self.heavy_exp / 1000))

        if self.range_exp < 1000:
            self.range_rank = 1
        else:
            self.range_rank = math.ceil(math.log2 (self.range_exp / 1000))


        self.strength = strength_base + self.level * strength_growth
        self.speed = speed_base + self.level * speed_growth
        self.precision = precision_base + self.level * precision_growth
        self.constitution = constitution_base + self.level * constitution_growth
        self.defense = defense_base + self.level * defense_growth
        self.reflex = reflex_base + self.level * reflex_growth
        self.evasion = evasion_base + self.level * evasion_growth
        self.resilience = resilience_base + self.level * resilience_growth
    
    def attack_power(self, weapon, target):
        total = 0

        strength_bonus = 1
        if self.strength > target.defense:
            strength_bonus += 0.1 * (self.strength - target.defense)
        
        speed_bonus = 1
        if self.speed > target.reflex:
            speed_bonus += 0.1 * (self.speed - target.reflex)       
        
        precision_bonus = 1
        if self.precision > target.evasion:
            precision_bonus += 0.1 * (self.precision - target.evasion)        
        
        constitution_bonus = 1
        if self.constitution > target.resilience:
            constitution_bonus += 0.1 * (self.constitution - target.resilience)        
        
        total = weapon.might * strength_bonus * speed_bonus * precision_bonus * constitution_bonus



        if self.affinity - target.affinity == 1:
            total = total * 2
        
        if self.affinity == 1 and target.affinity == 6:
            total = total * 2
        

        #checking to see if the unit has the weapon rank to weild the weapon
        if weapon.shape == 1:
            if self.blade_rank < weapon.rank:
                total = 0

        if weapon.shape == 2:
            if self.polearm_rank < weapon.rank:
                total = 0

        if weapon.shape == 3:
            if self.heavy_rank < weapon.rank:
                total = 0

        if weapon.shape == 4:
            if self.range_rank < weapon.rank:
                total = 0


        return total


class Foe:
    def __init__(self, affinity, might, strength, speed, precision, constitution, \
        defense, reflex, evasion, resilience):
        pass

        self.affinity = affinity

        self.might = might

        self.strength = strength
        self.speed = speed
        self.precision = precision
        self.constitution = constitution
        self.defense = defense
        self.reflex = reflex
        self.evasion = evasion
        self.resilience = resilience
    
    def attack_power(self, target):
        total = 0

        strength_bonus = 1
        if self.strength > target.defense:
            strength_bonus += 0.1 * (self.strength - target.defense)
        speed_bonus = 1
        if self.speed > target.reflex:
            speed_bonus += 0.1 * (self.speed - target.reflex)       
        precision_bonus = 1
        if self.precision > target.evasion:
            precision_bonus += 0.1 * (self.precision - target.evasion)        
        constitution_bonus = 1
        if self.constitution > target.resilience:
            constitution_bonus += 0.1 * (self.constitution - target.resilience)        
        
        total = self.might * strength_bonus * speed_bonus * precision_bonus * constitution_bonus

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

        self.renown_bonus = math.log((renown + 5), 5)

        self.gold_reward = self.renown_bonus * time * difficulty * \
            randint(800000 , (1200000 + self.setup)) * randint(800000 , (1200000 - self.setup)) / (1000000 * 1000000)
        self.renown_reward = self.renown_bonus * time * difficulty * \
            randint(800000 , (1199999 + self.setup)) * randint(800000 , (1199999 - self.setup)) / (999999 * 999999)

        self.CR = self.gold_reward + self.renown_reward

    def generate_new_quest():
        self.time = time

        self.setup = seed * (week + season * 12)

        self.renown_bonus = math.log((renown + 5), 5)

        self.gold_reward = self.renown_bonus * time * difficulty * \
            randint(800000 , (1200000 + self.setup)) * randint(800000 , (1200000 - self.setup)) / (1000000 * 1000000)
        self.renown_reward = self.renown_bonus * time * difficulty * \
            randint(800000 , (1199999 + self.setup)) * randint(800000 , (1199999 - self.setup)) / (999999 * 999999)

        self.CR = self.gold_reward + self.renown_reward

    def victory():
        global gold
        global renown

        gold += 1000 * self.gold_reward
        renown += 20 * self.renown_reward

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
    party_attack_power += A.attack_power(longsword, enemy)
    
    enemy_attack_power = 0
    enemy_attack_power += enemy.attack_power(A)

    #return 1 for victory, 0 for defeat
    if party_attack_power > enemy_attack_power:
        return 1
    else:
        return 0

def battle_4(A, B, C, D, enemy):
    party_attack_power = 0
    party_attack_power += A.attack_power(longsword, enemy)
    party_attack_power += B.attack_power(longsword, enemy)
    party_attack_power += C.attack_power(longsword, enemy)
    party_attack_power += D.attack_power(longsword, enemy)
    
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


#enemies
Zombie = Foe(1, 3, 2, 2, 2, 2, 2, 2, 2, 2)

#weapons
longsword = Weapon(5, 1, 2)

#characters
dude = Unit(50, 5, 5000, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5)

NPC = Unit(10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5)

Douglas = Unit(32, 2, 0, 100, 0, 0, \
    12, 0.2, 5, 0, 6, 0, 8, 0.1, \
        7, 0.2, 4, 0, 5, 0, 9, 0.2)

Lyra = Unit(10, 4, 0, 0, 0, 50, \
    3, 0.5, 8, 1.2, 7, 1.1, 2, 0.3, \
        2, 0.1, 5, 0.9, 8, 1, 1, 0)

Martin = Unit(0, 6, 0, 0, 0, 0, \
    0, 0, 2, 0.5, 0, 0, 4, 0.8, \
        1, 0.2, 0, 0, 0, 0, 3, 0.4)

Sera = Unit(0, 6, 0, 0, 0, 0, \
    0, 0, 3, 0.25, 2, 0,2, 0, 0, \
        0, 0, 3, 0, 0, 0, 0.15)

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
    print ("An archer from your home village. Has some potential")

def Martin_join():
    print ("Martin has joined the party!")

def Martin_background():
    print ("A common villager trust into an unfamliar position")

def Sera_join():
    print ("Sera has joined the party!")

def Sera_background():
    print ("A common villager trust into an unfamliar position")

def Pick_quest():
    print ("Pick your next quest")

#deployed units
Unit1 = Douglas
Unit2 = Lyra
Unit3 = Martin
unit4 = Sera

game_on = True
while game_on:
    background()

    text = input()

    Pick_quest()
