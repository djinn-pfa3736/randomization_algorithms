# Import package
import json
import random

import get_groups_from_json

# Global変数としてassignされたGroupを代入する
# Assigned group is set as global variable
# Groups = ['Treat', 'Control']
# for i in Groups:
#     print(i)
if __name__ == '__main__':
    get_study_groups = get_groups_from_json.GetStudyGroups()
    Groups = get_study_groups.get_var_Groups_ver1()
    print(Groups)
    print(Groups['study_groups'][0])
    print(Groups['study_groups'][1])


class Randomize (object):
    # def __init__(self):
    #     # * define AssinedGroup as global variable
    #     get_study_groups = get_groups_from_json.GetStudyGroups()
    #     get_study_groups.get_var_Groups_ver1()
    #     print('jsonから'+Groups['study_groups'][0]+'のグループ名を得ました')
    #     print('jsonから'+Groups['study_groups'][1]+'のグループ名を得ました')

    def simple_randomization_ver1(self):
         # * define AssinedGroup as global variable
        get_study_groups = get_groups_from_json.GetStudyGroups()
        get_study_groups.get_var_Groups_ver1()
        print('jsonから'+Groups['study_groups'][0]+'のグループ名を得ました')
        print('jsonから'+Groups['study_groups'][1]+'のグループ名を得ました')
        global AssinedGroup
        
        if random.random() > 0.5:  
            AssignedGroup = Groups['study_groups'][0]
            print(AssignedGroup)
        else:
            AssignedGroup = Groups['study_groups'][1]
            print(AssignedGroup)

if __name__ == '__main__':
    randomization = Randomize()
    randomization.simple_randomization_ver1()
