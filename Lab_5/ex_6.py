# Design a library catalog system with a base class LibraryItem and subclasses for different types of items like Book, DVD, and 
# Magazine. Include methods to check out, return, and display information about each item.

from datetime import datetime, timedelta

class LibraryItem:
    def __init__(self, title, item_id, available=True):
        self.title = title
        self.item_id = item_id
        self.available = available
        self.checkout_date = None

    def display_info(self):
        return f"{self.title} (ID: {self.item_id})"

    def check_out(self):
        if self.available:
            self.available = False
            self.checkout_date = datetime.now()
            return f"{self.title} checked out successfully."
        else:
            return f"{self.title} is not available for checkout."

    def return_item(self):
        if not self.available:
            self.available = True
            self.checkout_date = None
            return f"{self.title} returned successfully."
        else:
            return f"{self.title} is already available."

class Book(LibraryItem):
    def __init__(self, title, item_id, author, available=True):
        super().__init__(title, item_id, available)
        self.author = author

    def display_info(self):
        return f"Book: {super().display_info()}, Author: {self.author}"

class DVD(LibraryItem):
    def __init__(self, title, item_id, director, available=True):
        super().__init__(title, item_id, available)
        self.director = director

    def display_info(self):
        return f"DVD: {super().display_info()}, Director: {self.director}"

class Magazine(LibraryItem):
    def __init__(self, title, item_id, issue_number, available=True):
        super().__init__(title, item_id, available)
        self.issue_number = issue_number

    def display_info(self):
        return f"Magazine: {super().display_info()}, Issue Number: {self.issue_number}"


print("\n")
book = Book(title="The Catcher in the Rye", item_id="B001", author="J.D. Salinger")
print(book.display_info())
print(book.check_out())
print(book.return_item())

print("\n")

dvd = DVD(title="Inception", item_id="D001", director="Christopher Nolan")
print(dvd.display_info())
print(dvd.check_out())

print("\n")

magazine = Magazine(title="National Geographic", item_id="M001", issue_number=255)
print(magazine.display_info())
print(magazine.check_out())
