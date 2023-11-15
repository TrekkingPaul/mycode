#!/usr/bin/env python
"""Alta3 Research | RZFeeser@alta3.com
   Sending an SMTP (email) with Python

   To run a development server, run
   
   python3 -m smtpd -c DebuggingServer -n localhost:1025

   in a seperate tmux window before running this script."""

import smtplib
from email.mime.text import MIMEText

def main():
    sender = 'HanSolo@example.com'
    receivers = ['Chewbacca@example.com']
    port = 1025

    msg = MIMEText('The hyperdrive is less hyper and more drive. Can you check it out? Thanks.')

    msg['Subject'] = 'Hyperdrive is busted'
    msg['From'] = 'HanSolo@example.com'
    msg['To'] = 'Chewbacca@example.com'

    with smtplib.SMTP('localhost', port) as server:
        server.sendmail(sender, receivers, msg.as_string())

    print("Email has been sent.")

if __name__ == "__main__":
    main()

