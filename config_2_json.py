#!/usr/bin/python3
"""Alta3 Research | RZFeeser@alta3.com
This script will connect to an Arista EOS switch, and retrieve all of the configurations, provided
 that the eAPI is running."""

# python standard library
import json

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

    # Print STARTUP, RUNNING, and CANDIDATE configs
    print("Python configuration:\n" )
    print(device.get_config())

    # Print STARTUP, RUNNING, and CANDIDATE configs as JSON
    print("Converted JSON configuration:\n" )    
    print(json.dumps(device.get_config(),indent=4, separators=(',', ': ')))

    # end connection
    device.close()
    
if __name__ == "__main__":
    main()    

