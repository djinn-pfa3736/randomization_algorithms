import sys
import os
# Set directory
# *  directory is set to as data manager
os.chdir(os.path.dirname(os.path.abspath(__file__)))

sys.path += [os.path.dirname('../')]
sys.path += [os.path.dirname('.')]