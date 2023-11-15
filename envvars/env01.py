#!/usr/bin/python3
"""Alta3 Research | RZFeeser@alta3.com
   Learning to use os.getenv() set values within our program for container automation."""

# standard library
import os

def main():
    """Run-time program"""

    # Atttempt to retrieve the MYPORT var
    print(f'The value of MYPORT is: {os.getenv("MYPORT", default="8888")}')

    # attempt to retrieve the MYMODE var
    print(f'The value of MYMODE is: {os.getenv("MYMODE", default="normal")}')

if __name__ == "__main__":
    main()

