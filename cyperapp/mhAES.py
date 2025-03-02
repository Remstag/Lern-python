from Crypto.Cipher import AES
from Crypto.Util.Padding import *
import base64
KEy=b'KeyDayNeDuMaMayVoMaLay@1234ABCDX'
IV=b'ThisIsAnIV123456'
def mahoa(texxt):
    texxt=str(texxt)
    cipher=AES.new(KEy,AES.MODE_CBC,IV)
    damahoa=cipher.encrypt(pad(texxt.encode(),AES.block_size))
    return base64.b64encode(damahoa).decode()
def giaima(mh):
    cipher = AES.new(KEy, AES.MODE_CBC, IV)
    giaimaa = base64.b64decode(mh.strip())
    return unpad(cipher.decrypt(giaimaa), AES.block_size).decode("utf-8", errors="ignore").replace("\r\n", "\n")