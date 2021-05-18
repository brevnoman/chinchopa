class Library:
    books = []
    authors = []

    def __init__(self):
        pass

    def add(self):
        book_name = input("enter book name:\n")
        book_year = input("enter book year:\n")
        author_name = input("name of author:\n")
        author_country = input("enter authors country:\n")
        author_birthday = input("enter authors birthday:\n")
        author = Author(author_name, author_country, author_birthday)
        book = Book(book_name, book_year, author)
        if len(self.books) < 1:
            self.books.append(book)
            book.author.books.append(book.name)
            self.authors.append(book.author)
            Book.num_of_books += 1
            Author.num_of_authors += 1
        else:
            for stored_book in self.books:
                if book.name == stored_book.name and book.year == stored_book.year and book.author.name == stored_book.author.name:
                    print("this book is already in our library")
                    break
            else:
                self.books.append(book)
                Book.num_of_books += 1

            for i in self.authors:
                if book.author.name == i.name and book.author.country == i.country and book.author.birthday == i.birthday:
                    try:
                        if book.author.books[book.author.books.index(book.name)] in i.books:
                            break

                    except ValueError:
                        book.author.books.append(book.name)
                        i.books = book.author.books
                        break

            else:
                book.author.books.append(book.name)
                self.authors.append(book.author)
                Author.num_of_authors += 1

        print("Books:")
        for i in self.books:
            print(i.name, i.year, i.author.name)
        print("Authors:")
        for i in self.authors:
            print(i.name)

    def group_by_author(self, author):
        list_of_books = []
        for i in self.books:
            if i.author.name == author:
                list_of_books.append(str(i))
        if len(list_of_books) < 1:
            return "no books of this author"
        return list_of_books

    def group_by_year(self, year):
        list_of_books = []
        for i in self.books:
            if i.year == year:
                list_of_books.append(repr(i))
        if len(list_of_books) < 1:
            return "no books of this year"
        return list_of_books

    def __repr__(self):
        return "This is Library"

    def __str__(self):
        return f"here is {len(self.books)} books"


class Book:
    num_of_books = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author

    def __repr__(self):
        return f"{self.name}, {self.year}, {self.author.name}"

    def __str__(self):
        return f"{self.name}, {self.year}"


class Author:
    num_of_authors = 0

    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return f"{self.name}, {self.country}, {self.birthday}"

    def __str__(self):
        return f"{self.books}"


l = Library()


while True:
    choose = input("choose 'add new book'/'group by author'/'group by year':\n")
    if choose == 'add new book':
        l.add()
    elif choose == 'group by author':
        print(l.group_by_author(input("enter name of author:\n")))
    elif choose == 'group by year':
        print(l.group_by_year(input("enter year:\n")))
    else:
        print("there is no such option")
