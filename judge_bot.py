import telebot
from telebot import types
from config import token
import requests
import time
import json

bot = telebot.TeleBot(token)




A = [0]


@bot.message_handler(commands=['start'])
def grating(message):
    with open('ids', 'a') as f:
        f.write('%s\n' % message.chat.id)
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton('My profile')
    button2 = types.KeyboardButton('My Disputes')
    button3 = types.KeyboardButton('Disputes')
    button4 = types.KeyboardButton('About')
    markup.add(button1, button2, button3, button4)

    print(message.chat.id)

    bot.send_message(message.chat.id,'Hello',reply_markup = markup)



def My_Disputes(message):
    url = 'https://ropsten.etherscan.io/api?module=proxy&action=eth_call&to=0x745E33D378eD783130BcA0b969163AB74c0a1Fe6&data=0x1f7b6d32&tag=latest&apikey=YourApiKeyToken'

    resp = requests.get(url=url)
    data = json.loads(resp.text)

    n = (int(data['result'], 16))

    if A[0]<n:
        url = 'https://ropsten.etherscan.io/api?module=proxy&action=eth_call&to=0x745E33D378eD783130BcA0b969163AB74c0a1Fe6&data=0x03988f84000000000000000000000000000000000000000000000000000000000000000%s&tag=latest&apikey=YourApiKeyToken' % (
        A[0])
        resp = requests.get(url=url)
        data = json.loads(resp.text)
        # print(data)
        address = (data['result'][-40:])
        print(address)
        url = 'https://ropsten.etherscan.io/api?module=proxy&action=eth_call&to=0x%s&data=0x5a7a6afd0000000000000000000000000000000000000000000000000000000000000000&tag=latest&apikey=YourApiKeyToken' % (
        address)
        resp = requests.get(url=url)
        data = json.loads(resp.text)
        print(data)
        try:

            print(data['result'])
            markup = types.InlineKeyboardMarkup(row_width=2)
            button1 = types.InlineKeyboardButton(text='Accept', callback_data='AccDisp_%s_%s' % ('Dispute', address))
            button2 = types.InlineKeyboardButton(text='Decline', callback_data='DecDisp_%s_%s' % ('Dispute', address))
            markup.add(button1, button2)
            text = 'Deal:%s\nDescription:%s\n%s' % ('Ladnding', 'Required to do Landing, Details by Reference',
                                                    'https://docs.google.com/document/d/1ayi8hW5m2G8knbPpOXHW21J8qxSHT_nOhYdCFybd5j8/edit?usp=sharing')
            # @block_judgebot
            bot.send_message(186909038, 'new Dispute:\n%s' % text, reply_markup=markup)
            time.sleep(40)

        except:

            time.sleep(10)
        A[0]+=1


def My_profile(message):    # Personal info rating an etc
    Rating = '10'
    Succes_disputes = '10'
    Total_profit = '10'
    text = 'Your rating:%s\nSuccesfully disputes:%s\nTotal profit:%s' %(Rating, Succes_disputes, Total_profit)
    bot.send_message(message.chat.id, text)



def Disputes(message):
    markup = types.InlineKeyboardMarkup(row_width= 2)
    button1 = types.InlineKeyboardButton(text= 'Accept',callback_data='AccDisp_%s' %('Dispute_id'))
    button2 = types.InlineKeyboardButton(text= 'Decline',callback_data='DecDisp_%s'%('Dispute_id'))
    markup.add(button1,button2)
    bot.send_message(message.chat.id,'can you approove\ntest info about disput:', reply_markup= markup)



@bot.callback_query_handler(lambda c: c.data.split('_')[0] == 'AccDisp') # approover accept Dispute
def AccDis(c):
    bot.send_message(c.message.chat.id, '%s dispute Accepted' % (c.data.split('_')[1]))
    Contractor = 'Contractor'
    Executor = 'Executor'

    print(c.data.split('_')[2])
    address = c.data.split('_')[2]
    print(c.data.split('_')[1])

    markup = types.InlineKeyboardMarkup()
    button1 = (types.InlineKeyboardButton(text=Contractor, callback_data='_'.join(['Approve',Contractor,address])))
    button2 = (types.InlineKeyboardButton(text='Argument1', callback_data='Argument_%s_%s' % (c.data.split('_')[1], 'Contractor')))
    markup.add(button1,button2)

    button3 = (types.InlineKeyboardButton(text=Executor,callback_data='_'.join(['Approve',Executor,address])))
    button4 = (types.InlineKeyboardButton(text='Argument2', callback_data='Argument_%s_%s' % (c.data.split('_')[1], 'Executor')))
    markup.add(button3,button4)

    bot.send_message(c.message.chat.id,'Deal:%s\nDescription:%s\n%s' % ('Landing','Required to do Landing, Details by Reference','https://docs.google.com/document/d/1ayi8hW5m2G8knbPpOXHW21J8qxSHT_nOhYdCFybd5j8/edit?usp=sharing'),reply_markup = markup)


@bot.callback_query_handler(lambda c: c.data.split('_')[0] == 'Argument')
def Argument(c):
    text1 = 'The project is not completed, there are many not in accordance with the terms of reference'
    text2 = 'Everything was done exactly according to the terms of reference and on time'

    if c.data.split('_')[2] == 'Contractor':
        bot.send_message(c.message.chat.id, 'Argument %s\n%s\nDetails by Reference\nhttps://docs.google.com/document/d/15dnGhoDNcnt4E70-IUgXl5W4BVukR6-eM_rQ89bqd5c/edit?usp=sharing' % (c.data.split('_')[2],text1))

    else:
        bot.send_message(c.message.chat.id, 'Argument %s\n%s\nDetails by Reference\nhttps://docs.google.com/document/d/1KEwddvIPCRcIRBKAQYe2JUVJryiBtyE3PzYd4_Xtsfk/edit' % (c.data.split('_')[2],text2))









@bot.callback_query_handler(lambda c: c.data.split('_')[0] == 'Approve')
def Approve(c):
    #markup = types.InlineKeyboardMarkup()
    bot.send_message(c.message.chat.id,'Confirmed in favor of %s' % (c.data.split('_')[1]))
    address = c.data.split('_')[2]
    print(address)
    if c.data.split('_')[1] == 'Contractor':
        resp = requests.get('http://92.243.94.148/arbitr.php?result=0xe20335bb&deal=0x%s' % (address))
        print(resp.text)
        try:
            data = json.loads(resp.text)
        except:
            print(resp.text.splitlines())
            data = json.loads(resp.text.splitlines()[0])
        print(data)
        text = str(data['result'])
    else:
        pass
        text = ''
    sent = bot.send_message(c.message.chat.id, text)
    My_Disputes(c.message)


@bot.callback_query_handler(lambda c: c.data.split('_')[0] == 'DecDisp') # approover decline Dispute
def DecDis(c):
    bot.send_message(c.message.chat.id, '%s dispute Decline' % (c.data.split('_')[1]))

    My_Disputes(c.message)



def About(message):
    text = 'Arbitration service based on smart contracts and Reputation System. ' \
           'In case of conflict situations customers can open a dispute in our arbitration system. ' \
           'The arbitrators/judges stake their reputation and arbitrators reward distribution depending on it.' \
           'So they are motivated to resolve a dispute fairly.\n' \
           'We decided that this service can be massively improved thanks to reputation system, blockchain and smart contracts, so that:\n' \
           '\t\t- Judges will resolve the disputes fairly\n' \
           '\t\t- The system trust will increase\n' \
           '\t\t- The power centralization issue will be solved'
    bot.send_message(message.chat.id,text)



@bot.message_handler(content_types=["text"]) # function_manager
def Task_manager(message):

    if (message.text == 'My profile'):
        My_profile(message)
    elif (message.text == 'My Disputes'):
        My_Disputes(message)
    elif (message.text == 'Disputes'):
        Disputes(message)
    elif (message.text == 'About'):
        About(message)

def telegram_polling():
    try:
        bot.polling(none_stop=True, timeout=60) #constantly get messages from Telegram
    except requests.exceptions.ConnectionError as e:
        print(e)
        bot.stop_polling()
        time.sleep(10)
        telegram_polling()

if __name__ == '__main__':
    telegram_polling()