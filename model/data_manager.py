# Import packages
import logging
import os

import sqlite3
import sys


import pdb

# Logging setting
formatter = '%(levelname)s : %(asctime)s :%(message)s'
logging.basicConfig(level=logging.INFO, format=formatter)

# Set directory
# *  directory is set to as data manager
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import randomization

class DataManager(object):
    def __init__(self):
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        self.conn = sqlite3.connect("../data/patient.db")
        self.cursor = self.conn.cursor()

        self.randomization = randomization.Randomize()

    def connect(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS assignment (id INTEGER PRIMARY KEY \
        AUTOINCREMENT, recruted_date TEXT,hospital TEXT,hospital_id INTEGER,\
        patient_name TEXT, assign TEXT, exclusion INTEGER)")

        logging.info(msg='Connecting with patient.db')

    def add_case(self):
        # Get assigned_group
        # import randomization
        self.assigned_group = self.randomization.simple_randomization_ver1()
        self.cursor.execute("insert into assignment(recruted_date, assign) values ('2019-1-24',?)", [
            self.assigned_group])
        self.conn.commit()
        logging.info(msg='Insert a case into patient.db')

    def print_db(self):
        logging.info(msg='Showing cases from the instance')
        # self.conn = sqlite3.connect("../data/patient.db")
        # self.cursor = self.conn.cursor()

        self.cursor.execute('SELECT * FROM assignment ORDER BY id ASC')
        for rows in self.cursor.fetchall():
            print(rows)
        logging.info(msg='Ending print_db')

    def __del__(self):
        # conn = sqlite3.connect("../data/patient.db")
        self.conn.close()
        logging.info(msg='Disconnecting database')

if __name__ == '__main__':
    dm=DataManager()
    dm.add_case()
    dm.print_db()