from Triple_DES import *
import random
import os
import string
from tkinter import *
from tkinter import Button, filedialog
import secrets
from importlib.metadata import entry_points

widgets = []
win = Tk()
frames = {}


def setup():
    win.title("3-DES")
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

    b1 = Button(butframe, text="Mã hóa với 3-DES", command=lambda: show_frame("mhvb3DES"))
    b1.pack(side="left", padx=10, pady=100)

    b2 = Button(butframe, text="Giải mã với 3-DES", command=lambda: show_frame("gmvb3DES"))
    b2.pack(side="left", padx=10, pady=5)

    # Chỉ hiển thị frame sau khi tất cả frame đã được đăng ký
    if "mhvb3DES" in frames:
        show_frame("mhvb3DES")

    win.mainloop()