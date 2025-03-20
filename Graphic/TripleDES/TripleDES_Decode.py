from tkinter import *
from tkinter import  Button, filedialog


from Graphic.TripleDES import TripleDES_Algorithm

frames={}
def giaimavb3des(main_content,giatricu):
    frame = Frame(main_content)
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

    def settlaigiatri():
        entry.delete("1.0", "end")
        entry.insert("end", giatricu)

    def tamluu():
        global giatricu
        giatricu = output.get("1.0", "end")

    def get():
        try:
            # keyy = entry_key.get("1.0", "end").strip()
            # keyb = keyy.encode("utf-8")
            # iiv = entry_iv.get("1.0", "end").strip()
            # ivb = iiv.encode("utf-8")
            # text = entry.get("1.0", "end-1c")

            keyy = entry_key.get("1.0", "end").strip()
            keyb = bytes.fromhex(keyy) if all(c in "0123456789abcdefABCDEF" for c in keyy) else keyy.encode("utf-8")
            iiv = entry_iv.get("1.0", "end").strip()
            ivb = bytes.fromhex(iiv) if all(c in "0123456789abcdefABCDEF" for c in iiv) else iiv.encode("utf-8")
            text = entry.get("1.0", "end-1c")

            text = TripleDES_Algorithm.giaima(text, keyb, ivb)
            output.delete("1.0", "end")
            output.insert("end", text)
        except Exception as e:
            output.delete("1.0", "end")
            output.insert("end", "Something Wrong")

    def savefile():
        file_path = filedialog.asksaveasfilename(defaultextension="txt",
                                                 filetypes=[("Text", "*txt"),
                                                            ("All file", "*.*")])
        if file_path:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(output.get("1.0", "end"))

    label_frame = Frame(frame)
    label_frame.pack(side="top", fill="x")  # Dùng fill="x" để giãn đều

    label_key = Label(label_frame, text="Nhập key từ 16 đến 24 ký tự:", font=("Arial", 20))
    label_key.pack(side="left", expand=True)

    label_iv = Label(label_frame, text="Nhập IV đủ 8 kí tự:", font=("Arial", 20))
    label_iv.pack(side="left", expand=True)

    text_frame = Frame(frame)
    text_frame.pack(side="top", fill="x", pady=5)

    entry_key = Text(text_frame, wrap="word", height=2, width=60)
    entry_key.pack(side="left", expand=True, padx=5)

    entry_iv = Text(text_frame, wrap="word", height=2, width=60)
    entry_iv.pack(side="left", expand=True, padx=5)

    labelbg = Label(frame, text="Nhập bản mã đi:", font=("Arial", 20))
    labelbg.pack(pady=5)

    entry = Text(frame, wrap="word", height=8, width=50)
    entry.pack(fill="x", padx=5, pady=5)

    spacer = Label(frame, text=" ")  # Một label rỗng để tạo khoảng cách
    spacer.pack(pady=5)

    button = Button(frame, text="Giải mã với 3-DES", command=get)
    button.place(x=300, y=280)

    button = Button(frame, text="Lấy lại giá trị", command=settlaigiatri)
    button.place(x=500, y=280)

    button = Button(frame, text="Tạm lưu", command=tamluu)
    button.place(x=600, y=280)

    button = Button(frame, text="Nhập file", command=gmfile)
    button.place(x=700, y=280)

    button = Button(frame, text="Giải mã tiếp", command=sett)
    button.place(x=800, y=280)

    button = Button(frame, text="Lưu vào file", command=savefile)
    button.place(x=900, y=280)

    output = Text(frame, wrap="word", height=10, width=50)
    output.pack(fill="x", padx=5, pady=5)

    frames["gmvb3des"] = frame