# Import package
import random

# Global変数としてassignされたGroupを代入する
# Assigned group is set as global variable

class Randomize (object):
    def simple_randomization_ver1(self):
        if random.random() > 0.5:
            print('Aに割り当てられました')
        else:
            print('Bに割り当てられました')

simple_randomization=Randomize()
simple_randomization.simple_randomization_ver1()