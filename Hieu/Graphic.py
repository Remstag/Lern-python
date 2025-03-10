from BlowFish import *
import random
import os
import string
from tkinter import *
from tkinter import  Button, filedialog
import secrets
from importlib.metadata import entry_points
widgets = []
win=Tk()
frames = {}
def setup():
    win.title("BlowFish")
    win.geometry("1000x750")
    win.grid_rowconfigure(0, weight=1)
    win.grid_columnconfigure(0, weight=1)
def show_frame(page):
    frame = frames[page]
    frame.tkraise()  # Đưa frame lên trên
def inteface():
    butframe = Frame(win)
    butframe.grid(row=1, column=0, sticky="ew", pady=10)
    spacer = Label(butframe, text=" ")
    spacer.pack(side="left", padx=100, pady=100)
    b1 = Button(butframe, text="Mã hóa với BlowFish", command=lambda: show_frame("mhvbBF"))
    b1.pack(side="left", padx=10, pady=100)
    b2 = Button(butframe, text="Giải mã với BlowFish ", command=lambda: show_frame("gmvbBF"))
    b2.pack(side="left", padx=10, pady=5)
    show_frame("mhvbBF")
    win.mainloop()
