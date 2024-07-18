from tkinter import *
from tkinter import ttk
import time
import random
import difflib



class MainWindow:
    def __init(self, root):
        self.text = ["Success is not final, failure is not fatal: It is the courage to continue that counts.",
                    "The greatest glory in living lies not in never falling, but in rising every time we fall.",
                     "The way to get started is to quit talking and begin doing.",
                     "Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma – which is living with the results of other people's thinking.",
                     "If life were predictable it would cease to be life, and be without flavor.",
                     "If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough.",
                     "If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success.",
                     "Life is what happens when you're busy making other plans.",
                     "One day the people that don’t even believe in you will tell everyone how they met you.",
                     "The true meaning of life is to plant trees, under whose shade you do not expect to sit.",
                     "Challenges are what make life interesting and overcoming them is what makes life meaningful."]
        
        self.speed = 0
        self.accuracy = 0
        self.time_start = 0
        self.time_end = 0
        root.title("Python GUI")
        root.minsize(500, 500)
        for row in range(5):
            root.grid_rowconfigure(row, wight=1)
        for col in range(3):
            root.grid_columnfigure(col, weight=1)
        self.label_text = Label(
            root, text="Welcome to typeing speed calculator", wraplength=500)
        self.label_text.grid(row=0, column=0, columnspan=3, sticky="nsew")

        self.user_text = Text(root)
        self.user_text.grid(column=0, row=1, columnspan=3, sticky="nsew")

        self.btn_start = Button(root, text="Start/Restart", command=self.start)
        self.btn_start.grid(colmn=0, row=2, columnspan=1, sticky="nsew")
        self.btn_stop = Button(root, text="Stop", command=self.stop)
        self.btn_stop.grid(column=1, row=2, columnspan=1, sticky="nsew")
        self.btn_newtext = Button(root, text="New Text", command=self.new_text)
        self.btn_newtext.grid(column=2, row=2, columnspan=1, sticky="nsew")

        self.label_speed = Label(
            root, text=f"Your typing speed is {self.speed} WPM")
        self.label_speed.grid(row=3, column=0, columnspan=3, sticky="nsew")

        self.label_accuracy = Label(
            root, text=f"Your typing accuracy is {self.speed} %")
        self.label_accuracy.grid(row=4, column=0, columnspan= 3, sticky="nsew")

        def start(self):
            self.time_end = time.time()
            


