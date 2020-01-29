# Import packages

import randomization
import logging
import os
import get_date
import sqlite3
import sys


import pdb

# Logging setting
formatter = '%(levelname)s : %(asctime)s :%(message)s'
logging.basicConfig(level=logging.INFO, format=formatter)

# Set directory
# *  directory is set to as data manager
os.chdir(os.path.dirname(os.path.abspath(__file__)))

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
        self.assigned_group = self.randomization.simple_randomization_ver1()
        self.tm = get_date.TimeManager()

        # Get today
        self.today = self.tm.GetDate()
        logging.info(msg='self.today is '+self.today)

        self.cursor.execute("insert into assignment(recruted_date, assign) values (?,?)", [self.today,
                                                                                           self.assigned_group])

        self.conn.commit()

        logging.info(msg='Insert a case into patient.db')

    def add_case2(self,HospitalName='Hospital', HospitalID='11111', PatientName = 'No Name'):
        # Get assigned_group
        self.assigned_group = self.randomization.simple_randomization_ver1()
        self.tm=get_date.TimeManager()
        self.HospitalName= HospitalName
        self.PatientName = PatientName
        self.HospitalID = HospitalID
        # Get today
        self.today=self.tm.GetDate()
        logging.info(msg='self.today is '+self.today)

        self.cursor.execute("insert into assignment(exclusion, recruted_date, hospital,hospital_id , assign, patient_name) \
        values (?,?,?,?,?,?)",[0, self.today, self.HospitalName, self.HospitalID, self.assigned_group, self.PatientName])

        self.conn.commit()

        logging.info(msg='Insert a case into patient.db')

    def print_db(self):
        logging.info(msg='Showing cases from the instance')
        # self.conn = sqlite3.connect("../data/patient.db")
        # self.cursor = self.conn.cursor()

        self.cursor.execute('SELECT * FROM assignment ORDER BY id ASC')
        for rows in self.cursor.fetchall():
            print(rows)
        logging.info(msg='Print database')
        
    def get_db_for_tree(self):
        self.cursor.execute('SELECT id, recruted_date, hospital, hospital_id,\
        patient_name, assign FROM assignment WHERE exclusion == 0 ORDER BY id ASC')
        for self.rows in self.cursor.fetchall():
            print(self.rows)
            self.result=[]
            self.result=self.result.append(self.rows)
            
        logging.info(msg='Filter exclusion is zero')
        print(type(self.result))
        return self.result
        
    def __del__(self):
        # conn = sqlite3.connect("../data/patient.db")
        self.conn.close()
        logging.info(msg='Disconnecting database')


if __name__ == '__main__':
    dm = DataManager()
    dm.print_db()
    dm.get_db_for_tree()
