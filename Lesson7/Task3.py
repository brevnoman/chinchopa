# numbers_list = []
# chose = ""
#
#
# def make_operation():
#     while True:
#         choose = numbers_list[0]
#         if choose == "+":
#             addition()
#             break
#         elif choose == "-":
#             subtraction()
#             break
#         elif choose == "*":
#             multiplication()
#             break
#
#
# def addition():
#     result = int(numbers_list[1])
#     for i in numbers_list[1:]:
#         result = result + int(i)
#     print(result)
#
#
# def subtraction():
#     result = int(numbers_list[1])
#     for i in numbers_list[1:]:
#         result = result - int(i)
#     print(result)
#
#
# def multiplication():
#     result = int(numbers_list[1])
#     for i in numbers_list[1:]:
#         result = result * int(i)
#     print(result)
#
#
# while True:
#     numbers = input("input -, + or * first and then numbers through a space\n").split()
#     numbers_list = [i for i in numbers]
#     if len(numbers_list) < 3:
#         print("please write more numbers")
#         continue
#     else:
#         make_operation()
#     q_iut = input("want to try one more time? yes/no\n")
#     if q_iut.lower() != "yes" and q_iut.lower() != "no":
#         print("you can answer only yes or no")
#     elif q_iut.lower() == "no":
#         break


def make_operation(conditions):
    print(eval(conditions[0].join(conditions[1:])))


def main():
    conditions = input("choose +,- or * and then write nums that will ").split(" ")
    make_operation(conditions)