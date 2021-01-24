#coding:utf-8

"""
default

    text        = text to display
    width       = hauteur
    height      = largeur

.Checkbutton

    offvalue    = unchecked button default value
    onvalue     = checked button default value

tkinter.messagebox
    showerror
    showinfo
    showwarning
    askquestion
    askokcancel
    askyesno
    askretrycancel
"""

import tkinter
from tkinter import messagebox

app = tkinter.Tk()
app.title("22_tkinter_advanced.py")
app.geometry("600x600")

check_widget = tkinter.Checkbutton(app, text="scan_port", offvalue=2, onvalue=5)
check_widget.pack()

radio_widgetH = tkinter.Radiobutton(app, text="Homme", value=2)
radio_widgetF = tkinter.Radiobutton(app, text="Femme", value=1)
radio_widgetH.pack()
radio_widgetF.pack()

scale_widget = tkinter.Scale(app, from_=10, to=50, tickinterval=4+1)
scale_widget.pack()

spin_widget = tkinter.Spinbox(app, from_=5, to=100)
spin_widget.pack()

listbox_widget = tkinter.Listbox(app)
listbox_widget.insert(1, "Windows")
listbox_widget.insert(2, "MacOS")
listbox_widget.insert(3, "GNU/Linux")
listbox_widget.pack()

def show_modal_windows_error():
    messagebox.showerror(title="ERREUR", message="Un probelème est survenu !")

button_error = tkinter.Button(app, text="Déclancheur D'érreur", command=show_modal_windows_error)
button_error.pack()

def show_modal_windows_info():
    messagebox.showinfo(title="INFO", message="Une inforamtion fort utiles ;)")

button_info = tkinter.Button(app, text="Déclancheur d'info", command=show_modal_windows_info)
button_info.pack()

def show_modal_windows_warning():
    messagebox.showwarning(title="WARNING", message="Ceci est un avertissement")

button_warning = tkinter.Button(app, text="Déclancheur d'alerte", command=show_modal_windows_warning)
button_warning.pack()

def show_modal_windows_askquestion():
    messagebox.askquestion(title="Confirm", message="Etes vous vraiments sûr ?")

button_askquestion = tkinter.Button(app, text="askquestion", command=show_modal_windows_askquestion)
button_askquestion.pack()

def show_modal_windows_askokcancel():
    messagebox.askokcancel(title="Confirm", message="Voulez vous vraiment quittez ?")

button_askokcancel = tkinter.Button(app, text="askokcancel", command=show_modal_windows_askokcancel)
button_askokcancel.pack()

def show_modal_windows_askyesno():
    messagebox.askyesno(title="Confirm", message="C'est OUI où bien c'est NON")

button_askyesno = tkinter.Button(app, text="askyesno", command=show_modal_windows_askyesno)
button_askyesno.pack()

def show_modal_windows_askretrycancel():
    messagebox.askretrycancel(title="Retry ?", message="Voulez vous réesayez ?")

button_askretrycancel = tkinter.Button(app, text="askretrycancel", command=show_modal_windows_askretrycancel)
button_askretrycancel.pack()

app.mainloop()
