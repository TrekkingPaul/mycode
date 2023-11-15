#!/usr/bin/python3
"""Alta3 Research | rzfeeser@alta3.com
Updated the SQL language so that the table is only created if it does not
already exist, this prevents an error."""

# standard library
import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE IF NOT EXISTS COMPANY
 (ID INT PRIMARY KEY     NOT NULL,
 NAME           TEXT    NOT NULL,
 AGE            INT     NOT NULL,
 ADDRESS        CHAR(50),
 SALARY         REAL);''')
print("Table created successfully")

# always close your connection
conn.close()

