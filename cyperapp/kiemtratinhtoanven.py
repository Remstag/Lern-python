import hashlib
status=""
def shaa256(file_path):
    global  status
    hasher=hashlib.sha256()
    try:
        with open(file_path, "rb") as file:
            while chunk:= file.read(4096):
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception as e:
        status="Có lỗi xảy ra!!"
        return None
