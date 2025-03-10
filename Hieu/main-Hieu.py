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
def show_frame(page):
    frame = frames[page]
    frame.tkraise()  # Đưa frame lên trên
def mahoavb ():
        frame = Frame(win)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        def sett():
            entry.delete("1.0","end")
            entry.insert("end",output.get("1.0","end"))
        def get():
            try:
                keyy=entry_key.get("1.0","end").strip()
                keyb = keyy.encode("utf-8")
                iiv=entry_iv.get("1.0","end").strip()
                ivb=iiv.encode("utf-8")
                text = entry.get("1.0", "end-1c")
                text = Blowfish.mahoa(text,keyb,ivb)
                output.delete("1.0", "end")
                output.insert("end", text)
            except Exception as e:
                output.delete("1.0", "end")
                output.insert("end", "Lỗi rồi duma")
        def setkey():
            entry_key.delete("1.0","end")
            random_key = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
            entry_key.insert("end", random_key)
        def setiv():
            entry_iv.delete("1.0","end")
            random_iv = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
            entry_iv.insert("end", random_iv)
        def mhfile():
            file_path = filedialog.askopenfilename(title="Chọn file để mã hóa")
            if file_path:
                with open(file_path, "r",encoding="utf-8") as f:
                    data = f.read()
                entry.delete("1.0", "end")
                entry.insert("end", data)
        def savefile():
            file_path=filedialog.asksaveasfilename(defaultextension="txt",
                                                   filetypes=[("Text","*txt"),
                                                              ("All file","*.*")])
            if file_path:
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(output.get("1.0", "end"))

        label_frame = Frame(frame)
        label_frame.pack(side="top", fill="x")  # Dùng fill="x" để giãn đều

        label_key = Label(label_frame, text="Nhập key (đủ 32 kí tự):", font=("Arial", 20))
        label_key.pack(side="left", expand=True)

        label_iv = Label(label_frame, text="Nhập IV (đủ 16 kí tự):", font=("Arial", 20))
        label_iv.pack(side="left", expand=True)

        text_frame = Frame(frame)
        text_frame.pack(side="top", fill="x", pady=5)

        entry_key = Text(text_frame, wrap="word", height=2, width=60)
        entry_key.pack(side="left", expand=True, padx=5)

        entry_iv = Text(text_frame, wrap="word", height=2, width=60)
        entry_iv.pack(side="left", expand=True, padx=5)
        spacer = Label(frame, text=" ")  # Một label rỗng để tạo khoảng cách
        spacer.pack(pady=5)
        button = Button(frame, text="Tạo key tự động", command=setkey)
        button.place(x=200, y=90)
        button = Button(frame, text="Tạo IV tự động", command=setiv)
        button.place(x=700, y=90)
        labelbg =  Label(frame, text="Nhập văn bản thử đi:", font=("Arial", 20))
        labelbg.pack(pady=5)

        entry = Text(frame, wrap="word", height=10, width=50)
        entry.pack(fill="x",padx=5, pady=5)
        entry.pack(pady=5)

        spacer = Label(frame, text=" ")  # Một label rỗng để tạo khoảng cách
        spacer.pack(pady=5)

        button = Button(frame, text="Mã hóa với BlowFish", command=get)
        button.place(x=300, y=340)

        button = Button(frame, text="Nhập file", command=mhfile)
        button.place(x=700, y=340)

        button = Button(frame, text="Mã hóa tiếp", command=sett)
        button.place(x=800, y=340)

        button = Button(frame, text="Lưu vào file", command=savefile)
        button.place(x=900, y=340)

        output = Text(frame, wrap="word", height=10, width=50)
        output.pack(fill="x",padx=5, pady=5)

        frames["mhvb"] = frame
def giaimavb():
        frame = Frame(win)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        def gmfile():
            file_path = filedialog.askopenfilename(title="Chọn file để giải mã")
            if file_path:
                with open(file_path, "r",encoding="utf-8") as f:
                    data = f.read()
                entry.delete("1.0", "end")
                entry.insert("end", data)
        def sett():
            entry.delete("1.0","end")
            entry.insert("end",output.get("1.0","end"))
        def get():
            try:
                keyy = entry_key.get("1.0", "end").strip()
                keyb = keyy.encode("utf-8")
                iiv = entry_iv.get("1.0", "end").strip()
                ivb = iiv.encode("utf-8")
                text = entry.get("1.0", "end-1c")
                text = Blowfish.giaima(text,keyb,ivb)
                output.delete("1.0", "end")
                output.insert("end", text)
            except Exception as e:
                output.delete("1.0", "end")
                output.insert("end", "Lỗi rồi duma")
        def savefile():
            file_path=filedialog.asksaveasfilename(defaultextension="txt",
                                                   filetypes=[("Text","*txt"),
                                                              ("All file","*.*")])
            if file_path:
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(output.get("1.0", "end"))

        label_frame = Frame(frame)
        label_frame.pack(side="top", fill="x")  # Dùng fill="x" để giãn đều

        label_key = Label(label_frame, text="Nhập key (đủ 32 kí tự):", font=("Arial", 20))
        label_key.pack(side="left", expand=True)

        label_iv = Label(label_frame, text="Nhập IV (đủ 16 kí tự):", font=("Arial", 20))
        label_iv.pack(side="left", expand=True)

        text_frame = Frame(frame)
        text_frame.pack(side="top", fill="x", pady=5)

        entry_key = Text(text_frame, wrap="word", height=2, width=60)
        entry_key.pack(side="left", expand=True, padx=5)

        entry_iv = Text(text_frame, wrap="word", height=2, width=60)
        entry_iv.pack(side="left", expand=True, padx=5)

        labelbg = Label(frame, text="Nhập bản mã đi:", font=("Arial", 20))
        labelbg.pack(pady=5)

        entry = Text(frame, wrap="word", height=10, width=50)
        entry.pack(fill="x",padx=5, pady=5)

        spacer = Label(frame, text=" ")  # Một label rỗng để tạo khoảng cách
        spacer.pack(pady=5)

        button = Button(frame, text="Giải mã với BlowFish", command=get)
        button.place(x=300, y=310)

        button = Button(frame, text="Nhập file", command=gmfile)
        button.place(x=700, y=310)

        button = Button(frame, text="Giải mã tiếp", command=sett)
        button.place(x=800, y=310)

        button = Button(frame, text="Lưu vào file", command=savefile)
        button.place(x=900, y=310)

        output = Text(frame, wrap="word", height=10, width=50)
        output.pack(fill="x",padx=5, pady=5)

        frames["gmvb"] = frame

win.title("Test")
win.geometry("1000x750")
win.grid_rowconfigure(0, weight=1)
win.grid_columnconfigure(0, weight=1)
mahoavb()
giaimavb()
butframe = Frame(win)
butframe.grid(row=1, column=0, sticky="ew", pady=10)
spacer = Label(butframe, text=" ")
spacer.pack(side="left", padx=100, pady=100)
b1 = Button(butframe, text="Mã hóa với BlowFish", command=lambda: show_frame("mhvb"))
b1.pack(side="left", padx=10, pady=100)
b2 = Button(butframe, text="Giải mã với BlowFish ", command=lambda: show_frame("gmvb"))
b2.pack(side="left", padx=10, pady=5)
show_frame("mhvb")
win.mainloop()
