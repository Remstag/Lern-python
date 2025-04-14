import os
import random

quyen = ""
status = "❌ Xóa file thất bại"

def checkquyen(file_path):
    global quyen
    if not os.path.exists(file_path):
        quyen = "❌ File không tồn tại!"
        return False
    if not os.access(file_path, os.W_OK):
        quyen = "🚫 Không có quyền xóa file! Thử chạy với admin."
        return False
    quyen = "✅ Bạn có quyền xóa file này!"
    return True

def gutmann_patterns():
    patterns = []

    # 1–4: Ghi đè bằng dữ liệu ngẫu nhiên
    for _ in range(4):
        patterns.append("random")

    # 5–31: Ghi đè bằng các mẫu cụ thể (mô phỏng)
    fixed_patterns = [
        b'\x55', b'\xAA', b'\x92', b'\x49', b'\x24',
        b'\x00', b'\x11', b'\x22', b'\x33', b'\x44',
        b'\xFF', b'\x66', b'\x99', b'\xCC', b'\xF0',
        b'\x0F', b'\x5A', b'\xA5', b'\x3C', b'\xC3',
        b'\x69', b'\x96', b'\x18', b'\x81', b'\xE7',
        b'\x7E', b'\x1B'
    ]
    patterns.extend(fixed_patterns[:27])  # 27 mẫu → pass 5–31

    # 32–35: Ghi đè bằng dữ liệu ngẫu nhiên
    for _ in range(4):
        patterns.append("random")

    return patterns

# Hàm xóa file theo Gutmann
def xoafile_gutmann(file_path):
    global status
    if not checkquyen(file_path):
        return

    try:
        file_size = os.path.getsize(file_path)
        patterns = gutmann_patterns()

        with open(file_path, "r+b") as f:
            for i, pattern in enumerate(patterns):
                f.seek(0)
                if pattern == "random":
                    f.write(os.urandom(file_size))
                else:
                    f.write(pattern * file_size)
                f.flush()
                os.fsync(f.fileno())

        os.remove(file_path)
        status = "✅ Đã xóa an toàn bằng phương pháp Gutmann (35-pass)"
    except Exception as e:
        status = f"❌ Lỗi khi xóa file: {str(e)}"