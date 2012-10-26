#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode Tkinter tutorial

In this script, we use pack manager
to position two buttons in the
bottom right corner of the window. 

author: Jan Bodnar
last modified: December 2010
website: www.zetcode.com
"""

from Tkinter import *
from ttk import Frame, Button, Label, Style
from ttk import Entry


class ContactApp(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        
        self.initUI()

    def initUI(self):
        self.parent.title("Carnets d adresses")
        
        Style().configure("TButton", padding=(0, 5, 0, 5), 
            font='serif 10')
            
        nbcolumn=range(4)
        pad_column=3
        self.create_column(nbcolumn,pad_column)
#        self.columnconfigure(0, pad=3)
#        self.columnconfigure(1, pad=3)
#        self.columnconfigure(2, pad=3)
#        self.columnconfigure(3, pad=3)
        
        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)
        self.rowconfigure(4, pad=3)
        self.rowconfigure(5, pad=3)
        self.rowconfigure(6, pad=3)
        
        self.ca_txt=Listbox(self)
        self.ca_txt.grid(row=0,column=0,rowspan=7, columnspan=2, sticky=N+S)

        self.label_nom = Label(self, text="Nom")
        self.label_nom.grid(row=0,column=2,sticky=W)
        self.label_prenom = Label(self, text="Prenom")
        self.label_prenom.grid(row=2,column=2,sticky=W)
        self.label_num = Label(self, text="Telephone")
        self.label_num.grid(row=4,column=2,sticky=W)
        
        
                
        self.nom = Entry(self)
        self.nom.grid(row=1,column=2, columnspan=2, sticky=E)
        self.prenom = Entry(self)
        self.prenom.grid(row=3,column=2, columnspan=2, sticky=E)
        self.num_tel = Entry(self)
        self.num_tel.grid(row=5,column=2, columnspan=2, sticky=E)

        self.save = Button(self, text="Save")
        self.save.grid(row=6, column=2)
        self.delete = Button(self, text="Delete")
        self.delete.grid(row=6, column=3)
        self.pack()
        
    def create_column(self,mynb,mypad):
        for i in mynb:
            print i
        for i in mynb:
            print i
            self.columnconfigure(i, pad=mypad)
                     
def main():
    root = Tk()
#    root.geometry("300x200+300+300")
    app = ContactApp(root)
    return root, app
      

