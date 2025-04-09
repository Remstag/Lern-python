import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import pyperclip

frames={}
def taomatkhau(main_content):

    # Các chỉ số đánh giá độ mạnh yếu của mật khẩu
    def strong_pass(password):
        cnt_upper, cnt_lower, cnt_num, cnt_special = 0,0,0,0
        for i in password:
            if 'A' <= i <= 'Z': cnt_upper += 1
            elif 'a' <= i <= 'z': cnt_lower += 1
            elif '0' <= i <= '9': cnt_num += 1
            else:
                cnt_special += 1
        return cnt_upper, cnt_lower, cnt_num, cnt_special


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
            password_length_1 = int(password_length_text.get("1.0", "end").strip())
            password_length = tk.IntVar(value=password_length_1)
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

        cnt_upper, cnt_lower, cnt_num, cnt_special = strong_pass(password)

        mark_strong = 0
        mark_strong = calculation_markStrong(cnt_upper, cnt_lower, cnt_num, cnt_special, len(password))
        # Đánh giá độ mạnh (rất đơn giản)
        if 9 <= mark_strong <= 10:
            strength_label.config(text="🔐 Very Strong", fg="green4")
        elif 7 <= mark_strong <= 8:
            strength_label.config(text="✅ Strong", fg="green")
        elif 5 <= mark_strong <= 6:
            strength_label.config(text="⚠️ Medium", fg="yellow4")
        elif 3 <= mark_strong <= 4:
            strength_label.config(text="❌ Weak", fg="orange")
        else:
            strength_label.config(text="🚫 Very Weak", fg="red")

    # Sao chép mật khẩu
    def copy_password():
        password = password_entry.get()
        pyperclip.copy(password)
        messagebox.showinfo("Sao chép", "Đã sao chép mật khẩu vào clipboard.")


    # Khung chính căn giữa
    main_frame = tk.Frame(main_content)
    # main_frame.pack(expand=True)
    main_frame.grid(row=0, column=0, sticky="nsew")  # dùng grid
    # Bên trong main_frame: tất cả .grid(...)

    # Tiêu đề
    tk.Label(main_frame, text="Trình tạo mật khẩu ngẫu nhiên", font=("Helvetica", 18, "bold")).pack(pady=(10, 5))
    tk.Label(main_frame, text="Hãy tạo mật khẩu mạnh và đủ an toàn để bảo vệ tài khoản trên mạng của bạn.", font=("Helvetica", 10)).pack(pady=(0, 15))

    # Ô hiển thị mật khẩu
    password_frame = tk.Frame(main_frame)
    password_frame.pack()

    password_entry = tk.Entry(password_frame, font=("Helvetica", 14), width=20, justify="center")
    password_entry.pack(side="left", padx=5)

    strength_label = tk.Label(password_frame, text="", font=("Helvetica", 10, "bold"))
    strength_label.pack(side="left")

    # Nút tạo và sao chép
    button_frame = tk.Frame(main_frame)
    button_frame.pack(pady=10)

    generate_btn = tk.Button(button_frame, text="🔄 Tạo mới", command=generate_password, bg="#f0f0f0")
    generate_btn.pack(side="left", padx=10)

    copy_btn = tk.Button(button_frame, text="Sao chép", command=copy_password, bg="#008CFF", fg="white")
    copy_btn.pack(side="left", padx=10)

    # Thanh điều chỉnh độ dài
    tk.Label(main_frame, text="Độ dài mật khẩu:").pack()
    password_length_text = tk.Text(main_frame, wrap="word", height=1, width=4)
    password_length_text.pack(pady=(0,10))

    # password_length_label = tk.Label(main_frame,text=password_length, font=("Helvetica", 10, "bold"))
    # password_length_label.pack(pady=(0,10))
    # length_slider = ttk.Scale(main_frame, from_=1, to=30, variable=password_length, orient="horizontal")
    # length_slider.pack(pady=(0, 10))

    # Checkbox chọn ký tự
    tk.Label(main_frame, text="Ký tự được sử dụng:", font=("Helvetica", 10)).pack()

    option_frame = tk.Frame(main_frame)
    option_frame.pack()

    use_upper = tk.BooleanVar(value=True)
    use_lower = tk.BooleanVar(value=True)
    use_digits = tk.BooleanVar(value=True)
    use_symbols = tk.BooleanVar(value=False)

    tk.Checkbutton(option_frame, text="ABC", variable=use_upper).pack(side="left", padx=10)
    tk.Checkbutton(option_frame, text="abc", variable=use_lower).pack(side="left", padx=10)
    tk.Checkbutton(option_frame, text="123", variable=use_digits).pack(side="left", padx=10)
    tk.Checkbutton(option_frame, text="#$&", variable=use_symbols).pack(side="left", padx=10)

    frames["matkhau"] = main_frame
