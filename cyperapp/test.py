import mhAES
from tkinter import *
from tkinter import  Button, filedialog
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
            text = entry.get("1.0", "end-1c")
            text = mhAES.mahoa(text)
            output.delete("1.0", "end")
            output.insert("end", text+"\n")
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
            if file_path:  # Nếu người dùng không hủy chọn file
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(output.get("1.0", "end"))
        labelbg =  Label(frame, text="Nhập văn bản thử đi:", font=("Arial", 20))
        labelbg.pack(pady=5)
        entry = Text(frame, wrap="word", height=10, width=50)
        entry.pack(fill="x",padx=5, pady=5)
        entry.pack(pady=5)
        spacer = Label(frame, text=" ")  # Một label rỗng để tạo khoảng cách
        spacer.pack(pady=5)
        button = Button(frame, text="Mã hóa với AES", command=get)
        button.place(x=300, y=224)
        button = Button(frame, text="Nhập file", command=mhfile)
        button.place(x=700, y=224)
        button = Button(frame, text="Mã hóa tiếp", command=sett)
        button.place(x=800, y=224)
        button = Button(frame, text="Lưu vào file", command=savefile)
        button.place(x=900, y=224)
        output = Text(frame, wrap="word", height=10, width=50)
        output.pack(fill="x",padx=5, pady=5)
        frames["mhvb"] = frame
def giaimavb():
        frame = Frame(win)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        def gmfile():
            file_path = filedialog.askopenfilename(title="Chọn file để mã hóa")
            if file_path:
                with open(file_path, "r",encoding="utf-8") as f:
                    data = f.read()
                entry.delete("1.0", "end")
                entry.insert("end", data)
        def sett():
            entry.delete("1.0","end")
            entry.insert("end",output.get("1.0","end"))
        def get():
            text = entry.get("1.0", "end-1c")
            text = mhAES.giaima(text)
            output.delete("1.0", "end")
            output.insert("end", text)
        def savefile():
            file_path=filedialog.asksaveasfilename(defaultextension="txt",
                                                   filetypes=[("Text","*txt"),
                                                              ("All file","*.*")])
            if file_path:
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(output.get("1.0", "end"))
        labelbg = Label(frame, text="Nhập bản mã đi:", font=("Arial", 20))
        labelbg.pack(pady=5)
        entry = Text(frame, wrap="word", height=10, width=50)
        entry.pack(fill="x",padx=5, pady=5)
        spacer = Label(frame, text=" ")  # Một label rỗng để tạo khoảng cách
        spacer.pack(pady=5)
        button = Button(frame, text="Giải mã với AES", command=get)
        button.place(x=300, y=224)
        button = Button(frame, text="Nhập file", command=gmfile)
        button.place(x=700, y=224)
        button = Button(frame, text="Giải mã tiếp", command=sett)
        button.place(x=800, y=224)
        button = Button(frame, text="Lưu vào file", command=savefile)
        button.place(x=900, y=224)
        output = Text(frame, wrap="word", height=10, width=50)
        output.pack(fill="x",padx=5, pady=5)
        frames["gmvb"] = frame
win.title("Test")
win.geometry("1000x650")
win.grid_rowconfigure(0, weight=1)
win.grid_columnconfigure(0, weight=1)
mahoavb()
giaimavb()
butframe = Frame(win)
butframe.grid(row=1, column=0, sticky="ew", pady=10)
spacer = Label(butframe, text=" ")
spacer.pack(side="left", padx=200, pady=100)
b1 = Button(butframe, text="Mã hóa", command=lambda: show_frame("mhvb"))
b1.pack(side="left", padx=10, pady=100)
b2 = Button(butframe, text="Giải mã", command=lambda: show_frame("gmvb"))
b2.pack(side="left", padx=10, pady=5)
show_frame("mhvb")
win.mainloop()
