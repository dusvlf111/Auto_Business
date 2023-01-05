from tkinter import(
    Tk, Button, Radiobutton, Label, IntVar, StringVar, DoubleVar, 
    Menu, Frame, LabelFrame, Listbox, END, Scrollbar, N, E, W, S, 
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

#F

btn_F16 = Button(root, text="F16", width=5, height=2 ) 
btn_F17 = Button(root, text="F17", width=5, height=2 )
btn_F18 = Button(root, text="F18", width=5, height=2 )
btn_F19 = Button(root, text="F19", width=5, height=2 )

 
btn_F16.grid(row=0, column=0, sticky=N+E+W+S,  padx=3, pady=3 )
btn_F17.grid(row=0, column=1, sticky=N+E+W+S,  padx=3, pady=3 )
btn_F18.grid(row=0, column=2, sticky=N+E+W+S,  padx=3, pady=3 )
btn_F19.grid(row=0, column=3, sticky=N+E+W+S,  padx=3, pady=3 )

#------------------------------------------------------------------------------------------------- 
#clear

btn_clear = Button(root, text="<--", width=5, height=2)
btn_equal = Button(root, text="=", width=5, height=2)
btn_div = Button(root, text="/", width=5, height=2)
btn_mul = Button(root, text="*", width=5, height=2)

btn_clear.grid(row=1, column=0, sticky=N+E+W+S,  padx=3, pady=3 )
btn_equal.grid(row=1, column=1, sticky=N+E+W+S,  padx=3, pady=3 )
btn_div.grid(row=1, column=2, sticky=N+E+W+S,  padx=3, pady=3 )
btn_mul.grid(row=1, column=3, sticky=N+E+W+S,  padx=3, pady=3 )

#------------------------------------------------------------------------------------------------- 
#num79

btn_7 = Button(root, text="7", width=5, height=2)
btn_8 = Button(root, text="8", width=5, height=2)
btn_9 = Button(root, text="9", width=5, height=2)
btn_sub = Button(root, text="-", width=5, height=2)

btn_7.grid(row=2, column=0, sticky=N+E+W+S,  padx=3, pady=3 )
btn_8.grid(row=2, column=1, sticky=N+E+W+S,  padx=3, pady=3 )
btn_9.grid(row=2, column=2, sticky=N+E+W+S,  padx=3, pady=3 )
btn_sub.grid(row=2, column=3, sticky=N+E+W+S,  padx=3, pady=3 )

#------------------------------------------------------------------------------------------------- 
#num46

btn_4 = Button(root, text="4", width=5, height=2)
btn_5 = Button(root, text="5", width=5, height=2)
btn_6 = Button(root, text="6", width=5, height=2)
btn_pl = Button(root, text="+", width=5, height=2)

btn_4.grid(row=3, column=0, sticky=N+E+W+S,  padx=3, pady=3 )
btn_5.grid(row=3, column=1, sticky=N+E+W+S,  padx=3, pady=3 )
btn_6.grid(row=3, column=2, sticky=N+E+W+S,  padx=3, pady=3 )
btn_pl.grid(row=3, column=3, sticky=N+E+W+S,  padx=3, pady=3 )

#------------------------------------------------------------------------------------------------- 
#num13

btn_1 = Button(root, text="1", width=5, height=2)
btn_2 = Button(root, text="2", width=5, height=2)
btn_3 = Button(root, text="3", width=5, height=2)
btn_ent = Button(root, text="enter", width=5, height=2)

btn_1.grid(row=4, column=0, sticky=N+E+W+S,  padx=3, pady=3 )
btn_2.grid(row=4, column=1, sticky=N+E+W+S,  padx=3, pady=3 )
btn_3.grid(row=4, column=2, sticky=N+E+W+S,  padx=3, pady=3 )
btn_ent.grid(row=4, column=3, rowspan=2, sticky=N+E+W+S,  padx=3, pady=3 )

#------------------------------------------------------------------------------------------------- 
#num last

btn_0 = Button(root, text="0", width=5, height=2)
btn_dot = Button(root, text=".", width=5, height=2)

btn_0.grid(row=5, column=0, columnspan=2, sticky=N+E+W+S,  padx=3, pady=3 )
btn_dot.grid(row=5, column=2, sticky=N+E+W+S,  padx=3, pady=3 )



#------------------------------------------------------------------------------------------------- 

# def btncmd():
#     pass


# btn = Button(root, text="click", command=btncmd)
# btn.pack()

#-------------------------------------------------------------------------------------------------


root.mainloop()


