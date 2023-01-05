from tkinter import(
    Tk, Button, Radiobutton, Label, IntVar, StringVar, DoubleVar, Menu, Frame, LabelFrame
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

Label(root, text="메뉴를 선택해 주세요").pack(side="top")

Button(root, text="주문하기").pack(side="bottom")


#------------------------------------------------------------------------------------------------- 
# 메뉴프레임
frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack(side="left", fill="both", expand=True )


Button(frame_burger, text="햄버거").pack()
Button(frame_burger, text="치즈버거").pack()
Button(frame_burger, text="치킨버거").pack()
# ...............................................
#음료프레임
framee_drink = LabelFrame(root, text="음료")
framee_drink.pack(side="right", fill="both", expand=True)


Button(framee_drink, text="콜라").pack()
Button(framee_drink, text="사이다").pack()
Button(framee_drink, text="환타").pack()


#------------------------------------------------------------------------------------------------- 

# def btncmd():
#     pass


# btn = Button(root, text="click", command=btncmd)
# btn.pack()

#-------------------------------------------------------------------------------------------------


root.mainloop()


