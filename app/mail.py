# Mail Notification Class
# 04.13.2017
# This file contains a class used to send legit emails from a legit source


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


google_fi = "@msg.fi.google.com";
t_mobile = "@tmomail.net";
verizon = "@vtext.com";
at_t = "@txt.att.net";
at_t2 = "@mms.att.net";
metro_pcs = "@mymetropcs.com";
virgin_mobile = "@vmobl.com";
sprint_cell = "@messaging.sprintpcs.com";
us_cellular = "@email.uscc.net";

cellAddresses = [google_fi, t_mobile, verizon, at_t, metro_pcs, virgin_mobile, sprint_cell, us_cellular];


class SendMail( object ):
    def __init__(self, *args, **kwargs):
        self.FROM = kwargs.get('srcEmail');
        self.FROMP = kwargs.get('passw');
        self.FROMS = kwargs.get('srcServer');
        self.FROMSP = kwargs.get('srcServerPort');
        self.TO = kwargs.get('destEmail');
        self.DESTYPE = kwargs.get('desType');
        self.SUBJECT = kwargs.get('subject');
        self.BODY = kwargs.get('body');
        self.ATTACHMENT = kwargs.get('attachments');
    
        self.initialize();

    def initialize(self):
        '''
        Initialize class variables with default values
        '''
        if self.FROM == None:
            self.FROM = "";
        if self.FROMP == None:
            self.FROMP = "";
        if self.FROMS == None:
            self.FROMS = "smtp.gmail.com";
        if self.FROMSP == None:
            self.FROMSP = 587;
        if self.TO == None:
            self.TO = "";
        if self.DESTYPE == None:
            self.DESTYPE = 0;
        if self.SUBJECT == None:
            self.SUBJECT = "";
        if self.BODY == None:
            self.BODY = "";
        if self.ATTACHMENT == None:
            self.ATTACHMENT = [];

    def setSubject(self, sub):
        self.SUBJECT = sub;

    def setBody(self, body):
        self.BODY = body;

    def setReceiver(self, receiver):
        self.TO = receiver;

    def setSender(self, *args, **kwargs):
        self.FROM = kwargs.get('sender');
        self.FROMP = kwargs.get('passwd');
        self.FROMS = kwargs.get('server');
        self.FROMSP = kwargs.get('port'); 
        self.initialize();

    def setType(self, typ):
        self.DESTYPE = typ;



    def getSubject(self):
        return self.SUBJECT;

    def getBody(self):
        return self.BODY;

    def getReceiver(self):
        return self.TO;

    def getSender(self):
        return self.FROM;

    def getType(self):
        return self.DESTYPE;

    def send(self):
        '''
        Send the email notification
        '''

        if self.DESTYPE == 0:
            server = smtplib.SMTP(self.FROMS, self.FROMSP);

            self.sign_in(server);

            msg = MIMEMultipart();
            msg['From'] = self.FROM;
            msg['To'] = self.TO;
            msg['Subject'] = self.SUBJECT;
            msg.attach(MIMEText(self.BODY, 'plain'));

            text = msg.as_string();
            server.sendmail(self.FROM, self.TO, text);

            self.sign_out(server);
            
    def sign_in(self, server):
        '''
        Use the credentials to log into the "Sending" email
        '''
        server.ehlo()
        server.starttls();
        server.login(self.FROM, self.FROMP);
    
    def sign_out(self, server):
        '''
        Sign out from the originiating email server
        '''
        server.quit();
