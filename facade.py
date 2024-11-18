from singleton import LibraryCatalog
from observer import LibraryNotifier


class LibraryInterface:
    def __init__(self):
        self.catalog = LibraryCatalog.get_instance()
        self.notifier = LibraryNotifier()

    def add_book(self, book):
        self.catalog.add_book(book)
        self.notifier.notify(
            f"New book added: {book['title']} by {book['author']}")

    def return_book(self, book, user):
        self.catalog.add_book(book)
        self.notifier.notify(
            f"User {user.name} has returned book: {book['title']} by {book['author']}")

    def borrow_book(self, book, user):
        title = book['title']
        result = self.catalog.borrow_book(title)
        if result == True:
            self.notifier.notify(
                f"User {user.name} has borrowed book:  {book['title']} by {book['author']}")

    def list_books(self, iterator):
        for book in iterator:
            print(f"Title: {book['title']}, Author: {book['author']}")

    def subscribe_user(self, user_observer):
        self.notifier.subscribe(user_observer)
