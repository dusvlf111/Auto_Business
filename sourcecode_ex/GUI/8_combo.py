from tkinter import(
    Tk, Button, Radiobutton, Label, IntVar, StringVar
)
from tkinter.ttk import (
    Progressbar, Combobox
    )


root = Tk()
root.title("sungbin GUI")
root.geometry("640x480") #가로 x 세로





values = [str(i) + "day" for i in range(1, 32)]  # 1부터 31까지의 숫자
combobox = Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드 결제일") 

values = [str(i) + "day" for i in range(1, 32)]
read_Combobox = Combobox(root, height=10, values=values, state = "readonly")  # 읽기 전용
read_Combobox.current(0)            #0번째 인덱스 값 선택
read_Combobox.pack()





def btncmd():
    print(combobox.get())
    print(read_Combobox.get())


btn = Button(root, text="click", command=btncmd)
btn.pack()


root.mainloop()


