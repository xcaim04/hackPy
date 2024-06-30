"""
    Detect subdomains using Brute Force
    By: Carlos Javier Blanco
    xcaim04, OPEN SOURCE
"""

import requests
from os import path
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--target', help='Detect Subdomain')
parser = parser.parse_args()

def URL(url: str) -> None:
    try:
        requests.get(url)
    except requests.exceptions.RequestException as e:
        print(f'(-) Not Found: {url}')
    else:
        print(f'(+) Subdomains: {url}')

def main():

    if parser.target:
        if path.exists('subdomain.txt'):
            data = open('./subdomain.txt', 'r')
            data = data.read().split('\n')

            for subdomain in data:
                URL('http://'+subdomain+'.'+parser.target)
                URL('https://'+subdomain+'.'+parser.target)

    else:
        print('Err: Please provide a valid subdomain')
        sys.exit()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()