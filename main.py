# importing modules
import tkinter
import PIL
from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as tmsg
import json
from tkinter import filedialog
import random as rd
# database = con.connect(
#    host="localhost",
#    user="root",
#    passwd="Trush@9k"
# )


class Quiz:
    def __init__(self, master):
        self.opt_selected = IntVar()
        self.qn = 0
        self.correct = 0
        self.ques = self.create_q(master, self.qn)
        self.opts = self.create_options(master, 4)
        self.display_q(self.qn)
        self.button = Button(master, text="Back", command=self.back_btn)
        self.button.pack(side=BOTTOM)
        self.button = Button(master, text="Next", command=self.next_btn)
        self.button.pack(side=BOTTOM)

    def create_q(self, master, qn):
        w = Label(master, text=q[qn])
        w.pack(side=TOP)
        return w

    def create_options(self, master, n):
        b_val = 0
        b = []
        while b_val < n:
            btn = Radiobutton(master, text="foo", variable=self.opt_selected, value=b_val+1)
            b.append(btn)
            btn.pack(side=TOP, anchor="w")
            b_val = b_val + 1
        return b

    def display_q(self, qn):
        b_val = 0
        self.opt_selected.set(0)
        self.ques['text'] = q[qn]
        for op in options[qn]:
            self.opts[b_val]['text'] = op
            b_val = b_val + 1

    def check_q(self, qn):
        if self.opt_selected.get() == a[qn]:
            return True
        return False

    def print_results(self):
        print("Score: ", self.correct, "/", len(q))

    def back_btn(self):
        print("go back")

    def next_btn(self):
        if self.check_q(self.qn):
            print("Correct")
            self.correct += 1
        else:
            print("Wrong")
        self.qn = self.qn + 1
        if self.qn >= len(q):
            self.print_results()
        else:
            self.display_q(self.qn)


def welcome_window():
    def start_is_pressed():
        logo_label.destroy()
        title_label.destroy()
        start_button.destroy()
        exit_button.destroy()
        ranking_button.destroy()
        credit_button.destroy()
        rule_button.destroy()
        attach_new_quiz_button.destroy()
        entry_for_mysql()
        root.geometry("400x300")
        # startquiz()
    # logo
    logo_label = Label(
        root,
        image=photo1,
        background="#ffffff"
    )
    logo_label.pack()
    # title for the game
    title_label = Label(
        root,
        text="Quiz game for Cs",
        background="#ffffff",
        font=("Script MT Bold", 42, "bold")
    )
    title_label.pack()
    # Start Button
    start_button = Button(
        root,
        image=photo2,
        command=start_is_pressed
    )
    start_button.pack(pady=20)
    # Exit Button
    exit_button = Button(
        root,
        image=photo3,
        command=exitgame
    )
    exit_button.pack(side=BOTTOM,
                     pady=57)
    # Ranking Button
    ranking_button = Button(
        root,
        image=photo4,
        command=ranking
    )
    ranking_button.place(x=25, y=617)
    # credit button
    credit_button = Button(
        root,
        image=photo5,
        command=credit
    )
    credit_button.place(x=700, y=616)

    # rule button
    rule_button = Button(
        root,
        image=photo6,
        relief=FLAT,
        command=rule
    )
    rule_button.place(x=925, y=17)
    attach_new_quiz_button = Button(
        root,
        image=photo12,
        relief=FLAT,
        command=attach_new_quiz
    )
    attach_new_quiz_button.place(x=50, y=17)


def entry_for_mysql():
    def getvals():
        print(f"The value of username is {uservalue.get()}")
        print(f"The value of password is {passvalue.get()}")
        # mysql connector goes here
        userentry.destroy()
        passentry.destroy()
        user.destroy()
        password.destroy()
        submit_button.destroy()
        root.geometry("1024x768")
        real_game_starts_here()

    user = Label(root,
                 text="Username",
                 font=("Berlin Sans FB", 13,),
                 background="#ffffff"
                 )
    password = Label(root,
                     text="Password",
                     font=("Berlin Sans FB", 13),
                     background="#ffffff"
                     )
    user.grid(row=1, column=2)
    password.grid(row=2, column=2)

    uservalue = StringVar()
    passvalue = StringVar()

    userentry = Entry(root,
                      textvariable=uservalue,
                      font=("default", 20)
                      )
    passentry = Entry(root,
                      textvariable=passvalue,
                      font=("default", 20)
                      )

    userentry.grid(row=1, column=3)
    passentry.grid(row=2, column=3)

    submit_button = Button(text="Submit",
                           command=getvals,
                           font=("Berlin Sans FB", 15)
                           )
    submit_button.grid(row=3, column=3, pady=20,)


def real_game_starts_here():
    global primary_label

    # Primary_label
    primary_label = Label(
        root,
        background="#ffffff",
        border=1
    )
    primary_label.pack()
    # secondaru label
    sec_label = Label(
        primary_label,
        text=" Which Quiz will you like to play :",
        font=("Gabriola", 42, "bold"),
        background="#ffffff"
    )
    sec_label.grid()
    # covid quiz
    Label(primary_label, text="1.", font="Gabriola 48 bold", background="#ffffff").grid()
    Label(primary_label, text="2.", font="Gabriola 48 bold", background="#ffffff").grid()
    Label(primary_label, text="3.", font="Gabriola 48 bold", background="#ffffff").grid()
    Label(primary_label, text="4.", font="Gabriola 48 bold", background="#ffffff").grid()
    Label(primary_label, text="5.", font="Gabriola 48 bold", background="#ffffff").grid()
    covid_quiz_button = Button(
        primary_label,
        image=photo7,
        command=covid_quiz
    )
    covid_quiz_button.grid(row=1, column=2)
    # gk quiz
    gk_quiz_button = Button(
        primary_label,
        image=photo8,
        command=gk_quiz
    )
    gk_quiz_button.grid(row=2, column=2)
    # geography quiz
    geo_quiz_button = Button(
        primary_label,
        image=photo9,
        command=geo_quiz
    )
    geo_quiz_button.grid(row=3, column=2)
    # sportsquiz
    sport_quiz_button = Button(
        primary_label,
        image=photo10,
        command=sports_quiz
    )
    sport_quiz_button.grid(row=4, column=2)
    # literature quiz
    lit_quiz_button = Button(
        primary_label,
        image=photo11,
        command=lit_quiz
    )
    lit_quiz_button.grid(row=5, column=2)

# covid quiz
def covid_quiz():
    global q, a, options
    primary_label.pack_forget()
    with open("data.json") as f:
        data = json.load(f)
    q = [v for v in data[0].values()]
    a = [1,1,1,1,3,1,0,1,3,3]
    options = [v for v in data[1].values()]
    Quiz(root)

# GK quiz
def gk_quiz():
    global q, a, options
    primary_label.pack_forget()
    q = [
        "Capital of India",
        "South most city in India",
    ]

    options = [
        ["Delhi", "Mumbai", "Kolkata", "Chennai"],
        ["Delhi", "Mumbai", "Chennai", "Kanyakumari"],
    ]

    a = [1, 4]
    Quiz(root)

# geofraphy quiz
def geo_quiz():
    global q, a, options

    primary_label.pack_forget()
    q = [
        "Capital of maharashtra",
        "west most city in India",
    ]

    options = [
        ["6+6656565", "Mumbai", "Kolkata", "Chennai"],
        ["Delhi", "Mumbai", "Chennai", "kuchh"],
    ]
    a = [2, 4]
    chaliye_shuru_karte_hai = Quiz(root)
# sports quiz
def sports_quiz():
    primary_label.pack_forget()

# lit quiz
def lit_quiz():
    primary_label.pack_forget()


def attach_new_quiz():
    #file_name = filedialog.askopenfilename(
    #    initialdir="/C:/Users/user/PycharmProjects/CSProjectAim500",
    #    title="  ",
    #    filetypes=(("png",".png"),("all files","*.*"))
    #)
    pass


def exitgame():
    root.destroy()


def ranking():
    pass


def credit():
    pass


def rule():
    tmsg.showinfo("Rules",
                  "1.You can play only one quiz at a time "
                  "\n2.Once a question is answered you can't go back "
                  "3.JAi mata di let's rock")


if __name__ == '__main__':
    # All the basic requirements
    root = Tk()
    root.title("Quiz Game for Cs")
    root.wm_iconbitmap("trophy.ico")
    root.geometry("1024x768")
    root.minsize(400, 300)
    root.maxsize(1024, 768)
    root.config(background="#ffffff")
    # WELCOME WINDOW
    # LOGO for the quiz game
    photo1 = PhotoImage(file="1.png")
    # Start Button
    jpeg_image1 = Image.open("2.jpg")
    photo2 = ImageTk.PhotoImage(jpeg_image1)


    # Exit Button
    jpeg_image2 = Image.open("3.jpg")
    photo3 = ImageTk.PhotoImage(jpeg_image2)


    # ranking button
    jpeg_image3 = Image.open("4.jpg")
    photo4 = ImageTk.PhotoImage(jpeg_image3)

    # credits Button
    jpeg_image4 = Image.open("5.jpg")
    photo5 = ImageTk.PhotoImage(jpeg_image4)

    # Rule Button
    jpeg_image5 = Image.open("6.jpg")
    photo6 = ImageTk.PhotoImage(jpeg_image5)

    # Attach file button
    jpeg_image11 = Image.open("+.jpg")
    photo12 = ImageTk.PhotoImage(jpeg_image11)

    # COVID Image
    jpeg_image6 = Image.open("7.jpg")
    photo7 = ImageTk.PhotoImage(jpeg_image6)

    # GK image
    jpeg_image7 = Image.open("8.jpg")
    photo8 = ImageTk.PhotoImage(jpeg_image7)

    # Geography image
    jpeg_image8 = Image.open("9.jpg")
    photo9 = ImageTk.PhotoImage(jpeg_image8)

    # sports image
    jpeg_image9 = Image.open("10.jpg")
    photo10 = ImageTk.PhotoImage(jpeg_image9)

    # LITERATURE IMAGE
    jpeg_image10 = Image.open("11.jpg")
    photo11 = ImageTk.PhotoImage(jpeg_image10)

    welcome_window()
    root.mainloop()
