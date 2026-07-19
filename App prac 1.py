# Book Class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        status = "Available" if self.available else "Borrowed"
        print(f"{self.title} by {self.author} - {status}")


# Patron Class
class Patron:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book.title)

    def return_book(self, book):
        self.borrowed_books.remove(book.title)

    def show_books(self):
        if len(self.borrowed_books) == 0:
            print("No books borrowed.")
        else:
            print("Borrowed Books:")
            for book in self.borrowed_books:
                print("-", book)


# Library Class
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(book.title, "added successfully.")

    def display_books(self):
        print("\nLibrary Books:")
        for book in self.books:
            book.display()

    def borrow_book(self, title, patron):
        for book in self.books:
            if book.title == title:
                if book.available:
                    book.available = False
                    patron.borrow_book(book)
                    print(patron.name, "borrowed", book.title)
                else:
                    print("Book is already borrowed.")
                return
        print("Book not found.")

    def return_book(self, title, patron):
        for book in self.books:
            if book.title == title:
                if not book.available:
                    book.available = True
                    patron.return_book(book)
                    print(patron.name, "returned", book.title)
                else:
                    print("This book was not borrowed.")
                return
        print("Book not found.")


# Main Program
library = Library()

# Adding Books
book1 = Book("Python Basics", "John Smith")
book2 = Book("Data Structures", "Alice Brown")
book3 = Book("Machine Learning", "David Lee")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Create Patron
patron1 = Patron("Vrunda")

# Display Books
library.display_books()

# Borrow Book
print("\nBorrowing Book...")
library.borrow_book("Python Basics", patron1)

# Display Books Again
library.display_books()

# Show Borrowed Books
print()
patron1.show_books()

# Return Book
print("\nReturning Book...")
library.return_book("Python Basics", patron1)

# Display Books Again
library.display_books()

# Show Borrowed Books Again
print()
patron1.show_books()