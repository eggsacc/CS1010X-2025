#
# CS1010X --- Programming Methodology
#
# Mission 15 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hungry_games_classes import *
from engine import *
import simulation
import random

# I tested this AI, it just stands around collecting everything and eating
# when there's no living things around, and goes on a murder rampage
# the moment it acquires weapons and finds a living thing
class XX_AI(Tribute):

    # @brief Check health, eat panadol if headache
    # @note If no medicines available, just die
    # @retval Action if eat med, otherwise False
    def check_health(self):
        health = self.get_health()
        medicines = self.get_medicine()
        if(health <= 10 and medicines):
            return ("EAT", medicines[0])
        else:
            return False

    # @brief Check hunger, eat if humgri
    # @note If no food, just starve
    # @retval Action if eat food, otherwise False
    def check_hunger(self):
        hunger = self.get_hunger()
        foods = self.get_food()
        if(hunger <= 10 and foods):
            return ("EAT", foods[0])
        else:
            return False

    # @brief Scavenge for items
    # @retval False if nothing around, else action to pick up item
    def check_nearby_items(self):
        weapons = self.get_weapons()
        items_nearby = self.objects_around()

        if(not items_nearby):
            return False
        
        weapon = None
        living_thing = None
        medicine = None
        others = None

        for item in items_nearby:
            # Prioritize taking weapons if I have none or if it's higher damage
            # To survive is to kill
            if(isinstance(item, Weapon)):
                if(len(weapons) <= 2):
                    weapon = item
                    break
            
            # Living things! I picked up weapons for a reason
            # Stab them as hard as possible
            if(weapons and isinstance(item, LivingThing)):
                chosen = None
                max_damage = 0
                for weapon in weapons:
                    if(not isinstance(weapon, RangedWeapon) or (isinstance(weapon, RangedWeapon) and weapon.shots_left() > 0)):
                        if(weapon.max_damage() > max_damage):
                            chosen = weapon
                            max_damage = weapon.max_damage()
                if(chosen):
                    living_thing = item
                    weapon = chosen
                    break
            
            # Next is medicine, cos eating medicine makes my belly full too
            if(isinstance(item, Medicine)):
                if(medicine == None):
                    medicine = item
                elif(item.get_medicine_value() > medicine.get_medicine_value()):
                    medicine = item
    
            # Or just take whatever it is
            else:
                others = item
        
        # Kill first
        if(living_thing):
            return ("ATTACK", living_thing, weapon)
        # Else grab murder tool
        elif(weapon):
            return ("TAKE", weapon)
        # Else take medicine
        elif(medicine):
            return ("TAKE", medicine)
        # Else take whatever
        else:
            return ("TAKE", others)
        
    # @brief What to do if none of the previous checks return anything? idk
    #        Just reload the weapon if possible, or run around I guess
    # @retval Action if possible, else None
    def do_random(self):
        inventory = self.get_inventory()

        # Reload ranged weapons in free time
        weapons = self.get_weapons()
        ammos = [item for item in inventory if isinstance(item, Ammo)]
        if(weapons and ammos):
            for weapon in weapons:
                if(isinstance(weapon, RangedWeapon) and weapon.shots_left() < 1):
                    for ammo in ammos:
                        if(ammo.weapon_type() == weapon.get_name()):
                            return ("LOAD", weapon, ammo)
        
        # Run to another place for murder spree
        exits = self.get_exits()
        if exits:
            index = random.randint(0, len(exits)-1)
            direction = exits[index]
            return ("GO", direction)
        
        # :(
        return None


    def next_action(self):
        # ############### Available actions: ###############
        # ("ATTACK", LivingThing object, Weapon object)
        # ("TAKE", Thing object)
        # ("EAT", Food object)
        # ("GO", Direction)
        # ("LOAD", RangedWeapon object, Ammo object)

        # ############### Available methods: ###############
        # get_health()
        # get_weapons()
        # get_food()
        # get_medicine()
        # objects_around()
        # get_exits()
        # get_hunger()
        # get_inventory()
        # weapons - min_damage()
        # weapons - max_damage()
        # ammos - weapon_type()
        # ranged weapons - shots_left()
        
        # All the functions to iterate through
        moves = [self.check_health, self.check_hunger, self.check_nearby_items, self.do_random]
        
        for move in moves:
            action = move()
            if(action):
                return action

# NOTE: DO NOT remove the 2 lines of code below.
#
# In particular, you will need to modify the `your_AI = XX_AI` line so that
# `XX_AI` is the name of your AI class.
# For instance, if your AI class is called `MyPrecious_AI`, then you have to
# modify that line to:
#
#     your_AI = MyPrecious_AI
#
# Failure to do so will result in the following exception on Coursemology when
# you run the test cases:
#
#     Traceback (most recent call last):
#       in <module>
#     NameError: name 'your_AI' is not defined
#
# You have been warned!
time_limit = 50 # Modify if your AI needs more than 50 moves for task 2
your_AI = XX_AI # Modify if you changed the name of the AI class



##################
# Simulation Code
##################
##########
# Task 1 #
##########
# Goal:
# 1. Your AI should be able to pick up a Weapon / RangedWeapon
# 2. Your AI should be able to kill chicken
# 3. Your AI should be able to pick up chicken_meat after killing chicken

# Replace XX_AI with the class name of your AI
# Replace gui=True with gui=False if you do not wish to see the GUI
#simulation.task1(XX_AI("XX AI", 100), gui=True)


##########
# Task 2 #
##########
## 1. Your AI should be able to pick up a Weapon / RangedWeapon
## 2. Your AI should be able to move around and explore
## 3. Your AI should be able to find harmless Tribute and kill him

# Replace XX_AI with the class name of your AI
# Replace gui=True with gui=False if you do not wish to see the GUI

time_limit = 20    # You may change the time limit if your AI is taking too long
# simulation.task2(XX_AI("XX AI", 100), time_limit, gui=True)



#################
# Optional Task
#################
## You can create your own map and see how your AI behaves!

# Define the parameters of the map
def config():
    ## The game should have a 3x3 map
    game_map = GameMap(3)

    ## You can change the numbers to create different kinds of maps for
    ## the optional task.
    game_config = GameConfig()
    game_config.set_item_count(Weapon, 3)
    game_config.set_item_count(Animal, 10)
    game_config.set_item_count(RangedWeapon, 5)
    game_config.set_item_count(Food, 5)
    game_config.set_item_count(Medicine, 5)

    game = GameEngine(game_map, game_config)

    # Add some dummy tributes
    ryan = Tribute("Ryan", 100)
    waihon = Tribute("Wai Hon", 100)
    soedar = Tribute("Soedar", 100)

    game.add_tribute(ryan)
    game.add_tribute(waihon)
    game.add_tribute(soedar)

    # Yes, your AI can fight with himself
    #ai_clone = XX_AI("AI Clone", 100)
    #game.add_tribute(ai_clone)

    return game

# Replace XX_AI with the class name of your AI
# Replace gui=True with gui=False if you do not wish to see the GUI
simulation.optional_task(XX_AI("XX AI", 100), config, gui=True)
