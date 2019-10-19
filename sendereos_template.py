#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pyeos_client.NodeosConnect import RequestHandlerAPI
from pyeos_client.EOSChainApi import ChainAPI
from eosiopy.eosioparams import EosioParams
from eosiopy.nodenetwork import NodeNetwork
from eosiopy.rawinputparams import RawinputParams
from eosiopy import eosio_config

eosio_config.url="http://mainnet.genereos.io"
eosio_config.port=80
#https://api.pennstation.eosnewyork.io:7101
#connection  = RequestHandlerAPI(base_url='http://mainnet.genereos.io', headers={"Accept": "application/json"})
#chainapi = ChainAPI(connection)
#print(chainapi.get_info().json())

FROM="walletfromid"
TO="wallettoid"
PRIVATE_KEY="5Kh .... "
raw = RawinputParams("transfer", {
"from": FROM,
"memo": "remember to visit eoswin to play game and win the jack pot with referral id FROM",
"quantity": "0.00001 EOS",
"to": TO
}, FROM, "FROM@active")

eosiop_arams=EosioParams(raw.params_actions_list,PRIVATE_KEY)

print(eosiop_arams)

net=NodeNetwork.push_transaction(eosiop_arams.trx_json)

print(net)