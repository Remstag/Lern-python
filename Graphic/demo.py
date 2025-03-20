import tkinter as tk

def create_window():
    # Khởi tạo cửa sổ chính
    root = tk.Tk()
    root.title("PYTHON CRYPTION")

    # Lấy kích thước màn hình
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Tính kích thước mặc định (1/2 màn hình)
    window_width = screen_width // 2
    window_height = screen_height // 2

    # Tính vị trí để cửa sổ ở giữa màn hình
    x_pos = (screen_width - window_width) // 2
    y_pos = (screen_height - window_height) // 2

    # Thiết lập kích thước và vị trí cửa sổ
    root.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")

    # Chạy vòng lặp giao diện
    root.mainloop()

if __name__ == "__main__":
    create_window()
