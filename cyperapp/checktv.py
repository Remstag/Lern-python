from tkinter import *
from tkinter import  Button, filedialog
import random
import os
import string
import secrets
import kiemtratinhtoanven as cheeck
frames={}
def kiemtrafile(main_content):
    frame = Frame(main_content)
    frame.grid(row=0, column=0, sticky="nsew")
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    def getfile(i):
        file_path = filedialog.askopenfilename(title="Chọn file")
        if file_path:
            i.delete("1.0", "end")
            i.insert("end", file_path)
    def checktv():
        file_path1 = inputt1.get("1.0", "end").strip()
        file_path1 = file_path1.replace("/", "\\\\")
        file_path2 = inputt2.get("1.0", "end").strip()
        file_path2 = file_path2.replace("/", "\\\\")
        hash_goc=cheeck.shaa256(file_path1)
        hash_cancheck=cheeck.shaa256(file_path2)
        if(hash_goc and hash_cancheck):
            if hash_goc == hash_cancheck:
                outputt.delete("1.0", "end")
                outputt.insert("end", "✅ File không bị thay đổi.")
            else:
                outputt.delete("1.0", "end")
                outputt.insert("end", "❌ File đã bị thay đổi!")
        else:
            outputt.delete("1.0", "end")
            outputt.insert("end", "❌Có lỗi xảy ra!")

    labelbg = Label(frame, text="Kiểm tra tính toàn vẹn của file với SHA-256:", font=("Arial", 20))
    labelbg.pack(pady=5)

    inputt1=Text(frame,wrap="word",height=2,width=50)
    inputt1.pack(fill="x",padx=5,pady=5)

    button=Button(frame,text="Chọn file gốc",command=lambda: getfile(inputt1))
    button.pack(pady=5)

    inputt2 = Text(frame, wrap="word", height=2, width=50)
    inputt2.pack(fill="x", padx=5, pady=5)

    button = Button(frame, text="Chọn file cần kiểm tra", command=lambda: getfile(inputt2))
    button.pack(pady=5)

    outputt = Text(frame, wrap="word", height=5, width=50)
    outputt.pack(fill="x", padx=5, pady=5)

    button = Button(frame, text="Kiểm tra tính toàn vẹn", command=checktv)
    button.pack(pady=5)

    frames["checktv"]=frame