from prettytable import PrettyTable


class Product:
    type = None
    name = None
    price = None

    def __init__(self, l_type, l_name, l_price):
        self.type = l_type
        self.name = l_name
        self.price = l_price

    def __repr__(self):
        return f"{self.type}, {self.name}"


class ProductStore:
    products = []
    income = 0

    def __init__(self):
        pass

    def add(self, product, amount):
        for i in self.products:
            if product.name == i["product"].name:
                i["quantity"] = i["quantity"] + amount
                break
        else:
            self.products.append({
                "product": product,
                "price": round(product.price * 1.3, 2),
                "quantity": amount
            })

    def set_discount(self, product, percent):
        for i in self.products:
            if product.name == i["product"].name or product.type in i["product"].type:
                i["price"] = i["price"] - round(
                    (i["price"] * percent / 100), 2)
                return repr(i["product"]), i["price"]

    def sell_product(self, product, amount):
        for i in self.products:
            if product.name == i["product"].name:
                if i["quantity"] >= amount:
                    ProductStore.income += amount * i["price"]
                    i["quantity"] = i["quantity"] - amount
                    return "Congratulations on your purchase"
                else:
                    return f"not enough {product.name}'s in stock"

    def get_income(self):
        return self.income

    def get_all_products(self):
        table = PrettyTable()
        table.field_names = ["Name", "Quantity"]
        for i in self.products:
            table.add_row([i["product"].name, i["quantity"]])
        return table

    def get_product_info(self, product):
        table = PrettyTable()
        table.field_names = ["Name", "Quantity"]
        for i in self.products:
            if product.name == i["product"].name:
                table.add_row([product.name, i["quantity"]])
        return table


def main():
    p = Product("food", "ramen", 1.5)
    p1 = Product("Sport", "T-Shirt", 100)
    p2 = Product("food", "govna", 20)
    s = ProductStore()
    while True:
        print("add/ discount/ sell/ income/ see products/ see product info/ exit")
        choose = input("")
        if choose == "add":
            while True:
                adding = input("choose product")
                if adding == "p":
                    amount = int(input("write amount of product"))
                    s.add(p, amount)
                    break
                elif adding == "p1":
                    amount = int(input("write amount of product"))
                    s.add(p1, amount)
                    break
                elif adding == "p2":
                    amount = int(input("write amount of product"))
                    s.add(p2, amount)
                    break
                else:
                    print("there are no such product")

        elif choose == "discount":
            while True:
                adding = input("choose product")
                if adding == "p":
                    percent = int(input("write percent of product"))
                    print(s.set_discount(p, percent))
                    break
                elif adding == "p1":
                    percent = int(input("write percent of product"))
                    print(s.add(p1, percent))
                    break
                elif adding == "p2":
                    percent = int(input("write percent of product"))
                    print(s.add(p2, percent))
                    break
                else:
                    print("there are no such product")
        elif choose == "sell":
            while True:
                adding = input("choose product")
                if adding == "p":
                    amount = int(input("write amount of product"))
                    print(s.sell_product(p, amount))
                    break
                elif adding == "p1":
                    amount = int(input("write amount of product"))
                    print(s.sell_product(p1, amount))
                    break
                elif adding == "p2":
                    amount = int(input("write amount of product"))
                    print(s.sell_product(p2, amount))
                    break
                else:
                    print("there are no such product")
        elif choose == "income":
            print(s.get_income())
        elif choose == "see products":
            print(s.get_all_products())
        elif choose == "see product info":
            while True:
                adding = input("choose product")
                if adding == "p":
                    print(s.get_product_info(p))
                    break
                elif adding == "p1":
                    print(s.get_product_info(p1))
                    break
                elif adding == "p2":
                    print(s.get_product_info(p2))
                    break
                else:
                    print("there are no such product")
        elif choose == "exit":
            break
        else:
            print("wrong choose")

        # p = Product("food", "ramen", 1.5)
        # p1 = Product("Sport", "T-Shirt", 100)
        # p2 = Product("food", "govna", 20)
        # s = ProductStore()
        #
        # s.add(p, 20)
        # s.add(p1, 10)
        # s.add(p2, 2)
        # s.set_discount(p1, 15)
        # s.sell_product(p1, 10)
        # s.get_income()
        # s.get_all_products()
        # s.get_product_info(p)
        # g = input()


main()
