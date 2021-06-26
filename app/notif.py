##  Notification Class
#   Developer: nickumia
#   Supports only email/text for now


from mail import *
import safe

import os
import time


class Notifications(object):
    def __init__(self):
        self.phoneSettings = {
            "FROM"      : safe.email,
            "TO"        : "",
            "PASSWD"    : safe.email_password,
            "SERVER"    : "smtp.gmail.com",
            "PORT"      : 587,
            "TYPE"      : 0,
            "SUBJECT"   : "",
            "BODY"      : ""
        }
        self.phone =  SendMail(srcEmail=self.phoneSettings['FROM'], passw=self.phoneSettings['PASSWD'], srcServer=self.phoneSettings['SERVER'], srcServerPort=self.phoneSettings['PORT'], destEmail=self.phoneSettings['TO'], desType=self.phoneSettings['TYPE'], subject=self.phoneSettings['SUBJECT'], body=self.phoneSettings['BODY']);

    def phoneNotify(self, to, subject, body):
        '''
        Use MAIL class to send sms text messages
        '''
        if type(to) == str:
            self.phone.setReceiver(to);
        self.phone.setSubject(subject);
        self.phone.setBody(body);
        self.phone.send();
