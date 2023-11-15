#!/usr/bin/python3
"""Alta3 Research | rzfeeser@alta3.com
Select and read data from a table."""

# standard library
import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("ADDRESS = ", row[2])
    print("SALARY = ", row[3], "\n")

print("Operation done successfully")

# always close your connection
conn.close()

