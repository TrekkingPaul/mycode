#!/usr/bin/python3
"""Alta3 Research - astros on ISS"""

import urllib.request
import json

MAJORTOM = "http://api.open-notify.org/astros.json"

def main():
    """reading json from api"""
    groundctrl = urllib.request.urlopen(MAJORTOM)

    helmet = groundctrl.read()
    #print(helmet)

    helmetson = json.loads(helmet.decode("utf-8"))

    #print(type(helmet))
    #print(type(helmetson))
    print("People in space: " + str(helmetson["number"]))
    #print(helmetson["people"])
    #print(helmetson["people"][0])
    #print(helmetson["people"][1])
    #print(helmetson["people"][-1])

    for astro in helmetson["people"]:
        print(astro["name"] + " on the " + astro["craft"])

if __name__ == "__main__":
    main()
