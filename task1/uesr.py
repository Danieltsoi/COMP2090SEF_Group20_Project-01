class User:
    """Base User class"""
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name
        self.__borrowed_books = []

    # Getter methods
    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_borrowed_books(self):
        return self.__borrowed_books

    # Borrow a book
    def borrow_book(self, book):
        if book.borrow():
            self.__borrowed_books.append(book)
            return True
        return False

    # Return a book
    def return_book(self, book):
        if book.return_book():
            self.__borrowed_books.remove(book)
            return True
        return False


# Inheritance: Student extends User
class Student(User):
    def __init__(self, user_id, name, student_id):
        super().__init__(user_id, name)
        self.__student_id = student_id

    def __str__(self):
        return f"[Student] ID:{self.get_user_id()} | Name:{self.get_name()} | SID:{self.__student_id}"


# Inheritance: Staff extends User
class Staff(User):
    def __init__(self, user_id, name, department):
        super().__init__(user_id, name)
        self.__department = department

    def __str__(self):
        return f"[Staff] ID:{self.get_user_id()} | Name:{self.get_name()} | Dept:{self.__department}"
