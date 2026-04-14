class Book:
    """
    Book class: Encapsulates book attributes and borrow status.
    Demonstrates encapsulation with private attributes and getter methods.
    """
    def __init__(self, book_id: int , title: str , author: str ):
        # Private attributes (encapsulation)
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__is_borrowed = False

    # Getter methods
    def get_id(self) -> int:
        return self.__book_id

    def get_title(self) -> str:
        return self.__title

    def get_author(self) -> str:
        return self.__author

    def is_borrowed(self) -> bool:
        return self.__is_borrowed
        
    # Borrow a book
    def borrow(self) -> bool:
        if not self.__is_borrowed:
            self.__is_borrowed = True
            return True
        return False

    # Return a book
    def return_book(self) -> bool:
        if self.__is_borrowed:
            self.__is_borrowed = False
            return True
        return False

    def __str__(self) -> str:
        status = "Available" if not self.__is_borrowed else "Borrowed"
        return f"ID:{self.__book_id:2d} | {self.__title:<20} | {self.__author:<15} | [{status}]"
