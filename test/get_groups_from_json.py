# * Packages

import json
import os

# *  directory is set
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load json file
study_group_file = open('study_data.json', 'r')
study_group_object = json.load(study_group_file)
print(study_group_object)
print(study_group_object["study_groups"][0])


class GetStudyGroup(object):
    def __int__(self):
        study_group_file = open('study_data.json', 'r')
        study_group_object = json.load(study_group_file)
        global Groups
        Groups = study_group_object["study_groups"]
