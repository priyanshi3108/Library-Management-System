from utilis import issue
from utilis import book
def return_book():
    book_name = input("Enter book name: ").upper()
    book_key =  input("Enter key of book")
    issue.pop(book_key)
    book[book_key] = book_name
    
    print("Book Returned")