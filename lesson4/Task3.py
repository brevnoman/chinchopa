import random

# не вносит изменений в саму строку просто применяет в единичном случае рандомное смешение
string = input("Write some words:")
string1 = ''.join(random.sample(string, len(string)))
string2 = ''.join(random.sample(string, len(string)))
string3 = ''.join(random.sample(string, len(string)))
string4 = ''.join(random.sample(string, len(string)))
string5 = ''.join(random.sample(string, len(string)))
print(string1, string2, string3, string4, string5, sep="\n")

# меняет СПИСОК и при последующем обращении к нему он уже не будет прежним... ;(
# тут я немножко поизвращался
# string = input("Write some words:")
# l=list(string)
# i=1
# while i<6:
#     i=i+1
#     random.shuffle(l)
#     result = ''.join(l)
#     print(result)
