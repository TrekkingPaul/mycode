#!/usr/bin/env python3
"""RZFeeser | Alta3 Research
   A simple script that demonstrates using Netmiko against a Cisco NX-OS device."""

# standard library
import os

# python3 -m pip install --user netmiko
from netmiko import ConnectHandler

# call our router
def main():
    """run time code"""
    
    open_connection = ConnectHandler(device_type='cisco_nxos', ip='sandbox-nxos-1.cisco.com', username='admin', password="Admin_1234!")
        
    my_command = open_connection.send_command("show ver")

    #print(my_command)
    out = my_command.splitlines()
    for i in out:
        if "NXOS: version" in i:
            print(i)
        elif "Kernel uptime" in i:
            print(i)

## Call main()
if __name__ == "__main__":
    main()

