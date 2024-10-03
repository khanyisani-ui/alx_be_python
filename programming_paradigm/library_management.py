class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title
        self._is_checked_out = False
        
    def __str__(self) :
        return self.title
        
class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)
        print(f'Book "{book.title}" added to the library.')

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if not book._is_checked_out:
                    book._is_checked_out = True
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
                if book._is_checked_out:
                    book._is_checked_out = False
                    print(f'Book "{title}" has been returned.')
                    return book
                else:
                    print(f'Book "{title}" was not checked out.')
                    return None
        print(f'Book "{title}" not found in the library.')
        return None

    def list_available_books(self):
        available_books = [book for book in self._books if not book._is_checked_out]
        if available_books:
            print("Available books:")
            for book in available_books:
                print(f'- {book.title}')
        else:
            print("No books are currently available.")