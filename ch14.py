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


# Class Molecule

from atom import Atom
class Molecule:
    """A molecule with a name and a list of Atoms. """

    def __init__(self, name):
        """ (Molecule, str) -> NoneType
		
        Create a Molecule named name with no Atoms.
        """

        self.name = name
        self.atoms = []

    def add(self, a):
        """ (Molecule, Atom) -> NoneType
		
        Add a to my list of Atoms.
        """

        self.atoms.append(a)

    def translate(self, x, y, z):
        """ (Molecule, number, number, number) -> NoneType

        Move this Molecule, including all Atoms, by (x, y, z).
        """

        for atom in self.atoms:
            atom.translate(x, y, z)

    def __str__(self):
        """ (Molecule) -> str
		
        Return a string representation of this Molecule in this format:
            (NAME, (ATOM1, ATOM2, ...))
        """

        res = ''
        for atom in self.atoms:
            res = res + str(atom) + ', '
			
        # Strip off the last comma.
        res = res[:-2]
        return '({0}, ({1}))'.format(self.name, res)

    def __repr__(self):
        """ (Molecule) -> str

        Return a string representation of this Molecule in this format:
          Molecule("NAME", (ATOM1, ATOM2, ...))
        """

        res = ''
        for atom in self.atoms:
            res = res + repr(atom) + ', '
			
        # Strip off the last comma.
        res = res[:-2]
        return 'Molecule("{0}", ({1}))'.format(self.name, res)


if __name__ == '__main__':
    ammonia = Molecule("AMMONIA")
    ammonia.add(Atom(1, "N", 0.257, -0.363, 0.0))
    ammonia.add(Atom(2, "H", 0.257, 0.727, 0.0))
    ammonia.add(Atom(3, "H", 0.771, -0.727, 0.890))
    ammonia.add(Atom(4, "H", 0.771, -0.727, -0.890))
    ammonia.translate(0, 0, 0.2)
    assert ammonia.atoms[0].center[0] == 0.257
    assert ammonia.atoms[0].center[1] == -0.363
    assert ammonia.atoms[0].center[2] == 0.2
    print(repr(ammonia))
    print(ammonia)


# Exercises

# Task1

class Country:
    def __init__(self, name, population, area):
        """ (Country, str, int, int)
        A new Country named name with population people and area area.
        >>> canada = Country('Canada', 34482779, 9984670)
        >>> canada.name
        'Canada'
        >>> canada.population
        34482779
        >>> canada.area
        9984670
        """   
        self.name = name
        self.population = population
        self.area = area
    def is_larger(self, other):
        """ (Country, Country) -> bool
        
        Return whether this country is larger than other.
        >>> canada = Country('Canada', 34482779, 9984670)
        >>> usa = Country('United States of America', 313914040, 9826675)
        >>> canada.is_larger(usa)
        True
        >>> usa.is_larger(canada)
        False
        """ 
        
        return self.area > other.area


    def population_density(self):
        """ (Country) -> float
        Return the population density of this country.
        >>> canada = Country('Canada', 34482779, 9984670)
        >>> canada.population_density()
        3.4535722262227995
        """
        return self.population / self.area

    def __str__(self):
        """ (Country) -> str
        Return a printable representation of this country.
        >>> usa = Country('United States of America', 313914040, 9826675)
        >>> print(usa)
        United States of America has a population of 313914040 and is 9826675 square km.
        """ 
        return '{} has a population of {} and is {} square km.'.format(
            self.name, self.population, self.area)

    def __repr__(self):
        """ (Country) -> str
        
        Return a concise representation of this country.

        >>> canada = Country('Canada', 34482779, 9984670)
        >>> canada
        Country('Canada', 34482779, 9984670)
        """ 
        return "Country('{0}', {1}, {2})".format(
            self.name, self.population, self.area)

    if __name__ == '__main__': 
        import doctest
        print(doctest.testmod())

# Task 2
# a)
class Continent:
    def __init__(self, name, countries):
        """ (Continent, str, list of Country) -> NoneType

        A continent named name made up of countries.

        >>> canada = country.Country('Canada', 34482779, 9984670)
        >>> usa = country.Country('United States of America', 313914040,               
        9826675)
        >>> mexico = country.Country('Mexico', 112336538, 1943950)
        >>> countries = [canada, usa, mexico]
        >>> north_america = Continent('North America', countries)
        >>> north_america.name
        'North America'
        >>> for country in north_america.countries:
        print(country)
        Canada has a population of 34482779 and is 9984670 square km.
        United States of America has a population of 313914040 and is 9826675 
        square km.
        Mexico has a population of 112336538 and is 1943950 square km.
        """ 
        self.name = name
        self.countries = countries

# b)

    def total_population(self):
        """ (Continent) -> int
        Return the total population of all the
        countries in this continent.
        >>> canada = country.Country('Canada', 34482779, 9984670)
        >>> usa = country.Country('United States of America', 313914040,
        826675)
        >>> mexico = country.Country('Mexico', 112336538, 1943950)
        >>> countries = [canada, usa, mexico]
        >>> north_america = Continent('North America', countries)
        >>> north_america.total_population()
        460733357
        """ 
        total = 0
        for country in self.countries:
            total = total + country.population
        return total

# c)

    def __str__(self):
        """ (Continent) -> str
        Return a printable representation of this Continent.
        >>> canada = country.Country('Canada', 34482779, 9984670)
        >>> usa = country.Country('United States of America', 313914040, 
        9826675)
        >>> mexico = country.Country('Mexico', 112336538, 1943950)
        >>> countries = [canada, usa, mexico]
        >>> north_america = Continent('North America', countries)
        >>> print(north_america)
        North America
        Canada has a population of34482779 and is 9984670 square km.
        United States of America has a population of 313914040 and is 9826675 
        square km.
        Mexico has a population of 112336538 and is 1943950 square km.
        """
        res = self.name
        for country in self.countries:
            res = res + '\n' + str(country)

        return res

    if __name__ == '__main__': 
        import doctest
        print(doctest.testmod())

# Task 3

def __str__(self):
    """ (Student) -> str
    
    Return a string representation of this Student.
    
    >>> student = Student('Paul', 'Ajax', 'pgries@cs.toronto.edu',
    '1234')
    >>> student.__str__()
    'Paul\\nAjax\\npgries@cs.toronto.edu\\n1234\\nPrevious courses: \\nCurrent courses: '
    """ 
    
    member_string = super().__str__()

    return '''{}\n{}\nPrevious courses: {}\nCurrent courses: 
        {}'''.format(
            member_string,
            self.student_number,
            ' '.join(self.courses_taken),
            ' '.join(self.courses_taking))

# Member repr:
def __repr__(self):
    """ (Member) -> str
    
    Return a concise string representation of this Member.

    >>> member = Member('Paul', 'Ajax', 'pgries@cs.toronto.edu')
    >>> member.__repr__()
    "Member('Paul', 'Ajax', 'pgries@cs.toronto.edu')" 
    """ 
    return "Member('{}', '{}', '{}')".format(
        self.name, self.address, self.email)

# Faculty repr:
def __repr__(self):
    """ (Faculty) -> str
    
    Return a concise string representation of this Faculty.
    
    >>> faculty = Faculty('Paul', 'Ajax', 'pgries@cs.toronto.edu', 
    '1234')
    >>> faculty.__repr__()
    "Faculty('Paul', 'Ajax', 'pgries@cs.toronto.edu', 1234, [])" 
    """ 
    
    return "Faculty('{}', '{}', '{}', {}, [{}])".format(
        self.name, self.address, self.email, self.faculty_number,
        ','.join(self.courses_teaching))

# Student repr:
def __repr__(self):
    """ (Faculty) -> str

    Return a concise string representation of this Faculty.
    
    >>> student = Student('Paul', 'Ajax', 'pgries@cs.toronto.edu', 
    '1234')
    >>> student.__repr__()
    "Student('Paul', 'Ajax', 'pgries@cs.toronto.edu', 1234, [], [])" 
    """ 
    
    return "Student('{}', '{}', '{}', {}, [{}], [{}])".format(
        self.name, self.address, self.email, self.student_number,
        ','.join(self.courses_taken), ','.join(self.courses_taking))

# Task 4

class Nematode:
    """ A microscopic worm. """ 
    
    def __init__(self, length, gender, age):
        """ (Nematode, float, str, int) -> NoneType
        Create a new Nematode with body length (in millimeters; they are 
        about
        1 mm in length), gender (either hermaphrodite or male), and age (in
        days).
        >>> worm = Nematode(1.1, 'hermaphrodite', 2)
        >>> worm.length
        1.1
        >>> worm.gender
        'hermaphrodite'
        >>> worm.age
        2
        """ 
        
        self.length = length
        self.gender = gender
        self.age = age
        
    def __str__(self):
        """ (Nematode) -> str
        
        Return a string representation of this Nematode.
        
        >>> worm = Nematode(1.1, 'hermaphrodite', 2)
        >>> worm.__str__()'Nematode: 1.1mm long, gender is hermaphrodite, 2 days old'
        """ 

        return 'Nematode: {}mm long, gender is {}, {} days old'.format(
            self.length, self.gender, self.age)

    def __repr__(self):
        """ (Nematode) -> str

        Return a concise string representation of this Nematode.
        
        >>> worm = Nematode(1.1, 'hermaphrodite', 2)
        >>> worm.__repr__()
        "Nematode(1.1, 'hermaphrodite', 2)" 
        """ 
        
        return "Nematode({}, '{}', {})".format(
            self.length, self.gender, self.age)

# Task 5

class Point:
    def __init__(self, x, y):
        """ (Point, int, int) -> NoneTypeA new Point at position (x, y).
        >>> p = Point(1, 3)
        >>> p.x1>>> p.y3
        """ 
        self.x = x
        self.y = y


class LineSegment:
    def __init__(self, point1, point2):
        """ (LineSegment, Point, Point) -> NoneType
        A new LineSegment connecting point1 to point2.
        >>> p1 = Point(1, 3)
        >>> p2 = Point(3, 2)
        >>> segment = LineSegment(p1, p2)
        >>> segment.startpoint == p1
        True
        >>> segment.endpoint == p2
        True
        """ 
        self.startpoint = point1
        self.endpoint = point2

    def slope(self):
        """ (LineSegment) -> float
        >>> segment = LineSegment(Point(1, 1), Point(3, 2))
        >>> segment.slope()0.5
        """ 
        return (self.endpoint.y -self.startpoint.y) / \
            (self.endpoint.x -self.startpoint.x)