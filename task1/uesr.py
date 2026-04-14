class User:
    """Base User class"""
    def __init__(self, user_id: int, name: str):
        self.__user_id = user_id
        self.__name = name
        self.__borrowed_books = []

    # Getter methods
    def get_user_id(self) -> int:
        return self.__user_id

    def get_name(self) -> str:
        return self.__name

    def get_borrowed_books(self) -> list:
        return self.__borrowed_books

    # Borrow a book
    def borrow_book(self, book) -> bool:
        if book.borrow():
            self.__borrowed_books.append(book)
            return True
        return False

    # Return a book
    def return_book(self, book) -> bool:
        if book.return_book():
            self.__borrowed_books.remove(book)
            return True
        return False


# Inheritance: Student extends User
class Student(User):
    def __init__(self, user_id: int, name: str, student_id: str):
        super().__init__(user_id, name)
        self.__student_id = student_id

    def __str__(self):
        return f"[Student] ID:{self.get_user_id()} | Name:{self.get_name()}"


# Inheritance: Staff extends User
class Staff(User):
    def __init__(self, user_id: int, name: str, department: str):
        super().__init__(user_id, name)
        self.__department = department

    def __str__(self):
        return f"[Staff] ID:{self.get_user_id()} | Name:{self.get_name()}"
