import math

while True:
    hi=input("1 or 2?:")
    if hi=="1":
        ch=input("10 or 01")
        if ch=="10":
            ans1=input("write correct answer for !12=")
            right_ans1= math.factorial(12)
            if ans1==str(right_ans1):
                print("good job", right_ans1, "is write answer)")
                break
            else:
                print("wrong")
                break
        elif ch=="01":
            ans2=input("write correct answer for 1+2=")
            right_ans2=1+2
            if ans2==str(right_ans2):
                print("good job", right_ans2, "is write answer)")
                break
            else:
                print("wrong")
                break
    elif hi=="2":
        ch=input("jscript or 001")
        if ch=="001":
            ans3=input("write correct answer for 11*187=")
            rigth_ans3=11*187
            if ans3==str(rigth_ans3):
                print("good job", rigth_ans3, "is write answer)")
                break
            else:
                print("wrong")
                break
        elif ch=="jscript":
            ans4=input("write correct answer for 1+12")
            right_ans4="112"
            if ans4==right_ans4:
                print("wth, is this real, how can 1+12 be", right_ans4,"but you right...")
                break
            elif ans4=="13":
                print("sorry buddy, but this is question for jscript-guys")
                break
            else:
                print("wrong")
                break
    else:
        print("you should chose only from given options")
