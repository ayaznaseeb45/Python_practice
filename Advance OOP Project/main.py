# practice of OOP concepts in python
# -------------------------------
# Book Class
# -------------------------------
class Book:
    def __init__(self, title, author, category, book_id):
        self.title = title
        self.author = author
        self.category = category
        self.id = book_id
        self.available = True  # True if the book is in library

    def display_info(self):
        status = "Available" if self.available else "Borrowed"
        print(f"{self.title} | {self.author} | {self.category} | ID: {self.id} | {status}")

# Testing above code 

# book1 = Book("English", "joh bark", "story", 1)
# book1.display_info()
# print(book1.available)

# -------------------------
class User:
    def __init__(self, name, user_id):
        self.name = name
        self.id = user_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.available:
            print(f"{book.title} is already taken")
            return
        
        book.available = False
        self.borrowed_books.append(book)
        print(f"{self.name} has borrowed {book.title}")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.available = True
            self.borrowed_books.remove(book)
            print(f"{self.name} has returned book {book.title}")
        else:
            print("This book is not borrowed by you.")

    def view_borrowed_books(self):
        if not self.borrowed_books:
            print("No books borrowed.")
        else:
            for book in self.borrowed_books:
                print(book.title)

# User1 = User("ayaz", 1)
# print(User1.name)
# print(User1.borrowed_books)
# User1.borrow_book(book1)
# User1.view_borrowed_books()
# User1.return_book(book1)



class Student(User):
    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            print(f"{self.name} has already taken 3 books ")
            return
        else:
            super().borrow_book(book)

class Teacher(User):
    def borrow_book(self, book):
        if len(self.borrowed_books)>=5:
            print(f"{self.name} had already taken 5 books ")
            return
        super().borrow_book(book)


# Testing

# alice = Student("Alice", 1)
# book1 = Book("Python", "Author", "Programming", 1)
# book2 = Book("Math", "Author", "Math", 2)
# book3 = Book("History", "Author", "History", 3)
# book4 = Book("Science", "Author", "Science", 4)

# alice.borrow_book(book1)  
# alice.borrow_book(book2)  
# alice.borrow_book(book3)  
# alice.borrow_book(book4)  


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.users = []

    def add_books(self, book):
        self.books.append(book)
    
    def register_user(self, user):
        self.users.append(user)

    def list_book(self):
        for book in self.books:
            book.display_info()

    def search_books(self, keyword):
        found = False
        for book in self.books:
            if keyword.lower() in book.title.lower():
                book.display_info()
                found = True
        if not found:
            print("No books found")







# Testing Library class
# library = Library("City Library")
# book1 = Book("Python", "Author", "Programming", 1)
# library.add_books(book1)

# user1 = Student("Ayaz", 1)
# library.register_user(user1)
# user1.borrow_book(book1)



def main():
    # Create library
    library = Library("City Library")

    # Add sample books
    library.add_books(Book("Python", "Author A", "Programming", 1))
    library.add_books(Book("Math", "Author B", "Math", 2))
    library.add_books(Book("History", "Author C", "History", 3))

    # Add sample users
    student1 = Student("Alice", 101)
    teacher1 = Teacher("Bob", 201)
    library.register_user(student1)
    library.register_user(teacher1)


    while True:
        print("\n=== Library Menu ===")
        print("1. List all books")
        print("2. Search books")
        print("3. Borrow book")
        print("4. Return book")
        print("5. View borrowed books")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            library.list_book()

        elif choice == "2":
            User_input = input("Enter Book Name: ")
            library.search_books(User_input)
            
        elif choice == "3":
            user_name = input("Enter your username: ")
            pass
            

        elif choice == "4":
            pass
        elif choice == "6":
            print("Exiting Library System. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


