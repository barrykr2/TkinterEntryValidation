# Written by Barry Kruyssen Nov 2022.
# Feel free to use as you like :-)
# This is a widget built on the Tkinter Entry widget.
import tkinter as tk
from tkinter import ttk
import clsBallonToolTip as btt
import clsRightClickMenu as rightClickMenu

# used to initialise object so autocomplete works during development (not required at runtime)
import clsValidateData as validate
from datetime import datetime, timedelta


# An implementation of ttk.Entry with Events, Validation and Formatting
class EntryWithEvents(ttk.Entry):
    def __init__(self, master, max_len = None, widget_name = None, 
                 validation_method = None, set_justifiction = None,
                 tool_tip = None, **kw):
        super().__init__(master, **kw)
        
        self.master = master        
        self.max_len = max_len
        self.widget_name = widget_name
        self.validation_method = validation_method
        self.set_justifiction = set_justifiction
        self.tool_tip = tool_tip
        
        text_checker = self.master.register(self.is_valid_input)
        self.configure(validate="all", 
                       validatecommand=(text_checker, "%d", "%i","%P", 
                                        "%s", "%S", "%V", "%W"))

        rcm = rightClickMenu.RightClickMenu(self)
        
        # call popup menus when right click occurs
        self.bind('<Button-3>', rcm.popup)
        
        # bind Ctrl-d to function as in popup menu (Ctrl-d is not a normal functionality)
        self.bind("<Control-d>", rcm.delete_selected_with_e1)
        # bind Ctrl-a to function as in popup menu (Ctrl-a is not normally handled)
        self.bind("<Control-a>", rcm.select_all)
        
        #self.bind('<Control-a>', self.select_all)
        self.bind('<FocusOut>', self.do_validation)
        self.bind('<Return>', self.do_validation)
        
        # Initialise the field
        self.do_validation(None)
        
        if not self.tool_tip == None:
            btt.Tooltip(self, text = self.tool_tip, wraplength = 600)
        
    def is_valid_input(self, d_action, i_index, P_text, 
                       s_prior_text, S_changed_text,  
                       V_callback, W_widget_name):
                       
        if False:  # change to True to print parameters  (remove for runtime)
            print(str(datetime.today()) + ', ' + self.widget_name + ", " + d_action + ', ' + i_index + ', ' + 
                  P_text + ', ' + 
                  s_prior_text + ', ' + S_changed_text + ', ' + 
                  V_callback + ', ' + W_widget_name)
        
        if V_callback == 'focusin':
            # select text after 100ms
            self.master.after(100, self.__select_all)
            
        if V_callback == 'focusout':
            # deselect text
            #self.select_clear()
            pass

        if self.max_len:
            if len(P_text) > self.max_len:
                return False
            
            return True

    def do_validation(self, e):
        if not self.validation_method == None:
            data = self.get()
            
            # vaidate date using function passed in
            returnObj = validate.dataObj()   # initialise object so autocomplete works during development (not required at runtime)
            returnObj = self.validation_method(data)
            
            if self.tool_tip == None:
                if not returnObj.toolTip == None:
                    self.tool_tip = returnObj.toolTip

            if self.set_justifiction == None:
                if not returnObj.widgetJustification == None:
                    self.configure(justify = returnObj.widgetJustification)
    
            if returnObj.isValid:   # is valid so overwite data (delete and insert new)
                if not returnObj.value == None:
                    if not str(returnObj.value) == str(data):
                        self.delete(0, len(data))
                        self.insert(0, str(returnObj.value))
            elif len(data) > 0:
                self.master.after(1, lambda: self.focus_set())

    def select_all(self, key_press_event):
        self.master.after(1, self.__select_all)
        
    def __select_all(self):
        # select text
        self.select_range(0, 'end')
        # move cursor to the end
        self.icursor('end')
        #stop propagation
        return 'break'
