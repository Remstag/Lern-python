from Crypto.Cipher import AES
from Crypto.Util.Padding import *
import base64
#KEy=b'KeyDayNeDuMaMayVoMaLay@1234ABCDX'
#IV=b'ThisIsAnIV123456'
def mahoa(texxt, keyy, IV):
    texxt=str(texxt)

    cipher=AES.new(keyy,AES.MODE_CBC,IV)
    damahoa=cipher.encrypt(pad(texxt.encode(),AES.block_size))
   # return base64.b64encode(damahoa).decode()
    return damahoa.hex()
def giaima(mh,keyy,IV):
    cipher = AES.new(keyy, AES.MODE_CBC, IV)
    #giaimaa = base64.b64decode(mh.strip())
   # return unpad(cipher.decrypt(giaimaa), AES.block_size).decode("utf-8", errors="ignore").replace("\r\n", "\n")
    encrypted_bytes = bytes.fromhex(mh)
    giaima = unpad(cipher.decrypt(encrypted_bytes), AES.block_size)
    return giaima.decode("utf-8")