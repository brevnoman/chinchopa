from file_manager import File
from playsound import playsound
import os

def interface():
    while True:
        name = input("write file name:\n")
        path = input("write file path:\n")
        file = File(name, path)
        if os.path.isfile(os.path.join(path, name)):
            break
        else:
            choose = input("there is no such file or directory, want to create it?(y/n):\n")
            if choose == "y":
                file.create_file_if_not_exist()
                break
            if choose == "n":
                choose = input("want to choose another file?(y/n):\n")
                if choose == "y":
                    continue
                elif choose == "n":
                    break
            else:
                print("there is no such action")

    while True:
        choose = input("choose one action:\n"
                       "1.Open and read file\n"
                       "2.Replace file\n"
                       "3.Copy file\n"
                       "4.Delete file\n"
                       "5.Change file\n"
                       "6.Change path\n"
                       "exit. for exit\n")
        if choose == "1":
            for i in file.open():
                print(i)
        elif choose == "2":
            new_path = input("where do you like to replace file\n")
            file.replace(new_path)
        elif choose == "3":
            new_path = input("write path to insert copy\n")
            file.copy_file(new_path)
        elif choose == "4":
            file.delete_file()
        elif choose == "5":
            new_file = input("write name of the file you like to browse\n")
            file.change_name(new_file)
        elif choose == "6":
            new_path = input("write path you like to go\n")
            file.change_path(new_path)
        elif choose == "exit":
            print("Bye, have a beautiful time!")
            playsound(os.path.join(os.getcwd(), "img_0498.mp3"))
            break

interface()