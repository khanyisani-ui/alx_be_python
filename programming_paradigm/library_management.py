class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)
        print(f'Book "{book.title}" by {book.author} added to the library.')

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f'Book "{title}" has been checked out.')
                    return book
                else:
                    print(f'Book "{title}" is already checked out.')
                    return None
        print(f'Book "{title}" not found in the library.')
        return None

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f'Book "{title}" has been returned.')
                    return book
                else:
                    print(f'Book "{title}" was not checked out.')
                    return None
        print(f'Book "{title}" not found in the library.')
        return None

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            print("Available books:")
            for book in available_books:
                print(f'- {book}')
        else:
            print("No books are currently available.")
