#!/usr/bin/python3
"""Alta3 Research | RZFeeser@alta3
Using BeautifulSoup to make data selections from montypython.html"""

from bs4 import BeautifulSoup

def main():

    # retrieve the raw HTML using the open function then read in the data
    with open('montypython.html') as mp:
        raw_html = mp.read()

    # use the backend parser 'html.parser' to parse out the raw_html
    html = BeautifulSoup(raw_html, 'html.parser')

    # the select method on the html object allows the selection of
    # CSS selectors to locate elements in the document
    # return a list of paragraph elements (dict like)
    for p in html.select('p'):
        if p['id'] == 'camelot' or p['id'] == 'knights':
            print(p.text)


if __name__ == "__main__":
    main()

