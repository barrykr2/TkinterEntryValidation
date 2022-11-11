#from tkinter import *
import tkinter as tk
from tkinter import ttk
import clsRightClickMenu as rightClickMenu

root = tk.Tk()
root.geometry("500x400+200+100")


class Menu_Entry(ttk.Entry):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        
        rcm = rightClickMenu.RightClickMenu(self)
        
        # call popup menus when right click occurs
        self.bind('<Button-3>', rcm.popup)
        
        # bind Ctrl-d to function as in popup menu (Ctrl-d is not a normal functionality)
        self.bind("<Control-d>", rcm.delete_selected_with_e1)
        # bind Ctrl-a to function as in popup menu (Ctrl-a is not normally handled)
        self.bind("<Control-a>", rcm.select_all)

        # JUNK ----- I think
        #self.bind('<App>', self.popup)
        #self.context_menu = Menu(self, tearoff=0)
        #self.context_menu.add_command(label="Cut")
        #self.context_menu.add_command(label="Copy")
        #self.context_menu.add_command(label="Paste")
        


ent = Menu_Entry(root)
ent.pack()

ent2 = Menu_Entry(root)
ent2.pack()

root.mainloop()
