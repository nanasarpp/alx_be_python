
class Book:
    def __init__(self, title, author):
        self.title = title        # public attribute
        self.author = author      # public attribute
        self._is_checked_out = False   # private attribute (by convention)

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self._books = []   # private list to store Book objects

    def add_book(self, book):
        self._books.append(book)
        # print(f'Book "{book.title}" added to library.')

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and not book._is_checked_out:
                book._is_checked_out = True
                # print(f'You have checked out "{book.title}".')
                return
        print(f'Sorry, "{title}" is not available.')

    def return_book(self, title):
        for book in self._books:
            if book.title == title and book._is_checked_out:
                book._is_checked_out = False
                # print(f'You have returned "{book.title}".')
                # return
        # print(f'Cannot return "{title}". It may not belong to this library or is not checked out.')

    def list_available_books(self):
        available = [book for book in self._books if not book._is_checked_out]
        if not available:
            print("No books are currently available.")
        else:
            # print("Available books:")
            for book in available:
                print(f"{book}")

    
