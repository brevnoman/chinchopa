import json


def phonebook():
    empty_string = ""
    try:
        with open("phonebook.txt", "r") as f:
            phonebook_dict = json.load(f)

    except FileNotFoundError:
        with open("phonebook.txt", "w") as f:
            json.dump(list(), f)
        with open("phonebook.txt", "r") as f:
            phonebook_dict = json.load(f)

    while True:
        print(phonebook_dict)
        menu = input("what would you like to do (find/add/exit)\n")
        if menu == "find":
            find_choose(phonebook_dict)
            break
        elif menu == "add":
            add_numb(phonebook_dict)
            break
        elif menu == "exit":
            exit("bye")
        else:
            print("this is incorrect parameter, try one more time")

    save_changes(phonebook_dict)


def save_changes(phonebook_dict):
    with open("phonebook.txt", "w") as j:
        json.dump(phonebook_dict, j)
    with open("phonebook.txt", 'r') as j:
        data = [json.load(j)]
        print(data)


def find_choose(phonebook_dict):
    while True:
        find_option = input(
            "how would you like to find (full name/first name/ last name/telephone number/city/state or write exit to close programm)\n")
        if find_option == "full name":
            full_name = input("write full name:\t").split(" ")
            count = -1
            for i in phonebook_dict:
                count += 1
                if full_name[0] in i and full_name[1] in i:
                    print(i)
                    choose(count, phonebook_dict, i)
                    break
        elif find_option == "first name":
            first_name = input("write first name:\t")
            count = -1
            for i in phonebook_dict:
                count += 1
                if first_name in i:
                    print(i)
                    choose(count, phonebook_dict, i)
                    break
        elif find_option == "last name":
            last_name = input("write last name:\t")
            count = -1
            for i in phonebook_dict:
                count += 1
                if last_name in i:
                    print(i)
                    choose(count, phonebook_dict, i)
                    break
        elif find_option == "telephone number":
            number = input("write telephone number:\t")
            count = -1
            for i in phonebook_dict:
                count += 1
                if number in i:
                    print(i)
                    choose(count, phonebook_dict, i)
                    break
        elif find_option == "city":
            city = input("write city:\t")
            count = -1
            for i in phonebook_dict:
                count += 1
                if city in i:
                    print(i)
                    choose(count, phonebook_dict, i)
                    break
        elif find_option == "state":
            state = input("write state:\t")
            count = -1
            for i in phonebook_dict:
                count += 1
                if state in i:
                    print(i)
                    choose(count, phonebook_dict, i)
                    break
        elif find_option == "exit":
            exit("bye")
        else:
            print("this is incorrect parameter, try one more time")


def add_numb(phonebook_dict):
    number = input("number:\t")
    first_name = input("first name:\t")
    last_name = input("last_name:\t")
    city = input("city:\t")
    state = input("state:\t")
    account = [number, first_name, last_name, city, state]
    phonebook_dict.append(account)
    save_changes(phonebook_dict)
    stay_or_not()


def change(phonebook_dict, i):
    while True:
        choose = input("what would you like to change?(telephone number/ first name/ last name/ city/ state):\n")
        list = [1, 2, 3, 4]
        if choose == "telephone number":
            i[0] = input("write new number:\n")
            save_changes(phonebook_dict)
            stay_or_not()
        elif choose == "first name":
            i[1] = input("write new first name:\n")
            save_changes(phonebook_dict)
            stay_or_not()
        elif choose == "last name":
            i[2] = input("write new last name:\n")
            save_changes(phonebook_dict)
            stay_or_not()
        elif choose == "city":
            i[3] = input("write new city:\n")
            save_changes(phonebook_dict)
            stay_or_not()
        elif choose == "state":
            i[4] = input("write new state:\n")
            save_changes(phonebook_dict)
            stay_or_not()
        else:
            print("Wrong option input")


def delete(count, phonebook_dict, i):
    phonebook_dict.remove(phonebook_dict[count])
    save_changes(phonebook_dict)
    stay_or_not()


def choose(count, phonebook_dict, i):
    while True:
        next_move = input("what do you like to do with this contact(change/ delete/ exit)")
        if next_move == "change":
            change(phonebook_dict, i)
            break
        elif next_move == "delete":
            delete(count, phonebook_dict, i)
            break
        elif next_move == "exit":
            exit("bye)")
        else:
            print("incorrect choose")


def stay_or_not():
    while True:
        stay = input("do you want do something else?yes/no:\n")
        if stay == "yes":
            phonebook()
            exit()
        elif stay == "no":
            exit("ok, bye)")
        else:
            print("only yes or no")


phonebook()
