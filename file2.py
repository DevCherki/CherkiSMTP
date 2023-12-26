import re

# اطلب من المستخدم إدخال النص
text_to_search = input("Enter text to extract from a mailing list: \n")

# النمط الذي سيتم استخدامه لاستخراج البريد الإلكتروني
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# البحث واستخراج البريد الإلكتروني باستخدام re.findall
emails_found = re.findall(email_pattern, text_to_search)

# طباعة البريد الإلكتروني المستخرج
if emails_found:
    print("البريد الإلكتروني المستخرج:")
    for email in emails_found:
        print(email)
else:
    print("لم يتم العثور على أي عناوين بريد إلكتروني.")
