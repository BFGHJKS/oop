class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Book with ISBN {isbn} removed from the library.")
                return
        print(f"Book with ISBN {isbn} not found in the library.")

    def display_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(book)



if __name__ == "__main__":

    book1 = Book("Python Programming", "John Doe", "978-1-234-56789-0")
    book2 = Book("Data Structures in C++", "Jane Smith", "978-1-234-56789-1")

    library = Library()


    library.add_book(book1)
    library.add_book(book2)


    library.display_books()


    library.remove_book("978-1-234-56789-0")


    library.display_books()
