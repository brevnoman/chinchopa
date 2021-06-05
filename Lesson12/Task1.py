class Animal:
    def __init__(self):
        pass
    def talk(self):
        pass


class Cat(Animal):

    def talk(self):
        print("meow!")

class Dog(Animal):

    def talk(self):
        print("woof!")

class Furniture:

    def stand(self):
        print("it's just stand")

def make_it_talk(animal):
    if isinstance(animal, Cat) or isinstance(animal, Dog):
        animal.talk()
    else:
        print("this thing can't talk")



cat_obj=Cat()
dog_obj=Dog()
furniture_obj=Furniture()
make_it_talk(cat_obj)
make_it_talk(dog_obj)
make_it_talk(furniture_obj)