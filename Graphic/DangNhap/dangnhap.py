from tkinter import *
from tkinter import Button, filedialog, messagebox

from PIL.ImageOps import expand
import random
import os
import string
import secrets
from Graphic import giatricuu
from Graphic.Database import get_db_connection
giatricuu.x=0
frames={}
def dangnhap(main_content):
    def dangky():
        email = entry_email.get("1.0", "end-1c").strip()
        password = entry_pass.get("1.0", "end-1c").strip()
        random_iv = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=16))
        thoo=password+random_iv
        if not email or not password:
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin.")
            return

        try:
            def generate_key_from_password(thoo: str):
                import base64, hashlib
                key = hashlib.sha256(thoo.encode()).digest()
                return base64.urlsafe_b64encode(key)

            keyy = generate_key_from_password(thoo)
            conn = get_db_connection()
            cursor = conn.cursor()

            # Ở đây dùng email làm username luôn, có thể chỉnh lại nếu bạn có ô username riêng
            cursor.execute("INSERT INTO users (username, password, key) VALUES (?, ?, ?)",
                           (email, password, keyy))
            conn.commit()
            idd_user = cursor.lastrowid

            folder_name = str(email)
            base_path = r"C:\Appne"  # Đường dẫn gốc
            duongdan = os.path.join(base_path, folder_name)

            # Tạo thư mục nếu chưa tồn tại
            if not os.path.exists(duongdan):
                os.makedirs(duongdan)
                print(f"✅ Đã tạo thư mục tại: {duongdan}")
            else:
                print(f"📁 Thư mục đã tồn tại tại: {duongdan}")

            cursor.execute("INSERT INTO kho (link, id_user) VALUES (?, ?)", (duongdan, idd_user))
            conn.commit()

            conn.close()

            messagebox.showinfo("Thành công", "Đăng ký thành công!")

        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể đăng ký: {e}")
        finally:
          if conn:
            conn.close()

    def dangnhap():
        email = entry_email.get("1.0", "end-1c").strip()
        password = entry_pass.get("1.0", "end-1c").strip()

        if not email or not password:
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin.")
            return

        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (email, password))
            user = cursor.fetchone()
            conn.close()
            giatricuu.emailhientai=email
            giatricuu.passhientai=password
            if user:
                messagebox.showinfo("Thành công", "Đăng nhập thành công!")
                id_user, email, password, key = user
                giatricuu.emailhientai = email
                giatricuu.passhientai = password
                giatricuu.keyhientai = key
                giatricuu.uid = id_user
                conn = get_db_connection()
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM kho WHERE id_user = ? ", (id_user,))
                folder = cursor.fetchone()
                conn.close()
                file_id,path,id_u=folder
                giatricuu.duongdanfile=path

                giatricuu.x=1
                # Ở đây bạn có thể chuyển sang màn hình khác, hoặc lưu trạng thái đăng nhập
            else:
                messagebox.showerror("Lỗi", "Email hoặc mật khẩu không đúng.")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể đăng nhập: {e}")
    frame = Frame(main_content)
    frame.grid(row=0, column=0, sticky="nsew")
    for i in range(3):
        frame.grid_rowconfigure(i, weight=1)
        frame.grid_columnconfigure(i, weight=1)

    #Frame include nhapkey, nhapiv: label, text, button
    frame_dangnhap = Frame(frame,bd=2,relief="solid")
    frame_dangnhap.grid(row=1,column=1)
    for i in range(6):
        frame_dangnhap.grid_rowconfigure(i,weight=1)
    frame_dangnhap.grid_columnconfigure(0,weight=1)
    frame_dangnhap.grid_columnconfigure(1,weight=1)
    frame_dangnhap.grid_columnconfigure(2,weight=1)

    email_lb = Label(frame_dangnhap, text="Email",font=("Arial",14))
    email_lb.grid(row=0,column=1,sticky="w", padx = 10, pady=10)
    entry_email = Text(frame_dangnhap, wrap="word", height=2, width=60)
    entry_email.grid(row=1,column=1,sticky="nsew", padx = 10, pady=10)

    pass_lb = Label(frame_dangnhap, text="Pass", font=("Arial", 14))
    pass_lb.grid(row=2, column=1, sticky="w", padx = 10, pady=10)
    entry_pass = Text(frame_dangnhap, wrap="word", height=2, width=60)
    entry_pass.grid(row=3,column=1, sticky="nsew", padx = 10, pady=10)

    dn_btn = Button(frame_dangnhap,text="Đăng Nhập", font=("Arial",14),command=dangnhap)
    dn_btn.grid(row=4, column=1)

    dk_btn = Button(frame_dangnhap,text="Đăng Ký", font=("Arial",14), command=dangky)
    dk_btn.grid(row=5, column=1)


    frames["dangnhap"] = frame