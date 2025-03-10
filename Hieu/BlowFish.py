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
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    padded_data = pad(text, Blowfish.block_size)
    encrypted = cipher.encrypt(padded_data)

    # Ghép IV + ciphertext để giải mã sau
    encrypted_data = iv + encrypted
    encoded = base64.b64encode(encrypted_data)

    return encoded.decode().hex()

def giaima(text, key, iv):
    decoded = base64.b64decode(encoded)
    iv_dec = decoded[:Blowfish.block_size]
    ciphertext = decoded[Blowfish.block_size:]

    cipher_dec = Blowfish.new(key, Blowfish.MODE_CBC, iv_dec)
    decrypted = unpad(cipher_dec.decrypt(ciphertext), Blowfish.block_size)

    return decrypted.decode()