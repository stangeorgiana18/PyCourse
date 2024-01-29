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

# everything you can check in your particular email:
print(M.list())

# ('OK', [b'(\\HasNoChildren) "/" "INBOX"', b'(\\HasNoChildren) "/" "Notes"', b'(\\HasChildren \\Noselect) "/" "[Gmail]"', b'(\\All \\HasNoChildren) "/" "[Gmail]/All Mail"', b'(\\HasNoChildren \\Trash) "/" "[Gmail]/Bin"', b'(\\Drafts \\HasNoChildren) "/" "[Gmail]/Drafts"', b'(\\HasNoChildren \\Important) "/" "[Gmail]/Important"', b'(\\HasNoChildren \\Sent) "/" "[Gmail]/Sent Mail"', b'(\\HasNoChildren \\Junk) "/" "[Gmail]/Spam"', b'(\\Flagged \\HasNoChildren) "/" "[Gmail]/Starred"'])

print(M.select('inbox')) # ('OK', [b'11716'])


# after logging in, search our inbox; keywords capitalized

typ, data = M.search(None, 'SUBJECT "esti misto fata"')
# the data is just a list of email IDs that you need to fetch


print(typ) # OK
print(data, '\n') # [b'11716']; if no number returned, no message found; more numbers -- more messages related 


# the id above references the actual email
# to get the email itself we need to fetch the actual data

email_id = data[0]

result, email_data = M.fetch(email_id, '(RFC822)' ) # second argument -- protocol

print(email_data)

# grab the message itself
# index for it: ;  you may need to play around for this; in this case it's [0][1]
raw_email = email_data[0][1]
raw_email_string = raw_email.decode('utf-8') # decode in case of symbols


import email # to grab the actual message from the string

email_message = email.message_from_string(raw_email_string)

# email_message is an iterator

for part in email_message.walk():

    if part.get_content_type() == 'text/plain': # common: text/html if there's a linke inside of the email
        body = part.get_payload(decode = True)
        print(body) 
        
        # b'pe bune ca esti misto\r\n'

    # complicated bcs of going through that rostering email message and trying to 
    # get rid of all the other info that came in through the email data
        
 

# if dealing with emails that look the same every time (maybe from an API service)
# it'd make sense to not use the actual email library and use a script
