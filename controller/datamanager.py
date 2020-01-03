# Import packages
import os
import sqlite3
import logging

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
        
    def __del__(self):
        conn = sqlite3.connect('../data/' + self.n_db + '.db')
        conn.close()
        logging.info(msg='Disconnecting database')


data_manager = DataManager()
data_manager.DB =
del data_manager
