from tkinter import *

root = Tk()
root.title("TkInter App")
root.geometry("925x500+300+200")
root.configure(bg="white")
root.resizable(False, False)

label = Label(text="Hello Everyone!", fg="pink", bg="red", font=("Microsoft Yahei UI Light", 25, 'bold'), justify="center")
label.place(x= 30, y=100, height=48, width=334)
root.mainloop()