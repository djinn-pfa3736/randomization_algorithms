# * Packages

import json
import os

# os.chdir(os.path.dirname(os.path.abspath(__file__)))
# # Load json file
# study_group_file = open('study_data.json', 'r')
# study_group_object = json.load(study_group_file)
# print(study_group_object)
# print(study_group_object["study_groups"])
# print(study_group_object["study_groups"][0])


class GetStudyGroups(object):

    def get_var_Groups_ver1(self):
        global Groups
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        study_group_file = open('study_data.json', 'r')
        study_group_object = json.load(study_group_file)
        print(study_group_object)
        Groups = study_group_object
        return Groups

if __name__ == '__main__':
    get_study_groups = GetStudyGroups()
    get_study_groups.get_var_Groups_ver1()
    print(Groups['study_groups'][0])
    print(Groups['study_groups'][1])
    print(type(Groups))
