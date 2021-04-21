import random
class Simple:
    def cho(self):
        while True:
            choise = input()
            if choise == "y":
                break
            elif choise == "n":
                exit("ok bye)")
            else:
                print('you can chose only "y" or "n": ')
                continue
s=Simple()
while True:
    your_try = input("enter a number from 1 to 10, lets see your luck: ")
    if random.randrange(1, 11).__str__() == your_try.__str__():
        print("you are lucky today, would you like to try one more time y/n: ")
        s.cho()
    elif str.isdigit(your_try) and int(your_try) in range(1,11):
        print("mb next time, want try one more time? y/n: ")
        s.cho()

    else:
        print("You should choose only numbers from 1 to 10")