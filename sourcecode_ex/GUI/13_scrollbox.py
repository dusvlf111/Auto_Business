from tkinter import(
    Tk, Button, Radiobutton, Label, IntVar, StringVar, DoubleVar, Menu, Frame, LabelFrame, Listbox, END, Scrollbar
)
from tkinter.ttk import (
    Progressbar, Combobox
    )
import time


import tkinter.messagebox as msgbox 



root = Tk()
root.title("sungbin GUI")
root.geometry("640x480") #가로 x 세로
#------------------------------------------------------------------------------------------------- 

frame = Frame(root)
frame.pack()

 
#------------------------------------------------------------------------------------------------- 
sBAR = Scrollbar(frame)
sBAR.pack(side="right", fill="y")
#set이 없으면 스크롤을 내려도 다시 올라옴
lBOX = Listbox(frame, selectmode="extended", height=10, yscrollcommand=sBAR.set)
for i in range(1, 32): 
    lBOX.insert(END, str(i) + "일")
lBOX.pack(side="left")


sBAR.config(command=lBOX.yview)


#------------------------------------------------------------------------------------------------- 

# def btncmd():
#     pass


# btn = Button(root, text="click", command=btncmd)
# btn.pack()

#-------------------------------------------------------------------------------------------------


root.mainloop()


