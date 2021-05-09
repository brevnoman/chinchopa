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


teacher = Teacher("Biba", 44, "yes", "dengi")
student = Student("Boba", 11, "no", "bourgeoisie")
print(teacher.__dict__)
print(student.__dict__)
