import tkinter as tk
from tkinter import ttk
from time import sleep
from threading import Thread
from datetime import datetime


class status_bar_obj:
    def __init__(self, master: tk.Tk, default_text:str = '', text:str = ''):
        self.default_text = default_text
        self.statusVar = tk.StringVar()
        self.statusVar.set(text)
        self.sbar = ttk.Label(master, textvariable=self.statusVar, relief=tk.SUNKEN, anchor="w")
        self.sbar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def update(self, text:str = None):
        if text == None:
            text = self.default_text
            
        self.statusVar.set(text)
        self.sbar.update()
         

if __name__ == "__main__":
    root = tk.Tk()

    sb = status_bar_obj(master=root, default_text="Ready", text="Loading...")
