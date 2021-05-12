class Library:
    books=[]
    authors=[]
    def __init__(self):
        pass

    def add(self, book):
        if len(self.books)<1:
            self.books.append({"Name":book.name,
                               "Year": book.year,
                               "Author":book.author.name})
            book.author.books.append(book.name)
            self.authors.append({"Name":book.author.name,
                                 "Country":book.author.country,
                                 "Birthday":book.author.birthday,
                                 "Books":book.author.books})
        else:
            for i in range(len(self.books)):
                if book.name in self.books[i]["Name"]:
                    print("this book is already in our library")
                    break
            else:
                self.books.append({"Name":book.name,"Year": book.year, "Author":book.author.name})

            for i in range(len(self.authors)):
                if book.author.name == self.authors[i]["Name"]:
                    try:
                        if book.author.books[book.author.books.index(book.name)] in self.authors[i]["Books"]:
                            break

                    except ValueError:
                        book.author.books.append(book.name)
                        self.authors[i]["Books"] = book.author.books
                        break

            else:
                book.author.books.append(book.name)
                self.authors.append(
                    {"Name": book.author.name,
                     "Country": book.author.country,
                     "Birthday": book.author.birthday,
                     "Books": book.author.books})

        print(self.books)
        print(self.authors)

    def group_by_author(self, author):
        for i in self.books:
            if i["Author"]==author.name:
                print(i)

    def group_by_year(self, year):
        for i in self.books:
            if i["Year"] == year:
                print(i)
    #Ne ponyal, no ochen interestno
    # def __repr__(self):
    #     print()
    #
    # def __str__(self):
    #     print(self.books[random.randint(0, len(self.books))])



class Book:
    num_of_books=0

    def __init__(self,name, year, author):
        self.name=name
        self.year=year
        self.author=author
        Book.num_of_books+=1
class Author:

    def __init__(self, name, country, birthday):
        self.name=name
        self.country=country
        self.birthday=birthday
        self.books=[]



author_obj=Author("A", "U", "T")
author2_obj=Author("E","B","L")
book_obj=Book("BOOK", 1925, author_obj)
book2_obj=Book("Cock", 1488, author2_obj)
l=Library()

book3_obj=Book("NOS", 228, author_obj)
while True:

    l.add(book_obj)
    l.add(book2_obj)
    l.add(book3_obj)
    l.group_by_author(author_obj)
    l.group_by_year(1488)
