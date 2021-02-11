#coding:utf-8

"""
<nom_variable> = <nom_widget>(<widget_parent>, <params>...)
"""

import tkinter

app = tkinter.Tk()
app.title("21_tkinter_basic.py")

label_welcome = tkinter.Label(app, text="Bienvenue a tous !")
#label_welcome = tkinter.Label(app, justify="left", text="Bienvenue a tous !")
#print(label_welcome["text"])
#print(label_welcome.cget("text"))
#label_welcome["text"] = "Le nouveaux message"
#label_welcome.config(text="Le nouveaux message")
label_welcome.configure(text="Le nouveaux message")
label_welcome.pack()

message_Welcome = tkinter.Message(app, text="Message super long qui prend plusieurs lignes sur la fenetre")
message_Welcome.pack()

#entry_name = tkinter.Entry(app)
#entry_name = tkinter.Entry(app, width=45)
#entry_name = tkinter.Entry(app, width=45, show="*")
entry_name = tkinter.Entry(app, width=45, show="*", exportselection=False)
# empeche la copy auto dans le press papier
entry_name.pack()

def hello():
    print("Hello Sur Le terminal!")

button_hello = tkinter.Button(app, text="Hello", width=10, height=2, command=hello)
button_hello.pack()

def quit():
    exit()

button_quit = tkinter.Button(app, text="Quit", command=quit)
button_quit.pack()

app.mainloop()
