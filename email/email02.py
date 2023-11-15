#!/usr/bin/python
"""Alta3 Research | RZFeeser@alta3.com
   Using Python to use SMTP (email) with an attachment to send an message to a local
   test server.

   To run the SMTP server, run

   python3 -m smtpd -c DebuggingServer -n localhost:1025

   Use CTRL + C to stop the server."""

# standard library imports
import smtplib
from os.path import basename

"""Note:
   Multipurpose Internet Mail Extensions (MIME) is a standard that extends SMTP (email)
   to support sending things other than ASCII (text)"""
# standard library imports
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def main():
    """runtime code"""
    
    # SMTP routing information
    sender = 'dwight@example.com'
    receiver = 'jim@example.com'
    # declare our message will have non-ASCII attachments
    msg = MIMEMultipart()

    msg['Subject'] = 'Assigned parking spaces'
    msg['From'] = 'dwight@example.com'
    msg['To'] = 'jim@example.com'

    # this will be our attachement
    filename = 'assigned_spaces.txt'
    # open the file "assigned_spaces.txt"
    with open(filename, 'r') as f:
        part = MIMEApplication(f.read(), Name=basename(filename))

    # adds a header that describes our email as having "more than" just ASCII txt
    part['Content-Disposition'] = 'attachment; filename="{}"'.format(basename(filename))

    # takes our routing information & applies our attachment
    msg.attach(part)

    # we want some plain text in the body.
    msg.attach(MIMEText("Attached is a document with the assigned parking spots."))

    # not necessary, only would be used with an enterprise server (such as gmail or outlook)
    #user = 'username'
    #password = 'password'

    with smtplib.SMTP("localhost", 1025) as server:

        #server.login(user, password) # only necessary if we were using a production / enterprise server
        server.sendmail(sender, receiver, msg.as_string())
    
    print("Successfully sent email")

if __name__ == "__main__":
    main()

