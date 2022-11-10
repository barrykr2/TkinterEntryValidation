import tkinter as tk
from datetime import datetime, timedelta

class RightClickMenu():
    def __init__(self, master):
        self.master = master

        # create right click popup
        self.master.popup_menu = tk.Menu(self.master, tearoff=0, # background='#1c1b1a', fg='white',
                               activebackground='#534c5c',
                               activeforeground='Yellow')
        self.master.popup_menu.add_command(label="Cut                     ", command=self.Cut,
                                    accelerator='Ctrl+V')
        self.master.popup_menu.add_command(label="Copy                    ", command=self.Copy, compound=tk.LEFT,
                                    accelerator='Ctrl+C')
        
        self.master.popup_menu.add_command(label="Paste                   ", command=self.Paste, accelerator='Ctrl+V')
        self.master.popup_menu.add_separator()
        self.master.popup_menu.add_command(label="Select all", command=self.__select_all, accelerator="Ctrl+A")
        self.master.popup_menu.add_command(label="Delete", command=self.delete_only, accelerator=" Delete")
        self.master.popup_menu.add_command(label="Delete all", command=self.delete_selected, accelerator="Ctrl+D")
        
        self.master.popup_menu.bind('<Leave>', self.close_menu)

    def close_menu(self, event = None):
        self.master.popup_menu.unpost()
        self.master.focus()
        
    def popup(self, event):
        try:
            self.master.after(1, self.master.popup_menu.tk_popup(event.x_root, event.y_root, 0))
        finally:
            self.master.popup_menu.grab_release()
            
    def Copy(self):
        self.master.event_generate('<<Copy>>')

    def Paste(self):
        self.master.event_generate('<<Paste>>')

    def Cut(self):
        self.master.event_generate('<<Cut>>')

    def delete_selected_with_e1(self, event):
        self.master.select_range(0, tk.END)
        self.master.focus()
        self.master.event_generate("<Delete>")

    def delete_selected(self):
        self.master.select_range(0, tk.END)
        self.master.focus()
        self.event_generate("<Delete>")

    def delete_only(self):
        self.event_generate("<BackSpace>")

    def select_all(self, e = None):
        self.master.after(1, self.__select_all)
        
    def __select_all(self):
        self.master.select_range(0, tk.END)
        self.master.focus()
        return 'break'
