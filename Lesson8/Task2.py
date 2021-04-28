

def mathick(a=input("enter the number to be squared\n"),b=input("enter the number that will divide the squared\n")):
    try:
        result=int(a)*int(a)/int(b)
        print(result)
    except ZeroDivisionError:
        print("you cannot divide by zero, try one more time")
    except ValueError:
        print("you should enter only numbers")
mathick()