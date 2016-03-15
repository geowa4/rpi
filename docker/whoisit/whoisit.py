#!/usr/bin/env python

import argparse
import bluetooth
import requests

MAKER_URL = 'https://maker.ifttt.com/trigger/%s/with/key/%s'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ifttt', action='store', required=True)
    parser.add_argument('--address', action='append', required=True)
    args = parser.parse_args()
    num_inhabitants = 0
    for address in args.address:
        name = bluetooth.lookup_name(address)
        if name is not None:
            num_inhabitants += 1
    if num_inhabitants > 0:
        r = requests.post(
            MAKER_URL % ('whoisit', args.ifttt),
            data={'value1': num_inhabitants}
        )
    else:
        r = requests.post(MAKER_URL % ('nobodyhome', args.ifttt))
    print(r.text)

if __name__ == '__main__':
    main()
