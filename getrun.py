#!/usr/bin/python3
"""Alta3 Research | RZFeeser@alta3.com
This script will connect to an Arista EOS switch, and retrieve the running configuration, provided
 that the eAPI is running. The script expects the IP or hostname to be passed after the script name. For example:
 - python3 ~/mycode/getjson.py sw-1
 - python3 ~/mycode/getjson.py 192.168.0.1"""

# python standard library
import json
import sys

# python3 -m pip install napalm
from napalm import get_network_driver

def main():
    """runtime"""
    
    # collect the hostname or IP passed in as an argument
    hn = sys.argv[1]

    # Tell NAPALM to speak "eos" commands to our switches (very cisco-like)
    driver = get_network_driver('eos')

    # we can set HTTP, HTTPS, or SSH
    optional_args = {'transport': 'http'}

    # Hard-code the switch credentials & pass transport argument
    # the switch ID is now passed in
    device = driver(hn, 'admin', 'alta3', optional_args=optional_args)

    # Equates to: ssh into the switch, login, and enable
    device.open()

    ## Print STARTUP, RUNNING, and CANDIDATE configs
    #print("Python configuration:\n" )
    #print(device.get_config())
    #
    ## Print STARTUP, RUNNING, and CANDIDATE configs as JSON
    #print("Converted JSON configuration:\n" )    
    #print(json.dumps(device.get_config(),indent=4, separators=(',', ': ')))

    # This next line EXTRACTS the RUNNING config from the dict that also includes
    # STARTUP and CANDIDATE
    config = device.get_config()
    print(config.get('running'))

    # end connection
    device.close()
    
if __name__ == "__main__":
    # check if the correct number of arguments were supplied
    if len(sys.argv) != 2:
        print("You supplied ", len(sys.argv)-1, " arguments but 1 is needed")
        print("getjson.py requires: hostname")
        print("example: python3 getjson.py  sw-1")
    else:
        main() 

