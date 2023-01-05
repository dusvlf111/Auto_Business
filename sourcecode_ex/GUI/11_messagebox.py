from tkinter import(
    Tk, Button, Radiobutton, Label, IntVar, StringVar, DoubleVar, Menu
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
def info():
    msgbox.showinfo("알림","정상적으로 예매 하였습니다!!")

def warn():
    msgbox.showwarning("경고","해당 좌석은 매진되었습니다.")
            #느낌표 뜸
def error():
    msgbox.showerror("애러","결제 오류가 발생했습니다!")

def askok():
    msgbox.askokcancel("확인 / 취소","해당좌석은 유아동반석입니다. 예매하시겠습니까")


def retry():
    msgbox.askretrycancel("재시도 / 취소","일시적인 오류입니다 다시시도하시겠습니까?")

def yesno():
    msgbox.askyesno("예 / 아니요","해당 좌석은 역방향입니다. 예메하시겠습니까")

def yesnocancel():
    response = msgbox.askyesnocancel(title= None, message="예약 내역이 저장되지 않았습니다 \n 저장후 프로그램을 종료하시겠습니까?")

    print("응답:",response )
    if response == 1:
        print("예")
    elif response == 0:
        print("아니요")
    else :
        print("취소")

    #네 : 저장 후 종료          truem false none -> 예1 아니요0 그외...
    #아니요 : 저장하지 않고 종료
    #취소 : 프록그램 종료 취소 (현재 화면에서 계속 작업)
    





def askok():
    response = msgbox.askokcancel("확인 / 취소","해당좌석은 유아동반석입니다. 예매하시겠습니까")
    print("응답:",response )
    if response == 1:
        print("예")
    else :
        print("취소")
        
        
         
        
        
        
    #네 : 저장 후 종료          truem false none -> 예1 아니요0 그외...
    #아니요 : 저장하지 않고 종료
    #취소 : 프록그램 종료 취소 (현재 화면에서 계속 작업)
    







Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="애러").pack()
Button(root, command=askok, text="확인 취소").pack()
Button(root, command=retry, text="재시도 취소").pack()
Button(root, command=yesno, text="예 아니오").pack()
Button(root, command=yesnocancel, text="예 아니오 취소").pack()












#------------------------------------------------------------------------------------------------- 

def btncmd():
    pass


btn = Button(root, text="click", command=btncmd)
btn.pack()

#-------------------------------------------------------------------------------------------------


root.mainloop()


