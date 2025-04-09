from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Tạo khóa hợp lệ (24 byte cho 3DES)
#def generate_key():
#    return DES3.adjust_key_parity(get_random_bytes(24))  # Điều chỉnh parity cho hợp lệ

# Tạo IV hợp lệ (8 byte cho 3DES)
#def generate_iv():
#    return get_random_bytes(8)

# Hàm mã hóa 3DES
def mahoa(texxt, keyy, IV):
    if len(keyy) not in [16, 24]:
        raise ValueError("Khóa không hợp lệ! 3DES yêu cầu khóa 16 hoặc 24 byte.")
    if len(IV) != 8:
        raise ValueError("IV không hợp lệ! 3DES yêu cầu IV có 8 byte.")
    texxt = str(texxt)  # Chuyển dữ liệu sang chuỗi nếu chưa phải
    cipher = DES3.new(keyy, DES3.MODE_CBC, IV)  # Sử dụng chế độ CBC giống AES
    encrypted_bytes = cipher.encrypt(pad(texxt.encode(), DES3.block_size))  # Padding dữ liệu trước khi mã hóa
    return encrypted_bytes.hex()  # Chuyển kết quả thành hex để dễ lưu trữ

# Hàm giải mã 3DES
def giaima(mh, keyy, IV):
    if len(keyy) not in [16, 24]:
        raise ValueError("Khóa không hợp lệ! 3DES yêu cầu khóa 16 hoặc 24 byte.")
    if len(IV) != 8:
        raise ValueError("IV không hợp lệ! 3DES yêu cầu IV có 8 byte.")
    cipher = DES3.new(keyy, DES3.MODE_CBC, IV)
    encrypted_bytes = bytes.fromhex(mh)  # Chuyển dữ liệu hex về dạng bytes
    decrypted_text = unpad(cipher.decrypt(encrypted_bytes), DES3.block_size)  # Giải mã và loại bỏ padding
    return decrypted_text.decode("utf-8")  # Chuyển bytes về chuỗi UTF-8