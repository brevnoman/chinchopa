"""
open
read
copy
replace
delete
"""
import os


class File:
    def __init__(self, name: str, path:str):
        self.name = name
        self.path = path

    def create_file_if_not_exist(self):
        with open(os.path.join(self.path, self.name), "w") as file:
            file.write("")


    def get_name(self):
        return self.name

    def get_path(self):
        return self.path

    def open(self):
        with open(os.path.join(self.path, self.name), "r") as file:
            flag = True
            while flag:
                for i in range(100):
                    file.readline()
                while True:
                    choose = input("do you want read more? (y/n)\n")
                    if choose == "y":
                        break
                    elif choose == 'n':
                        flag = False
                        break
                    else:
                        print("you can choose only y or n")

    def delete_file(self):
        deleted_file = os.path.join(self.path, self.name)
        if os.path.exists(deleted_file):
            os.remove(deleted_file)
        else:
            raise Exception('File not found.')

    def change_path(self, new_path):
        self.path = new_path

    def change_name(self, new_name):
        self.name = new_name

    def copy_file(self, new_path):
        file_sourse = os.path.join(self.path, self.name)
        if os.path.exists(os.path.join(new_path, self.name)):
            counter = 1
            while True:
                file_name_list = self.name.split(".")
                file_name = file_name_list[0] + str(counter) + "." + file_name_list[1]
                if os.path.exists(os.path.join(self.path, file_name)):
                    counter += 1
                else:
                    file_destination = os.path.join(self.path, file_name)
                    break
        else:
            file_destination = os.path.join(new_path, self.name)
        with open(file_sourse, "r") as file:
            with open(file_destination, "w") as new_file:
                new_file.write(file.read())

    def replace(self, new_path):
        file_sourse = os.path.join(self.path, self.name)
        self.copy_file(new_path)
        os.remove(file_sourse)



# file = File("main.py" ,"D:\zalupa\drich\Lesson28")
# file.create_file_if_not_exist()
# file.copy_file("D:\zalupa\drich\Lesson28")
# file.copy_file("D:\zalupa\drich\Lesson28")
# file.copy_file("D:\zalupa\drich\Lesson28")
# file.copy_file("D:\zalupa\drich\Lesson28")
# file.replace("D:\zalupa\drich\Lesson27")
# file.change_name("delete_me.py")
# file.delete_file()