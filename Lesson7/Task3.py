numbers_list = []
chose = ""


def make_operation():
    while True:
        choose = input("choose one of following operations\n +, -, *")
        if choose == "+":
            addition()
            break
        elif choose == "-":
            subtraction()
            break
        elif choose == "*":
            multiplication()
            break
        else:
            print("you can chose only the suggested options")


def addition():
    result = 0
    for i in numbers_list:
        result = result + i
    print(result)


def subtraction():
    result = 0
    for i in numbers_list:
        result = result - i
    print(result)


def multiplication():
    result = 1
    for i in numbers_list:
        result = result * i
    print(result)


while True:
    numbers = input("input your numbers through a space\n").split()
    numbers_list = [int(i) for i in numbers if i.isdecimal()]
    if len(numbers_list) < 2:
        print("please write more numbers")
        continue
    else:
        make_operation()
    q_iut = input("want to try one more time? yes/no\n")
    if q_iut.lower() != "yes" and q_iut.lower() != "no":
        print("you can answer only yes or no")
    elif q_iut.lower() == "no":
        break
