import random, string
import tkinter as tk
from tkinter import Label, Frame, Button, Text
root = tk.Tk()
root.title("PYTHON CRYPTION")
def setPass():
    passWord.delete("1.0", "end")
    random_Pass = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
    passWord.insert("end", random_Pass)
    passWord.tag_add("custom_font", "1.0", "end")
    passWord.tag_configure("custom_font", font=("Arial", 13))

# Lấy kích thước màn hình và set kích thước cửa sổ = 1/2
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = int(screen_width * 0.8)
height = int(screen_height * 0.8)
x = int((screen_width - width) / 2)
y = int((screen_height - height) / 2)
root.geometry(f"{width}x{height}+{x}+{y}")
root.grid_rowconfigure(0,weight=1)
root.grid_columnconfigure(0,weight=1)


passWord_frame = Frame(root, bd=1, relief="solid")
passWord_frame.grid(row=0, column=0)
for i in range(3):
    passWord_frame.grid_rowconfigure(i, weight=1)
    passWord_frame.grid_columnconfigure(i,weight=1)
passWord = Text(passWord_frame, wrap="word", height=2, width=60)
passWord.grid(row=1,column=0)
taoPassAuto = Button(passWord_frame,text = "Tao Pass", height=4, width=10, command=setPass)
taoPassAuto.grid(row=1,column=1)

tinhNang = Frame(root, bd=1, relief="solid")


root.mainloop()