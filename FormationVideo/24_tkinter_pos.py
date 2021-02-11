#coding:utf-8

"""
n = nord
s = sud
e = est
w = ouest
"""

import tkinter

count = 0

def printHello():

    global count

    count += 1

    print(f"HELLO : {count}")

# window config
app = tkinter.Tk()
app.title("24_tkinter_pos.py")
app.geometry("650x490")
app.minsize(640, 480)
app.maxsize(1280, 960)

"""

# Positionnement widget
frame_btn = tkinter.LabelFrame(app, text="btn")
frame_TOP = tkinter.LabelFrame(app, text="pos")
frame_BOTTOM = tkinter.LabelFrame(app, text="pos")
frame_RIGHT = tkinter.LabelFrame(app, text="pos")
frame_LEFT = tkinter.LabelFrame(app, text="pos")

label_TOP = tkinter.Label(frame_TOP, text="TOP")
label_BOTTOM = tkinter.Label(frame_BOTTOM, text="BOTTOM")
label_RIGHT = tkinter.Label(frame_RIGHT, text="RIGHT")
label_LEFT = tkinter.Label(frame_LEFT, text="LEFT")
btn = tkinter.Button(frame_btn, text="HELLO", command=printHello)

#""---------------""

label_TOP.pack(expand=1, ipady=10)
label_BOTTOM.pack(expand=1, ipady=10)
label_RIGHT.pack(expand=1, ipadx=10)
label_LEFT.pack(expand=1, ipadx=10)

frame_TOP.pack(side="top", fill="x")
frame_BOTTOM.pack(side="bottom", fill="x")
frame_RIGHT.pack(side="right", fill="y")
frame_LEFT.pack(side="left", fill="y")
frame_btn.pack(fill="both", expand=1, ipadx=25, ipady=25, padx=1)

btn = tkinter.Button(frame_btn, text="HELLO", command=printHello)
btn.pack(expand=1, fill="both", padx=25, pady=25)
"""

"""
labelX = tkinter.Label(app, text="X")

labelx1 = tkinter.Label(app, text="COLUMN_1")
labelx2 = tkinter.Label(app, text="COLUMN_2")
labelx34 = tkinter.Label(app, text="COLUMN_3 COLUMN_4")
labelx5 = tkinter.Label(app, text="COLUMN_5")

labely1 = tkinter.Label(app, text="ROW_1           ")
labely2 = tkinter.Label(app, text="ROW_2")
labely34 = tkinter.Label(app, text="ROW_3\nROW_4")
labely5 = tkinter.Label(app, text="ROW_5")
labely6 = tkinter.Label(app, text="ROW_6")

labelX.grid(row=0, column=0)

labelx1.grid(row=0, column=1)
labelx2.grid(row=0, column=2)
labelx34.grid(row=0, column=3, columnspan=2)
labelx5.grid(row=0, column=5)

labely1.grid(row=1, column=0, sticky="w")
labely2.grid(row=2, column=0, sticky="w")
labely34.grid(row=3, column=0, rowspan=2, sticky="w")
labely5.grid(row=5, column=0, sticky="w")
labely6.grid(row=6, column=0, sticky="e")
"""

btn = tkinter.Button(app, text="HELLO", command=printHello)
btn.place(x=500, y=25)

# Main loop
app.mainloop()
