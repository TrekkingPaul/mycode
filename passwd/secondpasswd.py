#!/usr/bin/python3
"""Alta3 Research | RZFeeser@alta3.com
   paramiko with password access (getpass) to create an SSH tunnel
   and establish an SFTP connection over top"""

## import Paramiko so we can talk SSH
import paramiko # allows Python to ssh
import os # low level operating system commands
import getpass # we need this to accept passwords


def main():
    """run-time code"""

    ## where to connect to
    t = paramiko.Transport("10.10.2.3", 22) ## IP and port of bender

    ## how to connect (see other labs on using id_rsa private / public keypairs)
    t.connect(username="bender", password=getpass.getpass()) # notice the password references getpass

    ## Make an SFTP connection object
    sftp = paramiko.SFTPClient.from_transport(t)

    ## copy our firstpasswd.py script to bender
    sftp.put("firstpasswd.py", "firstpasswd.py") # move file to target location home directory

    ## close the connections
    sftp.close() # close the sftp connection
    t.close() # close ssh connection

if __name__ == "__main__":
    main()

