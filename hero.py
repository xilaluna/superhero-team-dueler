import random
from ability import Ability
from armor import Armor


class Hero:
    """
    Hero creation
    """

    def __init__(self, name, starting_health=100, ):
        """
        instance attributes
        """
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()
        self.armors = list()

    def fight(self, opponent):
        """
        Current Hero will take turns fighting the opponent hero passed in.
        """
        fighters = [self.name, opponent.name]
        winner = random.choice(fighters)
        return(f'{winner} won!')

    def add_ability(self, ability):
        """
        Adds abilities to the ability list
        """
        self.abilities.append(ability)

    def attack(self):
        """
        calulates the total damage of all ability attacks
        """
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        """
        adds armor to the armor list
        """
        self.armors.append(armor)

    def defend(self, damage_amt):
        """
        Calculate the total block amount from all armor blocks.
        return: total_block:Int
        """
        total_armor = 0
        for armor in self.armors:
            total_armor += armor.defend()
        return total_armor


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    ability = Ability("Great Debugging", 50)
    another_ability = Ability("Smarty Pants", 90)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    hero.add_ability(another_ability)
    print(hero.attack())
