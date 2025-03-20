from tkinter import *
from tkinter import  Button, filedialog
import random
import os
import string
import secrets
import xoafile
frames={}
def xoafil(main_content):
    frame=Frame(main_content)
    frame.grid(row=0, column=0, sticky="nsew")
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    def layfile():
        file_path = filedialog.askopenfilename(title="Chọn file cần xóa")
        if file_path:
            inentry.delete("1.0", "end")
            inentry.insert("end", file_path)
    def xoa():
        file_path=inentry.get("1.0", "end").strip()
        file_path=file_path.replace("/","\\\\")
        if (xoafile.checkquyen(file_path)==True):
            xoafile.xoafilee(file_path)
            outentry.delete("1.0", "end")
            outentry.insert("end", xoafile.quyen+"\n"+xoafile.status)
        else:
            outentry.delete("1.0", "end")
            outentry.insert("end", xoafile.quyen + "\n" + xoafile.status)
    labelbg = Label(frame, text="Xóa file với chuẩn DoD 5220.22-M:", font=("Arial", 20))
    labelbg.pack(pady=5)

    inentry = Text(frame, wrap="word", height=2, width=50)
    inentry.pack(fill="x", padx=5, pady=5)

    spacer = Label(frame, text=" ")  # Một label rỗng để tạo khoảng cách
    spacer.pack(pady=5)

    button = Button(frame, text="Chọn file", command=layfile)
    button.place(x=650, y=100)

    button = Button(frame, text="Xóa file", command=xoa)
    button.place(x=550, y=100)

    outentry = Text(frame, wrap="word", height=4, width=50)
    outentry.pack(fill="x", padx=5, pady=5)

    frames["xfvsdod"] = frame