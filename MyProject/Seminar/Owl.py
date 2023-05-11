from Animal import Animal
from Salmon import Salmon


class Owl(Animal):
    hunger = 0

    def addHunger(self, hunger):
        self.hunger += hunger

    def feed(self, hunger, food):
        if isinstance(food, Salmon):
            self.hunger -= hunger
        else:
            print("boo")

    def isHungry(self):
        if self.hunger > 0:
            print("I am hungry")
        else:
            print("I am NOT hungry")

    def voice(self):
        print("Ow")
