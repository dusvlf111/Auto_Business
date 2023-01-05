from tkinter import(
    Tk, Button, Radiobutton, Label, IntVar, StringVar, DoubleVar, Menu
)
from tkinter.ttk import (
    Progressbar, Combobox
    )
import time

root = Tk()
root.title("sungbin GUI")
root.geometry("640x480") #가로 x 세로


#-------------------------------------------------------------------------------------------------

def cerate_new_file():
    print("새파일을 만듭닏다")

menu = Menu(root)


menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command=cerate_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator()
menu_file.add_command(label="open file.....")
menu_file.add_separator()
menu_file.add_command(label="save all", state="disable") # 비활성화
menu_file.add_separator()
menu_file.add_command(label="exit", command=root.quit) # 종료
menu.add_cascade(label="File", menu=menu_file )

 
#에딧 메뉴 빈값
menu.add_cascade(label="edit")

#언어 메뉴 추가 라디오
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="python")
menu_lang.add_radiobutton(label="c")
menu_lang.add_radiobutton(label="C++")
menu_lang.add_radiobutton(label="java")
menu.add_cascade(label="File", menu=menu_lang )

# 뷰메뉴
 
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu.add_cascade(label="View", menu=menu_view)



root.config(menu=menu)


#-------------------------------------------------------------------------------------------------


def btncmd():
    pass


btn = Button(root, text="click", command=btncmd)
btn.pack()

#-------------------------------------------------------------------------------------------------


root.mainloop()


