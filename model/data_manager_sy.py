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

if __name__ == '__main__':
    randomization = randomization.Randomize()
    randomization.simple_randomization_ver1()


class DataManager(object):
    def __init__(self):
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        self.conn = sqlite3.connect("../data/patient.db")
        self.cursor = self.conn.cursor()

    def connect(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS assignment (id INTEGER PRIMARY KEY \
        AUTOINCREMENT, recruted_date TEXT,hospital TEXT,hospital_id INTEGER,\
        patient_name TEXT, assign TEXT, exclusion INTEGER)")

        logging.info(msg='Connecting with patient.db')

    def add_case(self):
        # Get assigned_group
        import randomization
        self.randomization = randomization.Randomize()
        self.assigned_group = self.randomization.simple_randomization_ver1()

        self.cursor.execute(
            "insert into assignment(recruted_date) values ('2019-1-12')")
        self.conn.commit()
        logging.info(msg='Insert a case into patient.db')
        
    def print_db(self):
        logging.info(msg='Showing cases from the instance')
        self.conn = sqlite3.connect("../data/patient.db")
        self.cursor = self.conn.cursor()
        for self.rows in self.cursor.fetchall():
            print(self.row)
        logging.info(msg='Ending print_db')

    def __del__(self):
        conn = sqlite3.connect("../data/patient.db")
        conn.close()
        logging.info(msg='Disconnecting database')


if __name__ == "__main__":
    data_manager = DataManager()
    data_manager.add_case()
    data_manager.print_db()
    # Connecting
    conn = sqlite3.connect('../data/patient.db')
    cursor = conn.cursor()
    logging.info(msg='Connecting database in the test')

    logging.info(msg='Showing the cases from the test')
    cursor.execute('SELECT * FROM assignment ORDER BY id ASC')
    for row in cursor.fetchall():
        print(row)
    conn.commit()
    conn.close()



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
