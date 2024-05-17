from book_manager import add_book, list_books
from utils import print_heading, print_footer
import unused_module
from operator import methodcaller

class Example:
    
    def sample(self): # this is an unused function 
        print("unused function")

    def book(self):
        print_heading("Book Management System")
        add_book("The Da Vinci Code","Dan Brown")
        add_book("To Kill a Mockingbird", "Harper Lee")
        books = list_books()
        for book in books:
            print(f"{book['title']} by {book['author']}")
        print_footer("END")
if __name__ == "__main__":
    example = Example()
    example.book()

    # Create a methodcaller for the 'sample' method
    caller = methodcaller("sample")
    caller(example)
    
    
