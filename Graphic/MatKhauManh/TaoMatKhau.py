import tkinter as tk
from tkinter import ttk, messagebox, Frame, filedialog
import random
import string
import pyperclip
from Graphic.Database import get_db_connection
from numpy.ma.extras import column_stack
import sqlite3
import os
from cryptography.fernet import Fernet
from Graphic import giatricuu
frames={}


def encrypt_file(path, fernet):
    try:
        with open(path, "rb") as f:
            data = f.read()
        encrypted = fernet.encrypt(data)
        with open(path, "wb") as f:
            f.write(encrypted)
    except Exception as e:
        print(f"Không thể mã hóa {path}: {e}")


def encrypt_user_folder():
    if giatricuu.mahoa==0:
        giatricuu.mahoa=1
        user_dir = giatricuu.duongdanfile
        key = giatricuu.keyhientai
        try:
            if not key:
                return
            fernet = Fernet(key)
            for filename in os.listdir(user_dir):
                full_path = os.path.join(user_dir, filename)
                if os.path.isfile(full_path):
                    encrypt_file(full_path, fernet)
            messagebox.showinfo("Thành công", "Mã hóa thư mục thành công!")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể mã hóa: {e}")
    else: messagebox.showerror("Lỗi", "Bạn đã mã hóa thư mục rồi")

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
    if (giatricuu.mahoa==1):
        giatricuu.mahoa=0
        user_dir = giatricuu.duongdanfile
        key = giatricuu.keyhientai
        if not key: return
        fernet = Fernet(key)

        for filename in os.listdir(user_dir):
            full_path = os.path.join(user_dir, filename)
            if os.path.isfile(full_path):
                decrypt_file(full_path, fernet)
    else : messagebox.showerror("Lỗi", "Không thể giải mã")
def taomatkhau(main_content):
    main_frame = tk.Frame(main_content)
    if(giatricuu.x==1):
        # Tính chỉ số của password dùng để xét độ mạnh yếu
        password = giatricuu.passhientai
        email=giatricuu.emailhientai
        def strong_pass(password):
            cnt_upper, cnt_lower, cnt_num, cnt_special = 0,0,0,0
            for i in password:
                if 'A' <= i <= 'Z': cnt_upper += 1
                elif 'a' <= i <= 'z': cnt_lower += 1
                elif '0' <= i <= '9': cnt_num += 1
                else:
                    cnt_special += 1
            return cnt_upper, cnt_lower, cnt_num, cnt_special

        # Tính điểm độ mạnh của Password
        def calculation_markStrong(cnt_upper, cnt_lower, cnt_num, cnt_special, length):
            mark = 0
            if 8 <= length <= 11: mark += 1
            if 1 <= cnt_upper <=2: mark += 1
            if 1 <= cnt_lower <= 2: mark += 1
            if 1 <= cnt_num <= 2: mark += 1
            if cnt_special == 1: mark += 1
            if length >= 12: mark += 2
            if cnt_upper >= 3: mark += 2
            if cnt_lower >= 3:mark += 2
            if cnt_num >= 3:mark += 2
            if cnt_special >= 2:mark += 2
            return mark

        # Hàm tạo mật khẩu
        def generate_password():
            try:
                password_length_default = int(password_length_text.get("1.0", "end").strip())
                password_length = tk.IntVar(value=password_length_default)
            except:
                password_length = tk.IntVar(value=0)

            length = password_length.get()
            chars = ''
            if use_upper.get():
                chars += string.ascii_uppercase
            if use_lower.get():
                chars += string.ascii_lowercase
            if use_digits.get():
                chars += string.digits
            if use_symbols.get():
                chars += string.punctuation

            if not chars:
                messagebox.showwarning("Chọn ký tự", "Vui lòng chọn ít nhất một loại ký tự.")
                return

            password = ''.join(random.choice(chars) for _ in range(length))
            password_entry.delete(0, tk.END)
            password_entry.insert(0, password)

        def check_pass(password):
            cnt_upper, cnt_lower, cnt_num, cnt_special = strong_pass(password)

            mark_strong = 0
            mark_strong = calculation_markStrong(cnt_upper, cnt_lower, cnt_num, cnt_special, len(password))
            # Đánh giá độ mạnh (rất đơn giản)
            if 9 <= mark_strong <= 10:
                return "🔐 Very Strong"
            elif 7 <= mark_strong <= 8:
                return "✅ Strong"
            elif 5 <= mark_strong <= 6:
                return "⚠️ Medium"
            elif 3 <= mark_strong <= 4:
                return "❌ Weak"
            else:
                return "🚫 Very Weak"
        def update_strong():
            pwd = password_entry.get()
            result = check_pass(pwd)
            if result == "🔐 Very Strong":
                strength_label.config(text="🔐 Very Strong", fg="green4")
            elif result == "✅ Strong":
                strength_label.config(text="✅ Strong", fg="green")
            elif result == "⚠️ Medium":
                strength_label.config(text="⚠️ Medium", fg="yellow4")
            elif result == "❌ Weak":
                strength_label.config(text="❌ Weak", fg="orange")
            else:
                strength_label.config(text="🚫 Very Weak", fg="red")
        # Sao chép mật khẩu
        def copy_password():
            password = password_entry.get()
            pyperclip.copy(password)
            messagebox.showinfo("Sao chép", "Đã sao chép mật khẩu vào clipboard.")

        from tkinter import filedialog

        from tkinter.simpledialog import askstring

        def select_file():
            if not giatricuu.emailhientai:
                messagebox.showwarning("Lỗi", "Chưa đăng nhập.")
                return

            # ✅ Nhập key giải mã
            if(giatricuu.mahoa==1):
                key = askstring("Nhập khóa", "File đang bị mã hóa. Nhập khóa để giải mã thư mục:")
                if not key:
                    messagebox.showwarning("Lỗi", "Bạn chưa nhập khóa.")
                    return
                # Gán key vào biến toàn cục để hàm giải mã khác dùng

                if isinstance(giatricuu.keyhientai, bytes):
                    giatricuu.keyhientai = giatricuu.keyhientai.decode()
                if (giatricuu.keyhientai==key):
                    # Đường dẫn thư mục cá nhân
                    messagebox.showinfo("Thành công", "Nhập key thành công!")
                    decrypt_user_folder()
                    base_path = r"C:\Appne"
                    user_dir = os.path.join(base_path, giatricuu.emailhientai)

                    if not os.path.exists(user_dir):
                        messagebox.showerror("Lỗi", "Không tìm thấy thư mục người dùng.")
                        return

                    # Chỉ cho phép lưu file trong thư mục cá nhân
                    path = filedialog.asksaveasfilename(
                        defaultextension=".txt",
                        filetypes=[("Text Files", "*.txt")],
                        title="Chọn tên file lưu mật khẩu",
                        initialdir=user_dir,
                        initialfile="passwords.txt"
                    )

                    if path:
                        abs_user_dir = os.path.abspath(user_dir)
                        abs_path = os.path.abspath(path)
                        if not abs_path.startswith(abs_user_dir):
                            messagebox.showerror("Lỗi", "Bạn chỉ được lưu file trong thư mục cá nhân của mình.")
                            return

                        nameF_path.set(path)
                else:
                    messagebox.showerror("Lỗi", "Sai key rồi địt mẹ mày.")
            else:
                base_path = r"C:\Appne"
                user_dir = os.path.join(base_path, giatricuu.emailhientai)

                if not os.path.exists(user_dir):
                    messagebox.showerror("Lỗi", "Không tìm thấy thư mục người dùng.")
                    return

                # Chỉ cho phép lưu file trong thư mục cá nhân
                path = filedialog.asksaveasfilename(
                    defaultextension=".txt",
                    filetypes=[("Text Files", "*.txt")],
                    title="Chọn tên file lưu mật khẩu",
                    initialdir=user_dir,
                    initialfile="passwords.txt"
                )

                if path:
                    abs_user_dir = os.path.abspath(user_dir)
                    abs_path = os.path.abspath(path)
                    if not abs_path.startswith(abs_user_dir):
                        messagebox.showerror("Lỗi", "Bạn chỉ được lưu file trong thư mục cá nhân của mình.")
                        return

                    nameF_path.set(path)

        def save_to_file():
            pwd = password_entry.get()
            path = nameF_path.get()
            if path == "Chưa chọn file" or not path.strip():
                messagebox.showwarning("Chưa chọn file", "Vui lòng chọn file lưu trữ trước.")
                return

            if not pwd:
                messagebox.showwarning("Mật khẩu trống", "Không có mật khẩu để lưu.")
                return
            if (giatricuu.mahoa == 1):
                messagebox.showwarning("Lỗi", "Thư mục đang bị mã hóa, vui lòng nhập lại")
                select_file()
            else:
                try:
                    with open(path, "a", encoding="utf-8") as f:
                        f.write(pwd + "\n")
                    messagebox.showinfo("Thành công", "Mật khẩu đã được lưu vào file.")
                except Exception as e:
                    messagebox.showerror("Lỗi", f"Không thể lưu file:\n{e}")



















        # Khung chính căn giữa

        # main_frame.pack(expand=True)
        main_frame.grid(row=0, column=0, sticky="nsew")  # dùng grid
        # Bên trong main_frame: tất cả .grid(...)
        main_frame.grid_rowconfigure(0,weight=1)
        main_frame.grid_rowconfigure(1,weight=5)
        main_frame.grid_columnconfigure(0,weight=1)

        #LAYOUT lever 1
        # Tạo frame chứa tiêu đề
        title_frame = Frame(main_frame)
        title_frame.grid(row=0, column=0)
        title_frame.grid_rowconfigure(0,weight=1)
        title_frame.grid_rowconfigure(1,weight=1)
        title_frame.grid_columnconfigure(0,weight=1)
        # Tạo frame chứa thông tin chính
        main_content_frame = Frame(main_frame, bg="violet", bd=2, relief="solid")
        main_content_frame.grid(row=1, column=0, sticky="nsew")
        main_content_frame.grid_rowconfigure(0,weight=1)
        main_content_frame.grid_columnconfigure(0,weight=1)

        #LAYOUT lever 2
        # Tạo label cho tiêu đề
        tk.Label(title_frame, text="Trình tạo mật khẩu ngẫu nhiên", font=("Arial", 20, "bold")).grid(row=0, column=0,pady=(0, 15))
        tk.Label(title_frame, text="Hãy tạo mật khẩu mạnh và đủ an toàn để bảo vệ tài khoản trên mạng của bạn.",font=("Arial", 14)).grid(row=1, column=0, pady=(0, 15))
        # Tạo khung con cho thông tin chính
        content_frame = Frame(main_content_frame, bg="white")
        content_frame.grid(row=0, column=0,sticky="nsew",padx=10,pady=10)
        content_frame.grid_rowconfigure(0,weight=1)
        content_frame.grid_rowconfigure(1, weight=1)

        content_frame.grid_columnconfigure(0,weight=1)

        #LAYOUT lever 3
        # Tao Frame chứa mật khẩu và nút làm mới, kiểm tra
        detail_frame_1 = Frame(content_frame)
        detail_frame_1.grid(row=0, column=0,sticky="nsew", pady=5)
        detail_frame_1.grid_rowconfigure(0,weight=1)
        detail_frame_1.grid_rowconfigure(1,weight=1)
        detail_frame_1.grid_columnconfigure(0,weight=1)
        detail_frame_1.grid_columnconfigure(1,weight=1)
        detail_frame_1.grid_columnconfigure(2,weight=1)

        frame_display_pass = Frame(detail_frame_1)
        frame_display_pass.grid(row = 0, column = 0, sticky = "nsew")
        for i in range(3):
            frame_display_pass.grid_rowconfigure(i,weight=1)
            frame_display_pass.grid_columnconfigure(i,weight=1)
        password_entry = tk.Entry(frame_display_pass, font=("Arial", 14), justify="center")
        password_entry.grid(row=1, column=1, sticky="ew", padx = 5)

        frame_display_strong = Frame(detail_frame_1)
        frame_display_strong.grid(row=1, column = 0, sticky="nsew")
        for i in range(3):
            frame_display_strong.grid_rowconfigure(i,weight=1)
        for i in range(2):
            frame_display_strong.grid_columnconfigure(i,weight=1)
        tk.Label(frame_display_strong, text="Mật khẩu mạnh: ", font=("Arial", 12, "bold")).grid(row=1, column=0,padx=10)
        strength_label = tk.Label(frame_display_strong, text="Default", font=("Arial", 12, "bold"))
        strength_label.grid(row=1, column=1,sticky="w")

        frame_display_renew = Frame(detail_frame_1)
        frame_display_renew.grid(row=0, column=1, rowspan = 2, sticky="nsew")
        for i in range(3):
            frame_display_renew.grid_rowconfigure(i,weight=1)
            frame_display_renew.grid_columnconfigure(i,weight=1)
        generate_btn = tk.Button(frame_display_renew, text="Tạo Mới", font=("Arial", 12, "bold"), command=generate_password, bg="lightgreen")
        generate_btn.grid(row=1,column=1, sticky="nsew", padx = 10, pady=10)

        frame_display_check = Frame(detail_frame_1)
        frame_display_check.grid(row=0,column=2,rowspan=2, sticky="nsew")
        for i in range(3):
            frame_display_check.grid_rowconfigure(i,weight=1)
            frame_display_check.grid_columnconfigure(i,weight=1)
        check_btn = tk.Button(frame_display_check, text="Kiểm Tra", font=("Arial", 12, "bold"),command=update_strong, bg="lightyellow")
        check_btn.grid(row=1,column=1, sticky="nsew", padx = 10, pady=10)


        # Tạo Frame chứa độ dài và options và nút Lưu và Sao chép
        detail_frame_2 = Frame(content_frame)
        detail_frame_2.grid(row=1, column=0, sticky="nsew", pady=5)
        for i in range(5):
            detail_frame_2.grid_rowconfigure(i, weight=1)
        detail_frame_2.grid_columnconfigure(0, weight=1)
        detail_frame_2.grid_columnconfigure(1, weight=1)

        frame_display_pwdlength = Frame(detail_frame_2)
        frame_display_pwdlength.grid(row=0,column=0,sticky="nsew")
        tk.Label(frame_display_pwdlength, text="Độ dài mật khẩu:", font=("Arial", 12, "bold")).pack(fill="both",side="left", padx=10)
        password_length_text = tk.Text(frame_display_pwdlength, wrap="word",font=("Arial", 12, "bold"), height=0.5, width=4)
        password_length_text.pack(fill="x",side="left",padx=10)

        use_upper = tk.BooleanVar(value=True)
        use_lower = tk.BooleanVar(value=True)
        use_digits = tk.BooleanVar(value=True)
        use_symbols = tk.BooleanVar(value=False)
        frame_display_optionUpper = Frame(detail_frame_2)
        frame_display_optionUpper.grid(row=1,column=0,sticky="nsew")
        tk.Checkbutton(frame_display_optionUpper, text="Sử dụng chữ hoa (A-Z)", font=("Arial", 12, "bold"), variable=use_upper).pack(fill="both",side="left", padx=10)

        frame_display_optionLower = Frame(detail_frame_2)
        frame_display_optionLower.grid(row=2,column=0,sticky="nsew")
        tk.Checkbutton(frame_display_optionLower, text="Sử dụng chữ thường (a-z)", font=("Arial", 12, "bold"), variable=use_lower).pack(fill="both",side="left", padx=10)

        frame_display_optionNum = Frame(detail_frame_2)
        frame_display_optionNum.grid(row=3,column=0,sticky="nsew")
        tk.Checkbutton(frame_display_optionNum, text="Sử dụng chữ số (0-9)", font=("Arial", 12, "bold"), variable=use_digits).pack(fill="both",side="left", padx=10)

        frame_display_optionSpecial = Frame(detail_frame_2)
        frame_display_optionSpecial.grid(row=4,column=0,sticky="nsew")
        tk.Checkbutton(frame_display_optionSpecial, text="Sử dụng ký hiêu đặc biệt (@#$...)", font=("Arial", 12, "bold"), variable=use_symbols).pack(fill="both",side="left", padx=10)

        frame_display_nameFile = Frame(detail_frame_2)
        frame_display_nameFile.grid(row=0,column=1,sticky="nsew")
        frame_display_nameFile.grid_rowconfigure(0,weight=1)
        for i in range(3):
            frame_display_nameFile.grid_columnconfigure(i,weight=1)
        nameF_path = tk.StringVar(value="Chưa chọn file")
        nameF = tk.Label(frame_display_nameFile, textvariable=nameF_path, font=("Arial", 20, "bold"))
        nameF.grid(row=0, column=1, sticky="nsew", padx=10)

        frame_display_inputFile = Frame(detail_frame_2)
        frame_display_inputFile.grid(row=1,column=1,sticky="nsew")
        frame_display_inputFile.grid_rowconfigure(0,weight=1)
        for i in range(3):
            frame_display_inputFile.grid_columnconfigure(i,weight=1)
        inputF_btn = tk.Button(frame_display_inputFile, text="Nhập file lưu trữ", font=("Arial", 12, "bold"), command=select_file)
        inputF_btn.grid(row=0,column=1, sticky="nsew", padx=10)

        frame_display_saveFile = Frame(detail_frame_2)
        frame_display_saveFile.grid(row=3,column=1,sticky="nsew")
        frame_display_saveFile.grid_rowconfigure(0,weight=1)
        for i in range(3):
            frame_display_saveFile.grid_columnconfigure(i,weight=1)
        saveF_btn = tk.Button(frame_display_saveFile, text="Lưu vào file", font=("Arial", 12, "bold"), bg="white", command=save_to_file)
        saveF_btn.grid(row=0, column=1, sticky="nsew", padx=10)

        saveF_btn = tk.Button(frame_display_saveFile, text="Mã hóa thư mục", font=("Arial", 12, "bold"), bg="white",command= encrypt_user_folder )
        saveF_btn.grid(row=1, column=1, sticky="nsew", padx=10)

        frame_display_copy = Frame(detail_frame_2)
        frame_display_copy.grid(row=4,column=1,sticky="nsew")
        frame_display_copy.grid_rowconfigure(0, weight=1)
        for i in range(3):
            frame_display_copy.grid_columnconfigure(i, weight=1)
        copy_btn = tk.Button(frame_display_copy, text="Sao chép", font=("Arial", 12, "bold"), bg="lightgreen", command=copy_password)
        copy_btn.grid(row=0, column=1, sticky="nsew", padx=10)
    else:
        main_frame.grid(row=0, column=0, sticky="nsew")
        label = tk.Label(main_frame, text="Vui lòng đăng nhập để sử dụng chức năng này", font=("Arial", 20))
        label.grid(row=3, column=3, sticky="w")

    frames["matkhau"] = main_frame
