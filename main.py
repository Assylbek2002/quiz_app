from tkinter import *


def signup():
    window.destroy()

    sign_up = Tk()
    sign_up.title("Sign Up")
    sign_up_canvas = Canvas(sign_up, width=700, height=700, bg="#121212")
    sign_up_canvas.pack()

    fname = StringVar()

    sign_up_frame = Frame(sign_up_canvas, bg="#121212")
    sign_up_frame.place(anchor=CENTER, relheight=0.8, relwidth=0.8, relx=0.5, rely=0.5)

    heading = Label(sign_up_frame, text="Quiz App", fg="#4257b2", bg="#121212")
    heading.config(font=('calibri 40'))
    heading.place(relx=0.3, rely=0.1)

    flabel = Label(sign_up_frame, text="Full Name", fg='white', bg='black')
    flabel.place(relx=0.21, rely=0.4)
    fname = Entry(sign_up_frame, bg='white', fg='black', textvariable=fname)
    fname.config(width=42)
    fname.place(relx=0.31, rely=0.4)

def exit_quiz():
    pass


window = Tk()
window.title("Quiz App")

canvas = Canvas(window, width=700, height=700, bg="#4257b2")
logo_image = PhotoImage(file="mylogo.png")
canvas.create_image(350, 200, image=logo_image)
canvas.pack()


start_button = Button(window, text="START", bg="#4257b2", fg="white", height=2, width=15, activebackground="#4257b2",
                      command=signup)
start_button.place(x=300, y=400)
exit_button = Button(window, text="EXIT", bg="#4257b2", fg="white", height=2, width=15, activebackground="#4257b2",
                     command=exit_quiz)
exit_button.place(x=300, y=450)


window.mainloop()