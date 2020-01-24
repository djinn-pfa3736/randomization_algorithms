# * Packages

import json
import os


class GetStudyGroups(object):

    def get_var_Groups_ver1(self):
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        self.study_group_file = open('study_data.json', 'r')
        self.study_group_object = json.load(self.study_group_file)
        return self.study_group_object

if __name__ == '__main__':
    get_study_groups = GetStudyGroups()
    Groups = get_study_groups.get_var_Groups_ver1()
    print(Groups['study_groups'][0])
    print(Groups['study_groups'][1])
    print(type(Groups))