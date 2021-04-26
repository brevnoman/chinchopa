# 1 Variant
# i=tuple(range(1,11))
# j=[]
# for p in i:
#     d=p**2
#     j.append(d)
# j=tuple(j)
# spisok=[i,j]
# print(i)
# print(j)
# print(spisok)

# 2 Variant
#spisok=[tuple(i for i in range(1,11)),tuple(i*i for i in range(1,11))]
#print (spisok)
# 3 Variant
# list1 = []
# for i in range(1, 11):
#     list1.append((i, i**2))
list2=list((i,i**2) for i in range(1,11))
print(list2)

