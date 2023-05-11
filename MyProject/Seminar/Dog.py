from Animal import Animal


class Dog(Animal):
    hunger = 0

    def feed(self, hunger, food):
        if food == "meat":
            self.hunger -= hunger
        else:
            print("vuf vuf")

    def voice(self):
        print("Vof")
