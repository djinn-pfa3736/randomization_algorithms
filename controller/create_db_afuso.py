# Import packages
import os
import sqlite3
import logging
import random

import pdb

# Set directory
# *  directory is set to as data manager
os.chdir(os.path.dirname(os.path.abspath(__file__)))
DATABASE_NAME = os.path.join(os.path.dirname(__file__),"db","xxx.db")
# Logging setting
formatter = '%(levelname)s : %(asctime)s :%(message)s'
logging.basicConfig(level=logging.INFO, format=formatter)

# Connecting
conn = sqlite3.connect('../data/patient.db')
cursor = conn.cursor()
logging.info(msg='Connecting database ' + 'from' + os.getcwd())

# Create Table
cursor.execute(
    "CREATE TABLE IF NOT EXISTS patient (id INTEGER PRIMARY KEY AUTOINCREMENT, hospital TEXT, name TEXT)")
cursor.execute(
    "CREATE TABLE IF NOT EXISTS assignment (id INTEGER PRIMARY KEY AUTOINCREMENT, assign TEXT)")
logging.info(msg='Create patient table ' + 'from' + os.getcwd())

# Test Insert
"""
cursor.execute("INSERT INTO patient VALUES ('Nakagami','Gushiken')")
cursor.execute("INSERT INTO patient VALUES ('Nakagami','Tamaki')")
cursor.execute("INSERT INTO patient VALUES ('Nakagami','Shiroma')")
cursor.execute("INSERT INTO patient VALUES ('Nakagami','Yamaguchi')")
cursor.execute("INSERT INTO patient VALUES ('Nakagami','Afuso')")
"""

cursor.execute("insert into patient(hospital, name) values('Nakagami', 'Gushiken')")
cursor.execute("insert into patient(hospital, name) values('Nakagami', 'Ueda')")
cursor.execute("insert into patient(hospital, name) values('Nakagami', 'Tamaki')")
cursor.execute("insert into patient(hospital, name) values('Nakagami', 'Shiroma')")
cursor.execute("insert into patient(hospital, name) values('Nakagami', 'Afuso')")

cursor.execute('SELECT * FROM patient ORDER BY id ASC')
# pdb.set_trace()
for row in cursor.fetchall():
    if random.random() > 0.5:
        cursor.execute("insert into assignment(assign) values('Control')")
    else:
        cursor.execute("insert into assignment(assign) values('Treat')")

cursor.execute("SELECT * FROM patient INNER JOIN assignment ON patient.id = assignment.id")
for row in cursor.fetchall():
    print(row)

# conn.commit()
conn.close()
