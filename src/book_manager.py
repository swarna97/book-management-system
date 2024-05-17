_books = []

def add_book(title, author):
    _books.append({"title": title, "author": author})

def list_books():
    return _books

def delete_book(title):
    global _books
    _books = [book for book in _books if book['title'] != title]