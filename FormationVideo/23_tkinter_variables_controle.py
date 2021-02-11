#coding:utf-8

"""
Type
    StringVar()     : chaîne de caractères [str]
    IntVar()        : nombre entier [int]
    DoubleVar()     : nombre flottant [float]
    BooleanVar()    : booléen [bool]
acces
    get()           :
    set()           :

widget
    Label           : text
    Entry           : champs de saisi
"""

import tkinter

def update_label(*args):
    var_label.set(var_entry.get())

def update_observer(*args):
    if var_gender.get() == 1:
        var_label_gender.set("HOMME")
        print("HOMME")
    elif var_gender.get() == 2:
        var_label_gender.set("FEMME")
        print("FEMME")

#GUI
app = tkinter.Tk()
app.geometry("400x300")
app.title("23_tkinter_variables_controle.py")

var_entry = tkinter.StringVar()
var_entry.trace("w", update_label)
entry = tkinter.Entry(app, textvariable=var_entry)

var_label = tkinter.StringVar()
label = tkinter.Label(app, textvariable=var_label)
var_label.set("Le label ...")
#print("Label :", var_entry.get())

var_gender = tkinter.IntVar()
var_gender.trace("w", update_observer)

radio1 = tkinter.Radiobutton(app, text="Homme", value=1, variable=var_gender)
radio2 = tkinter.Radiobutton(app, text="Femme", value=2, variable=var_gender)

var_label_gender = tkinter.StringVar()
label_gender = tkinter.Label(app, textvariable=var_label_gender)

entry.pack()
label.pack()
radio1.pack()
radio2.pack()
label_gender.pack()

app.mainloop()
