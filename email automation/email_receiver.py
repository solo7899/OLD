import imaplib
import email

from passwords import auth

mail = 'dolati.hamidreza78@gmail.com'
passwd = auth['password']
imap_server = 'imap.gmail.com'

with imaplib.IMAP4_SSL(imap_server) as server:
    server.login(mail, passwd)
    
    # print(server.list())
    print(server.select('"[Gmail]/Sent Mail"'))
    _, nums = server.search(None, 'ALL')
    
    for num in nums[0].split():
        _, data = server.fetch(num, '(RFC822)')
        message = email.message_from_bytes(data[0][1])

        print(f"""
message num: {num}
To: { message.get('To')}
""")
        for part in message.walk():
            if part.get_content_type() == 'text/plain':
                print(part.as_string())