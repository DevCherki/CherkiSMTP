
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

subject = input("SUBJECT: ")

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)

    for receiver in receivers:
        msg = MIMEMultipart()
        msg["Subject"] = subject
        msg["From"] = email
        msg["To"] = receiver

        html_part = MIMEText(html_content, "html")
        msg.attach(html_part)

        server.sendmail(email, receiver, msg.as_string())
        print_colored(f"Email sent successfully to {receiver}", Colors.OKGREEN)

    server.quit()
    print_colored("All emails sent successfully!", Colors.OKBLUE)

except Exception as e:
    print_colored(f"An error occurred while sending emails: {e}", Colors.FAIL)
