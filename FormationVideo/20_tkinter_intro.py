#coding:utf-8

import tkinter
#from tkinter import *

mainapp = tkinter.Tk()
mainapp.title("Mon Super Programme")

#mainapp.minsize(640, 480)
#mainapp.maxsize(1280, 720)
#mainapp.resizable(width=False, height=False)
#mainapp.positionfrom("user")
#mainapp.sizefrom("user")

#geometry("XxY+0+0")

screenX = int(mainapp.winfo_screenwidth())
screenY = int(mainapp.winfo_screenheight())

windowX = 800
windowY = 600

posX = (screenX // 2) - (windowX // 2)
posY = (screenY // 2) - (windowY // 2)

geo = f"{windowX}x{windowY}+{posX}+{posY}"

mainapp.geometry(geo)

mainapp.mainloop()
