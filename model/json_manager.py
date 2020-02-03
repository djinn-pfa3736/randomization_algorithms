# * Packages
import json
import os
import sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))

sys.path += [os.path.dirname('../')]
sys.path += [os.path.dirname('.')]


class JsonManager(object):
    def get_json_object(self):
        with open('../data/test_study_data.json', 'r') as self.f:
            self.json_dict = json.load(self.f)
            return self.json_dict
            

if __name__ == '__main__':
    json_manager = JsonManager()
    json_dict=json_manager.get_json_object()
    print(json_dict)
    print(json_dict['study_groups']['GroupA'])
    print(json_dict['study_groups']['GroupB'])