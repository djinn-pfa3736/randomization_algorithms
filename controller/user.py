# -*- coding: utf-8 -*-
import csv
import itertools
import logging
import os
import sys
import tkinter as tk
import tkinter.simpledialog as simpledialog
from tkinter import filedialog
import tkinter.ttk as ttk
from tkinter import messagebox


# Logging handlar
formatter = '%(levelname)s : %(asctime)s :%(message)s'
logging.basicConfig(level=logging.INFO, format=formatter)

# Set Directory
sys.path += [os.path.dirname('../')]
logging.info(msg=sys.path)
sys.path += [os.path.dirname('.')]
logging.info(msg=sys.path)
from model import data_manager, get_date

dm = data_manager.DataManager()
Database = dm.get_db_for_tree()

if __name__ == '__main__':
    Database = dm.get_db_for_tree()
    print(type(Database))


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        master.title("Simple randomization")
        master.geometry("500x500")
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
        # add case
        self.bt_add = tk.Button(self.fm_1)
        self.bt_add["text"] = "New case"
        self.bt_add.grid(row=1, column=0, padx=2, pady=2)
        self.bt_add["command"] = self.AddCase

        # export
        self.bt_export = tk.Button(self.fm_1)
        self.bt_export["text"] = "Export"
        self.bt_export.grid(row=2, column=0, padx=2, pady=2)
        self.bt_export["command"] = self.Export

        # Tree view
        self.tree = ttk.Treeview(self.fm_2)
        self.tree["column"] = (1, 2, 3, 4, 5, 6)
        self.tree["show"] = "headings"

        self.tree.column(1, width=50)
        self.tree.column(2, width=75)
        self.tree.column(3, width=75)
        self.tree.column(4, width=75)
        self.tree.column(5, width=75)
        self.tree.column(6, width=75)

        self.tree.heading(1, text="Study ID")
        self.tree.heading(2, text="Date")
        self.tree.heading(3, text="Institution")
        self.tree.heading(4, text="ID")
        self.tree.heading(5, text="Name")
        self.tree.heading(6, text="Assigned")

        self.tree.grid(row=0, column=0, padx=2, pady=2)

        self.List = dm.get_db_for_tree()

        for row_data in enumerate(self.List):
            logging.info(msg="Print in iterator")
            print(srow_data)
            self.tree.insert("", "end", values=row_data)
            logging.info(msg="Print in iterator end")

    # Def
    def AddCase(self):

        self.res_add1 = messagebox.askquestion("Confirmation", "Do you want to enroll a new case?\
                                               This operation cannot be undone.", icon='warning')
        print(self.res_add1)
        if self.res_add1 == 'yes':
            dm.add_case()
            dm.print_db()
            self.res_add2 = messagebox.showinfo(
                "Info", "New case is now added and assined, successfully.")
            print("showinfo", self.res_add2)
        else:
            return

        logging.info(msg='Add data base from GUI')

    def Export(self): 
        logging.info(msg='Launch Export from GUI')
        #self.dirpath = filedialog.askdirectory()
        fTyp=[('Export','*.csv')]
        self.dirpath=filedialog.asksaveasfilename(filetypes=fTyp)
        dm.get_db_for_csv(dirpath_csv=self.dirpath)
        logging.info(msg='Export output.csv from GUI')

root = tk.Tk()
app = Application(master=root)
app.mainloop()
