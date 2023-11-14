#!/usr/bin/python3
"""
Author: RZFeeser
This program harvests SpaceX data avail from https://api.spacexdata.com/v3/cores using the requests library.
"""

import requests
SPACEXURI = "https://api.spacexdata.com/v3/cores"

def main():
    coreData = requests.get(SPACEXURI)
    listOfCores = coreData.json()

    for core in listOfCores:
        print(core, end="\n\n")
        print(f"The core serial of this launch is {core['core_serial']} and was first launched on {core['original_launch']}. The details of this launch are {core['details']}.\n")
if __name__ == "__main__":
    main()
