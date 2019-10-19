import eospy.cleos
import eospy.keys
from eospy.types import Abi, Action
from eospy.utils import parse_key_file
import os
import pytz
import csv
import json
import datetime as dt
# this url is to a testnet that may or may not be working.
# We suggest using a different testnet such as kylin or jungle
#
ce = eospy.cleos.Cleos(url='http://mainnet.genereos.io')
#ce = eospy.cleos.Cleos(url='https://api.eosdetroit.io:443')
#ce = eospy.cleos.Cleos(url='https://fn.eossweden.se:443')
#ce = eospy.cleos.Cleos(url='https://api.eosio.cr:80')
#ce = eospy.cleos.Cleos(url='https://eos.greymass.com:443')
#ce = eospy.cleos.Cleos(url='http://api.hkeos.com:80')
#ce = eospy.cleos.Cleos(url='https://api.eosn.io')
#ce = eospy.cleos.Cleos(url='http://bp.cryptolions.io:8888')

# personal tool
test_key = eospy.keys.EOSKey('5Kh...')
# group tool
#key_groupown = eospy.keys.EOSKey('')
memo_txt = "EOS to the moon join EOSWIN.NET for grant prize. Referral ID: aa5151515152"
ACC_NAME_FROM=".."
#ACC_NAME_FROM="aa5151515152"
toaccount=".."
output_file="lissx.txt"

outstanding=[]
def transactionSingle(__toaccount):
    payload = [
            {
                'args': {
                    "from": ACC_NAME_FROM,  # sender
                    "to": __toaccount,  # receiver
                    "quantity": '0.0001 EOS',  # In EOS
                    "memo": memo_txt,
                },
                "account": "eosio.token",
                "name": "transfer",
                "authorization": [{
                    "actor": ACC_NAME_FROM,
                    "permission": "active",
                }],
            }
        ]

    #rpm = ce.get_chain_lib_info()
    #print(rpm)
    #Converting payload to binary
    data=ce.abi_json_to_bin(payload[0]['account'],payload[0]['name'],payload[0]['args'])
    #print(data)
    #print('------------------------------------------------')
    payload[0]['data']=data['binargs']
    payload[0].pop('args')
    #Inserting payload binary form as "data" field in original payload
    trx = {"actions":[payload[0]]}
    #trx['expiration'] = str((dt.datetime.utcnow() + dt.timedelta(seconds=60)).replace(tzinfo=pytz.UTC))
    #print(trx)

    try:
        resp = ce.push_transaction(trx, [test_key], broadcast=True)
        # use a string or EOSKey for push_transaction
        # key = "5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3"
        # use EOSKey:
        # resp = ce.push_transaction(trx, key, broadcast=True)
        print('--------TRX DONE---------------------------------------')
        print(resp)
        print('------------------------------------------------')
        return 1
    except:
        outstanding.append(__toaccount)
        print("An exception occurred")
        return 0


#    rows = csv.reader(f,delimiter=" ",lineterminator="\n")
#    next(rows, None)
#    for row in rows:
#        print(row[0])

print('Start open file now 30s...')
line=""
license_plate = {}

with open(output_file,"r",encoding='UTF-8') as f:
    line = f.readline()

list_one = line.strip().split(' ')

for userid in list_one:
    print(userid)
    result = transactionSingle(userid)

    if result==1 : 
       license_plate[userid]=1

print(outstanding)
   
