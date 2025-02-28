from tkinter import Tk, Button, filedialog, Label

# Tạo hoặc tải khóa
key = Fernet.generate_key()
cipher = Fernet(key)


def encrypt_file():
    file_path = filedialog.askopenfilename(title="Chọn file để mã hóa")
    if file_path:
        with open(file_path, "rb") as f:
            data = f.read()
        encrypted_data = cipher.encrypt(data)

        save_path = filedialog.asksaveasfilename(defaultextension=".enc", title="Lưu file mã hóa")
        if save_path:
            with open(save_path, "wb") as f:
                f.write(encrypted_data)

            with open("key.key", "wb") as key_file:
                key_file.write(key)

            status_label.config(text=f"Đã mã hóa: {save_path}")


# Tạo giao diện
win = Tk()
win.title("Mã hóa File")

Button(win, text="Chọn File để Mã hóa", command=encrypt_file).pack(pady=10)
status_label = Label(win, text="")
status_label.pack(pady=10)

win.mainloop()
