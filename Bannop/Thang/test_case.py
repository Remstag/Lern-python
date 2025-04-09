import os
import time
import Gutmann

# Tạo file lớn (10MB)
large_file = "large_test.txt"
with open(large_file, "wb") as f:
    f.write(os.urandom(10 * 1024 * 1024))  # 10MB dữ liệu ngẫu nhiên

# Kiểm tra tồn tại
assert os.path.exists(large_file), "Lỗi: File lớn không được tạo"

# Đo thời gian xóa
start_time = time.time()
Gutmann.gutmann_wipe(large_file)
end_time = time.time()

# Kiểm tra file đã bị xóa
assert not os.path.exists(large_file), "Lỗi: File lớn chưa bị xóa!"
print(f" Test case 3: Xóa file lớn - PASSED! (Thời gian: {end_time - start_time:.2f}s)")
