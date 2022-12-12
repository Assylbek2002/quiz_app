import sqlite3
from tkinter import *
from levels import *


def signup():
    window.destroy()
    global sign_up
    sign_up = Tk()
    sign_up.title("Sign Up")
    sign_up_canvas = Canvas(sign_up, width=700, height=700, bg="#4257b2")
    sign_up_canvas.pack()

    sign_up_frame = Frame(sign_up_canvas, bg="#4257b2")
    sign_up_frame.place(anchor=CENTER, relheight=0.8, relwidth=0.8, relx=0.5, rely=0.5)

    full_name = StringVar()
    username = StringVar()
    password = StringVar()

    heading = Label(sign_up_frame, text="Quiz Application", fg="white", bg="#4257b2")
    heading.config(font=('calibri 40'))
    heading.place(relx=0.2, rely=0.1)

    full_name_label = Label(sign_up_frame, text="Full Name", fg="white", bg="#4257b2", font=('yu gothic ui', 10, 'bold'))
    full_name_label.place(relx=0.18, rely=0.4)

    full_name_entry = Entry(sign_up_frame, highlightthickness=0, bg="#4257b2", fg='white', textvariable=full_name,
                            relief=FLAT, font=('yu gothic ui', 10, 'bold'))
    full_name_entry.config(width=42)
    full_name_entry.place(relx=0.31, rely=0.4)

    full_name_line = Canvas(sign_up_frame, width=300, height=2.0, bg="white", highlightthickness=0)
    full_name_line.place(relx=0.31, rely=0.440)

    username_label = Label(sign_up_frame, text="Username", fg="white", bg="#4257b2", font=('yu gothic ui', 10, 'bold'))
    username_label.place(relx=0.18, rely=0.5)

    user = Entry(sign_up_frame, bg="#4257b2", fg='white', textvariable=username, highlightthickness=0,
                 relief=FLAT, font=('yu gothic ui', 10, 'bold'))
    user.config(width=42)
    user.place(relx=0.31, rely=0.5)

    username_line = Canvas(sign_up_frame, width=300, height=2.0, bg="white", highlightthickness=0)
    username_line.place(relx=0.31, rely=0.54)

    password_label = Label(sign_up_frame, text="Password", fg="white", bg="#4257b2", font=('yu gothic ui', 10, 'bold'))
    password_label.place(relx=0.18, rely=0.6)

    password_entry = Entry(sign_up_frame, bg="#4257b2", fg='white', textvariable=password, show="*",
                           relief=FLAT, font=('yu gothic ui', 10, 'bold'))
    password_entry.config(width=42)
    password_entry.place(relx=0.31, rely=0.6)

    password_line = Canvas(sign_up_frame, width=300, height=2.0, bg="white", highlightthickness=0)
    password_line.place(relx=0.31, rely=0.64)

    def go_to_login():
        conn = sqlite3.connect("quiz_app.db")
        cur = conn.cursor()
        conn.commit()
        cur.execute('SELECT * FROM users')
        users = cur.fetchall()
        login(users)

    def add_user_to_database():
        check_values(full_name, username, password)
        conn = sqlite3.connect('quiz_app.db')
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS users(FULLNAME text, USERNAME text,PASSWORD text)')
        cur.execute("INSERT INTO users VALUES (?,?,?)", (full_name.get(), username.get(), password.get()))
        conn.commit()
        cur.execute('SELECT * FROM users')
        users = cur.fetchall()
        print(users)
        conn.close()
        login(users)

    sign_up_button = Button(sign_up_frame, text="Sign Up", command=add_user_to_database, bg="white", fg="black")
    sign_up_button.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)
    sign_up_button.place(relx=0.4, rely=0.8)

    already_have_account_button = Button(sign_up_frame, text='Already have an Account?', font=('yu gothic ui', 10, 'bold'),
                                         fg="white", bg="#4257b2", cursor="hand2", activebackground="#4257b2", bd=0,
                                         command=go_to_login)
    already_have_account_button.place(relx=0.36, rely=0.9)


def login(users_data):
    sign_up.destroy()
    global log_in
    log_in = Tk()
    log_in.title("Quiz App Login")

    username = StringVar()
    password = StringVar()

    log_in_canvas = Canvas(log_in, width=700, height=700, bg="#4257b2")
    log_in_canvas.pack()

    log_in_frame = Frame(log_in_canvas, bg="#4257b2")
    log_in_frame.place(anchor=CENTER, relheight=0.8, relwidth=0.8, relx=0.5, rely=0.5)

    heading = Label(log_in_frame, text="Log in", fg="white", bg="#4257b2")
    heading.config(font=('calibri 40'))
    heading.place(relx=0.2, rely=0.2)

    username_label = Label(log_in_frame, text="Username", fg="white", bg="#4257b2", font=('yu gothic ui', 10, 'bold'))
    username_label.place(relx=0.18, rely=0.5)

    user = Entry(log_in_frame, bg="#4257b2", fg='white', textvariable=username, highlightthickness=0,
                 relief=FLAT, font=('yu gothic ui', 10, 'bold'))
    user.config(width=42)
    user.place(relx=0.31, rely=0.5)

    username_line = Canvas(log_in_frame, width=300, height=2.0, bg="white", highlightthickness=0)
    username_line.place(relx=0.31, rely=0.54)

    password_label = Label(log_in_frame, text="Password", fg="white", bg="#4257b2", font=('yu gothic ui', 10, 'bold'))
    password_label.place(relx=0.18, rely=0.6)

    password_entry = Entry(log_in_frame, bg="#4257b2", fg='white', textvariable=password, show="*",
                           relief=FLAT, font=('yu gothic ui', 10, 'bold'))
    password_entry.config(width=42)
    password_entry.place(relx=0.31, rely=0.6)

    password_line = Canvas(log_in_frame, width=300, height=2.0, bg="white", highlightthickness=0)
    password_line.place(relx=0.31, rely=0.64)

    def check():
        for full_name, name, pas in users_data:
            if name == username.get() and pas == password.get():
                print(users_data)
                main_page(name)
                break
            else:
                error = Label(log_in_frame, text="Wrong Username or Password!", fg='black', bg='white')
                error.place(relx=0.37, rely=0.7)

    log = Button(log_in_frame, text='Login', padx=5, pady=5, width=5, command=check, fg="white", bg="black")
    log.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)
    log.place(relx=0.4, rely=0.7)


def check_values(full_name, username, password):
    if len(full_name.get()) == 0 and len(username.get()) == 0 and len(password.get()) == 0:
        error = Label(text="You haven't enter any field...Please Enter all the fields", fg='black', bg='white')
        error.place(relx=0.37, rely=0.7)

    elif len(full_name.get()) == 0 or len(username.get()) == 0 or len(password.get()) == 0:
        error = Label(text="Please Enter all the fields", fg='black', bg='white')
        error.place(relx=0.37, rely=0.7)

    elif len(full_name.get()) == 0 and len(password.get()) == 0:
        error = Label(text="Username and password can't be empty", fg='black', bg='white')
        error.place(relx=0.37, rely=0.7)

    elif len(username.get()) == 0 and len(password.get()) != 0:
        error = Label(text="Username can't be empty", fg='black', bg='white')
        error.place(relx=0.37, rely=0.7)

    elif len(username.get()) != 0 and len(password.get()) == 0:
        error = Label(text="Password can't be empty", fg='black', bg='white')
        error.place(relx=0.37, rely=0.7)


def main_page(username):
    log_in.destroy()
    global menu
    menu = Tk()
    menu.title("Main page")

    menu_canvas = Canvas(menu, width=700, height=700, bg="#4257b2")
    menu_canvas.pack()

    menu_frame = Frame(menu_canvas,bg="#4257b2")
    menu_frame.place(anchor=CENTER, relheight=0.8, relwidth=0.8, relx=0.5, rely=0.5)

    welcome = Label(menu_canvas, text=' W E L C O M E  T O  Q U I Z  S T A T I O N ', fg="white", bg="#4257b2")
    welcome.config(font=('yu gothic ui', 22, 'bold'))
    welcome.place(relx=0.1, rely=0.02)

    greet_username = "Welcome " + username

    greet_username_label = Label(menu_frame, text=greet_username, bg="#4257b2", font=('yu gothic ui', 15, 'bold'), fg="white")
    greet_username_label.place(relx=0.05, rely=0.15)

    select_level = Label(menu_frame, text='Select your Level', bg="#4257b2", font=('yu gothic ui', 15, 'bold'),
                  fg="white")
    select_level.place(relx=0.05, rely=0.25)

    var = IntVar()

    text_level = ["Easy", "Medium", "Hard"]
    text_place = [0.4, 0.5, 0.6]
    text_color = ["green", "orange", "red"]

    for i in range(0, len(text_level)):
        button = Radiobutton(menu_frame, text=text_level[i], bg=text_color[i], font=('yu gothic ui', 15, 'bold'),
                             value=i + 1, variable=var, fg="white", selectcolor=text_color[i])
        button.place(relx=0.05, rely=text_place[i])

    def navigate():
        x = var.get()
        print(x)
        if x == 1:
            menu.destroy()
            level("easy")
        elif x == 2:
            menu.destroy()
            level("medium")
        elif x == 3:
            menu.destroy()
            level("hard")
        else:
            pass

    start_game = Button(menu_frame, text="Let's Go", padx=5, pady=5, width=5, command=navigate, fg="white", bg="black")
    start_game.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)
    start_game.place(relx=0.70, rely=0.8)
    menu.mainloop()


def exit_quiz():
    window.destroy()


def start():
    global window
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


if __name__=='__main__':
    start()