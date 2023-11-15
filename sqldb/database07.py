#!/usr/bin/python3
"""Alta3 Research | rzfeeser@alta3.com
Update a record within the table."""

# standard library
import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute("UPDATE COMPANY set SALARY = 25000.00 where ID = 1")
conn.commit()
print("Total number of rows updated :", conn.total_changes)

cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
    # newsal = row[3] + 100000
    #print(newsal)
    newsal = str(newsal)
    keyid = str(row[0])
    conn.execute("UPDATE COMPANY set SALARY = SALARY + 100000.00 where ID = " + keyid)
    conn.commit()
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("ADDRESS = ", row[2])
    print("SALARY = ", row[3], "\n")

print("Operation done successfully")

# always close your connection
conn.close()

