"""Alta3 Research | RZFeeser@alta3.com
   Securely accept a password with getpass"""

#!/usr/bin/python3
# A simple Python program to demonstrate  getpass.getpass() to read password
import getpass

def main():
    """run-time code"""

    p = getpass.getpass()
    print("Password entered:", p)

if __name__ == "__main__":
    main()

