class Book:
    """Book class: Encapsulates book attributes and borrow status"""
    def __init__(self, book_id, title, author):
        # Private attributes (encapsulation)
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__is_borrowed = False

    # Getter methods
    def get_id(self):
        return self.__book_id

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def is_borrowed(self):
        return self.__is_borrowed

    # Borrow a book
    def borrow(self):
        if not self.__is_borrowed:
            self.__is_borrowed = True
            return True
        return False

    # Return a book
    def return_book(self):
        if self.__is_borrowed:
            self.__is_borrowed = False
            return True
        return False

    def __str__(self):
        status = "Available" if not self.__is_borrowed else "Borrowed"
        return f"ID:{self.__book_id} | {self.__title} | {self.__author} | {status}"
