# -*- coding: utf-8 -*-
"""
Created on Fri May 22 08:41:16 2020

@author: Gunashekar Chenna
"""
import tkinter as tk
import random as r
def doit():
    s=e1.get()
    l=int(e2.get())
    pw=''
    for i in range(0,l):
        pw+=r.choice(s)
    e3.insert(0,pw)
z=tk.Tk()
z.title("Password Generator")

l1=tk.Label(z,text="Enter the set of chars: ")
l1.grid(row=0,column=0,padx=10,pady=10,sticky='nwse')
e1=tk.Entry(z)
e1.grid(row=0,column=1,padx=10,pady=10,sticky='nwse')
l2=tk.Label(z,text="Enter length: ")
l2.grid(row=1,column=0,padx=10,pady=10,sticky='nwse')
e2=tk.Entry(z)
e2.grid(row=1,column=1,padx=10,pady=10,sticky='nwse')
b=tk.Button(z,text="get password", bg="black",fg="white",command=doit)
b.grid(row=2,column=0,padx=10,pady=10,sticky='nwse')
e3=tk.Entry(z)
e3.grid(row=2,column=1,padx=10,pady=10,sticky='nwse')


for i in range(3):
    z.grid_rowconfigure(i,weight=1)
for j in range(2):
    z.grid_columnconfigure(j,weight=1)
z.mainloop()