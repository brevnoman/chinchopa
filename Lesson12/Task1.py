class Animal:
    def __init__(self):
        pass
    def talk(self):
        if isinstance(self, Dog):
            print("woof")
        elif isinstance(self, Cat):
            print("meow")


class Cat(Animal):

    def __init__(self):
        super().__init__()
        pass
    def talk(self):
        print("meow!")

class Dog(Animal):
    def __init__(self):
        super().__init__()
        pass
    def talk(self):
        print("woof!")

class Furniture:
    def __init__(self):
        pass

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