# Import packages
import logging
import os
import pdb
import random
import sqlite3
import sys

# Logging setting
formatter = '%(levelname)s : %(asctime)s :%(message)s'
logging.basicConfig(level=logging.INFO, format=formatter)


# Set directory
# *  directory is set to as data manager
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# class DataManager(object):


class DataManager:
    def __init__(self):
        os.chdir(os.path.dirname(os.path.abspath(__file__)))

        self.conn = sqlite3.connect("../data/patient.db")
        self.cursor = self.conn.cursor()
        logging.info(msg='Connecting database' + 'from' + os.getcwd())

    def connection_close(self):
        self.conn.close()

    def simple_randomization(self):
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS assignment (id INTEGER PRIMARY KEY \
        AUTOINCREMENT, recruted_date TEXT,hospital TEXT, patient_name TEXT,\
         assign TEXT, exclusion INTEGER)")
        logging.info(msg='Create patient table' + 'from' + os.getcwd())

        self.cursor.execute('SELECT * FROM patient ORDER BY id ASC')
        # pdb.set_trace()
        for row in self.cursor.fetchall():
            if random.random() > 0.5:
                self.cursor.execute(
                    "insert into assignment(assign) values('Control')")
            else:
                self.cursor.execute(
                    "insert into assignment(assign) values('Treat')")
        self.cursor.execute(
            "SELECT * FROM patient INNER JOIN assignment ON patient.id = assignment.id")

    def print_db(self):
        for row in self.cursor.fetchall():
            print(row)

    def __del__(self):
        conn = sqlite3.connect("../data/patient.db")
        conn.close()
        logging.info(msg='Disconnecting database')


if __name__ == "__main__":
    # *  directory is set to as data manager
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    data_manager = DataManager()
    # pdb.set_trace()

    data_manager.cursor.execute(
        "insert into patient(hospital, patient_name, exclusion) values('Nakagami', 'Gushiken', '0')")
    data_manager.cursor.execute(
        "insert into patient(hospital, patient_name, exclusion) values('Nakagami', 'Ueda', '0')")
    data_manager.cursor.execute(
        "insert into patient(hospital, patient_name, exclusion) values('Nakagami', 'Tamaki', '0')")
    data_manager.cursor.execute(
        "insert into patient(hospital, patient_name, exclusion) values('Nakagami', 'Shiroma', '0')")
    data_manager.cursor.execute(
        "insert into patient(hospital, patient_name, exclusion) values('Nakagami', 'Afuso', '0')")

    data_manager.simple_randomization()
    data_manager.print_db()
