class Dog:
    """
    This is creates a dog
    """

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        print(f'dog initialized!')

    def bark(self):
        print(f'Woof!')
        pass
