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

menu1 = tkinter.Menu(mainmenu, tearoff=0)
menu1.add_command(label="Option1")
menu1.add_command(label="Option2")
menu1.add_command(label="Option3")

menu2 = tkinter.Menu(mainmenu, tearoff=0)
menu2.add_command(label="Commande1")
menu2.add_command(label="Commande2")
menu2.add_command(label="Commande3")

menu3 = tkinter.Menu(mainmenu, tearoff=0)
menu3.add_command(label="À propos", command=show_about)
menu3.add_separator()
menu3.add_command(label="Quit", command=app.destroy)


mainmenu.add_cascade(label="First", menu=menu1)
mainmenu.add_cascade(label="Second", menu=menu2)
mainmenu.add_cascade(label="Third", menu=menu3)

app.config(menu=mainmenu)
app.mainloop()

