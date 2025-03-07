import re
import email.utils
email_pattern = r'^[a-zA-Z][\w\.-]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$'
n = int(input())

for _ in range(n):
    name, email_addr = email.utils.parseaddr(input())
    if re.match(email_pattern, email_addr):
        print(email.utils.formataddr((name, email_addr)))
