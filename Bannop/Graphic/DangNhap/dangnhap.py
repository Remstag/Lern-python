from tkinter import *
from tkinter import Button, filedialog, messagebox

import mysql
from PIL.ImageOps import expand
import random
import os
import string
import secrets

from Bannop.Graphic.Database import get_db_connection

frames={}
def dangnhap(main_content):
    def dangky():
        email = entry_email.get("1.0", "end-1c").strip()
        password = entry_pass.get("1.0", "end-1c").strip()

        if not email or not password:
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin.")
            return

        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id_user INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                email TEXT NOT NULL
            )
            ''')

            # Ở đây dùng email làm username luôn, có thể chỉnh lại nếu bạn có ô username riêng
            cursor.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
                           (email, password, email))
            conn.commit()
            conn.close()

            messagebox.showinfo("Thành công", "Đăng ký thành công!")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể đăng ký: {e}")

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

    dn_btn = Button(frame_dangnhap,text="Đăng Nhập", font=("Arial",14))
    dn_btn.grid(row=4, column=1)

    dk_btn = Button(frame_dangnhap,text="Đăng Ký", font=("Arial",14), command=dangky)
    dk_btn.grid(row=5, column=1)


    frames["dangnhap"] = frame