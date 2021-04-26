s=input("input your string\n")
l=s.split(' ')
d={}
for i in l:
    if i!='':
        d[i]=l.count(i)
print(d)