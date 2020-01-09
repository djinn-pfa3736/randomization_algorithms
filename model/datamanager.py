# Import packages
import logging
import os
import sqlite3

from mysql.connector import cursor

# Set directory
# *  directory is set to as data manager
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Logging setting
formatter = '%(levelname)s : %(asctime)s :%(message)s'
logging.basicConfig(level=logging.INFO, format=formatter)


class DataManager(object):
    def __init__(self):
        conn = sqlite3.connect('../data/patient.db')
        logging.info(msg='Connecting database' + 'from' + os.getcwd())
        conn.close()

    def input_case(self):
        conn = sqlite3.connect('../data/patient.db')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO patient VALUES (2,'Tomishiro','Kinjyo','Control')")
        conn.commit()
        conn.close()

    def __del__(self):
        conn = sqlite3.connect('../data/patient.db')
        conn.close()
        logging.info(msg='Disconnecting database')


data_manager = DataManager()
data_manager.input_case()
