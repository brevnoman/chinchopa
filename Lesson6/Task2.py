from prettytable import PrettyTable
stock = {"banana": 6,"apple": 0,"orange": 32,"pear": 15}
prices = {"banana": 4,"apple": 2,"orange": 1.5,"pear": 3}
stocknames=list(stock.keys())
pricesnames=list(prices.keys())
stocknum=list(stock.values())
pricesnum=list(prices.values())
total=0
table=PrettyTable()
table.field_names=["Title:", "Amount:", "Price for one piece:", "Cost:"]
for i in range(len(stocknames)):
    table.add_row([stocknames[i], stocknum[i], pricesnum[i], stocknum[i]*pricesnum[i]])
    total+=stocknum[i]*pricesnum[i]
print(table)
print("Total price:",total)