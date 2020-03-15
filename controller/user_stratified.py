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
import sqlite3
import preference
import json
import shlex
import shutil
import subprocess
import datetime

# Logging handlar
formatter = '%(levelname)s : %(asctime)s :%(message)s'
logging.basicConfig(level=logging.INFO, format=formatter)

# Set Directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path += [os.path.dirname('../')]
# logging.info(msg=sys.path)
sys.path += [os.path.dirname('.')]
# logging.info(msg=sys.path)
# Import packages from model
from model import data_manager, get_date, json_manager

"""
# Make instances
dm = data_manager.DataManager()
json_manager = json_manager.JsonManager()
json_dict = json_manager.get_json_object()

# Data from Json
Contact = json_dict['study_preferences']['contact']
Number = int(json_dict['study_preferences']['number'])
Randomization = json_dict['study_preferences']['randomization']
PI = json_dict['study_preferences']['principal investigator']
Trial = json_dict['study_preferences']['trial']
Institution = json_dict['study_preferences']['institution']
"""

# Definition
"""
def get_progress_bar_length():
    NCase = dm.get_row_number()
    if NCase/Number > 1:
        return(1)
    else:
        return(NCase/Number)
"""

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        # Definition of variales
        self.dm = data_manager.DataManager()

        self.json_manager = json_manager.JsonManager()
        self.json_dict = self.json_manager.get_json_object()

        # Data from Json
        self.Contact = self.json_dict['study_preferences']['contact']
        self.Number = int(self.json_dict['study_preferences']['number'])
        self.Randomization = self.json_dict['study_preferences']['randomization']
        self.PI = self.json_dict['study_preferences']['principal investigator']
        self.Trial = self.json_dict['study_preferences']['trial']
        self.Institution = self.json_dict['study_preferences']['institution']

        master.title(self.Randomization)
        master.geometry("500x600")
        self.pack()
        self.create_widgets()

    # * Basic function
    # * Get  database into tree view
        if os.path.exists ("../data/patient.db") == False:
            dm.connect()
        else:
            pass
    def get_db_into_tree(self):
        self.Conn = sqlite3.connect("../data/patient.db")
        logging.info(msg='Connecting with patient.db')
        # Sql query
        self.sql = 'SELECT * FROM assignment ORDER BY id DESC'
        for rows in self.Conn.execute(self.sql):
            self.tree.insert("", "end", values=rows)
        self.Conn.close()

    # * Delete all rows in tree view
    def delete_all_tree(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

    def get_progress_bar_length(self):
        NCase = self.dm.get_row_number()
        if NCase/self.Number > 1:
            return(1)
        else:
            return(NCase/self.Number)

    def create_widgets(self):

        self.pw_main = tk.PanedWindow(self.master, orient='vertical')

        self.pw_main.pack(expand=True, fill=tk.BOTH, side="top")
        self.pw_header = tk.PanedWindow(
            self.pw_main, bg="grey", orient='vertical')
        self.pw_main.add(self.pw_header)
        self.pw_prs_bar = tk.PanedWindow(
            self.pw_main, bg="grey", orient='vertical')
        self.pw_main.add(self.pw_prs_bar)
        self.pw_1 = tk.PanedWindow(self.pw_main, bg="grey", orient='vertical')
        self.pw_main.add(self.pw_1)
        self.pw_2 = tk.PanedWindow(self.pw_main, bg="grey", orient='vertical')
        self.pw_main.add(self.pw_2)

        # Frame
        # fm_header containing study info
        self.fm_header = tk.LabelFrame(
            self.pw_header, bd=2, relief='ridge', text='Information')
        self.pw_header.add(self.fm_header)
        self.fm_prs_bar = tk.Frame(self.pw_prs_bar, bd=0, relief="flat")
        self.pw_prs_bar.add(self.fm_prs_bar)
        # fm_1 containing bt.add
        self.fm_1 = tk.Frame(self.pw_1, bd=0, relief="flat")
        self.pw_1.add(self.fm_1)
        # fm_2 containing export
        self.fm_2 = tk.Frame(self.pw_1, bd=0, relief="flat")
        self.pw_1.add(self.fm_2)
        # fm_3 containing treeview
        self.fm_3 = tk.Frame(self.pw_2, bd=0, relief="flat")
        self.fm_3.propagate(True)
        self.pw_2.add(self.fm_3)

        # Header
        self.lb_header_trial = tk.Label(self.fm_header)
        self.lb_header_trial["text"] = "Trial: " + self.Trial
        self.lb_header_trial.grid(row=0, column=0, padx=2, pady=2, sticky=tk.W)

        # self.lb_header_pi = tk.Label(self.fm_header)
        # self.lb_header_pi ["text"]= "PI: "+ PI +", Contact: " + Contact
        # self.lb_header_pi.grid(row= 1, column= 0, padx= 2, pady = 2, sticky =tk.W)

        self.lb_header_n = tk.Label(self.fm_header)
        self.lb_header_n["text"] = "Target sample size: " + str(self.Number)
        self.lb_header_n.grid(row=1, column=0, padx=2, pady=2, sticky=tk.W)

        # Progress bar in fm_header
        self.lb_header_zero = tk.Label(self.fm_prs_bar)
        self.lb_header_zero["text"] = "0"
        self.lb_header_zero.grid(
            row=0, column=0, padx=2, pady=2, sticky=tk.W + tk.E)
        # Widgets
        # Menubar
        self.menu_bar = tk.Menu(self)  # Menuクラスからmenu_barインスタンスを生成

        self.file_menu = tk.Menu(self.menu_bar)  # メニューバーに大項目「ファイル」を生成
        self.menu_bar.add_cascade(
            label="File", menu=self.file_menu)  # 大項目「ファイル」を配置
        self.file_menu.add_command(label="Create New Trial", command=self.MenuPreference)
        self.file_menu.add_command(label="Open Trial")  # 大項目「ファイル」に小項目「開く」を追加
        self.file_menu.add_separator()  # セパレーターを追加
        self.file_menu.add_command(label="Quit")

        self.edit_menu = tk.Menu(self.menu_bar)  # メニューバーに大項目「ファイル」を生成
        self.menu_bar.add_cascade(
            label="Edit", menu=self.edit_menu)  # 大項目「Edit」を配置
        self.edit_menu.add_command(label="Create New Stratification", command=self.MenuPreference)

        root.config(menu=self.menu_bar)  # メニューバーの配置

        def ProgressBar(self):
            self.ProgressBarLength = self.get_progress_bar_length()

            logging.info(msg="Progressbar"+str(self.ProgressBarLength))
            self.s = ttk.Style()
            self.s.theme_use('clam')
            if self.ProgressBarLength < 0.3:
                self.s.configure("Horizontal.TProgressbar",
                                 foreground='deeppink', background='deeppink')
            elif (self.ProgressBarLength >= 0.3 and self.ProgressBarLength < 0.6):
                self.s.configure("Horizontal.TProgressbar",
                                 foreground='gold', background='gold')
            elif (self.ProgressBarLength >= 0.6 and self.ProgressBarLength < 0.9):
                self.s.configure("Horizontal.TProgressbar",
                                 foreground='dodgerblue', background='dodgerblue')
            elif (self.ProgressBarLength >= 0.9 and self.ProgressBarLength < 1):
                self.s.configure("Horizontal.TProgressbar",
                                 foreground='royalblue', background='royalblue')
            else:
                self.s.configure("Horizontal.TProgressbar",
                                 foreground='slategray', background='slategray')
            # #Progressbar
            self.prs_bar = ttk.Progressbar(
                self.fm_prs_bar, orient='horizontal', length=400, mode='determinate', style="Horizontal.TProgressbar")
            self.prs_bar.configure(maximum=1, value=self.ProgressBarLength)
            self.prs_bar.grid(row=1, column=1, padx=2, pady=2,
                              sticky=(tk.N, tk.E, tk.S, tk.W))

            self.lb_header_max = tk.Label(self.fm_prs_bar)
            self.lb_header_max["text"] = str(self.Number)
            self.lb_header_max.grid(
                row=0, column=2, padx=2, pady=2, sticky=tk.W + tk.E)

        ProgressBar(self)

        # Button
        # add case
        self.bt_add = tk.Button(self.fm_1)
        self.bt_add["text"] = "Add"
        self.bt_add.grid(row=1, column=3, padx=2, pady=2, sticky=tk.W+tk.E)
        self.bt_add["command"] = self.AddCase

        # Spinbox institution
        self.sptxt = tk.StringVar()
        self.List_in = self.Institution
        self.spbox_in = tk.Spinbox(
            self.fm_1, width=10, textvariable=self.sptxt, value=self.List_in)
        self.spbox_in.grid(row=1, column=0, padx=2, pady=2, sticky=tk.W+tk.E)
        self.lb_spbox_in = tk.Label(self.fm_1)
        self.lb_spbox_in["text"] = "Institution"
        self.lb_spbox_in.grid(row=0, column=0, padx=2, pady=2)

        # entrybox_institutionalid(inid)
        self.en_inid = tk.Entry(self.fm_1, width=10)
        self.en_inid.grid(row=1, column=1, padx=2, pady=2, sticky=tk.W+tk.E)
        self.en_inid.insert(tk.END, '00000')
        self.lb_en_inid = tk.Label(self.fm_1)
        self.lb_en_inid["text"] = "ID"
        self.lb_en_inid.grid(row=0, column=1, padx=2, pady=2)

        # entrybox_name
        self.en_name = tk.Entry(self.fm_1, width=10)
        self.en_name.grid(row=1, column=2, padx=2, pady=2, sticky=tk.W+tk.E)
        self.en_name.insert(tk.END, 'Name')
        self.lb_en_name = tk.Label(self.fm_1)
        self.lb_en_name["text"] = "Name"
        self.lb_en_name.grid(row=0, column=2, padx=2, pady=2)

        # export
        self.bt_export = tk.Button(self.fm_2)
        self.bt_export["text"] = "Export"
        self.bt_export.grid(row=2, column=0, padx=2, pady=2, sticky=tk.W+tk.E)
        self.bt_export["command"] = self.Export

        # Tree view
        self.tree = ttk.Treeview(self.fm_3, height=20)
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

        self.tree.pack(fill=tk.BOTH)

        self.get_db_into_tree()

    # Input of information of new traial
    def MenuPreference(self):
        # Setup for top level
        self.new_trial_window = tk.Toplevel(master=self.master)
        self.new_trial_window.title("New Trial Setup")
        self.new_trial_window.geometry("500x700")

        # Setup paned window
        self.pw_new_trial = tk.PanedWindow(
            self.new_trial_window, bg="grey", orient='vertical')
        self.pw_new_trial.pack(expand=True, fill=tk.BOTH)

        # Setup frame
        self.fm_new_trial = tk.Frame(self.pw_new_trial, bd=2)
        self.pw_new_trial.add(self.fm_new_trial)

        """
        Notice:
        There are 3 columns in this window.
        First column : Labels for Input
        Second column: Input boxes
        Third column : Buttons for input
        """

        """
        Labels for first column
        """
        self.lb_trial = tk.Label(self.fm_new_trial)
        self.lb_trial["text"] = "Trial"
        self.lb_trial.grid(row=0, column=0, padx=2, pady=2, sticky=tk.E)

        self.lb_pi = tk.Label(self.fm_new_trial)
        self.lb_pi["text"] = "Primary Investigator"
        self.lb_pi.grid(row=1, column=0, padx=2, pady=2, sticky=tk.E)

        self.lb_contact = tk.Label(self.fm_new_trial)
        self.lb_contact["text"] = "Contact"
        self.lb_contact.grid(row=2, column=0, padx=2, pady=2, sticky=tk.E)

        self.lb_groupa = tk.Label(self.fm_new_trial)
        self.lb_groupa["text"] = "Group A"
        self.lb_groupa.grid(row=3, column=0, padx=2, pady=2, sticky=tk.E)

        self.lb_groupb = tk.Label(self.fm_new_trial)
        self.lb_groupb["text"] = "Group B"
        self.lb_groupb.grid(row=4, column=0, padx=2, pady=2, sticky=tk.E)

        self.lb_sample_size = tk.Label(self.fm_new_trial)
        self.lb_sample_size["text"] = "Sample size (> 5)"
        self.lb_sample_size.grid(row=6, column=0, padx=2, pady=2, sticky=tk.E)

        self.lb_list_box = tk.Label(self.fm_new_trial)
        self.lb_list_box["text"] = 'Institution'
        self.lb_list_box.grid(row=7, column=0, padx=2, pady=2, sticky=tk.E)

        self.lb_list_box = tk.Label(self.fm_new_trial)
        self.lb_list_box["text"] = 'Institution input'
        self.lb_list_box.grid(row=8, column=0, padx=2, pady=2, sticky=tk.E)

        self.lb_factor_box = tk.Label(self.fm_new_trial)
        self.lb_factor_box["text"] = 'Factors'
        self.lb_factor_box.grid(row=9, column=0, padx=2, pady=2, sticky=tk.E)

        self.lb_factor_input_lb = tk.Label(self.fm_new_trial)
        self.lb_factor_input_lb["text"] = 'Factor input'
        self.lb_factor_input_lb.grid(row=10, column=0, padx=2, pady=2, sticky=tk.E)

        """
        Second column for entry box
        """
        self.sample_institution = ['Hospital A', 'Hospital B', 'Hospital C']
        self.txt = tk.StringVar(value=self.sample_institution)
        self.lsbx_in = tk.Listbox(
            self.fm_new_trial, listvariable=self.txt, width=15, height=5)

        self.lsbx_in.grid(row=7, column=1, padx=2, pady=2, sticky=tk.W)

        # Entry box for institution list box
        self.en_in_plus = tk.Entry(self.fm_new_trial, width = 15)
        self.en_in_plus.grid(row=8, column=1, padx=2, pady=2, sticky=tk.W)

        # Entry boxes
        self.en_trial = tk.Entry(self.fm_new_trial, width=15)
        self.en_trial.grid(row=0, column=1, padx=2, pady=2, sticky=tk.W)
        self.en_trial.insert(tk.END, 'Trial Name')

        self.en_pi = tk.Entry(self.fm_new_trial, width=15)
        self.en_pi.grid(row=1, column=1, padx=2, pady=2, sticky=tk.W)
        self.en_pi.insert(tk.END, 'Name of PI')

        self.en_contact = tk.Entry(self.fm_new_trial, width=15)
        self.en_contact.grid(row=2, column=1, padx=2, pady=2, sticky=tk.W)
        self.en_contact.insert(tk.END, 'Contact')

        self.en_groupa = tk.Entry(self.fm_new_trial, width=15)
        self.en_groupa.grid(row=3, column=1, padx=2, pady=2, sticky=tk.W)
        self.en_groupa.insert(tk.END, 'Control group')

        self.en_groupb = tk.Entry(self.fm_new_trial, width=15)
        self.en_groupb.grid(row=4, column=1, padx=2, pady=2, sticky=tk.W)
        self.en_groupb.insert(tk.END, 'Treatment group')

        self.en_sample_size = tk.Entry(
            self.fm_new_trial, width=15, textvariable=tk.IntVar(value=100))
        self.en_sample_size.grid(row=6, column=1, padx=2, pady=2, sticky=tk.W)

        # Institution list box
        self.sample_institution = ['Hospital A', 'Hospital B', 'Hospital C']
        self.txt = tk.StringVar(value=self.sample_institution)
        self.lsbx_inst = tk.Listbox(
            self.fm_new_trial, listvariable=self.txt, width=15, height=5)
        self.lsbx_inst.grid(row=7, column=1, padx=2, pady=2, sticky=tk.W)

        # Entry box for institution list box
        self.en_inst_add = tk.Entry(self.fm_new_trial, width = 15)
        self.en_inst_add.grid(row=8, column=1, padx=2, pady=2, sticky=tk.W)

        # Factor list box
        self.sample_factors = ['Factor 1', 'Factor 2', 'Factor 3']
        self.txt = tk.StringVar(value=self.sample_factors)
        self.lsbx_fact = tk.Listbox(
            self.fm_new_trial, listvariable=self.txt, width=15, height=5)
        self.lsbx_fact.grid(row=9, column=1, padx=2, pady=2, sticky=tk.W)

        # Entry box for factor list box
        self.en_fact_add = tk.Entry(self.fm_new_trial, width = 15)
        self.en_fact_add.grid(row=10, column=1, padx=2, pady=2, sticky=tk.W)

        """
        Third column for buttons
        """
        self.bt_delete_inst = tk.Button(self.fm_new_trial, command=self.DeleteInstitute)
        self.bt_delete_inst["text"] = "Delete Institution"
        self.bt_delete_inst.grid(row=7, column=3, padx=2, pady=2, sticky=tk.W+tk.S)

        self.bt_add_inst = tk.Button(self.fm_new_trial, command=self.AddInstitute)
        self.bt_add_inst["text"] = "Add Institution"
        self.bt_add_inst.grid(row=8, column=3, padx=2, pady=2, sticky=tk.W)

        self.bt_delete_fact = tk.Button(self.fm_new_trial, command=self.DeleteFactor)
        self.bt_delete_fact["text"] = "Delete Factor"
        self.bt_delete_fact.grid(row=9, column=3, padx=2, pady=2, sticky=tk.W+tk.S)

        self.bt_add_fact = tk.Button(self.fm_new_trial, command=self.AddFactor)
        self.bt_add_fact["text"] = "Add Factor"
        self.bt_add_fact.grid(row=10, column=3, padx=2, pady=2, sticky=tk.W)


        """
        Buttons in the bottom of preference window.
        """
        self.bt_save_new_trial = tk.Button(self.fm_new_trial, command=self.SaveNewTrial)
        self.bt_save_new_trial["text"] = 'Save New Trial'
        self.bt_save_new_trial.grid(
            row=15, column=3, padx=2, pady=2, sticky=tk.W)
        self.bt_cancel_new_trial = tk.Button(self.fm_new_trial)
        self.bt_cancel_new_trial["text"] = 'Cancel'
        self.bt_cancel_new_trial["command"] = self.CancelNewTrial
        self.bt_cancel_new_trial.grid(
            row=15, column=4, padx=2, pady=2, sticky=tk.W)

    def AddInstitute(self):
        new_institute = self.en_inst_add.get()
        self.lsbx_inst.insert(0, new_institute)

    def DeleteInstitute(self):
        selected_idx = self.lsbx_inst.curselection()
        # print(selected_idx)
        self.lsbx_inst.delete(selected_idx[0])

    def AddFactor(self):
        new_factor = self.en_fact_add.get()
        self.lsbx_fact.insert(0, new_factor)

    def DeleteFactor(self):
        selected_idx = self.lsbx_fact.curselection()
        # print(selected_idx)
        self.lsbx_fact.delete(selected_idx[0])


    def SaveNewTrial(self):
        self.txt_new_trial_name = self.en_trial.get()
        self.txt_new_pi = self.en_pi.get()
        self.txt_new_contact = self.en_contact.get()
        self.txt_groupa = self.en_groupa.get()
        self.txt_groupb = self.en_groupb.get()
        logging.info(msg="The data is now gotten!")

        ret = messagebox.askyesno('Confirm', 'Are you sure about deleting current project and create new one?')
        if ret == True:

            # arg0 = '../data/study_data.json_' + datetime.datetime.now().strftime("%Y-%m-%d")
            # arg1 = '../data/patient.db_' + datetime.datetime.now().strftime("%Y-%m-%d")

            # # print(arg)
            # shutil.copy('../data/study_data.json', arg0)
            # shutil.copy('../data/patient.db', arg1)

            os.remove('../data/patient.db')
            subprocess.call(shlex.split("touch ../data/patient.db"))

            with open('../data/study_data.json',"w") as self.f:
                dict = {"study_groups": {"GroupA": self.en_groupa.get(), "GroupB": self.en_groupb.get()},
                        "study_preferences": {"trial": self.en_trial.get(),
                        "principal investigator": self.en_pi.get(),
                        "contact": self.en_contact.get(),
                        "number": self.en_samplesize.get(),
                        "randomization": self.en_method.get(),
                        "institution": self.lsbx_in.get(0, tk.END)}}
                print(dict)
                json.dump(dict, self.f)
            self.new_trial_window.destroy()

            json_dict = self.json_manager.get_json_object()

            # Data from Json
            Contact = json_dict['study_preferences']['contact']
            Number = int(json_dict['study_preferences']['number'])
            Randomization = json_dict['study_preferences']['randomization']
            PI = json_dict['study_preferences']['principal investigator']
            Trial = json_dict['study_preferences']['trial']
            Institution = json_dict['study_preferences']['institution']

            self.List_in = Institution
            self.spbox_in["value"] = self.List_in

            #ANCHOR reopen_main_window

            self.delete_all_tree()
            logging.info(msg='do the create widgets')
            self.lb_header_trial.grid_remove()
            self.lb_header_trial = tk.Label(self.fm_header)
            self.lb_header_trial["text"] = "Trial: " + Trial
            self.lb_header_trial.grid(row=0, column=0, padx=2, pady=2, sticky=tk.W)

            self.lb_header_n.grid_remove()
            self.lb_header_n = tk.Label(self.fm_header)
            self.lb_header_n["text"] = "Target sample size: " + str(Number)
            self.lb_header_n.grid(row=1, column=0, padx=2, pady=2, sticky=tk.W)

            logging.info(msg='end the create widgets')
            self.dm.reconnect()

    def CancelNewTrial(self):
        self.new_trial_window.destroy()

    def AddCase(self):
        self.ProgressBarLength = self.get_progress_bar_length()
        if self.ProgressBarLength >= 1:
            self.mes_warning_number = messagebox.showwarning(
                "Warning", "The enrollment is now over.")
            return
        else:
            # * Get text "self,HospitalName=None, HospitalID=None, PatientName = None"

            self.txt_HospitalName = self.spbox_in.get()
            self.txt_HospitalID = self.en_inid.get()
            self.txt_PatientName = self.en_name.get()
            print(self.txt_PatientName)
            logging.info(msg='Get value from entrybox')

            if (not self.txt_HospitalName or not self.txt_HospitalID or not self.txt_PatientName):
                self.mes_blank = messagebox.showwarning(
                    "Warning", "Please fill Institution, ID, and Name.")
                print(self.mes_blank)

                return
            else:

                # Message box
                self.mes_add_confirmation = messagebox.askquestion("Confirmation", "Do you want to enroll a new case?\
                                                    This operation cannot be undone.", icon='warning')
                print(self.mes_add_confirmation)
                if self.mes_add_confirmation == 'yes':
                    self.dm.add_case(HospitalName=self.txt_HospitalName,
                                HospitalID=self.txt_HospitalID, PatientName=self.txt_PatientName, Method=self.Randomization)
                    # dm.print_db()
                    self.mes_success = messagebox.showinfo(
                        "Info", "New case is now added and assined, successfully.")
                    print("showinfo", self.mes_success)

                    self.delete_all_tree()
                    self.get_db_into_tree()

                    # NOTE Progress bar is showing by rewriti the code of Progress bar.
                    self.ProgressBarLength = self.get_progress_bar_length()

                    logging.info(msg="Progressbar"+str(self.ProgressBarLength))
                    self.s = ttk.Style()
                    self.s.theme_use('clam')
                    if self.ProgressBarLength < 0.3:
                        self.s.configure(
                            "Horizontal.TProgressbar", foreground='deeppink', background='deeppink')
                    elif (self.ProgressBarLength >= 0.3 and self.ProgressBarLength < 0.6):
                        self.s.configure(
                            "Horizontal.TProgressbar", foreground='gold', background='gold')
                    elif (self.ProgressBarLength >= 0.6 and self.ProgressBarLength < 0.9):
                        self.s.configure(
                            "Horizontal.TProgressbar", foreground='dodgerblue', background='dodgerblue')
                    elif (self.ProgressBarLength >= 0.9 and self.ProgressBarLength < 1):
                        self.s.configure(
                            "Horizontal.TProgressbar", foreground='royalblue', background='royalblue')
                    else:
                        self.s.configure(
                            "Horizontal.TProgressbar", foreground='slategray', background='slategray')
                    # #Progressbar
                    self.prs_bar = ttk.Progressbar(
                        self.fm_prs_bar, orient='horizontal', length=400, mode='determinate', style="Horizontal.TProgressbar")
                    self.prs_bar.configure(
                        maximum=1, value=self.ProgressBarLength)
                    self.prs_bar.grid(row=1, column=1, padx=2,
                                      pady=2, sticky=(tk.N, tk.E, tk.S, tk.W))

                    self.lb_header_max = tk.Label(self.fm_prs_bar)
                    self.lb_header_max["text"] = str(self.Number)
                    self.lb_header_max.grid(
                        row=0, column=2, padx=2, pady=2, sticky=tk.W + tk.E)
                else:
                    return

            logging.info(msg='Add data base from GUI')

    def Export(self):
        logging.info(msg='Launch Export from GUI')
        #self.dirpath = filedialog.askdirectory()
        fTyp = [('Export', '*.csv')]
        self.dirpath = filedialog.asksaveasfilename(filetypes=fTyp)
        dm.get_db_for_csv(dirpath_csv=self.dirpath)
        logging.info(msg='Export output.csv from GUI')


root = tk.Tk()
app = Application(master=root)

app.mainloop()
