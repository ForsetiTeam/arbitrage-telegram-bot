import telebot
from telebot import types
from config import token
import requests
import time
from web3 import Web3
from web3.providers.rpc import HTTPProvider, KeepAliveRPCProvider
import json
import random



bot = telebot.TeleBot(token)

"""
url = 'https://ropsten.etherscan.io/api?module=proxy&action=eth_call&to=0x2449BAe8Ed365105329F9bE8C313cF68dEb0b49b&data=0x5a7a6afd0000000000000000000000000000000000000000000000000000000000000000&tag=latest&apikey=YourApiKeyToken'
resp = requests.get(url=url)
data = json.loads(resp.text)

contract_address = data['result'][:66].strip('0').strip('x').strip('0')
print(judge_address)

judge_id = (int(data['result'][66:].strip('0'),16))

id = data['id']
"""


#url = 'https://ropsten.etherscan.io/api?module=proxy&action=eth_call&to=0x7c91C48603f1ba48Cceb6A7F11382ABF72F580e9&data=0x1f7b6d32&tag=latest&apikey=YourApiKeyToken'

url = 'https://ropsten.etherscan.io/api?module=proxy&action=eth_call&to=0x745E33D378eD783130BcA0b969163AB74c0a1Fe6&data=0x1f7b6d32&tag=latest&apikey=YourApiKeyToken'


resp = requests.get(url=url)
data = json.loads(resp.text)
n = (int(data['result'],16))

for i in range(n):
    url = 'https://ropsten.etherscan.io/api?module=proxy&action=eth_call&to=0x745E33D378eD783130BcA0b969163AB74c0a1Fe6&data=0x03988f84000000000000000000000000000000000000000000000000000000000000000%s&tag=latest&apikey=YourApiKeyToken'%(i)
    resp = requests.get(url=url)
    data = json.loads(resp.text)
    #print(data)
    address = (data['result'][-40:])
    print(address)
    url = 'https://ropsten.etherscan.io/api?module=proxy&action=eth_call&to=0x%s&data=0x5a7a6afd0000000000000000000000000000000000000000000000000000000000000000&tag=latest&apikey=YourApiKeyToken'%(address)
    resp = requests.get(url=url)
    data = json.loads(resp.text)
    print(data)
    try:

        print(data['result'])
        markup = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton(text='Accept', callback_data='AccDisp_%s_%s' % ('Dispute',address))
        button2 = types.InlineKeyboardButton(text='Decline', callback_data='DecDisp_%s_%s' % ('Dispute',address))
        markup.add(button1, button2)
        text = 'Deal:%s\nDescription:%s\n%s' % ('Lending','Required to do Lending, Details by Reference','https://docs.google.com/document/d/1ayi8hW5m2G8knbPpOXHW21J8qxSHT_nOhYdCFybd5j8/edit?usp=sharing')
        #@block_judgebot
        bot.send_message(186909038,'new Dispute:\n%s'% text, reply_markup= markup)
        time.sleep(60)

    except:

        time.sleep(10)


