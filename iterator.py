class LibraryIterator:
    def __init__(self, books):
        self.books = books
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self.books):
            book = self.books[self._index]
            self._index += 1
            return book
        else:
            raise StopIteration
