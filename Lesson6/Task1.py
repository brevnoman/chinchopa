s=input("input your string\n")
l=s.split(' ')
d={i:l.count(i) for i in l if i!=''}
print(d)