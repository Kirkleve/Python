from Cat import Cat
from Owl import Owl
from Dog import Dog
from Salmon import Salmon

cat = Cat("cat1", 5)
cat.voice()

print(cat.getAge())

dog = Dog("dog1", 8)
dog.voice()
print("")

salmon = Salmon("salmon1", 3)
salmon.addHanger(5)
salmon.feed("eggs")
salmon.isHungry()
salmon.feed("bread")
salmon.isHungry()
print("")

owl = Owl("owl1", 6)
owl.addHunger(5)
owl.addHunger(5)
owl.isHungry()
owl.feed(4, dog)
owl.isHungry()
owl.feed(4, cat)
owl.feed(4, salmon)
owl.feed(4, salmon)
owl.isHungry()
owl.feed(4, salmon)
owl.isHungry()


