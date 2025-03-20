from tkinter import *
from tkinter import  Button, filedialog
import BlowFish
import random
import os
import string
import secrets
frames={}
def mahoavbbf(main_content):
    frame = Frame(main_content)
    frame.grid(row=0, column=0, sticky="nsew")
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    def sett():
        entry.delete("1.0", "end")
        entry.insert("end", output.get("1.0", "end"))

    def settlaigiatri():
        entry.delete("1.0", "end")
        entry.insert("end", giatricu)

    def tamluu():
        global giatricu
        giatricu = output.get("1.0", "end")

    def get():
        try:
            keyy = entry_key.get("1.0", "end").strip()
            keyb = keyy.encode("utf-8")
            iiv = entry_iv.get("1.0", "end").strip()
            ivb = iiv.encode("utf-8")
            text = entry.get("1.0", "end-1c")
            text = BlowFish.mahoa(text, keyb, ivb)
            output.delete("1.0", "end")
            output.insert("end", text)
        except Exception as e:
            output.delete("1.0", "end")
            output.insert("end", "Lỗi rồi duma")

    def setkey():
        entry_key.delete("1.0", "end")
        random_key = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
        entry_key.insert("end", random_key)

    def setiv():
        entry_iv.delete("1.0", "end")
        random_iv = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        entry_iv.insert("end", random_iv)

    def mhfile():
        file_path = filedialog.askopenfilename(title="Chọn file để mã hóa")
        if file_path:
            with open(file_path, "r", encoding="utf-8") as f:
                data = f.read()
            entry.delete("1.0", "end")
            entry.insert("end", data)

    def savefile():
        file_path = filedialog.asksaveasfilename(defaultextension="txt",
                                                 filetypes=[("Text", "*txt"),
                                                            ("All file", "*.*")])
        if file_path:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(output.get("1.0", "end"))

    label_frame = Frame(frame)
    label_frame.pack(side="top", fill="x")  # Dùng fill="x" để giãn đều

    label_key = Label(label_frame, text="Nhập key (đủ 32 kí tự):", font=("Arial", 20))
    label_key.pack(side="left", expand=True)

    label_iv = Label(label_frame, text="Nhập IV (đủ 8 kí tự):", font=("Arial", 20))
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
    button.place(x=250, y=90)
    button = Button(frame, text="Tạo IV tự động", command=setiv)
    button.place(x=950, y=90)
    labelbg = Label(frame, text="Nhập văn bản thử đi:", font=("Arial", 20))
    labelbg.pack(pady=5)

    entry = Text(frame, wrap="word", height=8, width=50)
    entry.pack(fill="x", padx=5, pady=5)
    entry.pack(pady=5)

    spacer = Label(frame, text=" ")  # Một label rỗng để tạo khoảng cách
    spacer.pack(pady=5)

    button = Button(frame, text="Mã hóa với BlowFish", command=get)
    button.place(x=300, y=310)

    button = Button(frame, text="Lấy lại giá trị", command=settlaigiatri)
    button.place(x=500, y=310)

    button = Button(frame, text="Tạm lưu", command=tamluu)
    button.place(x=600, y=310)

    button = Button(frame, text="Nhập file", command=mhfile)
    button.place(x=700, y=310)

    button = Button(frame, text="Mã hóa tiếp", command=sett)
    button.place(x=800, y=310)

    button = Button(frame, text="Lưu vào file", command=savefile)
    button.place(x=900, y=310)

    output = Text(frame, wrap="word", height=10, width=50)
    output.pack(fill="x", padx=5, pady=5)

    frames["mhvbBF"] = frame