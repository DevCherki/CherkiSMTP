import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# استخراج بيانات المستخدم
email = input("البريد الإلكتروني: ")
password = input("كلمة المرور: ")

# الحصول على مسار ملف نصي يحتوي على قائمة بريدية
txt_file_path = input("أدخل مسار ملف نصي (txt) يحتوي على قائمة بريدية مفصولة بمسافات: ")
with open(txt_file_path, "r") as txt_file:
    receivers_str = txt_file.read()

# استخدام قائمة بريدية مفصولة بمسافات
receivers = receivers_str.split()

# الحصول على محتوى ملف HTML من المستخدم
html_file_path = input("أدخل مسار ملف HTML: ")
with open(html_file_path, "r") as html_file:
    html_content = html_file.read()

sender = email
subject = "تأكيد حسابك"

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)

    for receiver in receivers:
        msg = MIMEMultipart()
        msg["Subject"] = subject
        msg["From"] = sender
        msg["To"] = receiver

        html_part = MIMEText(html_content, "html")
        msg.attach(html_part)

        server.sendmail(sender, receiver, msg.as_string())
        print(f"\033[92mتم إرسال الرسالة بنجاح إلى {receiver}\033[0m")

    server.quit()
    print("\033[94mتم إرسال جميع الرسائل بنجاح!\033[0m")

except Exception as e:
    print("\033[91mحدث خطأ أثناء إرسال الرسائل:", e, "\033[0m")
