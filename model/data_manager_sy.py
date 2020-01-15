# Import packages
import logging
import os
import sqlite3
import sys
import randomization

# Logging setting
formatter = '%(levelname)s : %(asctime)s :%(message)s'
logging.basicConfig(level=logging.INFO, format=formatter)


# Set directory
# *  directory is set to as data manager
os.chdir(os.path.dirname(os.path.abspath(__file__)))

randomization=randomization.Randomize()
randomization.simple_randomization_ver1()

# class DataManager:
#     def __init__(self):
#         os.chdir(os.path.dirname(os.path.abspath(__file__)))

#         self.conn = sqlite3.connect("../data/patient.db")
#         self.cursor = self.conn.cursor()

#     def connection_close(self):
#         self.conn.close()

#     def add_case(self):

#         self.cursor.execute(
#             "SELECT * FROM patient INNER JOIN assignment ON patient.id = assignment.id")

#     def print_db(self):
#         for row in self.cursor.fetchall():
#             print(row)

#     def __del__(self):
#         conn = sqlite3.connect("../data/patient.db")
#         conn.close()
#         logging.info(msg='Disconnecting database')


# if __name__ == "__main__":
#     # *  directory is set to as data manager
#     os.chdir(os.path.dirname(os.path.abspath(__file__)))

#     data_manager = DataManager()
#     # pdb.set_trace()

#     data_manager.cursor.execute(
#         "insert into patient(hospital, patient_name, exclusion) values('Nakagami', 'Gushiken', '0')")
#     data_manager.cursor.execute(
#         "insert into patient(hospital, patient_name, exclusion) values('Nakagami', 'Ueda', '0')")
#     data_manager.cursor.execute(
#         "insert into patient(hospital, patient_name, exclusion) values('Nakagami', 'Tamaki', '0')")
#     data_manager.cursor.execute(
#         "insert into patient(hospital, patient_name, exclusion) values('Nakagami', 'Shiroma', '0')")
#     data_manager.cursor.execute(
#         "insert into patient(hospital, patient_name, exclusion) values('Nakagami', 'Afuso', '0')")

#     data_manager.simple_randomization()
#     data_manager.print_db()
