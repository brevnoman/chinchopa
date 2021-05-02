import json


def write_file(data):

    with open("myfile.txt", "w") as write:
        # json.dump(your_string+" ", write)
        write.write(json.dumps(''.join(data)))


def open_file():
    with open("myfile.txt", "r") as read:
        reader = json.load(read)
        print(reader)


def main():
    try:
        with open("myfile.txt", "r") as f:
            data = [json.load(f)]
    except Exception:
        with open("myfile.txt", "r") as f:
            f.write(json.dumps(f))
    while True:
        with open("myfile.txt", "r") as f:
            data = [json.load(f)]
        your_string = input()
        data.append(''.join(your_string+" "))
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