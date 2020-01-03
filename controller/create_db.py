# Import packages
import os
import sqlite3
import logging

import pdb

# Set directory
# *  directory is set to as data manager
os.chdir(os.path.dirname(os.path.abspath(__file__)))

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
logging.info(msg='Create patient table ' + 'from' + os.getcwd())

# Test Insert
#cursor.execute("INSERT INTO patient VALUES (1,'Nakagami','Gushiken')")
# Print
# fetchall()

cursor.execute('SELECT * FROM patient ORDER BY id ASC')
tmp = cursor.fetchall()
pdb.set_trace()

for row in cursor.fetchall():
    print(row)
conn.commit()
conn.close()
