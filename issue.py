from utilis import book
from utilis import issue

def issued():
    book_name = input("Enter book name: ").upper()
    book_key =  input("Enter key of book: ")
    book.pop(book_key)
    issue[book_key] = book_name

    print("Book Issued")