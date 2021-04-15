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
