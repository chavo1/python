#!/usr/bin/env python3

# Object-Oriented Programming

# Function isinstance, Class object, and Class Book

# 'abc' is an instance of str, but 55.2 is not.
print(isinstance('abc', str))
print(isinstance(55.2, str))

# Function isinstance reports that both 'abc' and 55.2 are instances of class object:

print(isinstance(55.2, object))
print(isinstance('abc', object))

# classes and functions are instances of object:

print(isinstance(str, object))
print(isinstance(max, object))

# Class object has the following attributes (attributes are variables inside a class that refer to methods, functions, variables, or even other classes):
print(dir(object))

# str is a type, Book is a type:

from typing import List, Any

class Book:
    """Information about a book, including title, list of authors,
    publisher, ISBN, and price.
    """

    def __init__(self, title: str, authors: List[str], publisher: str,
                 isbn: str, price: float) -> None:
        """Create a new book entitled title, written by the people in authors,
        published by publisher, with ISBN isbn and costing price dollars.

        >>> python_book = Book( \
                'Practical Programming', \
                ['Campbell', 'Gries', 'Montojo'], \
                'Pragmatic Bookshelf', \
                '978-1-6805026-8-8', \
                25.0)
        >>> python_book.title
        'Practical Programming'
        >>> python_book.authors
        ['Campbell', 'Gries', 'Montojo']
        >>> python_book.publisher
        'Pragmatic Bookshelf'
        >>> python_book.ISBN
        '978-1-6805026-8-8'
        >>> python_book.price
        25.0
        """

        self.title = title
        # Copy the authors list in case the caller modifies that list later.
        self.authors = authors[:]
        self.publisher = publisher
        self.ISBN = isbn
        self.price = price

    def num_authors(self) -> int:
        """Return the number of authors of this book.

        >>> python_book = Book( \
                'Practical Programming', \
                ['Campbell', 'Gries', 'Montojo'], \
                'Pragmatic Bookshelf', \
                '978-1-6805026-8-8', \
                25.0)
        >>> python_book.num_authors()
        3
        """

        return len(self.authors)

    def __str__(self) -> str:
        """Return a human-readable string representation of this Book.
        """

        return """Title: {0}
Authors: {1}
Publisher: {2}
ISBN: {3}
Price: ${4}""".format(
    self.title, ', '.join(self.authors), self.publisher, self.ISBN, self.price)

    def __eq__(self, other: Any) -> bool:
        """Return True iff other is a book, and this book and other have
        the same ISBN.

        >>> python_book = Book( \
                'Practical Programming', \
                ['Campbell', 'Gries', 'Montojo'], \
                'Pragmatic Bookshelf', \
                '978-1-6805026-8-8', \
                25.0)
        >>> python_book_discounted = Book( \
                'Practical Programming', \
                ['Campbell', 'Gries', 'Montojo'], \
                'Pragmatic Bookshelf', \
                '978-1-6805026-8-8', \
                5.0)
        >>> python_book == python_book_discounted
        True
        >>> python_book == ['Not', 'a', 'book']
        False
        """

        return isinstance(other, Book) and self.ISBN == other.ISBN

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    python_book = Book(
        'Practical Programming',
        ['Campbell', 'Gries', 'Montojo'],
        'Pragmatic Bookshelf',
        '978-1-6805026-8-8',
        25.0)

    survival_book = Book(
        "New Programmer's Survival Manual",
        ['Carter'],
        'Pragmatic Bookshelf',
        '978-1-93435-681-4',
        19.0)

    print('{0} was written by {1} authors and costs ${2}'.format(
        python_book.title, python_book.num_authors(), python_book.price))

    print('{0} was written by {1} authors and costs ${2}'.format(
        survival_book.title, survival_book.num_authors(), survival_book.price))

python_book = Book(
    'Practical Programming',
    ['Campbell', 'Gries', 'Montojo'],
    'Pragmatic Bookshelf',
    '978-1-6805026-8-8',
    25.0)

survival_book = Book(
    "New Programmer's Survival Manual",
    ['Carter'],
    'Pragmatic Bookshelf',
    '978-1-93435-681-4',
    19.0)

print('{0} was written by {1} authors and costs ${2}'.format(
    python_book.title, python_book.num_authors(), python_book.price))

print('{0} was written by {1} authors and costs ${2}'.format(
    survival_book.title, survival_book.num_authors(), survival_book.price))

print(python_book)
print(type(python_book.__dict__), python_book.__dict__)
print(type(python_book.__module__), python_book.__module__)


# Inheritance

class Member:
    """ A member of a university. """
    def __init__(self, name: str, address: str, email: str) -> None:
        """Create a new member named name, with home address and email address. """
        self.name = name
        self.address = address
        self.email = email
class Faculty(Member):
    """ A faculty member at a university. """
    def __init__(self, name: str, address: str, email: str, faculty_num: str) -> None:
        """Create a new faculty named name, with home address, email address,
        faculty number faculty_num, and empty list of courses.
        """
        super().__init__(name, address, email)
        self.faculty_number = faculty_num
        self.courses_teaching = []
class Student(Member):
    """ A student member at a university. """
    def __init__(self, name: str, address: str, email: str, student_num: str) -> None:
        """Create a new student named name, with home address, email address,
        student number student_num, an empty list of courses taken, and an
        empty list of current courses.
        """
        super().__init__(name, address, email)
        self.student_number = student_num
        self.courses_taken = []
        self.courses_taking = []

paul = Faculty('Paul Gries', 'Ajax', 'pgries@cs.toronto.edu', '1234')
print(paul.name)
print(paul.email)
print(paul.faculty_number)

jen = Student('Jen Campbell', 'Toronto', 'campbell@cs.toronto.edu', '4321')
print(jen.name)
print(jen.email)
print(jen.student_number)