from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

# # Khóa bí mật (4 - 56 byte)
# key = b'lKSLDnnskjcLKADNflksjdnlksnvksajdf'
#
# # Dữ liệu cần mã hóa
# text = b'This is secret data.'
#
# # Tạo IV ngẫu nhiên (Blowfish sử dụng block size = 8 bytes)
# iv = get_random_bytes(Blowfish.block_size)


def mahoa(text, key, iv):
    # Chuyển text sang bytes
    data = text.encode('utf-8')
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    padded_data = pad(data, Blowfish.block_size)
    encrypted = cipher.encrypt(padded_data)
    return encrypted.hex()  # Trả về dạng hex để dễ truyền

def giaima(text_mahoa, key, iv):
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    encrypted_bytes = bytes.fromhex(text_mahoa)
    decrypted = cipher.decrypt(encrypted_bytes)
    unpadded = unpad(decrypted, Blowfish.block_size)
    return unpadded.decode('utf-8')