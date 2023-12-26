class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def print_colored(text, color):
    colored_text = f"{color}{text}{Colors.ENDC}"
    print(colored_text)

# طباعة النص الملون
colored_text = r'''
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


FACEBOOK: https://www.facebook.com/dev.cherki
INSTAGRAM: https://www.instagram.com/cherki_dev

'''

lines = colored_text.split('\n')

for i, line in enumerate(lines):
    if i % 2 == 0:
        color = Colors.OKGREEN
    elif i % 2 == 1:
        color = Colors.FAIL  # تم تغييره إلى الأحمر
    else:
        color = Colors.FAIL  # تم تغييره إلى الأحمر

    print_colored(line, color)
    
    
    # main.py

while True:
    print("[1] Gmail SMTP")
    print("[2] GMAIL EXTRATE")
    choice = input("Enter a number: ")

    if choice == '1':
        import file1
        file1.run()
    elif choice == '2':
        import file2
        file2.run()
    else:
        print("الرجاء اختيار رقم صحيح.")
# file1.py

def run():
    print("تم تشغيل ملف file1.py - Gmail SMTP")
    # قم بإضافة الكود الخاص بـ Gmail SMTP هنا
# file2.py

def run():
    print("تم تشغيل ملف file2.py - GMAIL EXTRATE")
    # قم بإضافة الكود الخاص بـ GMAIL EXTRATE هنا
