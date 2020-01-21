# Package
# References
# https://qiita.com/nnahito/items/ad1428a30738b3d93762s



import tkinter as tk
import os
import sys
import datetime

import pdb
import logging

import get_date
# Logging handlar
formatter = '%(levelname)s : %(asctime)s :%(message)s'
logging.basicConfig(level=logging.INFO, format=formatter)

# Set Directory
sys.path += [os.path.dirname('../')]
sys.path += [os.path.dirname('.')]

from model import data_manager
dm = data_manager.DataManager()
dm.print_db()

# pdb.set_trace()
# Time manager

# Function
## Definition functions
def DeleteEntryValue():
      # エントリーの中身を削除
    EditBoxName.delete(0, tk.END)

def AddCase():
    # Get
    Value_Name=EditBox_Name.get
    logging.info(msg='Get Name values from edit box')

tm = get_date.TimeManager()
today = tm.GetDate()

# Window
root = tk.Tk()
root.title(u"Simple randomization")
root.geometry("600x300")

# Frame
# Main frame
main_frm = tk.Frame(root)
main_frm.grid(column=0, row=0, sticky=tk.NSEW, padx=5, pady=10)

# Widgets
LabelName=tk.Label(main_frm, text=u'Name')
EditBoxName=tk.Entry(main_frm, width=10)
ButtonSubmit=tk.Button(text=u'Submit',command=DeleteEntryValue )

# Place
LabelName.grid(column = 0, row = 0)
EditBoxName.grid(column = 1, row = 0)
ButtonSubmit.grid(column = 2, row = 0)


# # Actions
# ButtonSubmit.bind("<Button-1>", DeleteEntryValue)
# ButtonSubmit.pack()
root.mainloop()
