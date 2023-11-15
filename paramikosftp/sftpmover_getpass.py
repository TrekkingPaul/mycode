#!/usr/bin/python3
## Try a real world test with getpass

## import Paramiko so we can talk SSH
import paramiko # allows Python to ssh
import os # low level operating system commands
import getpass # we need this to accept passwords

def transfer_to_remote_dir():
    rdir = input("Enter the full path of the remote directory to copy the file to: ")

    if rdir.startswith("/") and rdir.endswith("/"):
        return rdir
    elif rdir.startswith("/") and not rdir.endswith("/"):
        rdir = rdir + "/"
        return rdir
    elif rdir.endswith("/") and not rdir.startswith("/"):
        rdir = "/" + rdir
        return rdir
    else:
        rdir = "/" + rdir + "/"
        return rdir



def main():
    ## where to connect to
    t = paramiko.Transport("10.10.2.3", 22) ## IP and port of bender
    
    ## how to connect (see other labs on using id_rsa private / public keypairs)
    t.connect(username="bender", password=getpass.getpass()) # notice the password references getpass
    
    ## Make an SFTP connection object
    sftp = paramiko.SFTPClient.from_transport(t)
    
    rdir = transfer_to_remote_dir()
    print(rdir)

    ## copy our firstpasswd.py script to bender
    sftp.put("file_to_move.txt", rdir + "file_to_move.txt") # move file to target location home directory
    
    ## close the connection
    sftp.close() # close the connection
if __name__ == "__main__":
    main()

