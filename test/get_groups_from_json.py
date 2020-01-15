# * Packages

import json
import os

# *  directory is set 
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#Load json file
study_group1 = open ('study_data.json','r')
study_group2 = json.load(study_group1)
print(study_group2)