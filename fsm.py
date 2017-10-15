from transitions.extensions import GraphMachine

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_menu(self, update):
        text = update.message.text
        return text == 'menu'

    def is_going_to_playing(self, update):
        text = update.message.text
        return text == 'playing'

    def is_going_to_male(self, update):
        text = update.message.text
        return text == 'Boy'

    def is_going_to_follow(self, update):
        text = update.message.text
        return text == 'Yes'

    def is_going_to_deny(self, update):
        text = update.message.text
        return text == 'No'

    def is_going_to_Itachi(self, update):
        text = update.message.text
        return text == 'First'

    def is_going_to_Hoshigaki(self, update):
        text = update.message.text
        return text== 'Second'

    def is_going_to_Kakuzu(self, update):
        text = update.message.text
        return text == '1'

    def is_going_to_Zabuza(self, update):
        text = update.message.text
        return text == '2'


    def on_enter_menu(self, update):
        update.message.reply_text("There is a Telegram Echo bot with the theme of anime of Naruto\nEnjoy the RPG story!\n\nAuthor:Cayon Liow Keei Yann\n")
        update.message.reply_text("Wat can I help you?\n")
        update.message.reply_sticker('CAADBQADAQEAAvjGxQp623fRgMRgIAI')

    def on_enter_playing(self, update):
        update.message.reply_text('Just start playing')
        update.message.reply_text('有一天，你坐在客廳裏，看着漫畫，看到。。。突然覺得頭很昏，迷迷糊糊地就睡着了。')
        update.message.reply_text('當你起來的時候發現你已不在自家客廳裏，眼前的是一幕熟悉但又從未親眼看過的場景')
        self.photo_file = open('photo/sign.jpg', 'rb')
        update.message.reply_photo(self.photo_file)
        update.message.reply_text('走向鏡子！什麼！\n發現自己變成了：\nBoy：男的\nGirl：女的')

    def on_enter_male(self, update):
        self.photo_file = open('photo/kakashi.jpg', 'rb')
        update.message.reply_photo(self.photo_file)
        update.message.reply_text('你：什麼？？！我竟變成了卡卡西！！ 怎麼會這樣！！')
        update.message.reply_text('鳴人：卡卡西老師大事不妙了，趕快跟我走吧\nYes:哦哦哦好～等等我\nNo:這到底是怎麼回事！不要！我不要跟你走！')

    def on_enter_follow(self, update):
        update.message.reply_text('原來，組織『曉』為了得到一尾守鶴的力量，捉去了擁有一尾力量的祭品之力五代目風影我愛羅。為了救出我愛羅，砂忍向同盟國木葉求援，木葉方面派出卡卡西班前往拯救我愛羅。砂隱村的千代婆婆其後加入卡卡西班一同前往拯救我愛羅。五代目火影綱手再派出凱班作增援')
        update.message.reply_text('你跟凱需要兵分兩路前行，你選擇先出發，還是後出發？\nFirst：前出發\nSecond：後出發')

    def on_enter_deny(self, update):
        update.message.reply_text('鳴人：搞什麼啊！你受傷還沒回復哦說話神志不清的？老師我不管你了我愛羅被抓走了我要去救他了，你好好休息吧我一個人就可以了～')
        update.message.reply_text('你還沒有搞清楚到底發生了什麼事\n嗑磕磕（有人敲門）\n靜音：卡卡西前輩！很抱歉打擾你在修養，可是我們現在人手嚴重不足，可以請你帶領孩子們執行這一次的任務嗎？')
        update.message.reply_text('你：執行任務？孩子們？難道是\n1:志乃、雛田、牙他們？\n2：鹿丸、丁次、井野他們？')

    def on_enter_Itachi(self, update):
        update.message.reply_text('你為了避免鳴人獨自行動，從後追趕鳴人，發現敵人地達羅，在戰鬥數回合後你開啓了萬花筒寫輪眼，對地達羅使用可以轉換空間的曈術--神威，及控制結界，打斷了地達羅剩下的右手，磕事你才剛剛練成神威，不能熟練地控制空間的位置和大小，在體力方面亦明顯不能支撐這種術，很快就感到疲憊。')
        update.message.reply_text('凱也在這時候前來救援，地達羅見寡不敵衆，想要用自爆同歸於盡，這時候你該怎麼辦？\nQ:使用幻術，令地達羅暫時陷入幻境，趁這段時間逃離\nW：再次使用神威，把他和爆炸轉移到另一空間')

    def on_enter_Hoshigaki(self, update):
        update.message.reply_text('你選擇作爲第二批出發支援的隊伍，突然！一只鯊魚向你們襲擊是干柿鬼鮫！他使出水遁·爆水衝波，他一口氣吐出大量的水，將一大片低漥谷地瞬間變成湖泊，你與隊員深陷其中，你忙着救別人，突然眼前一黑無法動彈，在感覺查克拉被一點一點奪取而昏過去了')

    def on_enter_Kakuzu(self, update):
        update.message.reply_text('啊 猜錯了。是鹿丸、丁次、井野他們。因為上忍猿飛阿斯瑪在追捕『曉』成員飛段、角都時陣亡，第十班矢志為老師復仇，而你將暫替阿斯瑪，作為第十班的隊長，率領他們再戰飛段、角都。')
        update.message.reply_text('甫一對戰，你成功以雷遁·雷切偷襲角都，破了其土遁·土矛（因為雷屬性剋土屬性），並刺穿其心臟。正當卡卡西以為對方已被擊斃，殊不知對方原來擁有多個從其他忍者搶來的心臟，故能不死。')
        update.message.reply_text('幸虧大和及時率領鳴人、祭、櫻三人趕到，加入戰團中。你讓鳴人作第二次攻擊。鳴人亦不負所託，以影分身成功欺騙角都，並從其背後施以風遁·螺旋手裏劍，巨大的摧毀力再連破角都兩個心臟。最後，卡卡西以寫輪眼收拾倒在地上、動彈不得的角都，摧毀他最後一個心臟，及把角都的屍首帶回木葉隱村給綱手研究。')

    def on_enter_Zabuza(self, update):
        update.message.reply_text('啊 猜錯了。是他們志乃、雛田、牙。為了得知有關『曉』的情報、及追蹤正在尋找宇智波鼬的宇智波佐助，你們一行人決定以宇智波鼬為鎖定目標進行追捕。目前你們透過鳴人的影分身、已得知佐助的大約位置。不過途中遇上擁有特殊能力的鳶；陷入苦戰')
        update.message.reply_text('然後聽到佐助身受重傷，在甩掉鳶後，趕緊及帶人已早一步前往戰場，他也率眾快馬趕往，並開啓萬花筒寫輪眼。然而到達現場時，佐助早已被帶走了')

    def on_exit_waiting(self, update):
        print('Leaving Waiting')

    def on_exit_menu(self, update):
        print('Leaving Menu')

    def on_exit_playing(self, update):
        print('Leaving Playing')

    def is_going_back_waiting(self, update):
        text = update.message.text
        return text.lower() == 'waiting'
