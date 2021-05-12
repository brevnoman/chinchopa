class Library:
    books=[]
    authors=[]
    def __init__(self):
        pass

    def add(self, book):
        if len(self.books)<1:
            self.books.append(book)
            book.author.books.append(book.name)
            self.authors.append(book.author)
        else:
            for i in range(len(self.books)):
                if book.name == self.books[i].__dict__["name"] and book.year == self.books[i].__dict__["year"] and book.author == self.books[i].__dict__["author"]:
                    print("this book is already in our library")
                    break
            else:
                self.books.append(book)

            for i in range(len(self.authors)):
                if book.author.name == self.authors[i].__dict__["name"]:
                    try:
                        if book.author.books[book.author.books.index(book.name)] in self.authors[i].__dict__["books"]:
                            break

                    except ValueError:
                        book.author.books.append(book.name)
                        self.authors[i].__dict__["books"] = book.author.books
                        break

            else:
                book.author.books.append(book.name)
                self.authors.append(book.author)

        print("Books:")
        for i in range(len(self.books)):
            print(self.books[i].__dict__["name"],self.books[i].__dict__["year"], self.books[i].__dict__["author"].name)
        print("Authors:")
        for i in range(len(self.authors)):
            print(self.authors[i].__dict__)

    def group_by_author(self, author):
        for i in self.books:
            if i.__dict__["author"].name==author.name:
                print(i.__dict__["name"], i.__dict__["year"], i.__dict__["author"].name)

    def group_by_year(self, year):
        for i in self.books:
            if i.__dict__["year"] == year:
                print(i.__dict__["name"], i.__dict__["year"], i.__dict__["author"].name)
    #Ne ponyal, no ochen interestno
    def __repr__(self):
        return f"{Book.__name__}"

    def __str__(self):
        for i in range(len(self.authors)):
            return f"{Author.__name__}"



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
print(str(book_obj))
print(repr(book_obj))
book3_obj=Book("NOS", 228, author_obj)
while True:

    l.add(book_obj)
    print(author_obj.__dict__)
    l.add(book2_obj)
    l.add(book3_obj)
    l.group_by_author(author_obj)
    l.group_by_year(1488)
    print(Book.num_of_books)
