from Animal import Animal


class Salmon(Animal):
    hunger = 0

    def feed(self, food):
        if food == 'bread':
            self.hunger -= 5
        else:
            print("bulk")

    def addHanger(self, hunger):
        self.hunger += hunger

    def isHungry(self):
        if self.hunger > 0:
            print("I am hungry")
        else:
            print("I am NOT hungry")
