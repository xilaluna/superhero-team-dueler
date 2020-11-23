class Animal:
    """
    Animal class
    """

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'{self.name} is eating')

    def drink(self):
        print(f'{self.name} is drinking')


class Frog(Animal):
    def __init__(self, name):
        self.name = name

    def jump(self):
        print(f'{self.name} is jumping')


doggy = Animal("Anzu")
doggy.drink()
doggy.eat()

lenny = Frog('lenny')
lenny.drink()
lenny.eat()
lenny.jump()
