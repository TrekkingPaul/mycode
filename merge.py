#!/usr/bin/python3
"""Alta3 Research | RZFeeser@alta3.com
This script will connect to an Arista EOS switch, and merge a network configuration from the local file /home/student/mycode/merge.me"""

# python3 -m pip install napalm
from napalm import get_network_driver

def main():
    """runtime"""

    # Tell NAPALM to speak "eos" commands to our switches (very cisco-like)
    driver = get_network_driver('eos')

    # we can set HTTP, HTTPS, or SSH
    optional_args = {'transport': 'http'}

    # Hard-code the switch credentials & pass transport argument
    # the switch ID is now passed in
    device = driver('sw-1', 'admin', 'alta3', optional_args=optional_args)

    # Equates to: ssh into the switch, login, and enable
    device.open()

    # The next two lines of code are new
    device.load_merge_candidate("/home/student/mycode/merge.me")
    device.commit_config()

    # end connection
    device.close()
    
if __name__ == "__main__":
    main()

