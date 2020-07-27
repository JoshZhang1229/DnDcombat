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



#classes

class Unit:
    def __init__(self, exp, affinity, blade_exp, polearm_exp, heavy_exp, range_exp, \
        strength_base, strength_growth, speed_base, speed_growth, precision_base, precision_growth, \
        constitution_base, constitution_growth, defense_base, defense_growth, reflex_base, reflex_growth, \
        evasion_base, evasion_growth, resilience_base, resilience_growth):

        self.affinity = affinity

        self.level = math.floor(math.log2(exp))

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

dude = Unit(50, 5, 5000, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5)

print ("level" , dude.level)
print ("strength" , dude.strength)

NPC = Unit(10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5)

class Foe:
    def __init__(self, affinity, strength, speed, precision, constitution, \
        defense, reflex, evasion, resilience):
        pass

        self.affinity = affinity

        self.strength = strength
        self.speed = speed
        self.precision = precision
        self.constitution = constitution
        self.defense = defense
        self.reflex = reflex
        self.evasion = evasion
        self.resilience = resilience
    
    def attack_power(self, might, target):
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
        
        total = might * strength_bonus * speed_bonus * precision_bonus * constitution_bonus

        if self.affinity - target.affinity == 1:
            total = total * 2
        
        if self.affinity == 1 and target.affinity == 6:
            total = total * 2

        return total

Zombie = Foe(1, 2, 2, 2, 2, 2, 2, 2, 2)

class Weapon:
    def __init__(self, might, shape, rank):
        self.might = might
        self.shape = shape
        self.rank = rank

longsword = Weapon(5, 1, 2)

class Quest:
    pass


def battle_1(A, enemy):
    party_attack_power = 0
    party_attack_power += A.attack_power(longsword, enemy)
    print ("a strengthbonus" , A.attack_power(longsword, enemy))
    
    enemy_attack_power = 0
    enemy_attack_power += enemy.attack_power(2, A)

    print ("party attack power" , party_attack_power)
    print (enemy_attack_power)

    #return 1 for victory, 0 for defeat
    if party_attack_power > enemy_attack_power:
        print ("victory")
    else:
        print ("defeat")

battle_1(dude, Zombie)