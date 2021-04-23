l=list(range(1,101)) #main list
b=[]    #list that compare only needed numbers
listind=0   #index of "l" list
while listind<100:          #cycle to get 100 indeces and check every element
    c= l[listind]       #current element of "l" list
    listind += 1
    if c%7==0 and not c%5==0:   #check multiplicity to 7 and non-multiplicity to 5
        b.append(c)     #adding to "b" list suitable elements
print(b)
