from prettytable import PrettyTable
stock = {"banana": 6,"apple": 0,"orange": 32,"pear": 15}
prices = {"banana": 4,"apple": 2,"orange": 1.5,"pear": 3}
p=list(stock.keys())
o=list(prices.keys())
p1=list(stock.values())
o1=list(prices.values())
print(o)
print(p)
total=0
table=PrettyTable()
table.field_names=["Title:", "Amount:", "Price for one piece:", "Cost:"]
for i in range(len(p)):
    table.add_row([p[i], p1[i], o1[i], p1[i]*o1[i]])
    total+=p1[i]*o1[i]
print(table)
print("Total price:",total)