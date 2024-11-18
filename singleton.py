from iterator import LibraryIterator


class LibraryCatalog:
    _instance = None

    def __init__(self):
        if LibraryCatalog._instance is not None:
            raise Exception(
                "LibraryCatalog is a singleton! Use get_instance().")
        self.books = []

    @staticmethod
    def get_instance():
        if LibraryCatalog._instance is None:
            LibraryCatalog._instance = LibraryCatalog()
        return LibraryCatalog._instance

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, title):
        borrowed = True
        for book in self.books:
            if book['title'] == title:
                self.books.remove(book)
                print(f"Book '{title}' has been borrowed.")
                return borrowed
        print(f"Error: Book '{title}' not found in the catalog.")
        borrowed = False
        return borrowed

    def return_book(self, book):
        self.books.append(book)

    def get_iterator(self):
        return LibraryIterator(self.books)
