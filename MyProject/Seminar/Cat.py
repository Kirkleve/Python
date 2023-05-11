from Animal import Animal


class Cat(Animal):
    hunger = 0

    def voice(self):
        print("mew")

    def feed(self, hunger, food):
        if food == "fish":
            self.hunger -= hunger
        else:
            print("SSssshhhh...")
