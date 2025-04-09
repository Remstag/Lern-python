from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad



# Hàm mã hóa 3DES
def mahoa(text, key, iv):
    if len(key) not in [16, 24]:
        raise ValueError("Khóa không hợp lệ! 3DES yêu cầu khóa 16 hoặc 24 byte.")
    if len(iv) != 8:
        raise ValueError("IV không hợp lệ! 3DES yêu cầu IV có 8 byte.")
    texxt = str(text)  # Chuyển dữ liệu sang chuỗi nếu chưa phải
    cipher = DES3.new(key, DES3.MODE_CBC, iv)  # Sử dụng chế độ CBC giống AES
    encrypted_bytes = cipher.encrypt(pad(texxt.encode(), DES3.block_size))  # Padding dữ liệu trước khi mã hóa
    return encrypted_bytes.hex() # Trả về dạng hex để dễ truyền

def giaima(text_mahoa, key, iv):
    if len(key) not in [16, 24]:
        raise ValueError("Khóa không hợp lệ! 3DES yêu cầu khóa 16 hoặc 24 byte.")
    if len(iv) != 8:
        raise ValueError("IV không hợp lệ! 3DES yêu cầu IV có 8 byte.")
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    encrypted_bytes = bytes.fromhex(text_mahoa)  # Chuyển dữ liệu hex về dạng bytes
    decrypted_text = unpad(cipher.decrypt(encrypted_bytes), DES3.block_size)  # Giải mã và loại bỏ padding
    return decrypted_text.decode("utf-8")  # Chuyển bytes về chuỗi UTF-8
