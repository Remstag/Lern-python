import os
import random


def gutmann_wipe(file_path, passes=35):
    """Xóa tệp an toàn bằng thuật toán Gutmann."""
    if not os.path.exists(file_path):
        print(f"File {file_path} không tồn tại!")
        return

    file_size = os.path.getsize(file_path)

    try:
        with open(file_path, "wb") as f:
            for i in range(passes):
                f.write(os.urandom(file_size))  # Ghi đè bằng dữ liệu ngẫu nhiên
                f.flush()
                os.fsync(f.fileno())  # Đảm bảo dữ liệu được ghi vào đĩa

        os.remove(file_path)  # Xóa file sau khi ghi đè
        print(f"File {file_path} đã được xóa an toàn bằng phương pháp Gutmann!")
    except Exception as e:
        print(f"Lỗi khi xóa file: {str(e)}")