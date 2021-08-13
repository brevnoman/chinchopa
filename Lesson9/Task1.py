import json


def write_file(data):
    join = ''.join(data)
    with open("myfile.txt", "w") as write:
        # json.dump(your_string+" ", write)
        json.dump(join, write)


def open_file():
    with open("myfile.txt", "r") as read:
        reader = json.load(read)
        print(reader)


def main():
    data = ""
    try:
        with open("myfile.txt", "r") as f:
            data = [json.load(f)]
    except Exception:
        with open("myfile.txt", "w") as f:
            json.dump(data, f)
    while True:
        with open("myfile.txt", "r") as f:
            data = [json.load(f)]
            print(data)
        your_string = input()
        data.append(''.join(your_string + " "))
        write_file(data)
        open_file()


main()

# import json
#
#
# def write_file(your_string="Heello json World!!!"):
#     with open("myfile.txt", "w") as write:
#         json.dump(your_string, write)
# def open_file():
#     with open("myfile.txt", "r") as read:
#         reader = json.load(read)
#         print(reader)
# def main():
#     write_file()
#     open_file()
#
# main()
