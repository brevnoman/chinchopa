import random

i=0
l=[]
s=[]
while i<10:
    i+=1
    l.append(random.randint(1,10))
    s.append(random.randint(1,10))

print(l,s,sep="\n")
b=list(set(l).union(set(s)))
print(b)