# Import packages
import os
import sqlite3
import logging
import sys
import random

import pdb

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
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS assignment (id INTEGER PRIMARY KEY AUTOINCREMENT, assign TEXT)")

        self.cursor.execute('SELECT * FROM patient ORDER BY id ASC')
        # pdb.set_trace()
        for row in self.cursor.fetchall():
            if random.random() > 0.5:
                self.cursor.execute("insert into assignment(assign) values('Control')")
            else:
                self.cursor.execute("insert into assignment(assign) values('Treat')")
        self.cursor.execute("SELECT * FROM patient INNER JOIN assignment ON patient.id = assignment.id")

    def print_db(self):
        for row in self.cursor.fetchall():
            print(row)

    """
    def __del__(self):
        conn = sqlite3.connect('../data/' + self.n_db + '.db')
        conn.close()
        logging.info(msg='Disconnecting database')
    """

if __name__ == "__main__":
    # file_name = sys.argv[1]
    # Set directory
    # *  directory is set to as data manager
    # os.chdir(os.path.dirname(os.path.abspath(__file__)))

    data_manager = DataManager()

    # Logging setting
    formatter = '%(levelname)s : %(asctime)s :%(message)s'
    logging.basicConfig(level=logging.INFO, format=formatter)

    # pdb.set_trace()

    data_manager.cursor.execute("insert into patient(hospital, name) values('Nakagami', 'Gushiken')")
    data_manager.cursor.execute("insert into patient(hospital, name) values('Nakagami', 'Ueda')")
    data_manager.cursor.execute("insert into patient(hospital, name) values('Nakagami', 'Tamaki')")
    data_manager.cursor.execute("insert into patient(hospital, name) values('Nakagami', 'Shiroma')")
    data_manager.cursor.execute("insert into patient(hospital, name) values('Nakagami', 'Afuso')")

    data_manager.simple_randomization()
    data_manager.print_db()