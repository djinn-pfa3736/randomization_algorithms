import tkinter as tk

class Preference(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        master.title("Preference")
        master.geometry("300x300")
        self.pack()
        self.create_widgets()
    def create_widgets(self):
        #Pane
        self.pw_main = tk.PanedWindow(self.master, orient='vertical')
        self.pw_main.pack(expand=True, fill=tk.BOTH, side="top")
        #Frame
        self.fm = tk.Frame(self.pw_main, bd=0, relief="flat")
        self.pw_main.add(self.fm)
        #Label
        self.lb_groupa = tk.Label(self.fm)
        self.lb_groupa["text"]="Group A"
        self.lb_groupa.grid(row=0 , column= 0, padx= 2, pady = 2, sticky =tk.W + tk.E)
        self.lb_groupb = tk.Label(self.fm)
        
        self.lb_groupb["text"]="Group B"
        self.lb_groupb.grid(row=1 , column= 0, padx= 2, pady = 2, sticky =tk.W + tk.E)
        
if __name__ == '__main__':
    root = tk.Tk()
    preference = Preference(master=root)
    preference.mainloop()
    
