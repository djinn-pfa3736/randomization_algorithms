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
#Logging handlar
formatter = '%(levelname)s : %(asctime)s :%(message)s'
logging.basicConfig(level=logging.INFO, format=formatter)

# Set Directory
sys.path += [os.path.dirname('../')]
sys.path += [os.path.dirname('.')]

from model import data_manager

dm = data_manager.DataManager()
dm.print_db()

#pdb.set_trace()

#Window
root = tk.Tk()
root.title (u"単純無作為化")
root.geometry ("600x300")

#Label

Static1 = tk.Label(text=u'単純無作為化を行います')
Static1.place(x=100, y=100)
Static1.pack()


#Entry Box
EditBox_year = tk.Entry(width=10)
EditBox_year.pack()

#Definition functions
def DeleteEntryValue(event):
      #エントリーの中身を削除
  EditBox_year.delete(0, tk.END)
  
#Button
Button_delete = tk.Button(text=u'データ削除')
Button_delete.bind("<Button-1>",DeleteEntryValue) 
#左クリック（<Button-1>）されると，DeleteEntryValue関数を呼び出すようにバインド
Button_delete.pack()



#Get
Value_year = EditBox_year.get
logging.info(msg='Get values from edit box')
root.mainloop()