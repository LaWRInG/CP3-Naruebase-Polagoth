# import tkinter
#
# mainWindow = tkinter.Tk()
#
# mainWindow.mainloop()
from tkinter import *

def sayHallo():
    print("Hallo World")


mainWindow = Tk()
button = Button(mainWindow,text="Click me1",command = sayHallo).grid(row=0,column=1)
button2 = Button(mainWindow,text="Click me2",command = sayHallo).grid(row=1,column=1)
button3 = Button(mainWindow,text="Click me3",command = sayHallo).grid(row=1,column=2)
label = Label(mainWindow,text="Hello World",width =20,fg = "red",bg ="black",font=("TH SarabunPSK",50),anchor =E).grid(row=0,column=2)
# button.place(x = 50, y = 50 )
mainWindow.mainloop()
