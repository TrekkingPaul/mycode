#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   Reading in and writing out JSON"""

# standard library
import json

def main():
    with open("ciscoex.json", "r") as myfile:
        myjson = json.load(myfile)

    with open("ciscoex.txt", "w") as myfile:
        myfile.write(str(myjson["time"]) + " " +myjson["host"] + " " + myjson["type"])

if __name__ == "__main__":
    main()
