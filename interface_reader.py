#!/usr/bin/env python3
"""Alta3 Research | Exploring interfaces library"""

import netifaces
import argparse

def getIP():
    print(netifaces.interfaces())
    choice = input('Enter the interface name you want the IP of: ')
    ip = netifaces.ifaddresses(choice)[netifaces.AF_INET][0]['addr']
    print('IP of ' + choice + ' is ' + ip)

def main():
    getIP()
    for i in netifaces.interfaces():
        print('\n**************Details of Interface - ' + i + ' *********************')
        try:
            print('MAC: ', end='')
            print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr'])
            print('IP: ', end='')
            print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
        except:
            print('Could not collect adapter information')

if __name__ == '__main__':
    main()

