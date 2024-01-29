# SEND EMAILS WITH PYTHON

# SMTP - simple mail transfer protocol server
# domain name that you connect to to access your email programmatically
'''
import smtplib

# port number: 465 / 587 / no number 
smtp_object = smtplib.SMTP('smtp.gmail.com', 587)

# greet the server and establish the connection
# METHOD CALL SHOULD BE DONE DIRECTLY AFTER CREATING THE OBJECT
smtp_object.ehlo()

# port 587 -- TLS encryption -- all email, as you send it, is encrypted 
# that way, people cannot read your emails without being the actual recipient
# port 465 -- used ssl

# initiate this sort of encryption:
print(smtp_object.starttls()) # (220, b'2.0.0 Ready to start TLS')


# set the email and the passwords 

import getpass

# for gmail users, generate an app password instead of our notmal email password
# pass in the app password 

email = getpass.getpass("Email: ")
password = getpass.getpass('Password: ')

print(smtp_object.login(email, password)) # (235, b'2.7.0 Accepted')

# send an email to myself
from_address = email
to_address = email
subject = input("Enter the subject line: ")
message = input("Enter the body message: ")
msg = "Subject: " + subject + '\n' + message 

print(smtp_object.sendmail(from_address, to_address, msg))
# {} -- output if successful

# close the connection
smtp_object.quit()

'''

import imaplib

M = imaplib.IMAP4_SSL('imap.gmail.com')

import getpass

email = getpass.getpass("Email: ")
password = getpass.getpass("Password: ")

print(M.login(email, password)) # ('OK', [b'georgistan18@gmail.com authenticated (Success)'])

