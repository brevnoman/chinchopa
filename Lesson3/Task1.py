
changeable_string = str(input())
str_len = len(changeable_string)
while str_len < 2:
    print("you should try more longer words")

    changeable_string = str(input())
    str_len = len(changeable_string)

changeable_string = changeable_string+" "
first_2let = changeable_string[0:2]
last_2let = changeable_string[-3:-1]
print(first_2let+last_2let)
