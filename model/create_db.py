# Import packages
import os
import sqlite3
import logging

# Set directory
# *  directory is set to as data manager
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Logging setting
formatter = '%(levelname)s : %(asctime)s :%(message)s'
logging.basicConfig(level=logging.INFO, format=formatter)

# Connecting
conn = sqlite3.connect('../data/patient.db')
cursor = conn.cursor()
logging.info(msg='Connecting database' + 'from' + os.getcwd())

# Create Table
cursor.execute(
    "CREATE TABLE IF NOT EXISTS patient (id INTEGER PRIMARY KEY AUTOINCREMENT, hospital TEXT, name TEXT, assignd_group TEXT, exclusion INTEGER)")
logging.info(msg='Create patient table' + 'from' + os.getcwd())

cursor.execute('SELECT * FROM patient ORDER BY id ASC')
for row in cursor.fetchall():
    print(row)
conn.commit()
conn.close()
