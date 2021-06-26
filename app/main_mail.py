##  Mail server receiving inputs to send email
#   Developer: nickumia


import json
import socket

import notif


Mailer = notif.Notifications()

if __name__ == "__main__":
    print("Mail Server UP")
    mail_server = socket.socket()
    mail_server.bind(('', 4444))
    mail_server.listen(20)

    while True:
        connection,addr = mail_server.accept()
        request = connection.recv(2048)
        request_struct = json.loads(request)
        connection.close()
        Mailer.phoneNotify(None,
                            request_struct['title'],
                            (lambda: request_struct['text'] if 
                                request_struct['text'] != None else 
                                request_struct['img'][0])())
