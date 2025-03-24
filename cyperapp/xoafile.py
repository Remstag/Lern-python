import random
import os
quyen=""
status="❌ Xóa file thất bại"
def checkquyen(file_path):
    global quyen
    if not os.path.exists(file_path):
        quyen= "❌ File không tồn tại!"
        return False
    if not os.access(file_path, os.W_OK):
        quyen= "🚫 Không có quyền xóa file! Thử chạy với admin."
        return False
    quyen= "✅ Bạn có quyền xóa file này!"
    return True
def xoafilee(file_path):
    global status
    size=os.path.getsize(file_path)
    with open(file_path, "wb") as f:
        f.write(b'\x00' * size) #lan 1
        f.flush()

        f.write(b'xFF'*size) # lan 2
        f.flush()

        f.seek(0)
        f.write(os.urandom(size))
        f.flush()
    os.remove(file_path)
    status="✅ Xóa file thành công"

