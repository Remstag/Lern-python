from tkinter import *
from tkinter import  Button, filedialog, messagebox
import random
from cryptography.fernet import Fernet
from tkinter import simpledialog
import os
import string
import secrets
from Graphic.KiemTraTinhToanVen import kiemtratinhtoanven as cheeck
from Graphic import giatricuu
frames={}
def xoafil(main_content):
    frame=Frame(main_content)
    frame.grid(row=0, column=0, sticky="nsew")
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)
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
    def layfile():
        file_path = filedialog.askopenfilename(title="Chọn file tạo mã băm")
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
                    key = simpledialog.askstring("Nhập key", "File đang được mã hóa. Nhập key để giải mã:")
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
                            # Gọi hàm giải mã ở đây (giả sử bạn đã có hàm `giaima_noidung`)
                            with open(selected_path, "r", encoding="utf-8") as f:
                                data = f.read()
                            inentry.delete("1.0", "end")
                            inentry.insert("end", file_path)
                        except Exception as e:
                            messagebox.showerror("Lỗi giải mã", f"Không thể giải mã file:\n{str(e)}")
                else:
                    # Nếu không phải là file mã hóa, chỉ hiển thị nội dung
                    inentry.delete("1.0", "end")
                    inentry.insert("end", file_path)

            except Exception as e:
                messagebox.showerror("Lỗi đọc file", f"Không thể đọc file:\n{str(e)}")
    def taomb():
        file_path1 = inentry.get("1.0", "end").strip()
        file_path1 = file_path1.replace("/", "\\\\")
        hash_goc = cheeck.shaa256(file_path1)
        outentry.delete("1.0", "end")
        outentry.insert("end", hash_goc)

    def savefile():
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text", "*.txt"), ("All files", "*.*")],
            title="Chọn nơi lưu file"
        )

        if file_path:
            selected_path = os.path.abspath(file_path)
            appne_base = os.path.abspath("C:/Appne")

            # Nếu chưa đăng nhập: không cho lưu vào C:/Appne
            if not giatricuu.emailhientai:
                if selected_path.startswith(appne_base):
                    messagebox.showerror("Lỗi", "Bạn không được quyền truy cập vào mục này.")
                    return

            else:
                # Nếu đã đăng nhập: chỉ được lưu trong thư mục cá nhân
                user_dir = os.path.join(appne_base, giatricuu.emailhientai)
                abs_user_dir = os.path.abspath(user_dir)
                if selected_path.startswith(appne_base) and not selected_path.startswith(abs_user_dir):
                    messagebox.showerror("Lỗi", "Bạn chỉ được lưu file trong thư mục cá nhân của mình.")
                    return

            try:
                with open(selected_path, "w", encoding="utf-8") as file:
                    file.write(outentry.get("1.0", "end"))
                messagebox.showinfo("Thành công", "Lưu file thành công!")
            except Exception as e:
                messagebox.showerror("Lỗi khi lưu file", f"Không thể lưu file:\n{str(e)}")

    # Frame include nhapvanban, vanbanmahoa, tinhnang
    frame2 = Frame(frame, bg="violet", padx=2, pady=2, bd=1, relief="solid")
    frame2.grid(row=0, column=0, sticky="nsew")
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
    label_nvb = Label(Frame_label_nvb, text="File cần tạo mã băm", font=("Arial", 20))
    label_nvb.pack(side="left", fill="y")

    inentry = Text(nhapvanban_frame, wrap="word", height=10)
    inentry.grid(row=2, column=1, rowspan=2, sticky="ew")

    # Frame include button tinh nang
    tinhnang_frame = Frame(frame2, padx=2, pady=20, bd=1, relief="solid")
    tinhnang_frame.grid(row=0, column=1, sticky="nsew", rowspan=2)
    for i in range(6):
        tinhnang_frame.grid_rowconfigure(i, weight=1)
    for i in range(3):
        tinhnang_frame.grid_columnconfigure(i, weight=1)

    button = Button(tinhnang_frame, text="Nhập file", font=("Arial", 14), command=layfile)
    button.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

    button = Button(tinhnang_frame, text="Tạo mã băm", font=("Arial", 14), command=taomb)
    button.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

    button = Button(tinhnang_frame, text="Lưu mã băm", font=("Arial", 14), command=savefile)
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
    outentry = Text(vanbanmahoa_frame, wrap="word", height=10)
    outentry.grid(row=2, column=1, rowspan=2, sticky="ew")


    frames["taombb"] = frame