import random
from typing import List
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
        return(f'{winner} Won!')

    def add_ability(self, ability):
        pass


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")

    print(hero1.fight(hero2))
