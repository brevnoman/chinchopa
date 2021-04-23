import random
i=0
l=[]
while i<10:
    i+=1
    l.append(random.randrange(1000))
print("not sorted list:",l)
l.sort()
print("sorted list:",l)
print("largest num of list:",l[-1])