from tkinter import(
    Tk, Button, Radiobutton, Label, IntVar, StringVar
)
root = Tk()
root.title("sungbin GUI")
root.geometry("640x480")


Label(root, text="selected manu").pack()


burger_var = IntVar()
btn_burger1 = Radiobutton(root, text="buger", value=1, variable=burger_var)
btn_burger1.select()
btn_burger2 = Radiobutton(root, text="chbuger", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="bulbuger", value=3, variable=burger_var)


btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text="selected manu").pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="cola", value="cola", variable=drink_var)
btn_drink2 = Radiobutton(root, text="soda", value="soda", variable=drink_var)
btn_drink3 = Radiobutton(root, text="tea", value="tea", variable=drink_var)


btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()



def btncmd():
    print(burger_var.get())     
    print(drink_var.get())

btn = Button(root, text="click", command=btncmd)
btn.pack()


root.mainloop()


