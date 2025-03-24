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
        # Frame include nhapvanban, vanbanmahoa, tinhnang

    frame2 = Frame(frame, bg="violet", padx=2, pady=2, bd=1, relief="solid")
    frame2.grid(row=1, column=0, sticky="nsew")
    frame2.grid_rowconfigure(0, weight=1)
    frame2.grid_rowconfigure(1, weight=1)
    frame2.grid_columnconfigure(0, weight=1)
    frame2.grid_columnconfigure(1, weight=1)
    # Frame include nhapvanban
    nhapvanban_frame = Frame(frame2, padx=1, pady=20, bd=1, relief="solid")
    nhapvanban_frame.grid(row=0, column=0, sticky="nsew")
    for i in range(5):
        nhapvanban_frame.grid_rowconfigure(i, weight=1)
    nhapvanban_frame.grid_columnconfigure(0, weight=1)
    nhapvanban_frame.grid_columnconfigure(1, weight=4)
    nhapvanban_frame.grid_columnconfigure(2, weight=1)
    Frame_label_nvb = Frame(nhapvanban_frame)
    Frame_label_nvb.grid(row=0, column=1, sticky="ew")
    label_nvb = Label(Frame_label_nvb, text="File", font=("Arial", 20))
    label_nvb.pack(side="left", fill="y")

    inputt1 = Text(nhapvanban_frame, wrap="word", height=6)
    inputt1.grid(row=2, column=1, rowspan=2, sticky="ew")

    inputt2 = Text(nhapvanban_frame, wrap="word", height=6)
    inputt2.grid(row=4, column=1, rowspan=2, sticky="ew")

    # Frame include button tinh nang
    tinhnang_frame = Frame(frame2, padx=2, pady=20, bd=1, relief="solid")
    tinhnang_frame.grid(row=0, column=1, sticky="nsew", rowspan=2)
    for i in range(6):
        tinhnang_frame.grid_rowconfigure(i, weight=1)
    for i in range(3):
        tinhnang_frame.grid_columnconfigure(i, weight=1)

    button = Button(tinhnang_frame, text="Nhập file gốc", font=("Arial", 14), command=lambda: getfile(inputt1))
    button.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

    button = Button(tinhnang_frame, text="Nhập file cần kiểm tra", font=("Arial", 14), command=lambda: getfile(inputt2))
    button.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

    button = Button(tinhnang_frame, text="Kiểm tra toàn vẹn", font=("Arial", 14), command=checktv)
    button.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")

    # Frame include vanbanmahoa
    vanbanmahoa_frame = Frame(frame2, padx=2, pady=20, bd=1, relief="solid")
    vanbanmahoa_frame.grid(row=1, column=0, sticky="nsew")
    for i in range(5):
        vanbanmahoa_frame.grid_rowconfigure(i, weight=1)
    vanbanmahoa_frame.grid_columnconfigure(0, weight=1)
    vanbanmahoa_frame.grid_columnconfigure(1, weight=4)
    vanbanmahoa_frame.grid_columnconfigure(2, weight=1)

    Frame_label_vbmh = Frame(vanbanmahoa_frame)
    Frame_label_vbmh.grid(row=0, column=1, sticky="ew")
    label_vbmh = Label(Frame_label_vbmh, text="Trạng thái", font=("Arial", 20))
    label_vbmh.pack(side="left", fill="y")
    outputt = Text(vanbanmahoa_frame, wrap="word", height=10)
    outputt.grid(row=2, column=1, rowspan=2, sticky="ew")




    frames["checktv"]=frame