import pyotp
import smtplib
import os
import time
from email.message import EmailMessage
from email_validator import validate_email, EmailNotValidError

# Thông tin email gửi OTP (Bạn cần điền tài khoản email của mình)
SMTP_SERVER = "smtp.gmail.com"  # SMTP server của Gmail
SMTP_PORT = 587  # Cổng SMTP
EMAIL_SENDER = "hieu12102004@gmail.com"
EMAIL_PASSWORD = "your_app_password"  # Lưu ý: Dùng mật khẩu ứng dụng, không phải mật khẩu chính

# Tạo khóa bí mật (Lưu cho mỗi user)
SECRET_FILE = "secret_email.key"

if not os.path.exists(SECRET_FILE):
    secret = pyotp.random_base32()
    with open(SECRET_FILE, "w") as f:
        f.write(secret)
else:
    with open(SECRET_FILE, "r") as f:
        secret = f.read().strip()

totp = pyotp.TOTP(secret)
otp_code = totp.now()  # Tạo mã OTP hợp lệ

# Nhập email người nhận OTP
while True:
    email_receiver = input("Nhập email của bạn để nhận OTP: ")
    try:
        validate_email(email_receiver)
        break
    except EmailNotValidError:
        print("❌ Email không hợp lệ! Vui lòng nhập lại.")

# Gửi OTP qua email
def send_otp_email(otp, recipient):
    msg = EmailMessage()
    msg["Subject"] = "Mã OTP của bạn"
    msg["From"] = EMAIL_SENDER
    msg["To"] = recipient
    msg.set_content(f"🔐 Mã OTP của bạn là: {otp}\nMã có hiệu lực trong 30 giây.")

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Bảo mật kết nối
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)
        print(f"✅ Đã gửi mã OTP đến {recipient}")
    except Exception as e:
        print(f"❌ Lỗi khi gửi email: {e}")

send_otp_email(otp_code, email_receiver)

# Chờ người dùng nhập mã OTP
start_time = time.time()
for _ in range(3):  # Cho phép nhập tối đa 3 lần
    user_otp = input("Nhập mã OTP đã nhận qua email: ")

    # Kiểm tra thời gian hợp lệ (30 giây)
    if time.time() - start_time > 30:
        print("⏳ Mã OTP đã hết hạn! Vui lòng yêu cầu lại.")
        break

    if totp.verify(user_otp):
        print("✅ Xác thực thành công! Truy cập vào file password.txt")

        # Đọc nội dung file password.txt
        try:
            with open("password.txt", "r") as f:
                print("📄 Nội dung file password.txt:")
                print(f.read())
        except FileNotFoundError:
            print("❌ File password.txt không tồn tại.")
        break
    else:
        print("❌ Mã OTP không hợp lệ! Thử lại.")

else:
    print("⚠️ Quá số lần thử, từ chối truy cập!")
