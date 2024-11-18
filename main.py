from adapter import BookAdapter
from singleton import LibraryCatalog
from facade import LibraryInterface
from factory import *
from observer import UserObserver


# Singleton: LibraryCatalog
library_catalog = LibraryCatalog.get_instance()

# Adapter
json_data = '[{"title": "Harry Potter", "author": "J. K. Rowling"}, {"title": "Hobbit", "author": "J. R. R. Tolkien"}]'
xml_data = '''
<books>
    <book><title>Javascript basics</title><author>Jane Smith</author></book>
    <book><title>Java basics</title><author>James Smith</author></book>
</books>
'''

books_from_json = BookAdapter.from_json(json_data)
books_from_xml = BookAdapter.from_xml(xml_data)

for book in books_from_json + books_from_xml:
    library_catalog.add_book(book)

# Factory: UserFactory
student = UserFactory.create_user("student", "Alice")
teacher = UserFactory.create_user("teacher", "Jake")
# unknown = UserFactory.create_user("random", "Mike")
print(student)
print(teacher)
# print(unknown)

# Observer: Subskrypcja użytkowników
user1 = UserObserver("Alice")
user2 = UserObserver("Jake")
library_interface = LibraryInterface()
library_interface.subscribe_user(user1)
library_interface.subscribe_user(user2)

# Fasada: Dodawanie książek i powiadomienia
iterator = library_catalog.get_iterator()

library_interface.list_books(iterator)

library_interface.add_book({"title": "Ironman", "author": "Tony Stark"})
library_interface.borrow_book(
    {"title": "Spiderman", "author": "Peter Parker"}, teacher)
library_interface.borrow_book(
    {"title": "Ironman", "author": "Tony Stark"}, teacher)

library_interface.return_book(
    {"title": "Hulk", "author": "Bruce Banner"}, student)

library_interface.list_books(iterator)
