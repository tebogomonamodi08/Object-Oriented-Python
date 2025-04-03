class Libraries:
    '''This is the central class of our program. Manages the books.
    1.Stores collection of books 
    2. Find Books in the collection
    3. Add Books to the collection
    Relationships->Admin(add books to the collection)'''
    def __init__(self,collection = []):
        self.collection = collection

    def find_book(self, book_title):
        for book in self.collection:
            if book.title == book_title:
                return book
    

class Books:
    '''This class is a instance of a book, this class will store information about the book
    title, author, availability, able to change the availability of the book'''
    def __init__(self, title, author, availability = True):
        self.title = title
        self.author = author
        self.availability = availability

    def borrowed(self):
        self.availability = False

class Users:
    '''This is the base class for the two subclasses which is members and admin, the User has Attributes
    name  and the id'''

    def __init__(self, name,id):
        self.name = name
        self.id = id

class Admins(Users):
    '''Inherits from the Users class and can add books to a librabry instance'''
    def __init__(self, name, id):
        super().__init__(name, id)
    
    def add_book(self, library, book):
        '''This method add a books intance to a librabries intance list attribute'''
        library.collection.append(book)
    
    def view_books(self, library):
        for item in library.collection:
            print(item)


class Members(Users):
    '''Inherets form the Users class, has behaviours, borrow and return a book'''
    def __init__(self, name, id):
        super().__init__(name, id)

    def borrow_book(self, book_title, library):
        book = library.find_book(book_title)
        if book.availability:
            print('Book borrowed')
            book.borrowed()
        else:
            print('Title does not exist or book is not available')
        
