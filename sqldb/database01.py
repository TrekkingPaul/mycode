#!/usr/bin/python3
"""Alta3 Research | rzfeeser@alta3.com
Connect to a sqlite db, or create one if it does not already exist"""

# standard library
import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

# always close your connection
conn.close()

