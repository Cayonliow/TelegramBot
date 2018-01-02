import telegram

from transitions.extensions import GraphMachine
from firebase import firebase as firebaseAPI

import fsm as fsm1_para
from bs4 import BeautifulSoup
import requests
import time
import pandas

def get_web_page(url):
    resp = requests.get(
        url=url,
        cookies={'over18': '1'}
    )
    print("encoding: %s" % resp.encoding)
    resp.encoding=resp.apparent_encoding
    print("apparent_encoding: %s" %resp.apparent_encoding)
    print("encoding: %s" % resp.encoding)

    if resp.status_code != 200:
        print('Invalid url:', resp.url)
        return None
    else:
        return resp.text

class TocMachine2(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_wait_to_ask(self, update):
        text = update.message.text
        return text == '我要問問題'

    def is_going_to_ask_character(self, update):
        text = update.message.text
        return text == '這是誰'

    def is_going_to_ask_rate(self, update):
        text = update.message.text
        return text == '現在值多少錢'

    def is_going_to_ask_place(self, update):
        text = update.message.text
        return text == '身邊有忍者嗎'
    
    def is_going_to_check_character(self, update):
        list_name = []
        global list_name
        list_name=['宇智波佐助','春野櫻','漩渦鳴人','奈良鹿丸','山中井野','秋道丁次','旗木卡卡西','阿凱','大和','日向寧次','天天','李洛克','犬塚牙','日向雛田','油女志乃','我愛羅','手鞠','勘久郎','自來也','綱手','大蛇丸']
        text = update.message.text
        for i in list_name:
            if text == i and i != '重玩':
                return True
        
    def is_going_to_check_rate(self, update):
        text = update.message.text
        return (len(text)>0)

    def is_going_to_check_place(self, update):
        text = update.message.text
        if(text == '我要問問題' or text == '重玩'): 
            return False
        else:
            location = update.message.location
            return (location.longitude>0)

    
    def on_enter_empty2(self, update):
        reply_markup2 = fsm1_para.get_value()
        update.message.reply_text(text='繼續',reply_markup=reply_markup2)

    def on_enter_wait_to_ask(self, update):
        reply_markup2 = telegram.ReplyKeyboardMarkup([['這是誰'],['身邊有忍者嗎'],['現在值多少錢'],['我懂了，我要繼續玩'],['重玩']])
        update.message.reply_text(text='來來來,火影百科在此,有什麼想問的？',reply_markup=reply_markup2)

    def on_enter_ask_character(self, update):
        global list_name
        list_name=[['宇智波佐助','春野櫻','漩渦鳴人'],['奈良鹿丸','山中井野','秋道丁次'],['旗木卡卡西','阿凱','大和'],['日向寧次','天天','李洛克'],['犬塚牙','日向雛田','油女志乃'],['我愛羅','手鞠','勘久郎'],['自來也','綱手','大蛇丸'],['重玩'],['我懂了，我要繼續玩']]
        reply_markup2 = telegram.ReplyKeyboardMarkup(list_name)
        update.message.reply_text(text='你要問的是',reply_markup=reply_markup2)

    def on_enter_ask_rate(self, update):
        reply_markup2 = telegram.ReplyKeyboardMarkup([['美金 (USD)','港幣 (HKD)','英鎊 (GBP)'],['馬幣 (MYR)','一覽','人民幣 (CNY)'],['臺幣 (TWD)','韓元 (KRW)','歐元 (EUR)'],['我懂了，我要繼續玩'],['重玩']])
        update.message.reply_text(text='現在的價錢呢，你想問哪一種幣？',reply_markup=reply_markup2)   

    def on_enter_ask_place(self, update):
        location_type= telegram.KeyboardButton(text='我現在在',request_location=True)
        custom_keyboard = [[ location_type ],['我要問問題'],['我懂了，我要繼續玩'],['重玩']]
        reply_markup2 = telegram.ReplyKeyboardMarkup(custom_keyboard)
        update.message.reply_text(text='你現在在',reply_markup=reply_markup2)
    
    def on_enter_check_character(self, update):
        reply_markup2 = telegram.ReplyKeyboardMarkup([['我要問問題'],['重玩'],['我懂了，我要繼續玩']])
        print(update.message.text)
        print('in check')
        firebase = firebaseAPI.FirebaseApplication('https://yourbotfirebaseAPI.firebaseio.com', None)
        result = firebase.get('/',None)
        #print(result)
        #s1=unicode(update.message.text, "utf-8")
        #s = result[s1][u'data']
        s_data = result[update.message.text][u'data']
        s_photo = result[update.message.text][u'photo']
        update.message.reply_text(text=s_data,reply_markup=reply_markup2)
        update.message.reply_photo(photo=s_photo)

    def on_enter_check_place(self, update):
        reply_markup2 = telegram.ReplyKeyboardMarkup([['我要問問題'],['重玩'],['我懂了，我要繼續玩']])
        key='your key'
        s_place = 'https://maps.googleapis.com/maps/api/place/nearbysearch/xml?location='+str(update.message.location.latitude)+','+str(update.message.location.longitude)+'&radius=500&type=restaurant&key='+key
        print(s_place)
        page = get_web_page(s_place)
        print('page=')
        print(page)
        if page:
            soup = BeautifulSoup(page, 'html.parser')
            a = soup.find('name')
            print(a.text)
            b = soup.find('lat')
            print(b.text)
            c = soup.find('lng')
            print(c.text)
            print(time.localtime().tm_hour)
            if(time.localtime().tm_hour>=6 and time.localtime().tm_hour<=9):
                print('早餐')
                eat='早餐'
            if(time.localtime().tm_hour>=10 and time.localtime().tm_hour<=11):
                print('早午餐')
                eat='早午餐'
            if(time.localtime().tm_hour>=12 and time.localtime().tm_hour<=13):
                print('午餐')
                eat='午餐'
            if(time.localtime().tm_hour>=14 and time.localtime().tm_hour<=17):
                print('下午茶')
                eat='下午茶'
            if(time.localtime().tm_hour>=18 and time.localtime().tm_hour<=21):
                print('晚餐')
                eat='晚餐'
            if(time.localtime().tm_hour>=22 and time.localtime().tm_hour<=23):
                print('宵夜')
                eat='宵夜'
            if(time.localtime().tm_hour>=0 and time.localtime().tm_hour<=5):
                print('宵夜')
                eat='宵夜'

            str_to_reply='佐助在'+a.text+'吃'+eat

        update.message.reply_text(str_to_reply)
        update.bot.sendLocation(update.message.chat.id,float(b.text),float(c.text))
        update.message.reply_text(text='快去找他啊',reply_markup=reply_markup2)

    def on_enter_check_rate(self, update):
        reply_markup2 = telegram.ReplyKeyboardMarkup([['我要問問題'],['重玩'],['我懂了，我要繼續玩']])
        update.message.reply_text('忍者世界的貨幣是以‘兩’爲一單位，他的幣值是跟日幣是一樣的哦！！')
        update.message.reply_text('不如看看你國家的‘一元’可以換成多少‘兩’，讓你在忍者世界裏變成首富吧！！')
        dfs=pandas.read_html('http://rate.bot.com.tw/xrt?Lang=zh-TW')
        currency=dfs[0]
        currency=currency.ix[:,0:5]
        global f_text
        f_text = update.message.text
        for i in range(0,19):
            country_name=currency.iloc[i][0].split('  ')[0]
            if country_name=='日圓 (JPY)':
                global rate
                rate=float(currency.iloc[i][1])/float(currency.iloc[i][2])
                print(rate)

        if f_text=='一覽':
            update.message.reply_text('臺幣 (TWD)：'+str(round(1/rate,5)))
            for i in range(0,19):
                country_name=currency.iloc[i][0].split('  ')[0]
                if currency.iloc[i][2] == '-':
                    currency.iloc[i][2]='0'
                rate_in_country=float(currency.iloc[i][2])
                if country_name=='美金 (USD)':
                    update.message.reply_text(country_name+':'+str(round(rate/rate_in_country,5)))
                if country_name=='港幣 (HKD)':
                    update.message.reply_text(country_name+':'+str(round(rate/rate_in_country,5)))
                if country_name=='英鎊 (GBP)':
                    update.message.reply_text(country_name+':'+str(round(rate/rate_in_country,5)))
                if country_name=='歐元 (EUR)':
                    update.message.reply_text(country_name+':'+str(round(rate/rate_in_country,5)))
                if country_name=='韓元 (KRW)':
                    update.message.reply_text(country_name+':'+str(round(rate/rate_in_country,5)))
                if country_name=='馬來幣 (MYR)':
                    update.message.reply_text('馬幣 (MYR)：'+str(round(rate/rate_in_country,5)))
                if country_name=='人民幣 (CNY)':
                    update.message.reply_text(country_name+':'+str(round(rate/rate_in_country,5)))

            update.message.reply_text(text='看起來匯率不錯哦，看來可以炒個幣呢',reply_markup=reply_markup2)
        
        else:
            if f_text=='臺幣 (TWD)':
                update.message.reply_text('臺幣 (TWD)：'+str(round(1/rate,5)))
            else:
                for i in range(0,19):
                    country_name=currency.iloc[i][0].split('  ')[0]
                    if currency.iloc[i][2] == '-':
                        currency.iloc[i][2]='0'
                    rate_in_country=float(currency.iloc[i][2])
                    if(f_text=='馬幣 (MYR)'):
                        f_text='馬來幣 (MYR)'                   
                    if country_name==f_text:
                        if(country_name=='馬來幣 (MYR)'):
                            f_text='馬幣 (MYR)'
                        update.message.reply_text(f_text+':'+str(round(rate/rate_in_country,5)))
            update.message.reply_text(text='看起來匯率不錯哦，說不定可以去忍者世界當個首富呢',reply_markup=reply_markup2)


    def is_going_back_wait_to_ask(self, update):
        text = update.message.text
        return text == '我要問問題'

    def is_going_back_empty2(self, update):
        text = update.message.text
        return text == '我懂了，我要繼續玩' or text == '我懂了，我要繼續玩'
