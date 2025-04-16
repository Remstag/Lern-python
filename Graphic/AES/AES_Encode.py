from tkinter import *
from tkinter import  Button, filedialog, messagebox

from PIL.ImageOps import expand
from cryptography.fernet import Fernet
from Graphic.AES import AES_Algorithm
import random
import os
import string
import secrets
from Graphic import giatricuu
from tkinter import simpledialog
frames={}
def mahoavb(main_content):
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
        entry.insert("end", giatricuu.giatricu)

    def tamluu():
        giatricuu.giatricu = output.get("1.0", "end")

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
            if len(keyy) != 32:
                output.delete("1.0", "end")
                output.insert("end", "Lỗi key")
            elif len(iiv) != 16:
                output.delete("1.0", "end")
                output.insert("end", "Lỗi iv")
            else:
                output.delete("1.0", "end")
                output.insert("end", "Lỗi")

    def setkey():
        entry_key.delete("1.0", "end")
        a = random.choice([16, 24, 32])
        random_key = ''.join(random.choices(string.ascii_letters + string.digits +string.punctuation , k=a))
        entry_key.insert("end", random_key)
        entry_key.tag_add("custom_font", "1.0", "end")
        entry_key.tag_configure("custom_font", font=("Arial", 13))

    def setiv():
        entry_iv.delete("1.0", "end")
        random_iv = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=16))
        entry_iv.insert("end", random_iv)
        entry_iv.tag_add("custom_font", "1.0", "end")
        entry_iv.tag_configure("custom_font", font=("Arial", 13))





    def decrypt_file(path, fernet):
        try:
            with open(path, "rb") as f:
                data = f.read()
            decrypted = fernet.decrypt(data)
            with open(path, "wb") as f:
                f.write(decrypted)
        except Exception as e:
            print(f"Không thể giải mã {path}: {e}")

    def decrypt_user_folder():
        if (giatricuu.mahoa == 1):
            giatricuu.mahoa = 0
            user_dir = giatricuu.duongdanfile
            key = giatricuu.keyhientai
            if not key: return
            fernet = Fernet(key)

            for filename in os.listdir(user_dir):
                full_path = os.path.join(user_dir, filename)
                if os.path.isfile(full_path):
                    decrypt_file(full_path, fernet)
        else:
            messagebox.showerror("Lỗi", "Không thể giải mã")

    def mhfile():
        file_path = filedialog.askopenfilename(title="Chọn file để mã hóa")
        if file_path:
            appne_dir = os.path.abspath("C:/Appne")
            selected_path = os.path.abspath(file_path)

            # Kiểm tra nếu người dùng chưa đăng nhập và đang cố mở file trong C:/Appne
            if not giatricuu.emailhientai:
                if selected_path.startswith(appne_dir):
                    messagebox.showerror("Truy cập bị từ chối",
                                         "Bạn không được phép truy cập mục này, vui lòng đăng nhập")
                    return
            else:
                # Nếu đã đăng nhập thì chỉ được phép vào đúng thư mục cá nhân
                user_dir = os.path.join(appne_dir, giatricuu.emailhientai)
                abs_user_dir = os.path.abspath(user_dir)
                if selected_path.startswith(appne_dir) and not selected_path.startswith(abs_user_dir):
                    messagebox.showerror("Truy cập bị từ chối",
                                         "Bạn chỉ được phép truy cập thư mục cá nhân của mình.")
                    return

            try:
                with open(selected_path, "r", encoding="utf-8") as f:
                    data = f.read()

                # ==== Kiểm tra trạng thái file có mã hóa không ====
                if giatricuu.mahoa == 1 and selected_path.startswith(appne_dir):
                    key = simpledialog.askstring("Nhập key", "File đang được mã hóa. Nhập key để giải mã:")
                    if not key:
                        messagebox.showinfo("Hủy thao tác", "Bạn đã hủy việc giải mã.")
                        return
                    if isinstance(giatricuu.keyhientai, bytes):
                        giatricuu.keyhientai = giatricuu.keyhientai.decode()
                    if giatricuu.keyhientai == key:
                        messagebox.showinfo("Thành công", "Nhập key thành công!")
                        decrypt_user_folder()
                        try:
                            with open(selected_path, "r", encoding="utf-8") as f:
                                data = f.read()
                            entry.delete("1.0", "end")
                            entry.insert("end", data)
                        except Exception as e:
                            messagebox.showerror("Lỗi giải mã", f"Không thể giải mã file:\n{str(e)}")
                    else:
                        messagebox.showerror("Sai key", "Key không đúng!")
                else:
                    entry.delete("1.0", "end")
                    entry.insert("end", data)

            except Exception as e:
                messagebox.showerror("Lỗi đọc file", f"Không thể đọc file:\n{str(e)}")

    def savefile():
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text", "*.txt"), ("All files", "*.*")],
            title="Chọn nơi lưu file"
        )

        if file_path:
            appne_dir = os.path.abspath("C:/Appne")
            selected_path = os.path.abspath(file_path)


            # Kiểm tra nếu người dùng chưa đăng nhập và đang cố mở file trong C:/Appne
            if selected_path.startswith(appne_dir) and not giatricuu.emailhientai:
                messagebox.showerror("Truy cập bị từ chối",
                                     "Bạn không được phép truy cập mục này, vui lòng đăng nhập")
                return
            else:
                # Nếu đã đăng nhập thì chỉ được phép vào đúng thư mục cá nhân
                user_dir = os.path.join(appne_dir, giatricuu.emailhientai)
                abs_user_dir = os.path.abspath(user_dir)
                if selected_path.startswith(appne_dir) and not selected_path.startswith(abs_user_dir):
                    messagebox.showerror("Truy cập bị từ chối", "Bạn chỉ được phép truy cập thư mục cá nhân của mình.")
                    return

            try:

                if giatricuu.mahoa == 1 and selected_path.startswith(appne_dir):
                    key = simpledialog.askstring("Nhập key", "Thư mục đang được mã hóa. Nhập key để giải mã:")
                    if not key:
                        messagebox.showinfo("Hủy thao tác", "Bạn đã hủy việc giải mã.")
                        return
                    if isinstance(giatricuu.keyhientai, bytes):
                        giatricuu.keyhientai = giatricuu.keyhientai.decode()
                    if (giatricuu.keyhientai == key):
                        # Đường dẫn thư mục cá nhân
                        messagebox.showinfo("Thành công", "Nhập key thành công!")
                        decrypt_user_folder()
                        try:
                            with open(selected_path, "w", encoding="utf-8") as file:
                                file.write(output.get("1.0", "end"))
                            messagebox.showinfo("Thành công", "Lưu file thành công!")
                        except Exception as e:
                            messagebox.showerror("Lỗi khi lưu file", f"Không thể lưu file:\n{str(e)}")
                else:
                    try:
                        with open(selected_path, "w", encoding="utf-8") as file:
                            file.write(output.get("1.0", "end"))
                        messagebox.showinfo("Thành công", "Lưu file thành công!")
                    except Exception as e:
                        messagebox.showerror("Lỗi khi lưu file", f"Không thể lưu file:\n{str(e)}")
            except Exception as e:
                messagebox.showerror("Lỗi lưu", f"Không thể lưu file:\n{str(e)}")

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