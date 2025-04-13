from tkinter import *
from tkinter import Button, filedialog, messagebox
import os
from Graphic import giatricuu
from Graphic.XoaFile import gutmann  # Import module xóa file Gutmann

frames = {}


def xoafilegutmann(main_content):
    frame = Frame(main_content)
    frame.grid(row=0, column=0, sticky="nsew")
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

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
                inentry.delete("1.0", "end")
                inentry.insert("end", file_path)
            except Exception as e:
                messagebox.showerror("Lỗi đọc file", f"Không thể đọc file:\n{str(e)}")

    def xoa():
        file_path = inentry.get("1.0", "end").strip()
        file_path = file_path.replace("/", "\\")

        if os.path.exists(file_path):
            gutmann.gutmann_wipe(file_path)
            outentry.delete("1.0", "end")
            outentry.insert("end", f"File {file_path} đã được xóa an toàn bằng phương pháp Gutmann!\n")
        else:
            outentry.delete("1.0", "end")
            outentry.insert("end", "Lỗi: Không tìm thấy file!\n")

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
    label_nvb = Label(Frame_label_nvb, text="File cần xóa", font=("Arial", 20))
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

    button = Button(tinhnang_frame, text="Xóa file", font=("Arial", 14), command=xoa)
    button.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

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
    frames["xfvbgutmann"] = frame