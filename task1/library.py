from book import Book
from user import Student, Staff

class Library:
    """Library management system core class"""
    def __init__(self):
        self.__books = {}
        self.__users = {}

    # Add a book to the library
    def add_book(self, book):
        if book.get_id() not in self.__books:
            self.__books[book.get_id()] = book
            return True
        return False

    # Show all books
    def show_all_books(self):
        print("\n=== All Books ===")
        if not self.__books:
            print("No books in the library")
            return
        for book in self.__books.values():
            print(book)

    # Search book by title or ID
    def search_book(self, keyword):
        print(f"\n=== Search Result: {keyword} ===")
        found = []
        for book in self.__books.values():
            if (keyword.lower() in book.get_title().lower() or
                str(keyword) == str(book.get_id())):
                found.append(book)
        if not found:
            print("No matching books found")
        else:
            for book in found:
                print(book)
        return found

    # Borrow a book
    def borrow_book(self, user_id, book_id):
        user = self.__users.get(user_id)
        book = self.__books.get(book_id)
        if not user:
            print("❌ Error: User does not exist")
            return False
        if not book:
            print("❌ Error: Book does not exist")
            return False
        if user.borrow_book(book):
            print(f"✅ Borrow success: {book.get_title()}")
            return True
        else:
            print("❌ Borrow failed: Book already borrowed")
            return False

    # Return a book
    def return_book(self, user_id, book_id):
        user = self.__users.get(user_id)
        book = self.__books.get(book_id)
        if not user:
            print("❌ Error: User does not exist")
            return False
        if not book:
            print("❌ Error: Book does not exist")
            return False
        if user.return_book(book):
            print(f"✅ Return success: {book.get_title()}")
            return True
        else:
            print("❌ Return failed: Book not borrowed by this user")
            return False

    # Add a user
    def add_user(self, user):
        if user.get_user_id() not in self.__users:
            self.__users[user.get_user_id()] = user
            return True
        return False

    # Show all users
    def show_all_users(self):
        print("\n=== All Users ===")
        if not self.__users:
            print("No registered users")
            return
        for user in self.__users.values():
            print(user)


# Text-based menu interface
def main_menu():
    lib = Library()
    # Sample data
    lib.add_book(Book(1, "Python OOP Basics", "Zhang San"))
    lib.add_book(Book(2, "Data Structures", "Li Si"))
    lib.add_book(Book(3, "Machine Learning", "Wang Wu"))
    lib.add_user(Student(101, "Chan Tai Man", "S20260001"))
    lib.add_user(Staff(102, "Teacher Li", "Computer Science"))

    while True:
        print("\n" + "="*30)
        print(" Library Management System")
        print("="*30)
        print("1. Add Book")
        print("2. Show All Books")
        print("3. Search Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Show All Users")
        print("0. Exit")
        print("="*30)

        choice = input("Enter your choice: ")
        if choice == "0":
            print(" Thank you! Goodbye.")
            break
        elif choice == "1":
            try:
                bid = int(input("Enter book ID: "))
                title = input("Enter book title: ")
                author = input("Enter author: ")
                if lib.add_book(Book(bid, title, author)):
                    print("✅ Book added successfully!")
                else:
                    print("❌ Failed: Book ID already exists")
            except ValueError:
                print("❌ Error: ID must be a number")
        elif choice == "2":
            lib.show_all_books()
        elif choice == "3":
            keyword = input("Enter search keyword: ")
            lib.search_book(keyword)
        elif choice == "4":
            try:
                uid = int(input("Enter user ID: "))
                bid = int(input("Enter book ID: "))
                lib.borrow_book(uid, bid)
            except ValueError:
                print("❌ Error: ID must be a number")
        elif choice == "5":
            try:
                uid = int(input("Enter user ID: "))
                bid = int(input("Enter book ID: "))
                lib.return_book(uid, bid)
            except ValueError:
                print("❌ Error: ID must be a number")
        elif choice == "6":
            lib.show_all_users()
        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    main_menu()
