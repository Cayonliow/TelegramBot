import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine

import requests
import re


API_TOKEN = '463872076:AAGhNBC14QbV7kLw2M8sTQEdnvUSfmaDduo'
#WEBHOOK_URL = _get_ngrok_url()

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
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
        'Death',
        'Continue'
    ],
    transitions=[
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
            'source': 'menu',
            'dest': 'waiting',
            'conditions': 'is_going_back_waiting'
        },
        {
            'trigger': 'advance',
            'source': 'playing',
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
            'source': [
                'Hoshigaki',
                'LeiQie'
            ],
            'dest': 'Death',
            'conditions': 'is_going_to_Death'
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
            'source': [
                'ShenWei',
                'Kakuzu',
                'Zabuza'
            ],
            'dest': 'Continue',
            'conditions': 'is_going_to_Continue'
        }

    ],
    initial='waiting',
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
    machine.advance(update)
    print(machine.state)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__": 
    _set_webhook()
    app.run()

