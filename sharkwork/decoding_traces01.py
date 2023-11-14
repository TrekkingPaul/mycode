#!/usr/bin/env python
"""Alta3 Research | RZFeeser
   Any trace that is in *.pcapng must be first decoded to *.pcap
   this may be completed with the editcap utility. The editcap can be installed with tshark (sudo apt install tshark -y)

   editcap -F libpcap -T ether trace.pcapng trace.pcap
    
   The dpkt library is installed with:

   python3 -m pip install dpkt"""

import datetime
import dpkt

def mac_decode(old_mac):
    """returns a mac address decoded from hexadecimal
       this trick comes from the dpkt documentation"""
    return ':'.join('%02x' % dpkt.compat.compat_ord(b) for b in old_mac)

def main():
    with open('SIP_REGISTER_wp.pcap', 'rb') as f:
        pcap = dpkt.pcap.Reader(f)
        pkt_no = 0
        for ts, buf in pcap:
            pkt_no += 1
            print(f'Packet Number - {pkt_no}')
            print(f'Timestamp: {datetime.datetime.utcfromtimestamp(ts)}')
            eth = dpkt.ethernet.Ethernet(buf)
            print(f'src MAC - {mac_decode(eth.src)}')
            print(f'dst MAC - {mac_decode(eth.dst)}')

if __name__ == "__main__":
    main()
