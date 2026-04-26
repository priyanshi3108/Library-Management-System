from add import add
from show import show
from issue import issued
from return_book  import return_book
from show_issuedbook import issued_book

def library():
    while True:
        print("\n1. Add Book")
        print("2. Show Book")
        print("3. Issue Book")
        print("4. Show Issued Books")
        print("5. Return Book")
        print("6. Exit")
        choice = int(input("Enter your choice: "))

        if choice==1:   add()
        elif choice==2: show()
        elif choice==3: issued()
        elif choice==4: issued_book()
        elif choice==5: return_book()
        elif choice==6: 
            print("Thank you")
            break
        else:
            print("Invalid choice")
            
library()