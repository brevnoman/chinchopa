


ph_num = str(input("input your phone number like this (0991234567):"))
first_dig=ph_num[0]
while len(ph_num) !=10:
    ph_num=str(input("Please Try Again2:"))
    while ph_num.isdigit() !=True:
        ph_num=str(input("Please Try Again3:"))
print("Thank you!")