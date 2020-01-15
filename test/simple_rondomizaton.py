# Import package
import random

# Global変数としてassignされたGroupを代入する
# Assigned group is set as global variable


class Randomize (object):
    def __init__(self):
        #* define AssinedGroup as global variable
        global AsssinedGroup
    def simple_randomization_ver1(self):
        if random.random() > 0.5:
            print('Aに割り当てられました')
            AssinedGroup = 'A'
            print (AssinedGroup)
        else:
            print('Bに割り当てられました')
            AssinedGroup = 'B'
            print (AssinedGroup)


randomization = Randomize()
randomization.simple_randomization_ver1()
