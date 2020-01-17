import logging
import os
import sqlite3

# Set directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Logging setting
formatter = '%(levelname)s : %(asctime)s :%(message)s'
logging.basicConfig(level=logging.INFO, format=formatter)

# Connecting
conn = sqlite3.connect('../data/patient.db')
cursor = conn.cursor()
logging.info(msg='Connecting database' + 'from' + os.getcwd())

cursor.execute('SELECT * FROM assignment ORDER BY id ASC')
for row in cursor.fetchall():
    print(row)
conn.commit()
conn.close()

logging.info(msg="Complete showing database")
