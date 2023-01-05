from tkinter import(
    Tk, Button, Radiobutton, Label, IntVar, StringVar, DoubleVar
)
from tkinter.ttk import (
    Progressbar, Combobox
    )
import time

root = Tk()
root.title("sungbin GUI")
root.geometry("640x480") #가로 x 세로


#-------------------------------------------------------------------------------------------------


#                                                 #결정되지 않은 값
# # progressbar = Progressbar(root, maximum=100, mode='indeterminate') 
# progressbar = Progressbar(root, maximum=100, mode='determinate') 
# # progressbar.start(10) # 10 ms 마다 움직임
# progressbar.start(10) # 1 ms 마다 움직임
# progressbar.pack()


p_var2 = DoubleVar()
Progressbar1 = Progressbar(root, maximum=100, length=150, variable=p_var2)
Progressbar1.pack()



def btncmd2():
    for i in range(101):    #1부터 100
        time.sleep(0.01)  #0.01 대기
        
        
        p_var2.set(i) # progress bar 의 값 설정
        Progressbar1.update() # ui 업데이트 
        print(p_var2.get())


btn = Button(root, text="시작", command=btncmd2)
btn.pack()



#-------------------------------------------------------------------------------------------------



def btncmd():
    pass


btn = Button(root, text="click", command=btncmd)
btn.pack()

#-------------------------------------------------------------------------------------------------


root.mainloop()


