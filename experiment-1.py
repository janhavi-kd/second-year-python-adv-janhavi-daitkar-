class Book:
    def _init_(self, title, author):
        self.title = title
        self.author = author
        self.available = True  # Book is available by default


class Patron:
    def _init_(self, name):
        self.name = name
        self.borrowed_books = []  # List to store borrowed books


class Library:
    def _init_(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)  # Add book to library

    def register_patron(self, patron):
        self.patrons.append(patron)  # Register a new patron

    def borrow_book(self, patron, book):
        if book.available:
            book.available = False
            patron.borrowed_books.append(book)
            print(f"{patron.name} borrowed '{book.title}'")
        else:
            print(f"'{book.title}' is not available.")

    def return_book(self, patron, book):
        if book in patron.borrowed_books:
            book.available = True
            patron.borrowed_books.remove(book)
            print(f"{patron.name} returned '{book.title}'")
        else:
            print(f"{patron.name} has not borrowed '{book.title}'")


# Main Program
library = Library()

# Create Books
book1 = Book("Python Programming", "Guido van Rossum")
book2 = Book("Data Structures", "Mark Allen Weiss")

# Add Books to Library
library.add_book(book1)
library.add_book(book2)

# Register Patron
patron1 = Patron("Janhavi")
library.register_patron(patron1)

# Borrow Book
library.borrow_book(patron1, book1)

# Return Book
library.return_book(patron1, book1)