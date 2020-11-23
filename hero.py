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
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()

        if total_block >= damage_amt:
            return damage_amt
        else:
            return total_block

    def take_damage(self, damage):
        """
        receives damage and changes the heroe's health.
        """
        damage -= self.defend(damage)
        self.current_health -= damage

    def is_alive(self):
        """
        checks if a hero is a live or dead.
        """
        if self.current_health <= 0:
            return False
        else:
            return True

    def fight(self, opponent):
        """
        starts the fight for the heroes.
        """
        if not self.abilities or not opponent.abilities:
            print('Draw')
        else:
            while True:
                opponent.take_damage(self.attack())
                if opponent.is_alive():
                    pass
                else:
                    print(f'{self.name} wins!')
                    break

                self.take_damage(opponent.attack())
                if self.is_alive():
                    pass
                else:
                    print(f'{opponent.name} wins!')
                    break


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
