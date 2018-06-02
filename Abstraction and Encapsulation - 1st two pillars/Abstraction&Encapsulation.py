#Abstraction and Encapsulation

# Class => Library
# Layers of abstraction => display available books, to lend a book, to add a book

# Class => Customer
# Layers of abstraction => request for a book, return a book


class Library:

    def __init__(self,books):
        self.books = books

    def displayBooks(self):
        print("All books available in library: " + str(self.books))

    def lendBooks(self,books):
        for i in books:
            if i in self.books:
                self.books.remove(i)
                print(str(i) + " has been borrowed.")
            else:
                print("Sorry, the book is not available in our list.")

    def returnBooks(self,returnedBooks):
        self.books.extend(breturnedBooks)
        for i in books:
            print(str(i) + " has been returned. Thank you.")
            

class Customer:
    def requestBook(self):
        print("Enter the name of a book you would like to borrow: ")
        self.book = input()
        return self.book

    def returnBook(self):
        print("Enter the name of the book which you are returning: ")
        self.book = input()
        return self.book

def LibraryService(customer,library):             #Function takes a customer and a library as inputs and provides services
    while True:                                   #Run program until customer quits
        print("Enter 1 to display the available books")
        print("Enter 2 to request for a book")
        print("Enter 3 to return a book")
        print("Enter 4 to exit")
        userChoice = int(input())
        if userChoice is 1:
            library.displayBooks
        elif userChoice is 2:
            requestedBook = customer.requestBook()
            library.lendBooks(requestedBook)
        elif userChoice is 3:
            returnBook = customer.returnBook
            library.returnBooks(returnBook)
        elif userChoice is 4:
            quit()
