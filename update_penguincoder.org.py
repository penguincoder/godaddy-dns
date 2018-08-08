#!/usr/bin/env python3

# Full package imports
import sys
import os
import pif
# Partial imports
from godaddypy import Client, Account

domain = 'penguincoder.org'
a_record = '@'

userAccount = Account(api_key=os.environ['API_KEY'], api_secret=os.environ['API_SECRET'])
userClient = Client(userAccount)
publicIP = pif.get_public_ip('ident.me')

try:
    records = userClient.get_records(domain, name=a_record, record_type='A')
    for record in records:
        if publicIP != record["data"]:
            updateResult = userClient.update_record_ip(publicIP, domain, name=a_record, record_type='A')
            if updateResult is True:
                print('Update ended with no Exception.')
        else:
            print('No DNS update needed.')
except:
    print(sys.exc_info()[1])
    sys.exit()
