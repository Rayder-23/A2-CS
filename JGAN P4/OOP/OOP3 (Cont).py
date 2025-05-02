# Containment, basically nested classes and objects
# aka classes in classes

class Book:
    def __init__(self, title, author, genre, publication_year):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_year = publication_year

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Genre: {self.genre}")
        print(f"Publication Year: {self.publication_year}")
        print("----------------------")

class Librarian:
    def __init__(self, name):
        self.name = name

    def greet_patrons(self):
        print(f"Welcome to the library! I'm {self.name}, your librarian.")

class Library:
    def __init__(self, librarian):  # nested class
        self.books = [] # list to contain Book Objects
        self.librarian = librarian # Librarian objected contained within Library

    def add_book(self, book):   # another nested class
        self.books.append(book)

    def display_books(self):
        print("\nBooks in the Library:\n")
        for book in self.books:
            book.display_info() # using method from Book class


librarian = Librarian("Alice")
library = Library(librarian)

book1 = Book("Python Programming", "Guido van Rossum", "Programming", 2019)
book2 = Book("Data Science Handbook", "Jake VanderPlas", "Data Science", 2016)
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Classic", 1925)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.librarian.greet_patrons()
library.display_books()