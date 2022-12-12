from tkinter import *

import levels
from main import start
from levels import *


def show_mark(mark, quiz_level):
    sh = Tk()
    sh.title('Your Marks')

    st = "Your score is " + str(mark) + "/5"
    mlabel = Label(sh, text=st, fg="black", bg="white")
    mlabel.pack()

    def callsignUpPage():
        sh.destroy()
        start()

    def re_attempt():
        sh.destroy()
        if quiz_level == "easy":
            levels.level(quiz_level)
        elif quiz_level == "hard":
            levels.level(quiz_level)
        else:
            levels.level(quiz_level)

    b24 = Button(text="Re-attempt", command=re_attempt, bg="black", fg="white")
    b24.pack()

    from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
    from matplotlib.figure import Figure

    fig = Figure(figsize=(5, 4), dpi=100)
    labels = 'Marks Obtained', 'Total Marks'
    sizes = [int(mark), 5 - int(mark)]
    explode = (0.1, 0)
    fig.add_subplot(111).pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=0)

    canvas = FigureCanvasTkAgg(fig, master=sh)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    b23 = Button(text="Sign Out", command=callsignUpPage, fg="white", bg="black")
    b23.pack()

    sh.mainloop()