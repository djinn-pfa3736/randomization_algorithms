# Import packages
import logging
import os
import sqlite3

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
    "CREATE TABLE IF NOT EXISTS assignment (id INTEGER PRIMARY KEY \
        AUTOINCREMENT, recruted_date TEXT,hospital TEXT,hospital_id INTEGER,\
        patient_name TEXT, assign TEXT, exclusion INTEGER)")

logging.info(msg='Create assignment table')

cursor.execute(
            "insert into assignment(recruted_date) values ('2019-1-12')")
conn.commit()
        
cursor.execute('SELECT * FROM assignment ORDER BY id ASC')
for row in cursor.fetchall():
    print(row)
conn.commit()
conn.close()
