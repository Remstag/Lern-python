from tkinter import *
from tkinter import  Button, filedialog

from PIL.ImageOps import expand

import random
import os
import string
import secrets
from Graphic import giatricuu
frames={}
def thb(main_content):
    frame = Frame(main_content)
    frame.grid(row=0, column=0, sticky="nsew")
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_rowconfigure(1, weight=3)
    frame.grid_columnconfigure(0, weight=1)
    label=Label( frame, text="Vui lòng đăng nhập để sử dụng chức năng này", font=("Arial",20))
    label.grid(row=1,column=1,sticky="w")






    frames["thongbao"] = frame