# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


# TODO: create a basic class
class Book:
    def __init__(self, title):
        self.title = title
   


# TODO: create instances of the class
book1 = Book('Around the World in 80 days')
book2 = Book('War of the worlds')


# TODO: print the class and property
print(book1)
print(book1.title, book1.author, book1.pages)
