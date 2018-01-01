# TelegramBot
## Introduction
This is a Bot with the theme of Naruto Shippuden
![](https://i.imgur.com/T8P8FAg.jpg)

Here is a RPG game that let you be the character inside the story

According to the decision you make, you are facing diffrent story and also diffrent ending

Considering there are someone who don't know every character inside the story, you can ask question to the bot and the bot will reply from its understanding and also the pictures of the character. The data of relative character will be loaded from database

In addition, you can also ask the bot whether there are ninja nearby you. This can be done by sending your own location to the bot. Actually the bot will reply with the nearest restaurant and tell you there are ninja having their food. It is a quite good way to help you to decide what to eat in the afternoon

The currency rate of countries in glocal can be checked buy asking the currency in the world. THe currency is extractly the currency of Japan Yen.

## Telegram Stickers
My stickers pack = [yoyoNaruto](https://t.me/addstickers/yoyoNaruto)
![](https://i.imgur.com/2dU4Plo.png)


reference:
[Telegram 自製 sticker](https://blog.waterworld.com.hk/post/telegram-custom-sticker)
[貼圖寶庫](https://telegram.how/Stickers)

## Get Started
*    Install Dependency
```
pip3 install -r requirement.txt
```
*    Makefile
```
n:
	./ngrok http 5000

run:
	python3 app.py
```
*    Listening port 
        *    on port 4040
        *    `http://localhost:4040/inspect/http`
*    Finite State Machine
        *    Two FSM are used
                *    RPG FSM
                        *  State with story plot
                        *  `http://localhost:5000/show-fsm`
                        *  [oringal graph](https://i.imgur.com/E2RvqQ3.jpg)

                *    ASKIMG FSM
                        *  State with dynamic work
    
                        *  `http://localhost:5000/show-fsm2`
                        *  [oringal graph](https://i.imgur.com/3A4w1eK.png)


![](https://i.imgur.com/E2RvqQ3.jpg)

![](https://i.imgur.com/3A4w1eK.png)


## Tool Studies
*    python 3 is used for development
*    ngrok -expose a local web server to the internet
        *    [ngrok documentation](https://ngrok.com/docs)
        *    [ngrok github](https://github.com/inconshreveable/ngrok)
        *    [使用 ngrok 讓本機上的網站讓全世界看到 ](https://ithelp.ithome.com.tw/articles/10186454)
        *    [npm ngrok](https://www.npmjs.com/package/ngrok)
*    Git
        *    [Basic Git Tutorial](https://lee-w.github.io/git-tutorial/#/)
*    Transitions
        *    [transitions](https://github.com/pytransitions/transitions)
*    Flask as the Framework
        *    [Flask](http://flask.pocoo.org/)
*    pyGraphviz gor graphing
        *    [pyGraphviz](https://pypi.python.org/pypi/pygraphviz)
        *    [Getting started with Graphviz and Python](http://matthiaseisen.com/articles/graphviz/)
        *    [PyGraphviz](https://pygraphviz.github.io/documentation.html)
  
*    Example of TelegramBot:
        *    [Create a Telegram EchoBot](http://lee-w.github.io/posts/bot/2017/03/create-a-telegram-echobot/)
        *    [Example of Telegram Echobot](https://github.com/Lee-W/TOC-Project-2017)
        *    [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
        *    [Telegram Bot API](https://core.telegram.org/bots/api)
        *    [Telegram Weather Bot](https://github.com/neighborhood999/telegram-weather-bot)
        *    [Telegram Bot 開發起手式](https://neighborhood999.github.io/2016/07/19/Develop-telegram-bot/)



## Function
### Firebase
*    Data storage
*    The data of the chracter is stored in the database
*    Realtime Database is used
*    Authentication with email and respective  apiKey is get to access the database
*    photos are also stored in the storage folder of the databqse
*    folder url, databaseURL and apiKey of this bot are hiden


*    reference:
        *    [Firebase 是什麼 ? 集 APP 後端開發與分析於一身的強大工具！](https://tw.alphacamp.co/2016/07/22/firebase/)
        *    [Firebase網頁教學](http://sj82516-blog.logdown.com/posts/1048782/auth-firebase-web-operations-validation-review)

### BeautifulSoup
*    pulling data out of HTML and XML files
*    parsing the location data return in the format of xml by google maps api 
*    reference:
        *    [給初學者的 Python 網頁爬蟲與資料分析 解構並擷取網頁資料](http://blog.castman.net/%E6%95%99%E5%AD%B8/2016/12/22/python-data-science-tutorial-3.html)
        *    [Beautiful Soup 的用法](http://wiki.jikexueyuan.com/project/python-crawler-guide/beautiful-soup.html)
        *    [ Python爬蟲實戰 ](https://www.slideshare.net/tw_dsconf/python-78691041)

### Pandas
*    pulling data out of HTML and XML files
*    parsing the currency into table
*    reference:
        *   [Pandas ](http://wiki.jikexueyuan.com/project/start-learning-python/311.html)
        *   [[Python] Pandas 基礎教學](https://oranwind.org/python-pandas-ji-chu-jiao-xue/)


### Google Places API Web Service
*    API helps to find the location and return the nearby places searched
reference:
*    [Places API Web Service ](https://developers.google.com/places/web-service/search)


### Reference and Parsing Website 
*    [火影忍者人物](https://zh.wikipedia.org/wiki/Category:%E7%81%AB%E5%BD%B1%E5%BF%8D%E8%80%85%E4%BA%BA%E7%89%A9)
*    [臺灣銀行牌告匯率](http://rate.bot.com.tw/xrt?Lang=zh-TW)

