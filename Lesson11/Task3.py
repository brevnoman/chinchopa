# import weakref
#
#
# class Product:
#     instances=[]
#
#     def __init__(self, type, name, price):
#         self.__class__.instances.append(weakref.proxy(self))
#         self.type = type
#         self.name = name
#         self.price = price
#
#
#
# class ProductStore:
#
#     # def __init__(self, product, amount):
#     #     self.product=product
#     #     self.amount=amount
#
#
#     def add(product, amount, basket):
#         try:
#             basket.setdefault(product.__dict__["name"], basket[product.__dict__["name"]]+amount)
#         except KeyError:
#             basket.setdefault(product.__dict__["name"], amount)
#
#
# basket={}
# while True:
#
#     p = Product("food", "ramen", 1.5)
#     p2 = Product('Sport', 'Football T-Shirt', 100)
#     # s = ProductStore()
#     print((issubclass(Product, p))
#     # ProductStore.add(p, 10, basket)
#
#
#
#
#
#     #
#     # for instance in Product.instances:
#     #     print(instance.name)
#

from prettytable import PrettyTable


class Product:
    type = None
    name = None
    price = None

    def __init__(self, l_type, l_name, l_price):
        self.type = l_type
        self.name = l_name
        self.price = l_price


class ProductStore:
    products = []
    income = 0

    def __init__(self):
        pass


    def add(self, product, amount, ):
        try:
            for i in range(len(self.products)):
                if product.name in self.products[i].values():
                    self.products[i]={
                    "type": product.type,
                    "name": product.name,
                    "price": round(product.price * 1.3, 2),
                    "quantity": self.products[i]["quantity"]+amount
                    }
                    break
            else:
                raise KeyError
        except (KeyError, ValueError, TypeError):
            self.products.append({
            "type": product.type,
            "name": product.name,
            "price": round(product.price * 1.3, 2),
            "quantity": amount
            })
        print(self.products)


    def set_discount(self, product, percent):
        for i in range(len(self.products)):
            print(self.products[i])
            if product.name in self.products[i].values() or product.type in self.products[i].values():
                self.products[i]["price"]=self.products[i]["price"]-round((self.products[i]["price"]*percent/100), 2)
                print(self.products)


    def sell_product(self, product, amount):
        for i in range(len(self.products)):
            if product.name in self.products[i].values():
                if self.products[i]["quantity"] >= amount:
                    self.income = amount*self.products[i]["price"]
                    self.products[i]["quantity"]=self.products[i]["quantity"]-amount
                else:
                    print(f"not enough {product.name}'s in stock")

    def get_income(self):
        print(self.income)



    def get_all_products(self):
        table=PrettyTable()
        table.field_names=["Name", "Quantity"]
        for i in self.products:
            table.add_row([i["name"], i["quantity"]])
        print(table)

    def get_product_info(self, product):
        table=PrettyTable()
        table.field_names=["Name", "Quantity"]
        for i in range(len(self.products)):
            if product.name in self.products[i].values():
                table.add_row([product.name, self.products[i]["quantity"]])
        print(table)


def main():



while True:
    p= Product("food", "ramen", 1.5)
    p1= Product("Sport", "T-Shirt", 100)
    p2= Product("food", "govna", 20)
    s=ProductStore()

    s.add(p, 20)
    s.add(p1, 10)
    s.add(p2, 2)
    s.set_discount(p1, 15)
    s.sell_product(p1, 10)
    s.get_income()
    s.get_all_products()
    s.get_product_info(p)
    g=input()