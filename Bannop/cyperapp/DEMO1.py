import tkinter as tk
from tkinter import Label, Frame, Button,Text, filedialog
from PIL import Image, ImageTk
import BlowFish
import random, string
#cac bien toan cuc
import MHBF, GMBF, ENAES,GMAES, checktv, MHDES, GM3DES,xoafiledod, xoafilegutmann
frames = {}
def show_frame(page):
    frame = frames[page]
    frame.tkraise()  # Đưa frame lên trên

root = tk.Tk()
root.title("PYTHON CRYPTION")

# Lấy kích thước màn hình và set kích thước cửa sổ = 1/2
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = screen_width*100 // 135
height = screen_height*100 // 135
x = (screen_width - width) // 2
y = (screen_height - height) // 2
root.geometry(f"{width}x{height}+{x}+{y}")

# Cấu hình grid
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=8)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=9)

# Home
home = Frame(root, bg="lightgray", padx=5, pady=10)
home.grid(row=0, column=0, sticky="nsew")
Label(home, text="Home", font=("Arial", 14),background="lightgray").pack()


# Header
header = Frame(root, bg="white", height=40, width=50)
header.grid(row=0, column=1, sticky="nsew", columnspan=2)
Label(header, text="header", font=("Arial", 14), background="white").pack()

# User
user = Frame(header, bg="lightgray", padx=10, pady=10, relief="groove", bd=2)
user.place(relx=0.85, rely=0.01)  # Vị trí góc phải trên
Label(user, text="user", font=("Arial", 14)).pack()

# Main image (lock)
main_content = Frame(root, bg="white")
main_content.grid(row=1, column=1, sticky="nsew", columnspan=2)
main_content.grid_rowconfigure(0, weight=1)
main_content.grid_columnconfigure(0, weight=1)

# Moduls
moduls = Frame(root, bg="white", padx=5)
moduls.grid(row=1, column=0, sticky="nsew")
Label(moduls, text="moduls", font=("Arial", 14), background="white").pack()

butframe = Frame(moduls, bg="lightblue", height=400)
butframe.pack(side="top", fill="x", padx=5, pady=5)
butframe.pack_propagate(False)
butframe.grid_columnconfigure(0, weight=1)
butframe.grid_columnconfigure(1, weight=1)
butframe.grid_columnconfigure(2, weight=1)

MHBF.mahoavbbf(main_content)
frames.update(MHBF.frames)

GMBF.giaimavbbf(main_content)
frames.update(GMBF.frames)

ENAES.mahoavb(main_content)
frames.update(ENAES.frames)

GMAES.giaimavb(main_content)
frames.update(GMAES.frames)

MHDES.mahoavb3des(main_content)
frames.update(MHDES.frames)

GM3DES.giaimavb3des(main_content)
frames.update(GM3DES.frames)

checktv.kiemtrafile(main_content)
frames.update(checktv.frames)

xoafiledod.xoafil(main_content)
frames.update(xoafiledod.frames)

xoafilegutmann.xoafilegutmann(main_content)
frames.update(xoafilegutmann.frames)

spacer = Label(butframe, text=" ", bg="lightblue")  # Một label rỗng để tạo khoảng cách
spacer.grid(row=0, column=1, padx=10, pady=5, sticky="ew")
b1 = Button(butframe, text="Mã hóa AES",command=lambda: show_frame("mhvb"))
b1.grid(row=1,column = 1, padx=10, pady=5,sticky="ew")
b2 = Button(butframe, text="Giải mã AES",command=lambda: show_frame("gmvb"))
b2.grid(row=2, column=1, padx=10, pady=5,sticky="ew")
b3 = Button(butframe, text="Mã hóa 3-DES",command=lambda: show_frame("mhvb3des"))
b3.grid(row=3, column=1, padx=10, pady=5,sticky="ew")
b4 = Button(butframe, text="Giải mã 3-DES",command=lambda: show_frame("gmvb3des"))
b4.grid(row=4, column=1, padx=10, pady=5,sticky="ew")
b5 = Button(butframe, text="Mã hóa Blowfish",command=lambda: show_frame("mhvbBF"))
b5.grid(row=5, column=1, padx=10, pady=5,sticky="ew")
b6 = Button(butframe, text="Giải mã Blowfish",command=lambda: show_frame("gmvbBF"))
b6.grid(row=6, column=1, padx=10, pady=5,sticky="ew")

b7 = Button(butframe, text="Xóa File theo chuẩn DoD",command=lambda: show_frame("xfvbdod"))
b7.grid(row=7, column=1, padx=10, pady=5,sticky="ew")
b8 = Button(butframe, text="Xóa File theo chuẩn Gutmann",command=lambda: show_frame("xfvbgutmann"))
b8.grid(row=8, column=1, padx=10, pady=5,sticky="ew")
b9 = Button(butframe, text="Kiểm tra tính toàn vẹn",command=lambda: show_frame("checktv"))
b9.grid(row=9, column=1, padx=10, pady=5,sticky="ew")
b10 = Button(butframe, text="Mật khẩu",command=lambda: show_frame("matkhau"))
b10.grid(row=10, column=1, padx=10, pady=5,sticky="ew")
spacer = Label(butframe, text=" ",bg="lightblue")  # Một label rỗng để tạo khoảng cách
spacer.grid(row=11, column=1, padx=10, pady=5,sticky="ew")
spacer = Label(butframe, text=" ", bg="lightblue")  # Một label rỗng để tạo khoảng cách
spacer.grid(row=12, column=1, padx=10, pady=5, sticky="ew")
spacer = Label(butframe, text=" ", bg="lightblue")  # Một label rỗng để tạo khoảng cách
spacer.grid(row=13, column=1, padx=10, pady=5, sticky="ew")
spacer = Label(butframe, text=" ", bg="lightblue")  # Một label rỗng để tạo khoảng cách
spacer.grid(row=14, column=1, padx=10, pady=5, sticky="ew")
# Load ảnh vào (đảm bảo bạn có ảnh sẵn)
try:
    image = Image.open("Designer.jpeg")  # dùng ảnh bạn đã gửi
    image = image.resize((width, height))  # resize ảnh
    photo = ImageTk.PhotoImage(image)
    # Hiển thị ảnh nền full
    img_label = Label(main_content, image=photo)
    img_label.image = photo
    img_label.place(x=0, y=0, relwidth=1, relheight=1)

except Exception as e:
    Label(main_content, text="(Ảnh không load được)").pack()

# Footer
footer = Frame(root, bg="lightgray", height=30)
footer.grid(row=2, sticky="nsew", columnspan=2)
Label(footer, text="footer", font=("Arial", 14), background="lightgray").pack()

root.mainloop()






