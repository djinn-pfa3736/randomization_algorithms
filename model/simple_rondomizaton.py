# Import package
import random
import json
# Global変数としてassignされたGroupを代入する
# Assigned group is set as global variable
Groups = ['Treat','Control']
for i in Groups:
    print (i)

class Randomize (object):
    def __init__(self):
        #* define AssinedGroup as global variable
        global AsssinedGroup
    def simple_randomization_ver1(self):
        if random.random() > 0.5:
            print(Groups[0]+'に割り当てられました')
            AssinedGroup = Groups[0]
            print (AssinedGroup)
        else:
            print(Groups[1]+'に割り当てられました')
            AssinedGroup = Groups[1]
            print (AssinedGroup)


randomization = Randomize()
randomization.simple_randomization_ver1()
