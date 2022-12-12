import random
import time
from functools import partial
from tkinter import *
from questions import *
from mark import *


def level(quiz_level):
    def calc():
        global score
        if var.get() in (easy_answer or medium_answer or hard_answer):
            score += 1
        display()

    def display():
        if len(indexes) == 0:
            l.destroy()
            show_mark(score, quiz_level)
        elif len(indexes) == 1:
            next_question.configure(text="End", command=calc)
            print(indexes)
        if indexes:
            element_choice = random.choice(indexes)
            if quiz_level == "easy":
                question.configure(text=easyQ[element_choice][0])
            elif quiz_level == "medium":
                question.configure(text=mediumQ[element_choice][0])
            else:
                question.configure(text=hardQ[element_choice][0])
            for j in range(0, len(button_index)):
                if quiz_level == "easy":
                    options[j].configure(text=easyQ[element_choice][button_index[j]],
                                        value=easyQ[element_choice][button_index[j]])
                elif quiz_level == "medium":
                    options[j].configure(text=mediumQ[element_choice][button_index[j]],
                                         value=mediumQ[element_choice][button_index[j]])
                else:
                    options[j].configure(text=hardQ[element_choice][button_index[j]],
                                         value=hardQ[element_choice][button_index[j]])
            indexes.remove(element_choice)

            y = count_down()
            if y == -1:
                display()

    def count_down():
        check = 0
        for k in range(10, 0, -1):

            if k == 1:
                check = -1
            timer.configure(text=k)
            level_frame.update()
            time.sleep(1)

        timer.configure(text="Times up!")
        if check == -1:
            return -1
        else:
            return 0


    global l
    l = Tk()
    l.title('Quiz App - Easy Level')

    level_canvas = Canvas(l, width=700, height=700, bg="#4257b2")
    level_canvas.pack()

    level_frame = Frame(level_canvas, bg="#4257b2")
    level_frame.place(relwidth=0.85, relheight=0.85, relx=0.1, rely=0.1)

    global score
    score = 0
    indexes = [0, 1, 2, 3, 4]
    choice = random.choice(indexes)

    quiz_station = Label(level_canvas, text=' Q U I Z  S T A T I O N ', fg="white", bg="#4257b2")
    quiz_station.config(font=('yu gothic ui', 22, 'bold'))
    quiz_station.place(relx=0.3, rely=0.02)

    if quiz_level == "easy":
        question = Label(level_frame, text=easyQ[choice][0], font=('yu gothic ui', 13, 'bold'), bg="#4257b2", fg="white")
    elif quiz_level == "medium":
        question = Label(level_frame, text=mediumQ[choice][0], font=('yu gothic ui', 13, 'bold'), bg="#4257b2",
                         fg="white")
    else:
        question = Label(level_frame, text=hardQ[choice][0], font=('yu gothic ui', 13, 'bold'), bg="#4257b2",
                         fg="white")
    question.place(relx=0.5, rely=0.25, anchor=CENTER)

    var = StringVar()
    button_index = [1, 2, 3, 4]
    button_color = ["#fffc33", "red", "orange", "purple"]
    button_coordinate = [0.42, 0.52, 0.62, 0.72]
    options = []
    for i in range(0, len(button_index)):
        if quiz_level == "easy":
            option = Radiobutton(level_frame, text=easyQ[choice][button_index[i]], bg="#4257b2",
                                 font=('yu gothic ui', 14, 'bold'), value=easyQ[choice][button_index[i]],
                                 variable=var, selectcolor="white", fg=button_color[i])
        elif quiz_level == "medium":
            option = Radiobutton(level_frame, text=mediumQ[choice][button_index[i]], bg="#4257b2",
                                 font=('yu gothic ui', 14, 'bold'), value=easyQ[choice][button_index[i]],
                                 variable=var, selectcolor="white", fg=button_color[i])
        else:
            option = Radiobutton(level_frame, text=hardQ[choice][button_index[i]], bg="#4257b2",
                                 font=('yu gothic ui', 14, 'bold'), value=easyQ[choice][button_index[i]],
                                 variable=var, selectcolor="white", fg=button_color[i])
        option.place(relx=0.5, rely=button_coordinate[i], anchor=CENTER)
        options.append(option)
    indexes.remove(choice)

    timer = Label(l, bg="black", fg="white")
    timer.place(relx=0.53, rely=0.15, anchor=CENTER)

    submit_button = Button(level_frame, text="Submit", padx=5, pady=5, width=5, command=calc, fg="white",
                           bg="black")
    submit_button.place(relx=0.5, rely=0.82, anchor=CENTER)

    next_question = Button(level_frame, text="Next", padx=5, pady=5, width=5,
                           command=display,
                           fg="white", bg="black")
    next_question.place(relx=0.9, rely=0.82, anchor=CENTER)

    y = count_down()
    if y == -1:
        display()
    l.mainloop()