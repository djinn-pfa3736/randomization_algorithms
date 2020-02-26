# Import packages

import randomization
import logging
import os
import get_date
import sqlite3
import sys
import csv
import numpy as np

import pdb
import json_manager

# Logging setting
formatter = '%(levelname)s : %(asctime)s :%(message)s'
logging.basicConfig(level=logging.INFO, format=formatter)

# Set directory
# *  directory is set to as data manager
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class DataManager(object):
    def __init__(self):

        self.json_manager = json_manager.JsonManager()
        self.json_dict = self.json_manager.get_json_object()

        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        self.conn = sqlite3.connect("../data/patient.db")
        self.cursor = self.conn.cursor()

        a_count, b_count = self.get_assign_all()
        self.randomization = randomization.Randomize(10, a_count, b_count)
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS assignment (id INTEGER PRIMARY KEY \
        AUTOINCREMENT, recruted_date TEXT,hospital TEXT,hospital_id TEXT,\
        patient_name TEXT, assign TEXT, exclusion INTEGER)")

    def connect(self):
        dm = DataManager()
        # self.conn = sqlite3.connect("../data/patient.db")
        # self.cursor = self.conn.cursor()
        # self.randomization = randomization.Randomize()
        # self.cursor.execute(
        #     "CREATE TABLE IF NOT EXISTS assignment (id INTEGER PRIMARY KEY \
        # AUTOINCREMENT, recruted_date TEXT,hospital TEXT,hospital_id TEXT,\
        # patient_name TEXT, assign TEXT, exclusion INTEGER)")

        logging.info(msg='Connecting with patient.db')

    def reconnect(self):
        self.conn = sqlite3.connect("../data/patient.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS assignment (id INTEGER PRIMARY KEY \
            AUTOINCREMENT, recruted_date TEXT,hospital TEXT,hospital_id TEXT,\
            patient_name TEXT, assign TEXT, exclusion INTEGER)")

        # pdb.set_trace()

    def add_case(self,HospitalName = None, HospitalID = None, PatientName = None, Method = 'simple'):
        # Get assigned_group
        if(Method == 'simple'):
            self.assigned_group = self.randomization.simple_randomization()
        elif(Method == 'block'):
            self.assigned_group = self.randomization.block_randomization()
        self.tm=get_date.TimeManager()
        self.HospitalName= HospitalName
        self.PatientName = PatientName
        self.HospitalID = HospitalID
        # Get today
        self.today=self.tm.GetDate()
        logging.info(msg='self.today is ' + self.today)

        self.cursor.execute("insert into assignment(exclusion, recruted_date, hospital,hospital_id , assign, patient_name) \
        values (?,?,?,?,?,?)",[0, self.today, self.HospitalName, self.HospitalID, self.assigned_group, self.PatientName])

        self.conn.commit()

        logging.info(msg='Insert a case into patient.db')

    def print_db(self):
        logging.info(msg='Showing cases from the instance')
        self.conn = sqlite3.connect("../data/patient.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute('SELECT * FROM assignment ORDER BY id ASC')
        for rows in self.cursor.fetchall():
            print(rows)
        logging.info(msg='Print database')

    def get_row_number(self):
        self.cursor.execute('SELECT count(*) FROM assignment')
        self.result = self.cursor.fetchall()
        return(self.result[0][0])

    def get_assign_all(self):
        self.cursor.execute('SELECT * FROM assignment ORDER BY id ASC')

        a_count = 0
        b_count = 0
        for row in self.cursor.fetchall():
            # pdb.set_trace()
            if(row[5] == self.json_dict['study_groups']['GroupA']):
                a_count += 1
            else:
                b_count += 1
        logging.info(msg='Print database')
        if(a_count > b_count):
            a_count = a_count - b_count
            b_count = 0
        else:
            b_count = b_count - a_count
            a_count = 0

        return a_count, b_count


    def remove_sqlite_file(self):
        os.remove("../data/patient.db")

    def close(self):
        self.conn.close()
        logging.info(msg='Disconnecting database')

    def __del__(self):
        # conn = sqlite3.connect("../data/patient.db")
        self.conn.close()
        logging.info(msg='Disconnecting database')


if __name__ == '__main__':
    dm = DataManager()
    dm.remove_sqlite_file()
    dm.connect()
    dm.print_db()
