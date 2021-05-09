class Person:

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


class Student(Person):

    def __init__(self, name, age, sex, group):
        super().__init__(name, age, sex)
        self.group = group


class Teacher(Person):
    def __init__(self, name, age, sex, pay):
        super().__init__(name, age, sex)
        self.pay = pay


teacher = Teacher(1, 2, 3, 4)

print(teacher.__dict__)
