import logging
import os
# Set directory
# * directory is set to as test
from pyclbr import Class

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Logging setting
formatter = '%(levelname)s : %(asctime)s :%(message)s'
logging.basicConfig(level=logging.INFO, format=formatter)


# file delete
class Eraser(object):
    def delete_patient_db(self):
        os.remove('../data/patient.db')
        logging.info(msg='delete patient database')


# Do the function
erase = Eraser()
erase.delete_patient_db()
