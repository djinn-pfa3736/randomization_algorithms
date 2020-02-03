# Import package
import json
import random

import json_manager


class Randomize:

    def __init__(self):
        pass

    def simple_randomization_ver1(self):
        # * define AssinedGroup as global variable
        self.json_manager = json_manager.JsonManager()
        self.json_dict=self.json_manager.get_json_object()
        # self.get_study_groups = JsonManager()
        # self.Groups = self.get_study_groups.get_var_Groups_ver1()
        # * get random variable 0-1
        if random.random() > 0.5:
            self.AssignedGroup = self.json_dict['study_groups']['GroupA']
            print(self.AssignedGroup)
            return(self.AssignedGroup)
        else:
            self.AssignedGroup = self.json_dict['study_groups']['GroupB']
            print(self.AssignedGroup)
            return(self.AssignedGroup)


if __name__ == '__main__':
    randomization = Randomize()
    randomization.simple_randomization_ver1()
