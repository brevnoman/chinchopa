import unittest
from prettytable import PrettyTable


class Product:

    def __init__(self, l_type, l_name, l_price):
        self.type = l_type
        self.name = l_name
        self.price = l_price

    def __repr__(self):
        return f"{self.type}, {self.name}"


class ProductStore:


    def __init__(self):
        self.products = []
        self.income = 0

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
                    self.income += amount * i["price"]
                    i["quantity"] = i["quantity"] - amount
                    return "Congratulations on your purchase"
                else:
                    return f"not enough {product.name}'s in stock"

    def get_income(self):
        return self.income

    def get_all_products(self):
        # table = PrettyTable()
        # table.field_names = ["Name", "Quantity"]
        # for i in self.products:
        #     table.add_row([i["product"].name, i["quantity"]])
        # return table
        return f"{self.products}"

    def get_product_info(self, product):
        # table = PrettyTable()
        # table.field_names = ["Name", "Quantity"]
        # for i in self.products:
        #     if product.name == i["product"].name:
        #         table.add_row([product.name, i["quantity"]])
        # return table
        for i in self.products:
            if product.name in i["product"].name:
                return f"{i}"

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



class TuskTest(unittest.TestCase):
    def setUp(self) -> None:
        self.store = ProductStore()
        self.p = Product("food", "ramen", 1.5)
        self.store.add(self.p, 10)


    def test1(self):
        self.assertTrue(self.p.name in self.store.products[0]["product"].name, "ni")

    def test2(self):
        self.assertEqual(self.store.get_product_info(self.p), "{'product': food, ramen, 'price': 1.95, 'quantity': 10}", "net")

    def test3(self):
        self.assertEqual(self.store.get_all_products(), "[{'product': food, ramen, 'price': 1.95, 'quantity': 10}]", "net")