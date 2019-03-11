#!/usr/bin/env python3

# Task 2
# a) Creates a new database called census.db
import sqlite3 as dbapi

con = dbapi.connect('census.db')
cur = con.cursor()

cur.execute('''CREATE TABLE Capitals(Province TEXT,Capital TEXT, Population INTEGER)''')

con.commit()

table = [
    ('Newfoundland and Labrador', "St. John's", 172918),
    ('Prince Edward Island', 'Charlottetown', 58358),
    ('Nova Scotia', 'Halifax', 359183),
    ('New Brunswick', 'Fredericton', 81346),
    ('Quebec', 'Qeubec City', 682757),
    ('Ontario', 'Toronto', 4682897),
    ('Manitoba', 'Winnipeg', 671274),
    ('Saskatchewan', 'Regina', 192800),
    ('Alberta', 'Edmonton', 937845),
    ('British Columbia', 'Victoria', 311902),
    ('Yukon Territory', 'Whitehorse', 21405),
    ('Northwest Territories', 'Yellowknife', 16541),
    ('Nunavut', 'Iqaluit', 5236),
]

for row in table:
    cur.execute('INSERT INTO Capitals VALUES (?, ?, ?)', row)
con.commit()

# a) Retrieve the contents of the table

cur.execute('SELECT * FROM Capitals')
for row in cur.fetchall():
    print(row)
# b) Retrieve the populations of the provinces and capitals (in a list of tuples of the form [province population, capital population])

cur.execute('''SELECT Density.Population, Capitals.Population FROM Capitals INNER JOIN Density WHERE Capitals.Province = Density.Province''')
for row in cur.fetchall():
    print(row)
# c) Retrieve the land area of the provinces whose capitals have populations greater than 100,000

cur.execute('''SELECT Density.AreaFROM Capitals INNER JOIN Density WHERE Capitals.Province = Density.Province AND Capitals.Population > 100000''')
for row in cur.fetchall():
    print(row)
# d) Retrieve the provinces with land densities less than two people per square kilometer and capital city populations more than 500,000

cur.execute('''SELECT Density.ProvinceFROM Capitals INNER JOIN Density WHERE Capitals.Province = Density.Province AND Density.Population / Density.Area < 2AND Capitals.Population > 500000''')
for row in cur.fetchall():
    print(row)
# e) Retrieve the total land area of Canada

cur.execute('SELECT SUM(Area) FROM Density')
print(cur.fetchone())
# f) Retrieve the average capital city population

cur.execute('SELECT AVG(Population) FROM Capitals')
print(cur.fetchone())
# g) Retrieve the lowest capital city population

cur.execute('SELECT MIN(Population) FROM Capitals')
print(cur.fetchone())
# h) Retrieve the highest province/territory population

cur.execute('SELECT MAX(Population) FROM Density')
print(cur.fetchone())
# i) Retrieve the provinces that have land densities within 0.5 persons per square kilometer of on another—have each pair of provinces reported only once

cur.execute('''SELECT A.Province, B.Province 
                FROM Density A INNER JOIN Density B
                WHERE A.Province < B.Province
                AND ABS(A.Population / A.Area -B.Population / B.Area) < 0.5''')

for row in cur.fetchall():
    print(row)