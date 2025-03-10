from BlowFish import *
import BlowFish
import mhAES
import random
import kiemtratinhtoanven as cheeck
import os
import string
from tkinter import *
from tkinter import  Button, filedialog
import secrets
from importlib.metadata import entry_points
import xoafile
widgets = []
win=Tk()
frames = {}
def show_frame(page):
    frame = frames[page]
    frame.tkraise()  # Đưa frame lên trên

def mahoavbbf():
        frame = Frame(win)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

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
        button.place(x=200, y=90)
        button = Button(frame, text="Tạo IV tự động", command=setiv)
        button.place(x=700, y=90)
        labelbg = Label(frame, text="Nhập văn bản thử đi:", font=("Arial", 20))
        labelbg.pack(pady=5)

        entry = Text(frame, wrap="word", height=10, width=50)
        entry.pack(fill="x", padx=5, pady=5)
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
        output.pack(fill="x", padx=5, pady=5)

        frames["mhvbBF"] = frame

def giaimavbbf():
    frame = Frame(win)
    frame.grid(row=0, column=0, sticky="nsew")
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

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
            text = BlowFish.giaima(text, keyb, ivb)
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

    labelbg = Label(frame, text="Nhập bản mã đi:", font=("Arial", 20))
    labelbg.pack(pady=5)

    entry = Text(frame, wrap="word", height=10, width=50)
    entry.pack(fill="x", padx=5, pady=5)

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
    output.pack(fill="x", padx=5, pady=5)

    frames["gmvbBF"] = frame
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
                text = mhAES.mahoa(text,keyb,ivb)
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

        button = Button(frame, text="Mã hóa với AES", command=get)
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
                text = mhAES.giaima(text,keyb,ivb)
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

        button = Button(frame, text="Giải mã với AES", command=get)
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

def xoafil():
    frame=Frame(win)
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
    button.place(x=550, y=100)

    button = Button(frame, text="Xóa file", command=xoa)
    button.place(x=450, y=100)

    outentry = Text(frame, wrap="word", height=4, width=50)
    outentry.pack(fill="x", padx=5, pady=5)

    frames["xfvsdod"] = frame
def kiemtrafile():
    frame = Frame(win)
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
win.title("Test")
win.geometry("1000x750")
win.grid_rowconfigure(0, weight=1)
win.grid_columnconfigure(0, weight=1)
mahoavbbf()
giaimavbbf()
mahoavb()
giaimavb()
xoafil()
kiemtrafile()
butframe = Frame(win)
butframe.grid(row=2, column=0, columnspan=3, pady=80)
b1 = Button(butframe, text="Mã hóa với AES", command=lambda: show_frame("mhvb"))
b1.grid(row=0, column=0, padx=10, pady=5)

b2 = Button(butframe, text="Giải mã với AES", command=lambda: show_frame("gmvb"))
b2.grid(row=0, column=1, padx=10, pady=5)

b3 = Button(butframe, text="Xóa file an toàn theo chuẩn DoD", command=lambda: show_frame("xfvsdod"))
b3.grid(row=0, column=2, padx=10, pady=5)

b4 = Button(butframe, text="Kiểm tra tính toàn vẹn của file", command=lambda: show_frame("checktv"))
b4.grid(row=0, column=3, padx=10, pady=5)

b5 = Button(butframe, text="Mã hóa với BlowFish", command=lambda: show_frame("mhvbBF"))
b5.grid(row=1, column=0, padx=10, pady=5)

b6= Button(butframe, text="Giải mã với BlowFish", command=lambda: show_frame("gmvbBF"))
b6.grid(row=1, column=1, padx=10, pady=5)

show_frame("mhvb")
win.mainloop()
