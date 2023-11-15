#!/usr/bin/python3
"""Alta3 Research | RZFeeser@alta3
Using BeautifulSoup to select list items."""

# python3 -m pip install BeautifulSoup4
from bs4 import BeautifulSoup
# python3 -m pip install requests
from requests import get
from requests.exceptions import RequestException
from contextlib import closing

def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        # closing ensures any network connections get cleaned up
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors.
    This function just prints them, but you can
    make it do anything.
    """
    print(e)


def main():
    raw_html = simple_get('http://www.fabpedigree.com/james/mathmen.htm')
    html = BeautifulSoup(raw_html, 'html.parser')
    for i, li in enumerate(html.select('li')):
        print(i, li.text)

if __name__ == "__main__":
    main()

