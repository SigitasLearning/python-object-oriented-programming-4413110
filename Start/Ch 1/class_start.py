# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods


class Book:
    # TODO: Properties defined at the class level are shared by all instances

    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")

    # TODO: double-underscore properties are hidden from other classes
    __booklist = None


    # TODO: create a class method
    @classmethod
    def get_book_types(cls):
        return cls.BOOK_TYPES

    # TODO: create a static method
    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist
    

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def set_title(self, newtitle):
        self.title = newtitle

    def __init__(self, title:str, booktype):
        self.title = title
        if booktype in Book.BOOK_TYPES:
            self.booktype = booktype
        else:
            raise ValueError(f'{booktype} is not a valid book type')
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.booktype}')"


# TODO: access the class attribute
print(f'Book Types: {Book.get_book_types()}')

# TODO: Create some book instances
b1 = Book('Born to Cook', 'HARDCOVER')
b2 = Book('Misery', 'PAPERBACK')
b3 = Book('Python Cookbook', 'EBOOK')
#b4 = Book('Avengers', 'COMICS')


# TODO: Use the static method to access a singleton object
thebooks = Book.getbooklist()
thebooks.append(b1)
thebooks.append(b2)
thebooks.append(b3)
[print(b) for b in thebooks]

