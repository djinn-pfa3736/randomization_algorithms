# Import package
import json
import random

import get_groups_from_json


class Randomize (object):

    def simple_randomization_ver1(self):
        # * define AssinedGroup as global variable
        self.get_study_groups = get_groups_from_json.GetStudyGroups()
        self.Groups = self.get_study_groups.get_var_Groups_ver1()
        # * get random variable 0-1
        if random.random() > 0.5:
            self.AssignedGroup = self.Groups['study_groups'][0]
            print(self.AssignedGroup)
            return(self.AssignedGroup)
        else:
            self.AssignedGroup = self.Groups['study_groups'][1]
            print(self.AssignedGroup)
            return(self.AssignedGroup)


if __name__ == '__main__':
    randomization = Randomize()
    randomization.simple_randomization_ver1()
