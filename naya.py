# importing modules
import tkinter
import PIL
from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as tmsg
import mysql.connector as con
import random as rd
# database = con.connect(
#    host="localhost",
#    user="root",
#    passwd="Trush@9k"
# )

class GUI(Tk):
    def __init__(self):
        super().__init__()
        # All the basic requirements
        self.title("Quiz Game for Cs")
        self.wm_iconbitmap("trophy.ico")
        self.geometry("1024x768")
        self.minsize(400, 300)
        self.maxsize(1024, 768)
        self.config(background="#ffffff")

    def welcome(self):
        def covid_quiz(self):
            pass

        def exitgame(self):
            self.destroy()

        def ranking(self):
            pass

        def credit(self):
            pass

        def rule(self):
            tmsg.showinfo("Rules",
                          "1.\n2.\n3.\n")

        def start_is_pressed(self):
            logo_label.destroy()
            title_label.destroy()
            start_button.destroy()
            exit_button.destroy()
            ranking_button.destroy()
            credit_button.destroy()
            rule_button.destroy()
            entry_for_mysql()
            self.geometry("400x300")
            # startquiz()
        # WELCOME WINDOW
        # LOGO for the quiz game

        logo_label = Label(
            self,
            image=photo1,
            background="#ffffff"
        )
        logo_label.pack()
        # title for the game
        title_label = Label(
            self,
            text="Quiz game for Cs",
            background="#ffffff",
            font=("Script MT Bold", 42, "bold")
        )
        title_label.pack()

        # Start Button

        start_button = Button(
            self,
            image=photo2,
            command=start_is_pressed
        )
        start_button.pack(pady=20)

        # Exit Button

        exit_button = Button(
            self,
            image=photo3,
            command=exitgame
        )
        exit_button.pack(side=BOTTOM,
                         pady=57)

        # ranking button

        ranking_button = Button(
            self,
            image=photo4,
            command=ranking
        )
        ranking_button.place(x=25, y=617)

        # credits Button

        credit_button = Button(
            self,
            image=photo5,
            command=credit
        )
        credit_button.place(x=700, y=616)

        # Rule Button

        rule_button = Button(
            self,
            image=photo6,
            relief=FLAT,

            command=rule
        )
        rule_button.place(x=925, y=17)

    def entry_for_mysql(self):
        def getvals():
            print(f"The value of username is {uservalue.get()}")
            print(f"The value of password is {passvalue.get()}")
            # mysql connector goes here
            userentry.destroy()
            passentry.destroy()
            user.destroy()
            password.destroy()
            submit_button.destroy()
            self.geometry("1024x768")
            real_game_starts_here()

        user = Label(self,
                    text="Username",
                    font=("Berlin Sans FB", 13)
                     )
        password = Label(self,
                        text="Password",
                        font=("Berlin Sans FB", 13)
                        )
        user.grid(row=1, column=2)
        password.grid(row=2, column=2)

        uservalue = StringVar()
        passvalue = StringVar()

        userentry = Entry(self,
                      textvariable=uservalue,
                      font=("default", 20)
                        )
        passentry = Entry(self,
                      textvariable=passvalue,
                      font=("default", 20)
                        )

        userentry.grid(row=1, column=3)
        passentry.grid(row=2, column=3)

        submit_button = Button(
            self,
            text="Submit",
            command=getvals,
            font=("Berlin Sans FB", 15)
             )
        submit_button.grid(row=3, column=3, pady=20,)


        def real_game_starts_here(self):
        # Primary_label
            primary_label = Label(
                self,
                background = "#ffffff",
                border = 1
                )
            primary_label.pack()
            # covid quiz

            covid_quiz_button = Button(
                primary_label,
            image=photo7,
            command=covid_quiz
            )
            covid_quiz_button.pack()



if __name__ == '__main__':
    window = GUI()
    jpeg_image6 = Image.open("7.jpg")
    photo7 = ImageTk.PhotoImage(jpeg_image6)
    jpeg_image5 = Image.open("6.jpg")
    photo6 = ImageTk.PhotoImage(jpeg_image5)
    jpeg_image4 = Image.open("5.jpg")
    photo5 = ImageTk.PhotoImage(jpeg_image4)
    jpeg_image3 = Image.open("4.jpg")
    photo4 = ImageTk.PhotoImage(jpeg_image3)
    jpeg_image1 = Image.open("2.jpg")
    photo2 = ImageTk.PhotoImage(jpeg_image1)
    photo1 = PhotoImage(file="1.png")
    window.welcome()
    window.mainloop()