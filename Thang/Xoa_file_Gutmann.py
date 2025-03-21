from tkinter import *
from tkinter import Button, filedialog
import os
import Gutmann  # Import module xóa file Gutmann

frames = {}


def xoafilegutmann(main_content):
    frame = Frame(main_content)
    frame.grid(row=0, column=0, sticky="nsew")
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    def layfile():
        file_path = filedialog.askopenfilename(title="Chọn file cần xóa")
        if file_path:
            inentry.delete("1.0", "end")
            inentry.insert("end", file_path)

    def xoa():
        file_path = inentry.get("1.0", "end").strip()
        file_path = file_path.replace("/", "\\")

        if os.path.exists(file_path):
            Gutmann.gutmann_wipe(file_path)
            outentry.delete("1.0", "end")
            outentry.insert("end", f"File {file_path} đã được xóa an toàn bằng phương pháp Gutmann!\n")
        else:
            outentry.delete("1.0", "end")
            outentry.insert("end", "Lỗi: Không tìm thấy file!\n")

    labelbg = Label(frame, text="Xóa file với thuật toán Gutmann:", font=("Arial", 20))
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

    frames["xfvsgutmann"] = frame
