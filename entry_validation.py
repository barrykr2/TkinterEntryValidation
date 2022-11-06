import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("400x200")

class EntryWilthLimit(ttk.Entry):
    def __init__(self, master, max_len, widget_name, **kw):
        super().__init__(master, **kw)
        
        self.max_len = max_len
        self.widget_name = widget_name
        
        text_checker = root.register(self.is_valid_input)
        self.configure(validate="all", 
                       validatecommand=(text_checker, "%d", "%i","%P", 
                                        "%s", "%S", "%V", "%W"))
        
        
    def is_valid_input(self, d_action, i_index, P_text, 
                       s_prior_text, S_changed_text,  
                       V_callback, W_widget_name):
                       
        print(self.widget_name + ", " + d_action + ', ' + i_index + ', ' + P_text + ', ' + 
              s_prior_text + ', ' + S_changed_text + ', ' + 
              V_callback + ', ' + W_widget_name)
              
        if self.max_len:
            if len(P_text) > self.max_len:
                return False
            
            return True
        
entry_usename = EntryWilthLimit(root, max_len = 5, widget_name = 'entry_usename')
entry_usename.pack(expand=True)

entry_details = EntryWilthLimit(root, max_len = 7, widget_name = 'entry_detail')
entry_details.pack(expand=True)

root.mainloop()
