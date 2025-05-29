#
# CS1010X --- Programming Methodology
#
# Contest 15.1 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hungry_games_classes import *
#from contest_simulation import *
import random


class Player(Tribute):
    CRITICAL_HEALTH_THRESHOLD = 50
    CRITICAL_HUNGER_THRESHOLD = 50
    MAX_WEAPONS_TO_CARRY = 2

    def check_health(self):
        health = self.get_health()
        medicines = self.get_medicine()
        # Prioritize eating if below critical health AND have medicine
        if health <= self.CRITICAL_HEALTH_THRESHOLD and medicines:
            # Find the medicine with the highest healing value
            best_medicine = None
            max_value = 0
            for med in medicines:
                if med.get_medicine_value() > max_value:
                    max_value = med.get_medicine_value()
                    best_medicine = med
            if best_medicine:
                return ("EAT", best_medicine)
        return False

    def check_hunger(self):
        hunger = self.get_hunger()
        foods = self.get_food()
        # Prioritize eating if below critical hunger AND have food
        if hunger <= self.CRITICAL_HUNGER_THRESHOLD and foods:
            # Find the food with the highest hunger value
            best_food = None
            max_value = 0
            for food in foods:
                if food.get_food_value() > max_value:
                    max_value = food.get_food_value()
                    best_food = food
            if best_food:
                return ("EAT", best_food)
        return False

    def check_nearby_items(self):
        items_nearby = self.objects_around()
        if not items_nearby:
            return False

        health = self.get_health()
        weapons = self.get_weapons()

        best_target = None
        best_weapon_for_target = None
        best_weapon_nearby = None
        best_medicine_to_take = None
        best_food_to_take = None
        other_item_to_take = None

        for item in items_nearby:
            if isinstance(item, LivingThing):
                # Only attack if we have weapons & health
                if weapons and health > self.CRITICAL_HEALTH_THRESHOLD / 2:
                    chosen_weapon = None
                    max_damage = 0
                    for weapon in weapons:
                        # Check weapon usable
                        if not isinstance(weapon, RangedWeapon) or (isinstance(weapon, RangedWeapon) and weapon.shots_left() > 0):
                            if weapon.max_damage() > max_damage:
                                chosen_weapon = weapon
                                max_damage = weapon.max_damage()
                    if chosen_weapon:
                        # Found a target and a suitable weapon
                        best_target = item
                        best_weapon_for_target = chosen_weapon
                        break 

            elif isinstance(item, Weapon):
                # Take weapon
                if len(weapons) < self.MAX_WEAPONS_TO_CARRY:
                    if not best_weapon_nearby or item.max_damage() > best_weapon_nearby.max_damage():
                        best_weapon_nearby = item
                else: # Check if it's better
                    current_best_weapon = None
                    if weapons:
                        current_best_weapon = max(weapons, key=lambda w: w.max_damage())
                    if current_best_weapon and item.max_damage() > current_best_weapon.max_damage():
                        best_weapon_nearby = item 

            elif isinstance(item, Medicine):
                if not best_medicine_to_take or item.get_medicine_value() > best_medicine_to_take.get_medicine_value():
                    best_medicine_to_take = item

            elif isinstance(item, Food):
                # Always prioritize taking food
                if not best_food_to_take or item.get_food_value() > best_food_to_take.get_food_value():
                    best_food_to_take = item
            else: # Any other item
                if not other_item_to_take: 
                    other_item_to_take = item

        if best_target and best_weapon_for_target:
            return ("ATTACK", best_target, best_weapon_for_target)
        elif best_weapon_nearby:
            return ("TAKE", best_weapon_nearby)
        elif best_medicine_to_take:
            return ("TAKE", best_medicine_to_take)
        elif best_food_to_take:
            return ("TAKE", best_food_to_take)
        elif other_item_to_take:
            return ("TAKE", other_item_to_take)

        return False

    def do_random(self):
        inventory = self.get_inventory()

        # Reload ranged weapons in free time
        weapons = self.get_weapons()
        ammos = [item for item in inventory if isinstance(item, Ammo)]
        if weapons and ammos:
            for weapon in weapons:
                if isinstance(weapon, RangedWeapon) and weapon.shots_left() < 1:
                    for ammo in ammos:
                        # Match weapon type
                        if hasattr(ammo, 'weapon_type') and ammo.weapon_type() == weapon.get_name():
                            return ("LOAD", weapon, ammo)

        # Run to another place for murder spree or resource gathering
        exits = self.get_exits()
        if exits:
            index = random.randint(0, len(exits) - 1)
            direction = exits[index]
            return ("GO", direction)

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

        moves = [
            self.check_health,
            self.check_hunger,
            self.check_nearby_items,
            self.do_random
        ]

        for move_func in moves:
            action = move_func()
            if action:
                return action

        return None


#######################################
# Testing Code
#######################################

# We only execute code inside the if statement if this file is
# not being imported into another file
# if __name__ == '__main__':
#     def qualifer_map(size, wrap):
#         game_config = GameConfig()
#         game_config.set_item_count(Weapon, 10)
#         game_config.set_item_count(RangedWeapon, 10)
#         game_config.set_item_count(Food, 10)
#         game_config.set_item_count(Medicine, 10)
#         game_config.set_item_count(Animal, 10)
#         game_config.steps = 1000

#         def spawn_wild_animals(game):
#             for i in range(3):
#                 animal = DefaultItemFactory.create(WildAnimal)
#                 game.add_object(animal[0])
#                 GAME_LOGGER.add_event("SPAWNED", animal[0])
#         game_config.add_periodic_event(20, spawn_wild_animals, "Spawn Wild Animals")

#         return (GameMap(size, wrap=wrap), game_config)

#     # Create 6 AI Clones
#     tributes = []
#     for i in range(6):
#         # An AI is represented by a tuple, with the Class as the first element,
#         # and the name of the AI as the second
#         ai = (Player, "AI" + str(i))
#         tributes.append(ai)

#     # Qualifier Rounds
#     # Uncomments to run more rounds, or modify the rounds list
#     # to include more rounds into the simulation
#     # (Note: More rounds = longer simulation!)
#     rounds = [qualifer_map(4, False),
#               #qualifer_map(4, False),
#               #qualifer_map(4, False),
#               qualifer_map(4, True),
#               #qualifer_map(4, True),
#               #qualifer_map(4, True),
#              ]



#     match = Match(tributes, rounds)
#     print("Simulating matches... might take a while")

#     # Simulate without the graphics
#     #match.text_simulate_all()

#     # Simulate a specific round with the graphics
#     # Due to limitation in the graphics framework,
#     # can only simulate one round at a time
#     # Round id starts from 0
#     match.gui_simulate_round(0)
