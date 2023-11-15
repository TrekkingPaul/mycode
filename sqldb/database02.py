#!/usr/bin/python3
"""Alta3 Research | rzfeeser@alta3.com
Exclusive creation of a table. This will FAIL if the table already exists."""

# standard library
import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE COMPANY
 (ID INT PRIMARY KEY     NOT NULL,
 NAME           TEXT    NOT NULL,
 AGE            INT     NOT NULL,
 ADDRESS        CHAR(50),
 SALARY         REAL);''')
print("Table created successfully")

# always close your connection
conn.close()

