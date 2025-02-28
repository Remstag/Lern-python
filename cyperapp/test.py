from Crypto.Cipher import AES
from Crypto.Util.Padding import *
from tkinter import *
from tkinter import  Button, filedialog
import base64
from importlib.metadata import entry_points
KEy=b'KeyDayNeDuMaMayVoMaLay@1234ABCDX'
IV=b'ThisIsAnIV123456'
def mahoa(texxt):
    texxt=str(texxt)
    cipher=AES.new(KEy,AES.MODE_CBC,IV)
    damahoa=cipher.encrypt(pad(texxt.encode(),AES.block_size))
    return base64.b64encode(damahoa).decode()
def giaima(mh):
    cipher = AES.new(KEy, AES.MODE_CBC, IV)
    giaimaa = base64.b64decode(mh.strip())
    return unpad(cipher.decrypt(giaimaa), AES.block_size).decode("utf-8", errors="ignore").replace("\r\n", "\n")
d=0
widgets = []
def check(val):
    global d
    d=val
    update()

def update():
    global widgets
    for widget in widgets:
        widget.destroy()  # Xóa các widget đã tạo
    widgets.clear()
    if (d==1):
        def get():
            text = entry.get("1.0", "end-1c")
            text = mahoa(text)
            output.delete("1.0", "end")
            output.insert("end", text)
        labelbg = Label(win, text="Nhập văn bản thử đi:", font=("Arial", 20))
        labelbg.pack(pady=5)
        entry = Text(win, wrap="word", height=10, width=50)
        entry.pack(fill="x",padx=5, pady=5)
        button = Button(win, text="Mã hóa", command=get)
        button.pack(pady=5)
        output = Text(win, wrap="word", height=10, width=50)
        output.pack(fill="x",padx=5, pady=5)
        widgets.extend([labelbg, entry, button, output])
    elif d==2:
        def get2():
            text = entry.get("1.0", "end-1c")
            text = giaima(text)
            output.delete("1.0", "end")
            output.insert("end", text)
        labelbg = Label(win, text="Nhập bản mã đi:", font=("Arial", 20))
        labelbg.pack(pady=5)
        entry = Text(win, wrap="word", height=10, width=50)
        entry.pack(fill="x",padx=5, pady=5)
        button = Button(win, text="Giải mã", command=get2)
        button.pack(pady=5)
        output = Text(win, wrap="word", height=10, width=50)
        output.pack(fill="x",padx=5, pady=5)
        widgets.extend([labelbg, entry, button, output])
    elif d==3:
        def mhfile():
            file_path = filedialog.askopenfilename(title="Chọn file để mã hóa")
            if file_path:
                with open(file_path, "r",encoding="utf-8") as f:
                    data = f.read()
                encrypted_data=mahoa(data)
                output.delete("1.0", "end")

                output.insert("end", encrypted_data+"\n")

        labelbg = Label(win, text="Chọn file đi:", font=("Arial", 20))
        labelbg.pack(pady=5)
        button = Button(win, text="Chọn file để mã hóa", command=mhfile)
        button.pack(pady=5)
        output = Text(win, wrap="word", height=10, width=50)
        output.pack(fill="x", padx=5, pady=5)
        widgets.extend([labelbg, button, output])
    elif d==4:
        def gmfile():
            file_path = filedialog.askopenfilename(title="Chọn file để giải mã")
            if file_path:
                with open(file_path, "rb") as f:
                    data = f.read()
                encrypted_data=giaima(data)
                output.delete("1.0", "end")
                output.insert("end", encrypted_data + "\n")

        labelbg = Label(win, text="chọn file đi:", font=("Arial", 20))
        labelbg.pack(pady=5)
        button = Button(win, text="Chọn file để giải mã", command=gmfile)
        button.pack(pady=5)
        output = Text(win, wrap="word", height=10, width=50)
        output.pack(fill="x", padx=5, pady=5)
        widgets.extend([labelbg, button, output])
win=Tk()
win.title("Test")
win.geometry("1000x750")
b1 = Button(win, text="Mã hóa", command=lambda:check(1))
b1.place(x=250, y=600)
b2 = Button(win, text="Giải mã", command=lambda:check(2))
b2.place(x=350, y=600)
b3 = Button(win, text="Mã hóa file", command=lambda:check(3))
b3.place(x=450, y=600)
b4 = Button(win, text="Giải mã file", command=lambda:check(4))
b4.place(x=550, y=600)
win.mainloop()
