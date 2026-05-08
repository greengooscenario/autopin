#!/usr/bin/python3

# autopin main file
# ###################

# imports

from configparser import ConfigParser
import imaplib
import sys


# main program logic

creds = ConfigParser()
creds.read("credentials.ini")

imapserver = creds.get("Credentials", "imapserver")
username = creds.get("Credentials", "username")
password = creds.get("Credentials", "password")

print(username)

##here will come the main loop

# instantiate an IMAP4 class with SSL

imap = imaplib.IMAP4_SSL(imapserver)
print(imap.login(username, password))
print(imap.list())

