#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygeoip
import sys


gi = pygeoip.GeoIP('GeoLiteCity.dat')

# Define functions to:
# Get record by hostname
def get_hostname_info(hostname):
    '''Get the country details using host address'''
    try:
        rec = gi.record_by_name(hostname)
        print(f'Details for {hostname}')
        print(str(rec))
    except Exception:
        print('an error occured\nAborting...')
        sys.exit(1)

# Get record by address
def get_addr_info(address):
    '''Get country record by IP address'''
    try:
        rec = gi.record_by_addr(address)
        print(f'Details for {address}')
        print(str(rec))
    except Exception:
        print('An error occurred.\nAborting...')
        sys.exit(1)


# Get user input
hostname = ''
addr = ''

def get_input():
    mode = input('Enter address (a) or hostname (h)')
    if mode.lower() == 'a':
        address = input('Enter the address\t')
        # call the function
        get_add_info(addr)
    elif mode.lower() == 'h':
        hostname = input('Enter the hostname:\t')
        # call get_hostname_info
        get_hostname_info(hostname)
    else:
        print('Wrong choice. Try again...')
        get_input()


get_input()

if len(hostname) > 0:
    try:
        get_hostname_info(hostname)
        print('===================================================')
    except Exception:
        print('An error occurred')
elif len(addr) > 0:
    try:
        get_address_info(addr)
        print('===================================================')
    except Exception:
        print('An error occurred')

