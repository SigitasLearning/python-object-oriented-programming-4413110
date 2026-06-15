# Python Object Oriented Programming by Joe Marini course example
# Using the __str__ and __repr__ magic methods


from typing import Any


class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price
        self._discount = 0.1

    # The __str__ function is used to return a user-friendly string
    # representation of the object
    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"

    # TODO: __getattribute__ called when an attr is retrieved. Don't
    # directly access the attr name otherwise a recursive loop is created
    def __getattribute__(self, name: str) -> Any:
        if name == 'price':
            p = super().__getattribute__('price')
            d = super().__getattribute__("_discount")
            return round(p - p * d, 2)
        return super().__getattribute__(name)

    # TODO: __setattr__ called when an attribute value is set. Don't set the attr
    # directly here otherwise a recursive loop causes a crash
    def __setattr__(self, name: str, value: Any) -> None:
        if name == 'price':
            tv = type(value)
            if  tv is not float and tv is not int:
                raise ValueError("The price must be float or int")
        return super().__setattr__(name, value)

    # TODO: __getattr__ called when __getattribute__ lookup fails - you can
    # pretty much generate attributes on the fly with this method
    def __getattr__(self, name):
        return f'{name} is not defined on Book'

b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)

print(b1)
b1.price = 49.99
print(b1)

b1.price = 50
b1.price = float("35.99")

print(b1.year)

