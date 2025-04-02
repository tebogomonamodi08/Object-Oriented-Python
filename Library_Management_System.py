class Libraries:
    '''This class is the central class for the system, it will 
    manage the collection of books in the library'''
    def __init__(self, books):
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)

    def find_book(self, book):
        for item in self.books:
            if book.title == self.books.title:
                return True
        
        
        
class Books:
    '''This class allows instances of books to be created'''
    def __init__(self, title, author, availability):
        self.title = title
        self.author = author
        self.availability = availability
        
class Users:
    '''This class allows us to store the Users and 
    give them behaviours they can do'''
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
class Admin(Users):
    '''This class inherits from the user class'''
    def __init__(self, name,id):
        super().__init__(name,id)
        
    def add_book(self, library, book):
        library.add_book(book)
        
class Member(Users):
    '''This class will store the member information
    and give them functionality'''
    def __init__(self, name, id):
        super().__init__(name, id)
        
    def borrow_book(self,book_name, library, Book):
        if library.find_book(book_name) and Book.availability:
            print('Borrowed')
        else:
            print('Book not found or not available')