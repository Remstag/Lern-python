from tkinter import *
from tkinter import  Button, filedialog

from PIL.ImageOps import expand

from Graphic.AES import AES_Algorithm
import random
import os
import string
import secrets
frames={}
def mahoavb(main_content,giatricu):
    frame = Frame(main_content)
    frame.grid(row=0, column=0, sticky="nsew")
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_rowconfigure(1, weight=3)
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
            text = AES_Algorithm.mahoa(text, keyb, ivb)
            output.delete("1.0", "end")
            output.insert("end", text)
        except Exception as e:
            output.delete("1.0", "end")
            output.insert("end", "Lỗi rồi duma")

    def setkey():
        entry_key.delete("1.0", "end")
        random_key = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
        entry_key.insert("end", random_key)
        entry_key.tag_add("custom_font", "1.0", "end")
        entry_key.tag_configure("custom_font", font=("Arial", 13))

    def setiv():
        entry_iv.delete("1.0", "end")
        random_iv = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        entry_iv.insert("end", random_iv)
        entry_iv.tag_add("custom_font", "1.0", "end")
        entry_iv.tag_configure("custom_font", font=("Arial", 13))

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

    #Frame include nhapkey, nhapiv: label, text, button
    nhapkeyiv_frame = Frame(frame,padx=2,pady=10,bd=1,relief="solid")
    nhapkeyiv_frame.grid(row=0,column=0,sticky="nsew")
    for i in range(5):
        if i%2==0:
            nhapkeyiv_frame.grid_rowconfigure(i, weight=1)
        else:
            nhapkeyiv_frame.grid_rowconfigure(i, weight=6)
    for i in range(7):
        if i%2==0:
            nhapkeyiv_frame.grid_columnconfigure(i, weight=1)
        else:
            nhapkeyiv_frame.grid_columnconfigure(i, weight=3)
    #Label key, text key, button key
    label_key = Label(nhapkeyiv_frame, text="KEY", font=("Arial",20))
    label_key.grid(row=1,column=1,sticky="w")
    entry_key = Text(nhapkeyiv_frame, wrap="word", height=2, width=60)
    entry_key.grid(row=1,column=3)
    button_key = Button(nhapkeyiv_frame, text="Tạo key", font=("Arial",14),command=setkey)
    button_key.grid(row=1,column=5,sticky="ew")
    #Label iv, text iv, button iv
    label_iv = Label(nhapkeyiv_frame, text="IV", font=("Arial",20))
    label_iv.grid(row=3,column=1,sticky="w")
    entry_iv = Text(nhapkeyiv_frame, wrap="word", height=2, width=60)
    entry_iv.grid(row=3, column=3)
    button_iv = Button(nhapkeyiv_frame, text="Tạo iv", font=("Arial",14), command=setiv)
    button_iv.grid(row=3,column=5,sticky="ew")

    #Frame include nhapvanban, vanbanmahoa, tinhnang
    frame2 = Frame(frame,bg="violet",padx=2,pady=2,bd=1,relief="solid")
    frame2.grid(row=1,column=0,sticky="nsew")
    frame2.grid_rowconfigure(0,weight=1)
    frame2.grid_rowconfigure(1,weight=1)
    frame2.grid_columnconfigure(0,weight=1)
    frame2.grid_columnconfigure(1,weight=1)
    #Frame include nhapvanban
    nhapvanban_frame = Frame(frame2, padx=2, pady=20,bd=1,relief="solid")
    nhapvanban_frame.grid(row=0,column=0,sticky="nsew")
    for i in range(5):
        nhapvanban_frame.grid_rowconfigure(i, weight=1)
    nhapvanban_frame.grid_columnconfigure(0,weight=1)
    nhapvanban_frame.grid_columnconfigure(1, weight=4)
    nhapvanban_frame.grid_columnconfigure(2, weight=1)
    Frame_label_nvb = Frame(nhapvanban_frame)
    Frame_label_nvb.grid(row=0,column=1,sticky="ew")
    label_nvb = Label(Frame_label_nvb, text="Bản rõ", font=("Arial",20))
    label_nvb.pack(side="left",fill="y")

    entry = Text(nhapvanban_frame, wrap="word", height=10)
    entry.grid(row=2,column=1,rowspan=2,sticky="ew")

    #Frame include button tinh nang
    tinhnang_frame = Frame(frame2,padx=2,pady=20,bd=1,relief="solid")
    tinhnang_frame.grid(row=0,column=1,sticky="nsew",rowspan=2)
    for i in range(6):
        tinhnang_frame.grid_rowconfigure(i,weight=1)
    for i in range(3):
        tinhnang_frame.grid_columnconfigure(i,weight=1)
    button = Button(tinhnang_frame, text="Mã hóa", font=("Arial",14),command=get)
    button.grid(row=0,column=1,padx=5, pady=5,sticky="nsew")

    button = Button(tinhnang_frame, text="Lấy lại giá trị", font=("Arial",14),command=settlaigiatri)
    button.grid(row=1,column=1,padx=5, pady=5,sticky="nsew")

    button = Button(tinhnang_frame, text="Tạm lưu", font=("Arial",14),command=tamluu)
    button.grid(row=2,column=1,padx=5, pady=5,sticky="nsew")

    button = Button(tinhnang_frame, text="Nhập file", font=("Arial",14),command=mhfile)
    button.grid(row=3,column=1,padx=5, pady=5,sticky="nsew")

    button = Button(tinhnang_frame, text="Mã hóa tiếp", font=("Arial",14),command=sett)
    button.grid(row=4,column=1,padx=5, pady=5,sticky="nsew")

    button = Button(tinhnang_frame, text="Lưu vào file", font=("Arial",14),command=savefile)
    button.grid(row=5,column=1,padx=5, pady=5,sticky="nsew")

    #Frame include vanbanmahoa
    vanbanmahoa_frame = Frame(frame2, padx=2, pady=20,bd=1,relief="solid")
    vanbanmahoa_frame.grid(row=1,column=0,sticky="nsew")
    for i in range(5):
        vanbanmahoa_frame.grid_rowconfigure(i, weight=1)
    vanbanmahoa_frame.grid_columnconfigure(0,weight=1)
    vanbanmahoa_frame.grid_columnconfigure(1, weight=4)
    vanbanmahoa_frame.grid_columnconfigure(2, weight=1)

    Frame_label_vbmh = Frame(vanbanmahoa_frame)
    Frame_label_vbmh.grid(row=0, column=1, sticky="ew")
    label_vbmh = Label(Frame_label_vbmh, text="Bản mã hóa", font=("Arial", 20))
    label_vbmh.pack(side="left", fill="y")
    output = Text(vanbanmahoa_frame, wrap="word", height=10)
    output.grid(row=2, column=1, rowspan=2, sticky="ew")


    # #Frame label nhapkey, nhapiv
    # label_frame = Frame(frame)
    # label_frame.pack(side="top", fill="x")  # Dùng fill="x" để giãn đều
    #
    # label_key = Label(label_frame, text="Nhập key (đủ 32 kí tự):", font=("Arial", 20))
    # label_key.pack(side="left", expand=True)
    #
    # label_iv = Label(label_frame, text="Nhập IV (đủ 16 kí tự):", font=("Arial", 20))
    # label_iv.pack(side="left", expand=True)
    #
    # #Frame text nhapkey, nhapiv
    # text_frame = Frame(frame)
    # text_frame.pack(side="top", fill="x", pady=5)
    #
    # entry_key = Text(text_frame, wrap="word", height=2, width=60)
    # entry_key.pack(side="left", expand=True, padx=5)
    #
    # entry_iv = Text(text_frame, wrap="word", height=2, width=60)
    # entry_iv.pack(side="left", expand=True, padx=5)
    #
    #
    # spacer = Label(frame, text=" ")  # Một label rỗng để tạo khoảng cách
    # spacer.pack(pady=5)
    #
    # #button nhapkey nhapiv
    # button = Button(frame, text="Tạo key tự động", command=setkey)
    # button.place(x=250, y=90)
    # button = Button(frame, text="Tạo IV tự động", command=setiv)
    # button.place(x=950, y=90)
    #
    # labelbg = Label(frame, text="Nhập văn bản thử đi:", font=("Arial", 20))
    # labelbg.pack(pady=5)
    #
    # entry = Text(frame, wrap="word", height=8, width=50)
    # entry.pack(fill="x", padx=5, pady=5)
    # entry.pack(pady=5)
    #
    # spacer = Label(frame, text=" ")  # Một label rỗng để tạo khoảng cách
    # spacer.pack(pady=5)
    #
    # button = Button(frame, text="Mã hóa với AES", command=get)
    # button.place(x=300, y=310)
    #
    # button = Button(frame, text="Lấy lại giá trị", command=settlaigiatri)
    # button.place(x=500, y=310)
    #
    # button = Button(frame, text="Tạm lưu", command=tamluu)
    # button.place(x=600, y=310)
    #
    # button = Button(frame, text="Nhập file", command=mhfile)
    # button.place(x=700, y=310)
    #
    # button = Button(frame, text="Mã hóa tiếp", command=sett)
    # button.place(x=800, y=310)
    #
    # button = Button(frame, text="Lưu vào file", command=savefile)
    # button.place(x=900, y=310)
    #
    # labelbg = Label(frame, text="Văn bản đã mã hóa:", font=("Arial", 20))
    # labelbg.pack(pady=5)
    # output = Text(frame, wrap="word", height=10, width=50)
    # output.pack(fill="x", padx=5, pady=5)

    frames["mhvbaes"] = frame