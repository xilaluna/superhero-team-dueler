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


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)
    print(my_hero.current_health)
