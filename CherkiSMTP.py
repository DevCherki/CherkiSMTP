import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ANSI escape codes for text color
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

# Your text
text = r'''
 ________
< CHERKI >
 --------
    \
     \
                                   .::!!!!!!!:.
  .!!!!!:.                        .:!!!!!!!!!!!!
  ~~~~!!!!!!.                 .:!!!!!!!!!UWWW$$$
      :$$NWX!!:           .:!!!!!!XUWW$$$$$$$$$P
      $$$$$##WX!:      .<!!!!UW$$$$"  $$$$$$$$#
      $$$$$  $$$UX   :!!UW$$$$$$$$$   4$$$$$*
      ^$$$B  $$$$\     $$$$$$$$$$$$   d$$R"
        "*$bd$$$$      '*$$$$$$$$$$$o+#"
             """"          """""""
   _____ _               _    _    _____ __  __ _______ _____
  / ____| |             | |  (_)  / ____|  \/  |__   __|  __ \
 | |    | |__   ___ _ __| | ___  | (___ | \  / |  | |  | |__) |
 | |    | '_ \ / _ \ '__| |/ / |  \___ \| |\/| |  | |  |  ___/
 | |____| | | |  __/ |  |   <| |  ____) | |  | |  | |  | |
  \_____|_| |_|\___|_|  |_|\_\_| |_____/|_|  |_|  |_|  |_|


FACEBOOK:dev.cherki
'''

# Print the colored text
colored_text = f"{Colors.WARNING}{text}{Colors.ENDC}"
print(colored_text)

# استخراج بيانات المستخدم
email = input("EMAIL: ")
password = input("PASSWORD APP: ")

# الحصول على مسار ملف نصي يحتوي على قائمة بريدية
txt_file_path = input("Enter the path to a text (txt) file containing your mailing list separated by lines: ")
with open(txt_file_path, "r") as txt_file:
    receivers_str = txt_file.read()

# استخدام قائمة بريدية مفصولة بمسافات
receivers = receivers_str.split()

# الحصول على محتوى ملف HTML من المستخدم
html_file_path = input("Enter the message in (html) file format: ")
with open(html_file_path, "r") as html_file:
    html_content = html_file.read()

sender = email
subject = input("SUBJECT: ")

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
