from abc import abstractmethod


class Animal:
    age = 0
    name = ""

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def voice(self):
        pass

    @abstractmethod
    def feed(self, hunger, food):
        pass
