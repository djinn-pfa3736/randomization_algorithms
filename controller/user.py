

# Packaage

import tkinter as tk
import os
import sys

import pdb

# Set Directory
sys.path += [os.path.dirname('../')]
from model import data_manager

dm = data_manager.DataManager()
dm.print_db()


# # Window文字
# root = tk.Tk()
# w = tk.Label(root, text="単純ランダム化プログラム")
# w.pack()

# # ボタン設定
# # button = tk.Button(frame,
# #                    text="Add case"
# #                    command= dm.print_db())
# root.mainloop()
