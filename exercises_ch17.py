#!/usr/bin/env python3

# Task 1
# a) Creates a new database called census.db
import sqlite3 as dbapi

con = dbapi.connect('census.db')

# b) Makes a database table called Density that will hold the name of the province or territory (TEXT), 
# the population (INTEGER), and the land area (REAL)

cur = con.cursor()
cur.execute('''CREATE TABLE Density(Province TEXT,Population INTEGER, Area REAL)''')
con.commit()

# c) Inserts the data from Table 34, 2001 Canadian Census Data, on page 365

table = [
    ('Newfoundland and Labrador', 512930, 370501.69),
    ('Prince Edward Island', 135294, 5684.39),
    ('Nova Scotia', 908007, 52917.43),
    ('New Brunswick', 729498, 71355.67),
    ('Quebec', 7237479, 1357743.08),
    ('Ontario', 11410046, 907655.59),
    ('Manitoba', 1119583, 551937.87),
    ('Saskatchewan', 978933, 586561.35),
    ('Alberta', 2974807, 639987.12),
    ('British Columbia', 3907738, 926492.48),
    ('Yukon Territory', 28674,474706.97),
    ('Northwest Territories', 37360, 1141108.37),
    ('Nunavut', 26745, 1925460.18),
]

for row in table:
    cur.execute('INSERT INTO Density VALUES (?, ?, ?)', row)
con.commit()
# d) Retrieves the contents of the table

cur.execute('SELECT * FROM Density')
for row in cur.fetchall():
    print(row)
# e) Retrieves the populations

cur.execute('SELECT Population FROM Density')
for row in cur.fetchall():
    print(row)
# f) Retrieves the provinces that have populations of less than one million

cur.execute('''SELECT Province FROM Density WHERE Population < 1000000''')
for row in cur.fetchall():
    print(row)
# g) Retrieves the provinces that have populations of less than one million or greater than five million

cur.execute('''SELECT Province FROM Density WHERE Population < 1000000 OR Population > 5000000''')
for row in cur.fetchall():
    print(row)
# h) Retrieves the provinces that do not have populations of less than one million or greater than five million

cur.execute('''SELECT Province FROM Density WHERE NOT(Population < 1000000 OR Population > 5000000)''')
for row in cur.fetchall():
    print(row)
# i) Retrieves the populations of provinces that have a land area greater than 200,000 square kilometers

cur.execute('''SELECT Population FROM Density WHERE Area > 200000''')
for row in cur.fetchall():
    print(row)
# j) Retrieves the provinces along with their population densities (popula- tion divided by land area)

cur.execute('SELECT Province, Population / Area FROM Density')
for row in cur.fetchall():
    print(row)



