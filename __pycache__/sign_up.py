from tkinter import *
from PIL import ImageTk

sign_up = Tk()
# sign_up.geometry("800x650+200+300")
sign_up.resizable(False, False)
sign_up.title("Sign Up")

background = ImageTk.PhotoImage(file="bg.jpg")
label = Label(sign_up, image=background)
label.grid()

frame = Frame(sign_up)
frame.place(x= 554, y=100)

heading = Label(frame, text="CREATE AN ACCOUNT", bg="white", fg="firebrick1", font=("Microsoft Yahei UI", 18, "bold" ), justify="center")
heading.grid(row=0, column=0, padx=10, pady=10)

emaillabel = Label(frame, text="Email", fg="firebrick1", font=("Microsoft Yahei UI", 10, "bold") )
emaillabel.grid(row=1, column=0, sticky="W", padx=25)

emailEntry = Entry(frame, width=25, fg="white", bg="firebrick1", font=("Microsoft Yahei UI", 10, "bold") )
emailEntry.grid(row=2, column=0, sticky="W", padx=25, pady=(10,0))


userlabel = Label(frame, text="Username", fg="firebrick1", font=("Microsoft Yahei UI", 10, "bold") )
userlabel.grid(row=3, column=0, sticky="W", padx=25, pady=(10,0))

userEntry = Entry(frame, width=25, fg="white", bg="firebrick1", font=("Microsoft Yahei UI", 10, "bold") )
userEntry.grid(row=4, column=0, sticky="W", padx=25, pady=(10,0))

passwordlabel = Label(frame, text="Password", fg="firebrick1", font=("Microsoft Yahei UI", 10, "bold") )
passwordlabel.grid(row=5, column=0, sticky="W", padx=25)

passwordEntry = Entry(frame, width=25, fg="white", bg="firebrick1", font=("Microsoft Yahei UI", 10, "bold") )
passwordEntry.grid(row=6, column=0, sticky="W", padx=25, pady=(10,0))


confirmlabel = Label(frame, text="Confirm Password", fg="firebrick1", font=("Microsoft Yahei UI", 10, "bold") )
confirmlabel.grid(row=7, column=0, sticky="W", padx=25, pady=(10,0))

confirmEntry = Entry(frame, width=25, fg="white", bg="firebrick1", font=("Microsoft Yahei UI", 10, "bold") )
confirmEntry.grid(row=8, column=0, sticky="W", padx=25)

terms = Checkbutton(frame, text="I agree to the terms and conditions", font=("Microsoft Yahei UI", 9, "bold"),
                    bg="white", fg="firebrick1", cursor="hand2", activebackground="white", 
                    activeforeground= "firebrick1" )
terms.grid(row=9, column=0, pady=10, padx=15)

sign_up = Button(frame, text="Sign Up", font=("Open Sans", 16, "bold"),
                    fg="white", bg="firebrick1", cursor="hand2", activeforeground="white", 
                    activebackground= "firebrick1", width=17, border=0 )
sign_up.grid(row=10, column=0, padx=15)

already = Label(frame, text="Don't have an account?", font=("Open Sans", 9, "bold"), bg="white", fg="firebrick1",)
already.grid(row=11, column=0, sticky="W", padx=25, pady=16)

loginButton = Button(frame, text="Login", font=("Open Sans", 9, "bold underline"), bg="white", fg="blue",
                     activebackground="white", activeforeground="blue", bd=0, cursor="hand2")
loginButton.place(x=170, y=484)
sign_up.mainloop()