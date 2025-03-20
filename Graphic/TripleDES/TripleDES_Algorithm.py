from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad



# Hàm mã hóa 3DES
def mahoa(text, key, iv):
    # Chuyển text sang bytes
    data = text.encode('utf-8')
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    padded_data = pad(data, DES3.block_size)
    encrypted = cipher.encrypt(padded_data)
    return encrypted.hex()  # Trả về dạng hex để dễ truyền

def giaima(text_mahoa, key, iv):
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    encrypted_bytes = bytes.fromhex(text_mahoa)
    decrypted = cipher.decrypt(encrypted_bytes)
    unpadded = unpad(decrypted, DES3.block_size)
    return unpadded.decode('utf-8')
