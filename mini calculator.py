# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math

c = float(input('input 1st number='))
b = float(input('input 2nd number='))
print("choose act", '* for Multiplication', "/ for Division", '- for Subtraction', "+ for Addition",
      "^ for power 1st on 2nd", "|| for Subtraction Modulus", "// for floor division", sep="\n")
while True:
    d = str(input())
    if d == "*":
        v = c * b
        print('answer=', v)
        break
    elif d == "/":
        v = c / b
        print('answer=', v)
        break
    elif d == "-":
        v = c - b
        print('answer=', v)
        break
    elif d == "+":
        v = c + b
        print('answer=', v)
        break
    elif d == "^":
        v = c ** b
        print('answer=', v)
        break
    elif d == "||":
        v =math.fabs(c-b)
        print('answer=', v)
        break
    elif d == "//":
        v = c // b
        print('answer=', v)
        break
    else:
        print('choose else act')
