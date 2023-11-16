#!/usr/bin/python3
"""Alta3 Research | RZFeeser@alta3.com
This script will take a validation file, and compare it to the actual running configuration. In effect, we are making a check or assertion that our running configuration is what we expect it to be."""

# standard library
import pprint as pp

# python3 -m pip install napalm
from napalm import get_network_driver

def main():
    """runtime"""

    # Tell NAPALM to speak "eos" commands to our switches (very cisco-like)
    driver = get_network_driver('eos')

    # we can set HTTP, HTTPS, or SSH
    optional_args = {'transport': 'http'}

    # Hard-code the switch credentials & pass transport argument
    device = driver('sw-1', 'admin', 'alta3', optional_args=optional_args)

    # Equates to: ssh into the switch, login, and enable
    device.open()

    # compare the running configuration with our expected configuration
    # display the results with "pretty print"
    pp.pprint(device.compliance_report("/home/student/mycode/sw1_validate.yml"))

    # close the connection
    device.close()
    
if __name__ == "__main__":
    main()

