from tkinter import *
from tkinter import ttk
import time
import random
import difflib


class MainWindow:
    def __init(self, root):
        self.text = ["The greatest glory in living lies not in never falling, but in rising every time we fall.",
                     "The way to get started is to quit talking and begin doing.",
                     "Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma – which is living with the results of other people's thinking.",
                     "If life were predictable it would cease to be life, and be without flavor.",
                     "If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough.",
                     "If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success.",
                     "Life is what happens when you're busy making other plans.",
                     "One day the people that don’t even believe in you will tell everyone how they met you.",
                     "The true meaning of life is to plant trees, under whose shade you do not expect to sit.",
                     "The quick brown fox jumps over the lazy dog."]
        
        self.speed = 0
        self.accuracy = 0
        self.time_start = 0
        self.time_end = 0
        root.title("Python GUI")
        root.minsize(500, 500)