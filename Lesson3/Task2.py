



ph_num = str(input("input your phone number 10 digits:"))
while True:
    if ph_num.isdigit() !=True:
        ph_num=str(input("Please Try Again(invalid numbers):"))

    elif len(ph_num) !=10:
        ph_num=str(input("Please Try Again(your phone number should be 10 characters long):"))
    else:
        print("Thank you!")
        break