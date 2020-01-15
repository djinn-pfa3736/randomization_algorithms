#Import packages
import logging
import os
import random

#Class
if __name__ == "__main__":
    class Rondmization:
        def simple_rondomization(self):
            if random.random() > 0.5:
                return('A')
            else:
                return('B')