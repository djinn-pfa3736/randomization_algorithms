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
from tkinter import ttk as ttk

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

# Make instances
dm = data_manager.DataManager()
json_manager = json_manager.JsonManager()
json_dict=json_manager.get_json_object()

Contact = json_dict['study_preferences']['contact']

Number = json_dict['study_preferences']['number']
Rondomization =json_dict['study_preferences']['randomization']
PI = json_dict['study_preferences']['principal investigator']
Trial =json_dict['study_preferences']['trial']
Institution = json_dict['study_preferences']['institution']
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        master.title(Rondomization)
        master.geometry("500x600")
        self.pack()
        self.create_widgets()
    # * Basic function
    ## * Get  database into tree view
    def get_db_into_tree(self):
        self.Conn = sqlite3.connect("../data/patient.db")
        logging.info(msg='Connecting with patient.db')
        #Sql query
        self.sql = 'SELECT * FROM assignment ORDER BY id DESC'
        for rows in self.Conn.execute(self.sql):
            self.tree.insert("","end",values= rows)
        self.Conn.close()
    ## * Delete all rows in tree view
    def delete_all_tree (self):
        for row in self.tree.get_children():
                self.tree.delete(row)
    def create_widgets(self):
        # Pane
        self.pw_main = tk.PanedWindow(self.master, orient='vertical')
        
        self.pw_main.pack(expand=True, fill=tk.BOTH, side="top")
        self.pw_header = tk.PanedWindow(self.pw_main, bg = "grey", orient = 'vertical')
        self.pw_main.add(self.pw_header)
        self.pw_prs_bar = tk.PanedWindow(self.pw_main, bg = "grey", orient = 'vertical')
        self.pw_main.add(self.pw_prs_bar)
        self.pw_1 = tk.PanedWindow(self.pw_main, bg="grey", orient='vertical')
        self.pw_main.add(self.pw_1)
        self.pw_2 = tk.PanedWindow(
            self.pw_main, bg="grey", orient='vertical')
        self.pw_main.add(self.pw_2)
        
        
        # Frame
        # fm_header containing study info
        self.fm_header = tk.LabelFrame(self.pw_header, bd = 2 , relief = 'ridge', text='Information')
        self.pw_header.add (self.fm_header)
        self.fm_prs_bar = tk.Frame(self.pw_prs_bar, bd=0, relief="flat")
        self.pw_prs_bar.add(self.fm_prs_bar)
        ## fm_1 containing bt.add 
        self.fm_1 = tk.Frame(self.pw_1, bd=0, relief="flat")
        self.pw_1.add(self.fm_1)
        ## fm_2 containing export
        self.fm_2 = tk.Frame(self.pw_1, bd =0, relief= "flat")
        self.pw_1.add(self.fm_2)
        ## fm_3 containing treeview
        self.fm_3 = tk.Frame(self.pw_2, bd=0, relief="flat")
        self.fm_3.propagate(True)
        self.pw_2.add(self.fm_3)
        
    
        #Header
        self.lb_header_trial = tk.Label(self.fm_header)
        self.lb_header_trial ["text"]= "Trial: "+Trial
        self.lb_header_trial.grid(row= 0, column= 0, padx= 2, pady = 2, sticky =tk.W)
        
        # self.lb_header_pi = tk.Label(self.fm_header)
        # self.lb_header_pi ["text"]= "PI: "+ PI +", Contact: " + Contact
        # self.lb_header_pi.grid(row= 1, column= 0, padx= 2, pady = 2, sticky =tk.W)
        
        self.lb_header_n = tk.Label(self.fm_header)
        self.lb_header_n ["text"]= "Target sample size: " + str(Number)
        self.lb_header_n.grid(row= 1, column= 0, padx= 2, pady = 2, sticky =tk.W)
        
        #Progress bar in fm_header
        self.lb_header_zero = tk.Label(self.fm_prs_bar)
        self.lb_header_zero ["text"]= "0"
        self.lb_header_zero.grid(row= 0, column= 0, padx= 2, pady = 2, sticky =tk.W + tk.E)
        
        
        self.prs_bar=ttk.Progressbar(self.fm_prs_bar, orient= 'horizontal', length= 400, mode='determinate')
        self.prs_bar.grid(row= 1, column= 1, padx= 2, pady = 2, sticky =tk.W + tk.E)
        
        
        self.lb_header_max = tk.Label(self.fm_prs_bar)
        self.lb_header_max ["text"]= str(Number)
        self.lb_header_max.grid(row=0 , column= 2, padx= 2, pady = 2, sticky =tk.W + tk.E)
        
        

        # Bt
        # add case
        self.bt_add = tk.Button(self.fm_1)
        self.bt_add["text"] = "Add"
        self.bt_add.grid(row=1, column=3, padx=2, pady=2, sticky=tk.W+tk.E)
        self.bt_add["command"] = self.AddCase
        # spinbox_institution
        self.sptxt = tk.StringVar()
        self.List_in = Institution
        self.spbox_in = tk.Spinbox(self.fm_1,width = 10,textvariable=self.sptxt, value = self.List_in)
        self.spbox_in.grid (row= 1, column= 0, padx= 2, pady = 2, sticky =tk.W+tk.E)
        self.lb_spbox_in = tk.Label (self.fm_1)
        self.lb_spbox_in["text"]= "Institution"
        self.lb_spbox_in.grid(row = 0, column = 0, padx = 2, pady =2)
        
        
        # entrybox_institutionalid(inid)
        self.en_inid = tk.Entry(self.fm_1, width = 10)
        self.en_inid.grid(row= 1, column= 1, padx= 2, pady = 2, sticky =tk.W+tk.E)
        self.en_inid.insert(tk.END, '00000')
        self.lb_en_inid = tk.Label (self.fm_1)
        self.lb_en_inid["text"]= "ID"
        self.lb_en_inid.grid(row = 0, column = 1, padx = 2, pady =2)
        
        # entrybox_name
        self.en_name = tk.Entry(self.fm_1, width = 10)
        self.en_name.grid(row= 1, column= 2, padx= 2, pady = 2, sticky =tk.W+tk.E)
        self.en_name.insert(tk.END, 'Name')
        self.lb_en_name = tk.Label (self.fm_1)
        self.lb_en_name["text"]= "Name"
        self.lb_en_name.grid(row = 0, column = 2, padx = 2, pady =2)
        
        # export
        self.bt_export = tk.Button(self.fm_2)
        self.bt_export["text"] = "Export"
        self.bt_export.grid(row=2, column=0, padx=2, pady=2, sticky=tk.W+tk.E)
        self.bt_export["command"] = self.Export

        # Tree view
        self.tree = ttk.Treeview(self.fm_3,height = 20)
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

        # self.Conn = sqlite3.connect("../data/patient.db")
        # logging.info(msg='Connecting with patient.db')
        # #Sql query
        # self.sql = 'SELECT * FROM assignment ORDER BY id DESC'
        # for rows in self.Conn.execute(self.sql):
        #     self.tree.insert("","end",values= rows)
        # self.Conn.close()

    # Def
    def AddCase(self):
        
        #* Get text "self,HospitalName=None, HospitalID=None, PatientName = None"
        
        self.txt_HospitalName= self.spbox_in.get()
        self.txt_HospitalID= self.en_inid.get()
        self.txt_PatientName= self.en_name.get()
        print(self.txt_PatientName)
        logging.info(msg = 'Get value from entrybox')
        
        if (not self.txt_HospitalName or not self.txt_HospitalID or not self.txt_PatientName):
            self.mes_blank = messagebox.showwarning("Warning", "Please fill Institution, ID, and Name.")
            print(self.mes_blank)
            
            return
        else:
       
            #Message box
            self.mes_add_confirmation = messagebox.askquestion("Confirmation", "Do you want to enroll a new case?\
                                                This operation cannot be undone.", icon='warning')
            print(self.mes_add_confirmation)
            if self.mes_add_confirmation == 'yes':
                dm.add_case(HospitalName=self.txt_HospitalName, HospitalID=self.txt_HospitalID, PatientName=self.txt_PatientName)
                #dm.print_db()
                self.mes_success = messagebox.showinfo(
                    "Info", "New case is now added and assined, successfully.")
                print("showinfo", self.mes_success)
                
                self.delete_all_tree ()
                self.get_db_into_tree()

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
