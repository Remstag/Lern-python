from tkinter import *
from tkinter import  Button, filedialog
from Graphic.BlowFish import BlowFish_Algorithm

frames={}
def giaimavbbf(main_content,giatricu):
    frame = Frame(main_content)
    frame.grid(row=0, column=0, sticky="nsew")
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_rowconfigure(1, weight=3)
    frame.grid_columnconfigure(0, weight=1)

    def settlaigiatri():
        entry.delete("1.0", "end")
        entry.insert("end", giatricu)

    def tamluu():
        global giatricu
        giatricu = output.get("1.0", "end")
    def gmfile():
        file_path = filedialog.askopenfilename(title="Chọn file để giải mã")
        if file_path:
            with open(file_path, "r", encoding="utf-8") as f:
                data = f.read()
            entry.delete("1.0", "end")
            entry.insert("end", data)

    def sett():
        entry.delete("1.0", "end")
        entry.insert("end", output.get("1.0", "end"))

    def get():
        try:
            keyy = entry_key.get("1.0", "end").strip()
            keyb = keyy.encode("utf-8")
            iiv = entry_iv.get("1.0", "end").strip()
            ivb = iiv.encode("utf-8")
            text = entry.get("1.0", "end-1c")
            text = BlowFish_Algorithm.giaima(text, keyb, ivb)
            output.delete("1.0", "end")
            output.insert("end", text)
        except Exception as e:
            output.delete("1.0", "end")
            output.insert("end", "Lỗi rồi duma")

    def savefile():
        file_path = filedialog.asksaveasfilename(defaultextension="txt",
                                                 filetypes=[("Text", "*txt"),
                                                            ("All file", "*.*")])
        if file_path:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(output.get("1.0", "end"))

    # Frame include nhapkey, nhapiv: label, text, button
    nhapkeyiv_frame = Frame(frame, padx=2, pady=10, bd=1, relief="solid")
    nhapkeyiv_frame.grid(row=0, column=0, sticky="nsew")
    for i in range(5):
        if i % 2 == 0:
            nhapkeyiv_frame.grid_rowconfigure(i, weight=1)
        else:
            nhapkeyiv_frame.grid_rowconfigure(i, weight=6)
    for i in range(7):
        if i % 2 == 0:
            nhapkeyiv_frame.grid_columnconfigure(i, weight=1)
        else:
            nhapkeyiv_frame.grid_columnconfigure(i, weight=3)
    # Label key, text key, button key
    label_key = Label(nhapkeyiv_frame, text="KEY", font=("Arial", 20))
    label_key.grid(row=1, column=1, sticky="w")
    entry_key = Text(nhapkeyiv_frame, wrap="word", height=2, width=60)
    entry_key.grid(row=1, column=3)
    # button_key = Button(nhapkeyiv_frame, text="Tạo key tự động", font=("Arial", 14), command=setkey)
    # button_key.grid(row=1, column=5, sticky="ew")
    # Label iv, text iv, button iv
    label_iv = Label(nhapkeyiv_frame, text="IV", font=("Arial", 20))
    label_iv.grid(row=3, column=1, sticky="w")
    entry_iv = Text(nhapkeyiv_frame, wrap="word", height=2, width=60)
    entry_iv.grid(row=3, column=3)
    # button_iv = Button(nhapkeyiv_frame, text="Tạo iv tự động", font=("Arial", 14), command=setiv)
    # button_iv.grid(row=3, column=5, sticky="ew")

    # Frame include nhapvanban, vanbanmahoa, tinhnang
    frame2 = Frame(frame, bg="violet", padx=2, pady=2, bd=1, relief="solid")
    frame2.grid(row=1, column=0, sticky="nsew")
    frame2.grid_rowconfigure(0, weight=1)
    frame2.grid_rowconfigure(1, weight=1)
    frame2.grid_columnconfigure(0, weight=1)
    frame2.grid_columnconfigure(1, weight=1)
    # Frame include nhapvanban
    nhapvanban_frame = Frame(frame2, padx=2, pady=20, bd=1, relief="solid")
    nhapvanban_frame.grid(row=0, column=0, sticky="nsew")
    for i in range(5):
        nhapvanban_frame.grid_rowconfigure(i, weight=1)
    nhapvanban_frame.grid_columnconfigure(0, weight=1)
    nhapvanban_frame.grid_columnconfigure(1, weight=4)
    nhapvanban_frame.grid_columnconfigure(2, weight=1)
    Frame_label_nvb = Frame(nhapvanban_frame)
    Frame_label_nvb.grid(row=0, column=1, sticky="ew")
    label_nvb = Label(Frame_label_nvb, text="Bản rõ", font=("Arial", 20))
    label_nvb.pack(side="left", fill="y")

    entry = Text(nhapvanban_frame, wrap="word", height=10)
    entry.grid(row=2, column=1, rowspan=2, sticky="ew")

    # Frame include button tinh nang
    tinhnang_frame = Frame(frame2, padx=2, pady=20, bd=1, relief="solid")
    tinhnang_frame.grid(row=0, column=1, sticky="nsew", rowspan=2)
    for i in range(6):
        tinhnang_frame.grid_rowconfigure(i, weight=1)
    for i in range(3):
        tinhnang_frame.grid_columnconfigure(i, weight=1)
    button = Button(tinhnang_frame, text="Giải mã", font=("Arial", 14), command=get)
    button.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

    button = Button(tinhnang_frame, text="Lấy lại giá trị", font=("Arial", 14), command=settlaigiatri)
    button.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

    button = Button(tinhnang_frame, text="Tạm lưu", font=("Arial", 14), command=tamluu)
    button.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")

    button = Button(tinhnang_frame, text="Nhập file", font=("Arial", 14), command=gmfile)
    button.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")

    button = Button(tinhnang_frame, text="Giải mã tiếp", font=("Arial", 14), command=sett)
    button.grid(row=4, column=1, padx=5, pady=5, sticky="nsew")

    button = Button(tinhnang_frame, text="Lưu vào file", font=("Arial", 14), command=savefile)
    button.grid(row=5, column=1, padx=5, pady=5, sticky="nsew")

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
    label_vbmh = Label(Frame_label_vbmh, text="Bản mã hóa", font=("Arial", 20))
    label_vbmh.pack(side="left", fill="y")
    output = Text(vanbanmahoa_frame, wrap="word", height=10)
    output.grid(row=2, column=1, rowspan=2, sticky="ew")

    frames["gmvbBF"] = frame