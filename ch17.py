#!/usr/bin/env python3

# Databases
# as of Python 3.3.0, the standard library includes a module called "sqlite3" for working with it


# Saving Changes

# con.commit()
# con.close()

# connect to db
import sqlite3 
con = sqlite3.connect('population.db')
cur = con.cursor()

cur.execute('SELECT Region, Population FROM PopByRegion')
print(cur.fetchone())
print(cur.fetchall())
cur.fetchone()
print(cur.fetchall())
# To put the data in a particular order, we could sort the list returned by fetchall. However, 
# it is more efficient to get the database to do the sorting for us by adding an ORDER BY clause to the query like this:

cur.execute('SELECT Region, Population FROM PopByRegion ORDER BY Region')
print(cur.fetchall())

# By changing the column name after the phrase ORDER BY, we can change the way the database sorts. 
# As the following code demonstrates, we can also specify whether 
# we want values sorted in ascending (ASC) or descending (DESC) order:

cur.execute('''SELECT Region, Population FROM PopByRegion ORDER BY Population DESC''')
print(cur.fetchall())

# We can also use * to indicate that we want all columns:

cur.execute('SELECT Region FROM PopByRegion')
print(cur.fetchall())

cur.execute('SELECT * FROM PopByRegion')
print(cur.fetchall())


### Query Conditions

# We can select a subset of the data by using the keyword WHERE to specify condi- tions that the rows we want must satisfy.
# For example, we can get the regions with populations greater than one million using the greater-than operator:


cur.execute('SELECT Region FROM PopByRegion WHERE Population > 1000000')
print(cur.fetchall())
# Result "[('Southeastern Africa',)]"

# we can also use the AND, OR, and NOT operators. To get a list of regions with populations greater than one million 
# that have names that come before the letter L in the alphabet, we would use this (we are using a 
# triple-quoted string for the SQL statement so that it can span multiple lines):

cur.execute('''SELECT Region FROM PopByRegion WHERE Population > 1000000 AND Region < "L"''')
print(cur.fetchall())

### Updating and Deleting


# Data often changes over time, so we need to be 
# able to change the information stored in databases. To do that, we can use the UPDATE command

cur.execute('SELECT * FROM PopByRegion WHERE Region = "Japan"')
print(cur.fetchone())

cur.execute('''UPDATE PopByRegion SET Population = 100700 WHERE Region = "Japan"''')
cur.execute('SELECT * FROM PopByRegion WHERE Region = "Japan"')
print(cur.fetchone())

# We can also delete records from the database:

cur.execute('DELETE FROM PopByRegion WHERE Region < "L"')
cur.execute('SELECT * FROM PopByRegion')
print(cur.fetchall())

# In both cases, all records that meet the WHERE condition are affected. If we don’t include a WHERE condition, 
# then all rows in the database are updated or removed. Of course, we can always put records back into the database:

cur.execute('INSERT INTO PopByRegion VALUES ("Japan", 100562)')
cur.execute('SELECT * FROM PopByRegion WHERE Region = "Japan"')
print(cur.fetchall())

# cur.execute('DROP TABLE PopByRegion')
# Using NULL for Missing Data
# cur.execute('DROP TABLE Test')
# cur.execute('INSERT INTO PopByRegion VALUES ("Mars", NULL)')
# cur.execute('CREATE TABLE Test (Region TEXT NOT NULL, ' 'Population INTEGER)')
# cur.execute('INSERT INTO Test VALUES (NULL, 456789)')

##### Using Joins to Combine Tables

# adding table that contains the names of countries, the regions that they are in, and their populations:

# insert data into the new table

cur.execute('''INSERT INTO PopByCountry VALUES("Eastern Asia", "China", 1285238)''')

countries = [("Eastern Asia", "DPR Korea", 24056), ("Eastern Asia", 
"Hong Kong (China)", 8764), ("Eastern Asia", "Mongolia", 3407), ("Eastern Asia",
"Republic of Korea", 41491), ("Eastern Asia", "Taiwan", 1433), ("North America",
"Bahamas", 368), ("North America", "Canada", 40876), ("North America", "Greenland", 43),
("North America", "Mexico", 126875), ("North America", "United States", 493038)]

for c in countries:
     cur.execute('INSERT INTO PopByCountry VALUES (?, ?, ?)', (c[0], c[1], c[2]))
     

con.commit()

cur.execute('''
SELECT PopByRegion.Region, PopByCountry.Country 
FROM   PopByRegion INNER JOIN PopByCountry
WHERE  (PopByRegion.Region = PopByCountry.Region)
AND    (PopByRegion.Population > 1000000)
''')

print(cur.fetchall())

# Removing Duplicates

cur.execute('''
SELECT PopByRegion.Region
FROM   PopByRegion INNER JOIN PopByCountry
WHERE  (PopByRegion.Region = PopByCountry.Region)
AND    ((PopByCountry.Population * 1.0) / PopByRegion.Population > 0.10)''')

print(cur.fetchall())

cur.execute('''
SELECT DISTINCT PopByRegion.Region
FROM PopByRegion INNER JOIN PopByCountry
WHERE (PopByRegion.Region = PopByCountry.Region)
AND ((PopByCountry.Population * 1.0) / PopByRegion.Population > 0.10)''')

print(cur.fetchall())



# cur.execute('''
# CREATE TABLE PopByCountry(
# Region TEXT NOT NULL,
# Country TEXT NOT NULL,
# Population INTEGER NOT NULL,
# CONSTRAINT CountryKey PRIMARY KEY (Region, Country))''')

# Traceback (most recent call last):
#   File "./ch17.py", line 146, in <module>
#     CONSTRAINT CountryKey PRIMARY KEY (Region, Country))''')
# sqlite3.OperationalError: table PopByCountry already exists


# Advanced Features

cur.execute('SELECT SUM (Population) FROM PopByRegion')

print(cur.fetchone())

# Grouping

cur.execute('''SELECT Region, SUM (Population) FROM PopByCountry GROUP BY Region''')
print(cur.fetchall())

cur.execute('''SELECT SUM (Population) FROM PopByCountry WHERE Region = "North America"''')
print(cur.fetchall())

cur.execute('''SELECT SUM (Population) FROM PopByCountry WHERE Region = "Eastern Asia"''')
print(cur.fetchall())

# Self-Joins

cur.execute('''SELECT Country FROM PopByCountry WHERE (ABS(Population - Population) < 1000)''')
print(cur.fetchall())


cur.execute('''
SELECT A.Country, B.Country
FROM PopByCountry A INNER JOIN PopByCountry B
WHERE (ABS(A.Population - B.Population) <= 1000)
AND (A.Country != B.Country)''')
print(cur.fetchall())

# Nested Queries


# This result is wrong—Hong Kong has a projected population of 8,764,000, so eastern Asia shouldn’t 
# have been returned. Because other countries in eastern Asia have populations that are not 8,764,000, 
# though, eastern Asia was included in the final results.

cur.execute('''SELECT DISTINCT Region FROM PopByCountry
                   WHERE (PopByCountry.Population != 8764)''')

print(cur.fetchall())

# regions that have countries with a population of 8,764,000, as shown in the following code

cur.execute('''
SELECT DISTINCT Region
FROM PopByCountry
WHERE (PopByCountry.Population = 8764) ''')

print(cur.fetchall())

# Now we want to get the names of regions that were not in the results of our first query. To do this, we will use a WHERE condition and NOT IN:
cur.execute(''' SELECT DISTINCT Region FROM PopByCountry WHERE Region NOT IN
    (SELECT DISTINCT Region
     FROM PopByCountry
     WHERE (PopByCountry.Population = 8764))
''')

print(cur.fetchall())
