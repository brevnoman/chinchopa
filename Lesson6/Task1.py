s=input("input your string\n")
l=s.split(' ')
d={}
for i in l:
    if i!='':
        d.setdefault(i,l.count(i))
    else:
        break
print(d)