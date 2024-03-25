# library_management_system.py

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.borrowed_by = None

    def borrow(self, user):
        if self.borrowed_by is None:
            self.borrowed_by = user
            return True
        else:
            print("Book already borrowed by", self.borrowed_by.name)
            return False

    def return_book(self):
        if self.borrowed_by is not None:
            self.borrowed_by = None
            return True
        else:
            print("Book is not currently borrowed.")
            return False


class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def borrow_book(self, book):
        return book.borrow(self)

    def return_book(self, book):
        return book.return_book()


class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)


# Example usage:
if __name__ == "__main__":
    # Create books
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084")

    # Creating users
    user1 = User("Alice", 1)
    user2 = User("Bob", 2)

    # Creating library
    library = Library()

    # Adding books to library
    library.add_book(book1)
    library.add_book(book2)

    # Adding users to library
    library.add_user(user1)
    library.add_user(user2)

    # Borrowing a book
    user1.borrow_book(book1)

    # Try to borrow the same book again
    user2.borrow_book(book1)

    # Return the borrowed book
    user1.return_book(book1)

    # Remove a book from the library
    library.remove_book(book2)
