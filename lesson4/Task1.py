import random

while True:
    your_try = input("enter a number from 1 to 10, lets see your luck: ")
    #if random.randrange(1, 11).__str__() == your_try.__str__():
    if "1" == your_try.__str__():
        while True:
            choise = input("you are lucky today, would you like to try one more time y/n: ")
            if choise == "y":
                break
            elif choise == "n":
                exit("ok bye)")
            else:
                print('you can chose only "y" or "n": ')
                continue

    elif str.isdigit(your_try) and int(your_try) in range(1,11):
        while True:
            choise = input("mb next time, want try one more time? y/n: ")
            if choise == "y":
                break
            elif choise == "n":
                exit("ok bye)")
            else:
                print('you can chose only "y" or "n": ')
                continue

    else:
        print("You should choose only numbers from 1 to 10")

# более чистый вариант для консоли

# while True:
#     your_try = input("enter a number from 1 to 10, lets see your luck: ")
#     if random.randrange(1, 11).__str__() == your_try.__str__():
#         choise = input("you are lucky today, would you like to try one more time y/n: ")
#         while True:
#             choise = input()
#             if choise == "y":
#                 break
#             elif choise == "n":
#                 exit("ok bye)")
#             else:
#                 print('you can chose only "y" or "n": ')
#                 continue
#
#     else:
#       choise = input("you are lucky today, would you like to try one more time y/n: ")
#         while True:
#             choise = input()
#             if choise == "y":
#                 break
#             elif choise == "n":
#                 exit("ok bye)")
#             else:
#                 print('you can chose only "y" or "n": ')
#                 continue
