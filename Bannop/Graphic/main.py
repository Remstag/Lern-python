import tkinter as tk
from tkinter import Label, Frame, Button
from PIL import Image, ImageTk, ImageFilter


#cac bien toan cuc
from BlowFish import BlowFish_Decode, BlowFish_Encode
from AES import AES_Encode, AES_Decode
from TripleDES import TripleDES_Encode, TripleDES_Decode
from XoaFile import xoafiledod, xoafilegutmann
from KiemTraTinhToanVen import checktv, taomabam
from MatKhauManh import TaoMatKhau, thongbao
from DangNhap import dangnhap
import giatricuu
import Database
from Graphic import giatricuu
Database.init_db()
frames = {}
def show_frame(page):
    frame = frames[page]
    frame.tkraise()  # Đưa frame lên trên
def show_framedb(page):
    TaoMatKhau.taomatkhau(main_content)
    frames.update(TaoMatKhau.frames)
    frame = frames[page]
    frame.tkraise()
def update_header(text):
    header_label.config(text=text)
root = tk.Tk()
root.title("PYTHON CRYPTION")

# content = Frame(root, bg="white", padx=5, pady=10)

# Lấy kích thước màn hình và set kích thước cửa sổ = 1/2
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = int(screen_width * 0.8)
height = int(screen_height * 0.8)
x = int((screen_width - width) / 2)
y = int((screen_height - height) / 2)
root.geometry(f"{width}x{height}+{x}+{y}")

# Cấu hình grid
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=8)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=9)

# Home
home = Frame(root, bg="red4", padx=5, pady=10,bd=1,relief="solid")
home.grid(row=0, column=0, sticky="nsew")
but_home = Button(home, text="Home", font=("Arial", 14),background="lightgray",command=lambda: [update_header("Home"),show_frame("home")]).pack()


# Header
header = Frame(root, bg="white", height=40, width=50,bd=1,relief="solid")
header.grid(row=0, column=1, sticky="nsew", columnspan=2)
header_label = Label(header, text="", font=("Arial", 14), background="white")
header_label.pack(expand=True)
# User
user = Frame(header, bg="lightgray", bd=1,relief="solid")
# user.pack(side="right", padx=5, pady=2)
user.place(relx=0.8, rely=0, relwidth=0.2, relheight=1.0)  # Vị trí góc phải trên
Label(user, text="BTL Python", font=("Arial", 14)).pack(expand=True,fill="both")
Label(user, text="Nhóm 12", font=("Arial", 14)).pack(expand=True,fill="both")

# Main image (lock)
main_content = Frame(root, bg="white",bd=1,relief="solid")
main_content.grid(row=1, column=1, sticky="nsew", columnspan=2)
main_content.grid_rowconfigure(0, weight=1)
main_content.grid_columnconfigure(0, weight=1)

# Moduls
moduls = Frame(root, bg="white", padx=5,bd=1,relief="solid")
moduls.grid(row=1, column=0, sticky="nsew")
Label(moduls, background="white").pack()

butframe = Frame(moduls, bg="lightblue", height=400)
butframe.pack(side="top", fill="x", padx=5, pady=5)
butframe.pack_propagate(False)
butframe.grid_columnconfigure(0, weight=1)
butframe.grid_columnconfigure(1, weight=1)
butframe.grid_columnconfigure(2, weight=1)

AES_Encode.mahoavb(main_content)
AES_Decode.giaimavb(main_content)
frames.update(AES_Encode.frames)
frames.update(AES_Decode.frames)

BlowFish_Encode.mahoavbbf(main_content)
BlowFish_Decode.giaimavbbf(main_content)
frames.update(BlowFish_Encode.frames)
frames.update(BlowFish_Decode.frames)

TripleDES_Encode.mahoavb3des(main_content)
TripleDES_Decode.giaimavb3des(main_content)
frames.update(TripleDES_Encode.frames)
frames.update(TripleDES_Decode.frames)

xoafiledod.xoafil(main_content)
xoafilegutmann.xoafilegutmann(main_content)
frames.update(xoafiledod.frames)
frames.update(xoafilegutmann.frames)

checktv.kiemtrafile(main_content)
frames.update(checktv.frames)
taomabam.xoafil(main_content)
frames.update(taomabam.frames)




dangnhap.dangnhap(main_content)
frames.update(dangnhap.frames)

spacer = Label(butframe, text=" ", bg="lightblue")
spacer.grid(row=0, column=1, padx=10, pady=5, sticky="ew")




#Ma hoa - giai ma AES
b1 = Button(butframe, text="Mã hóa AES", font=("Arial",13),command=lambda: [update_header("Mã hóa AES"),show_frame("mhvbaes")])
b1.grid(row=1,column = 1, padx=10, pady=5,sticky="ew")
b2 = Button(butframe, text="Giải mã AES", font=("Arial",13),command=lambda: [update_header("Giải mã AES"),show_frame("gmvbaes")])
b2.grid(row=2, column=1, padx=10, pady=5,sticky="ew")

#Ma hoa - giai ma 3-DES
b3 = Button(butframe, text="Mã hóa 3-DES", font=("Arial",13),command=lambda: [update_header("Mã hóa 3-DES"),show_frame("mhvb3des")])
b3.grid(row=3, column=1, padx=10, pady=5,sticky="ew")
b4 = Button(butframe, text="Giải mã 3-DES", font=("Arial",13),command=lambda: [update_header("Giải mã 3-DES"),show_frame("gmvb3des")])
b4.grid(row=4, column=1, padx=10, pady=5,sticky="ew")

#Ma hoa - giai ma Blowfish
b5 = Button(butframe, text="Mã hóa Blowfish", font=("Arial",13),command=lambda: [update_header("Mã hóa Blowfish"),show_frame("mhvbBF")])
b5.grid(row=5, column=1, padx=10, pady=5,sticky="ew")
b6 = Button(butframe, text="Giải mã Blowfish", font=("Arial",13),command=lambda: [update_header("Giải mã Blowfish"),show_frame("gmvbBF")])
b6.grid(row=6, column=1, padx=10, pady=5,sticky="ew")

#Xoa file chuan DoD
b7 = Button(butframe, text="Xóa File theo chuẩn DoD", font=("Arial",13),command=lambda: [update_header("Xóa File theo chuẩn DoD"),show_frame("xfvbdod")])
b7.grid(row=7, column=1, padx=10, pady=5,sticky="ew")

#Xoa file chuan Gutmann
b8 = Button(butframe, text="Xóa File theo chuẩn Gutmann", font=("Arial",13),command=lambda: [update_header("Xóa File theo chuẩn Gutmann"),show_frame("xfvbgutmann")])
b8.grid(row=8, column=1, padx=10, pady=5,sticky="ew")

#Kiem tra tinh toan ven
b9 = Button(butframe, text="Kiểm tra tính toàn vẹn", font=("Arial",13),command=lambda: [update_header("Kiểm tra tính toàn vẹn"),show_frame("checktv")])
b9.grid(row=9, column=1, padx=10, pady=5,sticky="ew")

#Tao - Ma hoa - Luu tru mat khau manh

b10 = Button(butframe, text="Mật khẩu", font=("Arial",13),command=lambda: [update_header("Mật khẩu"),show_framedb("matkhau")])
b10.grid(row=10, column=1, padx=10, pady=5,sticky="ew")


b11 = Button(butframe, text="Tạo file mã băm", font=("Arial",13),command=lambda: [update_header("Mã băm"),show_frame("taombb")])
b11.grid(row=11, column=1, padx=10, pady=5,sticky="ew")

dangnhap_btn = Button(butframe, text="Đăng Nhập", font=("Arial",13),command=lambda: [update_header("Đăng Nhập"),show_frame("dangnhap")])
dangnhap_btn.grid(row=12,column = 1, padx=10, pady=5,sticky="ew")
dangky_btn = Button(butframe, text="Đăng Ký", font=("Arial",13),command=lambda: [update_header("Đăng ký"),show_frame("dangky")])
dangky_btn.grid(row=13, column=1, padx=10, pady=5,sticky="ew")


spacer = Label(butframe, text=" ", bg="lightblue")
spacer.grid(row=14, column=1, padx=10, pady=5, sticky="ew")
spacer = Label(butframe, text=" ", bg="lightblue")
spacer.grid(row=15, column=1, padx=10, pady=5, sticky="ew")
# Load ảnh vào (đảm bảo bạn có ảnh sẵn)
home_page = Frame(main_content, bg="white",bd=1,relief="solid")
home_page.grid(row=0, column=0, sticky="nsew")
try:
    image = Image.open("Image/Background2.jpg")  # dùng ảnh bạn đã gửi
    image = image.resize((height, height))  # resize ảnh
    image = image.filter(ImageFilter.GaussianBlur(radius=0))
    photo = ImageTk.PhotoImage(image)
    # Hiển thị ảnh nền full
    img_label = Label(home_page, image=photo)
    img_label.image = photo
    img_label.place(x=0, y=0, relwidth=1, relheight=1)

except Exception as e:
    Label(home_page, text="(Ảnh không load được)").pack()

# Footer
footer = Frame(root, bg="lightgray", height=30,bd=1,relief="solid")
footer.grid(row=2, sticky="nsew", columnspan=2)
Label(footer, text="Posts and Telecommunications Institute of Technology", font=("Arial", 14), fg="red", background="lightgray").pack(expand=True,fill="both")

frames["home"] = home_page
root.mainloop()






