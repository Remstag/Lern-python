from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
import time

# Sinh khóa 24 byte an toàn hơn
def generate_key():
    return DES3.adjust_key_parity(get_random_bytes(24))  # Điều chỉnh parity cho hợp lệ

# Sinh IV an toàn hơn: 4 byte timestamp + 4 byte random
def generate_iv():
    return int(time.time()).to_bytes(4, 'big') + get_random_bytes(4)

# Hàm mã hóa
def encrypt_3des(plaintext, key, iv):
    cipher = DES3.new(key, DES3.MODE_CFB, iv)  # Dùng chế độ CFB
    encrypted_text = cipher.encrypt(plaintext.encode())  # Chuyển sang bytes và mã hóa
    return encrypted_text

# Hàm giải mã
def decrypt_3des(encrypted_text, key, iv):
    cipher = DES3.new(key, DES3.MODE_CFB, iv)
    decrypted_text = cipher.decrypt(encrypted_text).decode()  # Giải mã rồi chuyển về chuỗi
    return decrypted_text

# Mã hóa và giải mã file
def encrypt_file(input_file, output_file, key, iv):
    with open(input_file, 'rb') as f:
        plaintext = f.read()
    cipher = DES3.new(key, DES3.MODE_CFB, iv)
    encrypted_text = cipher.encrypt(plaintext)
    with open(output_file, 'wb') as f:
        f.write(iv + encrypted_text)  # Lưu IV vào đầu file

def decrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as f:
        iv = f.read(8)  # Lấy 8 byte IV từ file
        encrypted_text = f.read()
    cipher = DES3.new(key, DES3.MODE_CFB, iv)
    decrypted_text = cipher.decrypt(encrypted_text)
    with open(output_file, 'wb') as f:
        f.write(decrypted_text)

# Demo
key = generate_key()  # Tạo khóa 24 byte
iv = generate_iv()  # Tạo IV 8 byte
plaintext = "Hello, this is a secure message!"

encrypted_text = encrypt_3des(plaintext, key, iv)
decrypted_text = decrypt_3des(encrypted_text, key, iv)

print("Plaintext:", plaintext)
print("Encrypted (hex):", encrypted_text.hex())
print("Decrypted:", decrypted_text)

# Mã hóa và giải mã file (demo)
encrypt_file("input.txt", "encrypted.bin", key, iv)
decrypt_file("encrypted.bin", "decrypted.txt", key)
