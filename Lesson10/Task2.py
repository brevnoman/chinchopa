
class Dog:
    age_factor = 7

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def human_age(self):
        print(f"{self.name} is {self.age * Dog.age_factor} years old in human equivalent")


dog_obj = Dog("Solomon", 14)
dog_obj.human_age()
