import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine
from fsm2 import TocMachine2

import requests
import re

API_TOKEN = '463872076:AAGhNBC14QbV7kLw2M8sTQEdnvUSfmaDduo'
#WEBHOOK_URL = _get_ngrok_url()
global reply_markup


app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'empty',
        'waiting',
        'menu',
        'playing',
        'male',
        'female',
        'follow',
        'deny',
        'Itachi',
        'LeiQie',
        'ShenWei',
        'Kakuzu',
        'Zabuza',
	    'Hoshigaki',
        'followm',
        'denym',
        'poison1',
        'poison2',
        'Sasori',
        'Chiyo',
        'self',
        'kill',
        'spymeet',
        'punch',
        'nopunch',
        'yes',
        'no',
        'catchSai',
        'catchSasuke',
        'Death',
        'Continue'

    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'empty',
            'dest': 'waiting',
            'conditions': 'is_going_to_waiting'
        },
        {
            'trigger': 'advance',
            'source': 'waiting',
            'dest': 'menu',
            'conditions': 'is_going_to_menu'
        },
        {
            'trigger': 'advance',
            'source': 'waiting',
            'dest': 'playing',
            'conditions': 'is_going_to_playing'
        },
        {
            'trigger': 'advance',
            'source':[
                'waiting',
                'menu',
                'playing',
                'male',
                'female',
                'follow',
                'deny',
                'Itachi',
                'LeiQie',
                'ShenWei',
                'Kakuzu',
                'Zabuza',
                'Hoshigaki',
                'followm',
                'denym',
                'poison1',
                'poison2',
                'Sasori',
                'Chiyo',
                'self',
                'kill',
                'spymeet',
                'punch',
                'nopunch',
                'yes',
                'no',
                'catchSai',
                'catchSasuke',
                'Death',
                'Continue'
            ],
            'dest': 'waiting',
            'conditions': 'is_going_back_waiting'
        },
        {
            'trigger': 'advance',
            'source': 'playing',
            'dest': 'male',
            'conditions': 'is_going_to_male'
        },
        {
            'trigger': 'advance',
            'source': 'playing',
            'dest': 'female',
            'conditions': 'is_going_to_female'
        },
        {
            'trigger': 'advance',
            'source': 'male',
            'dest': 'deny',
            'conditions': 'is_going_to_deny'
        },
        {
            'trigger': 'advance',
            'source': 'male',
            'dest': 'follow',
            'conditions': 'is_going_to_follow'
        },
        {
            'trigger': 'advance',
            'source': 'follow',
            'dest': 'Itachi',
            'conditions': 'is_going_to_Itachi'
        },
        {
            'trigger': 'advance',
            'source': 'follow',
            'dest': 'Hoshigaki',
            'conditions': 'is_going_to_Hoshigaki'
        },
        {
            'trigger': 'advance',
            'source': 'Itachi',
            'dest': 'LeiQie',
            'conditions': 'is_going_to_LeiQie'
        },
        {
            'trigger': 'advance',
            'source': 'Itachi',
            'dest': 'ShenWei',
            'conditions': 'is_going_to_ShenWei'
        },
        {
            'trigger': 'advance',
            'source': 'deny',
            'dest': 'Kakuzu',
            'conditions': 'is_going_to_Kakuzu'
        },
        {
            'trigger': 'advance',
            'source': 'deny',
            'dest': 'Zabuza',
            'conditions': 'is_going_to_Zabuza'
        },
        {
            'trigger': 'advance',
            'source': 'female',
            'dest': 'followm',
            'conditions': 'is_going_to_followm'
        },
        {
            'trigger': 'advance',
            'source': 'female',
            'dest': 'denym',
            'conditions': 'is_going_to_denym'
        },
        {
            'trigger': 'advance',
            'source': 'followm',
            'dest': 'poison1',
            'conditions': 'is_going_to_poison1'
        },
        {
            'trigger': 'advance',
            'source': 'followm',
            'dest': 'poison2',
            'conditions': 'is_going_to_poison2'
        },
        {
            'trigger': 'advance',
            'source': 'poison2',
            'dest': 'Sasori',
            'conditions': 'is_going_to_Sasori'
        },
        {
            'trigger': 'advance',
            'source': 'Sasori',
            'dest': 'Chiyo',
            'conditions': 'is_going_to_Chiyo'
        },
        {
            'trigger': 'advance',
            'source': 'Sasori',
            'dest': 'self',
            'conditions': 'is_going_to_self'
        },
        {
            'trigger': 'advance',
            'source': 'denym',
            'dest': 'kill',
            'conditions': 'is_going_to_kill'
        },
        {
            'trigger': 'advance',
            'source': 'denym',
            'dest': 'spymeet',
            'conditions': 'is_going_to_spymeet'
        },
        {
            'trigger': 'advance',
            'source': 'spymeet',
            'dest': 'punch',
            'conditions': 'is_going_to_punch'
        },
        {
            'trigger': 'advance',
            'source': 'spymeet',
            'dest': 'nopunch',
            'conditions': 'is_going_to_nopunch'
        },
        {
            'trigger': 'advance',
            'source': 'punch',
            'dest': 'yes',
            'conditions': 'is_going_to_yes'
        },
        {
            'trigger': 'advance',
            'source': 'punch',
            'dest': 'no',
            'conditions': 'is_going_to_no'
        },
        {
            'trigger': 'advance',
            'source': 'yes',
            'dest': 'catchSai',
            'conditions': 'is_going_to_catchSai'
        },
        {
            'trigger': 'advance',
            'source': 'yes',
            'dest': 'catchSasuke',
            'conditions': 'is_going_to_catchSasuke'
        },
        {
            'trigger': 'advance',
            'source': [
                'Hoshigaki',
                'LeiQie',
                'poison1',
                'self',
                'catchSai',
                'kill',
                'nopunch'
            ],
            'dest': 'Death',
            'conditions': 'is_going_to_Death'
        },
        {
            'trigger': 'advance',
            'source': [
                'ShenWei',
                'Kakuzu',
                'Zabuza',
                'Chiyo',
                'catchSasuke'
            ],
            'dest': 'Continue',
            'conditions': 'is_going_to_Continue'
        }

    ],
    initial='empty',
    auto_transitions=False,
    show_conditions=True,
)

machine2 = TocMachine2(
    states=[
        'empty2',
        'wait_to_ask',
        'ask_character',
        'ask_rate',
        'ask_place',
        'check_character',
        'check_place',
        'check_rate'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'empty2',
            'dest': 'wait_to_ask',
            'conditions': 'is_going_to_wait_to_ask'
        },
        {
            'trigger': 'advance',
            'source': 'wait_to_ask',
            'dest': 'ask_character',
            'conditions': 'is_going_to_ask_character'
        },
        {
            'trigger': 'advance',
            'source': 'wait_to_ask',
            'dest': 'ask_rate',
            'conditions': 'is_going_to_ask_rate'
        },
        {
            'trigger': 'advance',
            'source': 'wait_to_ask',
            'dest': 'ask_place',
            'conditions': 'is_going_to_ask_place'
        },
        {
            'trigger': 'advance',
            'source': 'ask_character',
            'dest': 'check_character',
            'conditions': 'is_going_to_check_character'
        },
        {
            'trigger': 'advance',
            'source': 'ask_place',
            'dest': 'check_place',
            'conditions': 'is_going_to_check_place'
        },
        {
            'trigger': 'advance',
            'source': 'ask_rate',
            'dest': 'check_rate',
            'conditions': 'is_going_to_check_rate'
        },
        {
            'trigger': 'advance',
            'source':[
                'ask_character',
                'ask_rate',
                'ask_place',
                'check_character',
                'check_place',
                'check_rate'
            ],
            'dest': 'wait_to_ask',
            'conditions': 'is_going_back_wait_to_ask'
        }, 
        {
            'trigger': 'advance',
            'source':'wait_to_ask',
            'dest': 'empty2',
            'conditions': 'is_going_back_empty2'
        }
    ],
    initial='empty2',
    auto_transitions=False,
    show_conditions=True,
)

def _get_ngrok_url():
    response = requests.get('http://127.0.0.1:4040')
    if response.status_code != requests.codes.ok:
        print('ngrok is not open')
        sys.exit(1)
    print('ngrok is open')
    result = re.findall('{\\\\"URL\\\\":\\\\"https://.*.ngrok.io\\\\",\\\\"Proto\\\\":\\\\"https\\\\"',str(response.text))
    result = re.findall(':\\\\".*[.]ngrok[.]io',result[0])
    print('get : '+result[0][3:])
    return result[0][3:]+'/hook'

def _set_webhook():
    WEBHOOK_URL = _get_ngrok_url()
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    update.bot = bot
    machine.advance(update)
    print('NOW STATE:')
    print(machine.state)
    machine2.advance(update)
    print('NOW STATE:')
    print(machine2.state)
    #print(update.update_id)
    print('\nlocation:')
    print(update.message.location)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')

@app.route('/show-fsm2', methods=['GET'])
def show_fsm2():
    byte_io = BytesIO()
    machine2.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm2.png', mimetype='image/png')

if __name__ == "__main__": 
    _set_webhook()
    app.run()

