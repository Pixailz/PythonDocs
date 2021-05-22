#coding:utf-8

"""
tearoff=0       Enleve l'index 0 des menu

add_checkbutton()
add_radiobutton()
add_separator
"""

import tkinter
from time import sleep

def show_about():

    about_window = tkinter.Toplevel(app)
    about_window.title("À propos ...")
    lb = tkinter.Label(about_window, text="https://github.com/Pixailz/Python")
    lb.pack(fill="both", expand=1)
    # explosif ..
    show_about()



app = tkinter.Tk()
app.geometry("640x480")
app.title("25_tkinter_menu.py")

# Widget
mainmenu = tkinter.Menu(app)

option = tkinter.Menu(mainmenu, tearoff=0)
option.add_command(label="Option1")
option.add_command(label="Option2")
option.add_command(label="Option3")

command = tkinter.Menu(mainmenu, tearoff=0)
command.add_command(label="Commande1")
command.add_command(label="Commande2")
command.add_command(label="Commande3")

menu = tkinter.Menu(mainmenu, tearoff=0)
menu.add_command(label="À propos", command=show_about)
menu.add_separator()
menu.add_command(label="Quit", command=app.destroy)


mainmenu.add_cascade(label="Options", menu=option)
mainmenu.add_cascade(label="Commande", menu=command)
mainmenu.add_cascade(label="Menu", menu=menu)

app.config(menu=mainmenu)
app.mainloop()

