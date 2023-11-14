#!/usr/bin/python3
"""
Author: RZFeeser
This program harvests SpaceX data avail from
https://api.spacexdata.com/v3/cores using the
Python Standard Library methods
"""

import urllib.request
import json

SPACEXURI = "https://api.spacexdata.com/v3/cores"

def main():
    coredata = urllib.request.urlopen(SPACEXURI)

    xstring = coredata.read().decode()
    print(type(xstring))

    listOfCores = json.loads(xstring)
    print(type(listOfCores))

    for core in listOfCores:
        print(core, end="\n\n")

if __name__ == "__main__":
    main()
