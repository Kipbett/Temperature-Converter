#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 13:38:52 2019

@author: brian
"""

from tkinter import *

def calculate():
    temp = int(entry.get())
    temp = 9/5*temp+32
    output_label.configure(text="Converted {:.2f}".format(temp))
    entry.delete(0, END)
    
root = Tk()

output = Label(text="Enter Temperature in celcius: ")
output.grid(row=0, column=0)
entry = Entry(root, width = 4)
entry.grid(row=0, column=1)
calc_button = Button(text="Convert", command=calculate)
calc_button.grid(row=0, column=3)
convert = Label(text="Converted: ")
convert.grid(row=1, column=0)
output_label = Label()
output_label.grid(row=1, column=1)

root.mainloop()