# LICENSE
# Original Copyright: Asad Dhamani
# Modified slightly by: seamus tuohy
# GNU GENERAL PUBLIC LICENSE - Version 2, June 1991
# https://github.com/dhamaniasad/waybackcheck/tree/2697166c784f09678665245ea9eb3322b92ea88e

# Import libraries

from sys import argv as arg
import urllib2 as urllib
import json


def get_archived_url(inputurl):
    # Submit url to wayback machine
    wbkurl = "http://web.archive.org/save/" # wayback machine submission url
    try:
        urllib.urlopen(wbkurl+inputurl) # Submit the url
    except urllib.HTTPError as err:
        return inputurl

    # Return latest snapshot url
    wbkav = "http://archive.org/wayback/available?url=" # wayback machine availability api url
    wbcheck = urllib.urlopen(wbkav+inputurl) # open wayback availability url
    wbcheckjson = json.load(wbcheck) # load json data
    archived_snapshots = wbcheckjson['archived_snapshots']
    latest_snapshot = archived_snapshots['closest']['url']
    return latest_snapshot

def main():
    inputurl = arg[1] # take in url as argument
    archivedurl = get_archived_url(inputurl)
    print archivedurl


if __name__ == '__main__':
    main()
