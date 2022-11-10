#!/usr/bin/env python3

#   Example:
#               generic_popup.py --location "+0+18" --className "whatever_className" --items "Item 1" "sep" "Item 2" --commands "command1" "nop" "command2" --menu_colors "#242424" "#FFFFFF" "#FCB827"
#
#   Note:
#               Items and commands are stored in lists.  But, think of it as a dictionary:
#
#               { 'Item1' : 'command1', 'Item2' : 'command2' }
#
#               "-" = Generate a menu Separator
#               command "nop" = Don't execute a command for the associated item

from argparse import ArgumentParser
from subprocess import Popen
from tkinter import *

parser = ArgumentParser()
parser.add_argument('--className', help='Override the popup classname.')
parser.add_argument('--location', help='Location to display the popup.')
parser.add_argument('--items', nargs='*', help='Menu Items to display.')
parser.add_argument('--commands', nargs='*', help='Commands to execute.')
parser.add_argument('--menu_colors', nargs=4,
                    help='Override the colors, of the popup menu.  Colors must be specified in hex format and in the order: bg fg highlightbg highlightfg')

args = parser.parse_args()

def onclose(evt) -> None:
    popup.grab_release()
    my_w.destroy()

def onexecute(cmd: str) -> None:
    Popen(cmd, shell=True)
    onclose('')

my_w = Tk(className='tp_popup_menu' if not args.className else args.className)
my_w.geometry(f"0x0{'+0+20' if not args.location else args.location}")
my_w.state("withdrawn")
my_w.update()

popup_params = { 'master' : my_w, 'relief' : RAISED, 'tearoff' : 0 }

if args.menu_colors:
    mc = args.menu_colors

    popup_params.update({'bg' : mc[0], 'fg' : mc[1], 'activebackground' : mc[2], 'activeforeground' : mc[3] })

popup = Menu(**popup_params)

popup.bind('<Escape>', onclose)
popup.bind('<FocusOut>', onclose)

for i in range(len(args.items)):
    if args.items[i] != '-':
        popup.add_command(label=f' {args.items[i]}', command=lambda cmd=args.commands[i] : onexecute(cmd))
    else:
        popup.add_separator()

# SIDE NOTE: In my opinion, setting geometry and doing an update(), shouldn't
# change the state of a window.
my_w.geometry(f'{popup.winfo_width() + 2}x{popup.winfo_height() + 2}')
my_w.update()

popup.tk_popup(my_w.winfo_rootx(), my_w.winfo_rooty())

my_w.mainloop()