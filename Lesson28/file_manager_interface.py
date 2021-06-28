from file_manager import File
from playsound import playsound
import os

def interface():
    name = input("write file name:\n")
    path = input("write file path:\n")
    file = File(name, path)
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
            file.open()
        elif choose == "2":
            new_path = input("where do you like to replace file")
            file.replace(new_path)
        elif choose == "3":
            new_path = input("write path to insert copy")
            file.copy_file(new_path)
        elif choose == "4":
            file.delete_file()
        elif choose == "5":
            new_file = input("write name of the file you like to browse")
            file.change_name(new_file)
        elif choose == "6":
            new_path = input("write path you like to go")
            file.change_path(new_path)
        elif choose == "exit":
            print("Bye, have a beautiful time!")
            playsound(os.path.join(os.getcwd(), "img_0498.mp3"))
            break

interface()