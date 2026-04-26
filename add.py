from utilis import book

def add():
    book_id = input("Enter book ID: ")
    name = input("Enter book name: ").upper()

    book[book_id] =  name
    print("Book added successfully!")