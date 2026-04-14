from book import Book
from user import Student, Staff

class Library:
    """Core library system with complete management functions"""
    def __init__(self):
        self.__books = {}
        self.__users = {}

    def add_book(self, book: Book) -> bool:
        if book.get_id() not in self.__books:
            self.__books[book.get_id()] = book
            return True
        return False

    def add_user(self, user) -> bool:
        if user.get_user_id() not in self.__users:
            self.__users[user.get_user_id()] = user
            return True
        return False

    def get_book(self, book_id: int):
        return self.__books.get(book_id)

    def get_user(self, user_id: int):
        return self.__users.get(user_id)

    def show_all_books(self):
        print("\n==================== All Books ====================")
        if not self.__books:
            print("No books available.")
            return
        for book in self.__books.values():
            print(book)

    def show_all_users(self):
        print("\n==================== All Users ====================")
        if not self.__users:
            print("No users registered.")
            return
        for user in self.__users.values():
            print(user)


def main():
    lib = Library()
    # Default test data
    lib.add_book(Book(1, "Python OOP", "Prof. Chan"))
    lib.add_book(Book(2, "Data Structures", "Prof. Ren"))
    lib.add_user(Student(101, "Chan Tai Man", "S2026001"))
    lib.add_user(Staff(102, "Dr. Lee", "Computer Science"))

    while True:
        print("\n================================================")
        print("           Library Management System")
        print("================================================")
        print("1. Add Book")
        print("2. Show All Books")
        print("3. Show All Users")
        print("4. Borrow Book")
        print("5. Return Book")
        print("0. Exit")
        print("================================================")

        choice = input("Enter option: ")

        if choice == "0":
            print("System closed.")
            break

        elif choice == "1":
            try:
                bid = int(input("Book ID: "))
                title = input("Title: ")
                author = input("Author: ")
                if lib.add_book(Book(bid, title, author)):
                    print("✅ Book added successfully.")
                else:
                    print("❌ Book ID already exists.")
            except ValueError:
                print("❌ Invalid input.")

        elif choice == "2":
            lib.show_all_books()

        elif choice == "3":
            lib.show_all_users()

        elif choice == "4":
            try:
                uid = int(input("User ID: "))
                bid = int(input("Book ID: "))
                user = lib.get_user(uid)
                book = lib.get_book(bid)
                if user and book:
                    if user.borrow_book(book):
                        print("✅ Borrow successful.")
                    else:
                        print("❌ Book is already borrowed.")
                else:
                    print("❌ User or book not found.")
            except ValueError:
                print("❌ Invalid input.")

        elif choice == "5":
            try:
                uid = int(input("User ID: "))
                bid = int(input("Book ID: "))
                user = lib.get_user(uid)
                book = lib.get_book(bid)
                if user and book:
                    if user.return_book(book):
                        print("✅ Return successful.")
                    else:
                        print("❌ Book was not borrowed.")
                else:
                    print("❌ User or book not found.")
            except ValueError:
                print("❌ Invalid input.")

        else:
            print("❌ Invalid option.")

if __name__ == "__main__":
    main()
