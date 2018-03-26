# from Tkinter import *
# from tkinter import *

try:
    # import Tkinter as tk
    from Tkinter import *
except:
    # import tkinter as tk
    from tkinter import *

import subprocess

def show_entry_fields():
   print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
   print
   name = e1.get()
   surname = e2.get()
   branchName = createBranchName(name,surname)
   command = "./somebashfile.sh %s" % (branchName)
   subprocess.call(command,shell=True)

def createBranchName(name,surname):
    name = str.capitalize(name.replace(" ",""))
    surname = str.capitalize(surname.replace(" ",""))
    newString = name + surname
    replaceString = newString.replace(" ","")
    print("replaceString:" + replaceString)
    return replaceString

master = Tk()
master.wm_title("InterviewBox")
Label(master, text="First Name").grid(row=0)
Label(master, text="Last Name").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master, text='Exit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Submit', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

mainloop( )