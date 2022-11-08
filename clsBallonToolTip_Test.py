""" tk_ToolTip_class101.py
gives a Tkinter widget a tooltip as the mouse is above the widget
tested with Python27 and Python34  by  vegaseat  09sep2014
www.daniweb.com/programming/software-development/code/484591/a-tooltip-class-for-tkinter

Modified to include a delay time by Victor Zaccardo, 25mar16
"""

try:
    # for Python2
    import Tkinter as tk
except ImportError:
    # for Python3
    import tkinter as tk

import clsBallonToolTip as btt

# testing ...
if __name__ == '__main__':
    root = tk.Tk()
    btn1 = tk.Button(root, text="button 1")
    btn1.pack(padx=10, pady=5)
    button1_ttp = btt.CreateToolTip(btn1, \
   'Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, '
   'consectetur, adipisci velit. Neque porro quisquam est qui dolorem ipsum '
   'quia dolor sit amet, consectetur, adipisci velit. Neque porro quisquam '
   'est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit.')

    btn2 = tk.Button(root, text="button 2")
    btn2.pack(padx=10, pady=5)
    button2_ttp = btt.CreateToolTip(btn2, \
    "First thing's first, I'm the realest. Drop this and let the whole world "
    "feel it. And I'm still in the Murda Bizness. I could hold you down, like "
    "I'm givin' lessons in  physics. You should want a bad Vic like this.")
    root.mainloop()