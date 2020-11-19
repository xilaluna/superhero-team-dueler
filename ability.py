import random


class Ability:
    """
    Sets the Heroes abilities
    """

    def __init__(self, name, max_damage):
        """
        initilaizes a heroes abilities attributes
        """
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        """
        Return a value between 0 and the value set by self.max_damage.
        """
        random_damage_value = random.randint(0, self.max_damage)
        return random_damage_value
