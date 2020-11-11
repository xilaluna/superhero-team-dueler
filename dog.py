class Dog:
    """
    This is creates a dog
    """

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        print("dog initialized!")


new_dog = Dog('Rex', 'SuperDog')
print(new_dog.breed)
