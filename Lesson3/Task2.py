


ph_num = str(input("input your phone number 10 digits:"))
while len(ph_num) !=10:
    ph_num=str(input("Please Try Again:"))
    while ph_num.isdigit() !=True:
        ph_num=str(input("Please Try Again:"))
print("Thank you!")