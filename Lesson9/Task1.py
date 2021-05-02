import json


def write_file(your_string="Heello json World!!!"):
    with open("myfile.txt", "w") as write:
        json.dump(your_string, write)
def open_file():
    with open("myfile.txt", "r") as read:
        reader = json.load(read)
        print(reader)
def main():
    write_file()
    open_file()

main()