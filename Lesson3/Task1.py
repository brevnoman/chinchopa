

a = str(input())
str_len = len(a)
while str_len < 2:
    print("you should try more longer word's")
    a = str(input())
    str_len = len(a)
a=a+" "
first_2let= a[0:2]
last_2let= a[-3:-1]
print(first_2let+last_2let)
