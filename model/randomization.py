# Import package
import json
import random
import numpy as np

import json_manager


class Randomize:

    def __init__(self, block_size, a_count, b_count):
        self.block_size = block_size
        self.block_a_count = a_count
        self.block_b_count = b_count

    def simple_randomization(self):
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

    def block_randomization(self):
        self.json_manager = json_manager.JsonManager()
        self.json_dict=self.json_manager.get_json_object()
        # self.get_study_groups = JsonManager()
        # self.Groups = self.get_study_groups.get_var_Groups_ver1()
        # * get random variable 0-1
        if(self.block_a_count + self.block_b_count < self.block_size):
            diff = self.block_a_count - self.block_b_count
            res_size = self.block_size - (self.block_a_count + self.block_b_count)
            if(abs(diff) == res_size):
                if(diff > 0):
                    self.AssignedGroup = self.json_dict['study_groups']['GroupB']
                    print(self.AssignedGroup)
                    self.block_b_count += 1
                    return(self.AssignedGroup)
                else:
                    self.AssignedGroup = self.json_dict['study_groups']['GroupA']
                    print(self.AssignedGroup)
                    self.block_a_count += 1
                    return(self.AssignedGroup)
            else:
                if random.random() > 0.5:
                    self.AssignedGroup = self.json_dict['study_groups']['GroupA']
                    print(self.AssignedGroup)
                    self.block_a_count += 1
                    return(self.AssignedGroup)
                else:
                    self.AssignedGroup = self.json_dict['study_groups']['GroupB']
                    print(self.AssignedGroup)
                    self.block_b_count += 1
                    return(self.AssignedGroup)
        else:
            self.block_size = np.ceil(5*random.random()) * 2
            self.block_a_count = 0
            self.block_b_count = 0

            if random.random() > 0.5:
                self.AssignedGroup = self.json_dict['study_groups']['GroupA']
                print(self.AssignedGroup)
                self.block_a_count += 1
                return(self.AssignedGroup)
            else:
                self.AssignedGroup = self.json_dict['study_groups']['GroupB']
                print(self.AssignedGroup)
                self.block_b_count += 1
                return(self.AssignedGroup)




if __name__ == '__main__':
    randomization = Randomize(10)
    randomization.simple_randomization()
