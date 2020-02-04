import tkinter as tk

class Preference(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        master.title("Preference")
        master.geometry("300x300")
        self.pack()
        # self.create_widgets()
if __name__ == '__main__':
    root = tk.Tk()
    preference = Preference(master=root)
    preference.mainloop()
