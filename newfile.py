import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


email = "servicedotte@gmail.com"
password = "kcdwrhsfluianmiv"

sender = email
subject = "تأكيد حسابك"

try:
    # قراءة قائمة المستلمين من ملف data.txt
    with open("data.txt", "r") as file:
        receivers = [line.strip() for line in file]

   
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

   
    server.login(email, password)

   
    for receiver in receivers:
       
        msg = MIMEMultipart()
        msg["Subject"] = subject
        msg["From"] = sender
        msg["To"] = receiver

       
        with open("index.html", "r") as file:
            html_content = file.read()
            html_part = MIMEText(html_content, "html")
            msg.attach(html_part)

        server.sendmail(sender, receiver, msg.as_string())
        print(f"\033[92mتم إرسال الرسالة بنجاح إلى {receiver}\033[0m")

   
    server.quit()

    print("\033[94mتم إرسال جميع الرسائل بنجاح!\033[0m")

except Exception as e:
    print("\033[91mحدث خطأ أثناء إرسال الرسائل:", e, "\033[0m")
