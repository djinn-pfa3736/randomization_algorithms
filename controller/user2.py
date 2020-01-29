# -*- coding: utf-8 -*-

import tkinter as tk
import logging
import sys
import os
from tkinter import messagebox
import tkinter.simpledialog as simpledialog

# Logging handlar
formatter = '%(levelname)s : %(asctime)s :%(message)s'
logging.basicConfig(level=logging.INFO, format=formatter)

# Set Directory
sys.path += [os.path.dirname('../')]
sys.path += [os.path.dirname('.')]
from model import data_manager
from model import get_date

dm = data_manager.DataManager()

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        master.title("Simple randomization")
        master.geometry("350x500")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Pane
        self.pw_main = tk.PanedWindow(self.master, orient='vertical')
        self.pw_main.pack(expand=True, fill=tk.BOTH, side="top")

        self.pw_1 = tk.PanedWindow(self.pw_main, bg="grey", orient='vertical')
        self.pw_main.add(self.pw_1)
        self.pw_2 = tk.PanedWindow(
            self.pw_main, bg="yellow", orient='vertical')
        self.pw_main.add(self.pw_2)
        # Frame
        self.fm_1 = tk.Frame(self.pw_1, bd=2, relief="ridge")
        self.pw_1.add(self.fm_1)
        self.fm_2 = tk.Frame(self.pw_2, bd=2, relief="ridge")
        self.pw_2.add(self.fm_2)
        # Frame top (pw_1)
        # Label "menu"
        self.lb = tk.Label(self.fm_1)
        self.lb["text"] = "Case manager"
        self.lb.pack(side="left")
        self.lb.grid(row=0, column=0, padx=2, pady=2)

        # Bt
        self.bt_add = tk.Button(self.fm_1)
        self.bt_add["text"] = "Add case"
        self.bt_add.grid(row=1, column=0, padx=2, pady=2)
        self.bt_add["command"] = self.AddCase()
    
    # Def
    def AddCase(self, action):
        dm.add_case(action)
        self.res = messagebox.showinfo("Info","New case is now add and assined, successfully.")
        print("showinfo",self.res)
        # self.message_add = tk.Message(self.fm_2)
        # self.message_add["text"]="New case is now add and assined, successfully."
        # self.message_add.pack()
        print("New case is now add and assined, successfully.")
        logging.info (msg='Show data base from GUI')

    #     self.en = tk.Entry(self)
    #     self.en.focus_set()
    #     self.bt=tk.Button(self)
    #     self.bt["text"]="ボタン"
    #     self.bt["command"]=self.print_txtval
    #     self.bt.pack(side="bottom")
    # def print_txtval(self):
    #     val_en=self.en.get()
    #     print(val_en)


root = tk.Tk()
app = Application(master=root)
app.mainloop()
