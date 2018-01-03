import telegram

from transitions.extensions import GraphMachine
from firebase import firebase

global reply_markup 
reply_markup = telegram.ReplyKeyboardMarkup([['開始！']])

def get_value():
    try:
        global reply_markup
        return reply_markup
    except KeyError: 
        return None 

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_waiting_from_waiting(self, update):
        text = update.message.text
        print('hrllo')
        return text != '開始！' and text != '重玩' and text!= 'menu' and text!='我要問問題' and text!='冒險'and text!='這是誰' and text!='身邊有忍者嗎' and text!='現在值多少錢'and text!='我懂了，我要繼續玩'

    def is_going_to_waiting(self, update):
        text = update.message.text
        return text == '開始！' or text == '重玩' 

    def is_going_to_menu(self, update):
        text = update.message.text
        return text == 'menu'

    def is_going_to_playing(self, update):
        text = update.message.text
        return text == '冒險'

    def is_going_to_male(self, update):
        text = update.message.text
        return text == '男的'

    def is_going_to_female(self, update):
        text = update.message.text
        return text == '女的'

    def is_going_to_follow(self, update):
        text = update.message.text
        return text == '哦哦哦好～等等我'

    def is_going_to_deny(self, update):
        text = update.message.text
        return text == '這到底是怎麼回事！不要！我不要跟你走！'

    def is_going_to_Itachi(self, update):
        text = update.message.text
        return text == '前出發'

    def is_going_to_Hoshigaki(self, update):
        text = update.message.text
        return text== '後出發'

    def is_going_to_Kakuzu(self, update):
        text = update.message.text
        return text == '志乃、雛田、牙?'

    def is_going_to_Zabuza(self, update):
        text = update.message.text
        return text == '鹿丸、丁次、井野?'

    def is_going_to_LeiQie(self, update):
        text = update.message.text
        return text == '使用幻術，令地達羅暫時陷入幻境，趁這段時間逃離'

    def is_going_to_ShenWei(self, update):
        text = update.message.text
        return text == '再次使用神威，把他和爆炸轉移到另一空間'

    def is_going_to_followm(self, update):
        text = update.message.text
        return text == '哦哦哦好～等等我'

    def is_going_to_denym(self, update):
        text = update.message.text
        return text == '這到底是怎麼回事！不要！我不要跟你走！'

    def is_going_to_poison1(self, update):
        text = update.message.text
        return text == '那就相信千代婆婆一次吧'

    def is_going_to_poison2(self, update):
        text = update.message.text
        return text == '不管她啦！我相信是混合毒！'

    def is_going_to_Sasori(self, update):
        text = update.message.text
        return text == '走！'

    def is_going_to_Chiyo(self, update):
        text = update.message.text
        return text == '其中一份交給千代好了，不然我也戰鬥不下去啊'
 
    def is_going_to_self(self, update):
        text = update.message.text
        return text == '兩份都給自己好了，我負責戰鬥，速戰速決！'
 
    def is_going_to_kill(self, update):
        text = update.message.text
        return text == '鳴人你是說要去救我愛羅嗎？'

    def is_going_to_spymeet(self, update):
        text = update.message.text
        return text == '鳴人你是說要趕快趕到草忍村的天地橋，等待大蛇丸身邊的臥底會出現嗎？'

    def is_going_to_punch(self, update):
        text = update.message.text
        return text == '打就打！誰叫你說佐助壞話！'

    def is_going_to_nopunch(self, update):
        text = update.message.text
        return text == '先忍着！任務結束就痛扁你一頓'

    def is_going_to_yes(self, update):
        text = update.message.text
        return text == '暗殺佐助。'

    def is_going_to_no(self, update):
        text = update.message.text
        return text == '暗殺鳴人。'

    def is_going_to_catchSai(self, update):
        text = update.message.text
        return text == '任務重要，要把佐井抓住'

    def is_going_to_catchSasuke(self, update):
        text = update.message.text
        return text == '佐助重要，不顧一切也要帶他回木葉'

    def is_going_to_Death(self, update):
        text = update.message.text
        return text == '噢不'

    def is_going_to_Continue(self, update):
        text = update.message.text
        return text == '成功了'

    def on_enter_waiting(self, update):
        global reply_markup
        reply_markup = telegram.ReplyKeyboardMarkup([['冒險','menu'],['重玩','我要問問題']])
        update.message.reply_text(text='你現在在一個虛擬世界，唯有做出正確的選擇，才能離開，又或許，你根本不想離開這個忍者世界',reply_markup=reply_markup)
	
    def on_enter_menu(self, update):
        global reply_markup
        reply_markup = telegram.ReplyKeyboardMarkup([['Get it']])
        update.message.reply_text("There is a Telegram Echo bot with the theme of anime of Naruto\nEnjoy the RPG story!\n\nAuthor:Cayon Liow Keei Yann\n")
        update.message.reply_sticker('CAADBQADAQEAAvjGxQp623fRgMRgIAI')
        update.message.reply_text(text='Hi!',reply_markup=reply_markup)

    def on_enter_playing(self, update):
        global reply_markup
        reply_markup = telegram.ReplyKeyboardMarkup([['男的','女的'],['重玩','我要問問題']])
        update.message.reply_text('Just start playing')
        update.message.reply_text('有一天,你坐在客廳裏，看着漫畫，看到。。。突然覺得頭很昏，迷迷糊糊地就睡着了。')
        update.message.reply_text('當你起來的時候發現你已不在自家客廳裏，眼前的是一幕熟悉但又從未親眼看過的場景')
        update.message.reply_sticker('CAADBQADIwADmsj5D8R7mQ7vXgl3Ag')
        update.message.reply_text(text='走向鏡子！什麼！\n發現自己變成了',reply_markup=reply_markup)
        

    def on_enter_male(self, update):
        global reply_markup
        reply_markup = telegram.ReplyKeyboardMarkup([['哦哦哦好～等等我'],['這到底是怎麼回事！不要！我不要跟你走！'],['重玩','我要問問題']])
        update.message.reply_sticker('CAADBQADJAADmsj5DxDN34F40M4rAg')
        update.message.reply_text('你：什麼？？！我竟變成了卡卡西！！ 怎麼會這樣！！')
        update.message.reply_sticker('CAADBQADJgADmsj5D3B58IgX0bkqAg')
        update.message.reply_text(text='鳴人：卡卡西老師大事不妙了，趕快跟我走吧',reply_markup=reply_markup)

    def on_enter_female(self, update):
        global reply_markup
        reply_markup = telegram.ReplyKeyboardMarkup([['哦哦哦好～等等我'],['這到底是怎麼回事！不要！我不要跟你走！'],['重玩','我要問問題']])
        update.message.reply_sticker('CAADBQADJQADmsj5Dx6waONiGbFFAg')
        update.message.reply_text('你：什麼？？！我竟變成了小櫻！！ 怎麼會這樣！！')
        update.message.reply_sticker('CAADBQADJgADmsj5D3B58IgX0bkqAg')
        update.message.reply_text(text='鳴人：小櫻大事不妙了，趕快跟我走吧',reply_markup=reply_markup)

    def on_enter_follow(self, update):
        global reply_markup
        reply_markup = telegram.ReplyKeyboardMarkup([['前出發','後出發'],['重玩','我要問問題']])
        update.message.reply_text('原來，組織『曉』為了得到一尾守鶴的力量，捉去了擁有一尾力量的祭品之力五代目風影我愛羅。為了救出我愛羅，砂忍向同盟國木葉求援，木葉方面派出卡卡西班前往拯救我愛羅。砂隱村的千代婆婆其後加入卡卡西班一同前往拯救我愛羅。五代目火影綱手再派出凱班作增援')
        update.message.reply_sticker('CAADBQADJwADmsj5Dw0cb10rWm3WAg')
        update.message.reply_text(text='你跟凱需要兵分兩路前行，你選擇',reply_markup=reply_markup)

    def on_enter_deny(self, update):
        global reply_markup
        reply_markup = telegram.ReplyKeyboardMarkup([['志乃、雛田、牙?'],['鹿丸、丁次、井野?'],['重玩','我要問問題']])
        update.message.reply_sticker('CAADBQADJgADmsj5D3B58IgX0bkqAg')
        update.message.reply_text('鳴人：搞什麼啊！你受傷還沒回復哦說話神志不清的？老師我不管你了我愛羅被抓走了我要去救他了，你好好休息吧我一個人就可以了～')
        update.message.reply_text('你還沒有搞清楚到底發生了什麼事\n嗑磕磕（有人敲門）')
        update.message.reply_sticker('CAADBQADLQADmsj5D9XDgt7kEYNrAg')
        update.message.reply_text('靜音：卡卡西前輩！很抱歉打擾你在修養，可是我們現在人手嚴重不足，可以請你帶領孩子們執行這一次的任務嗎？')
        update.message.reply_text(text='你：執行任務？孩子們？難道是',reply_markup=reply_markup)

    def on_enter_Itachi(self, update):
        global reply_markup
        reply_markup = telegram.ReplyKeyboardMarkup([['使用幻術，令地達羅暫時陷入幻境，趁這段時間逃離'],['再次使用神威，把他和爆炸轉移到另一空間'],['重玩','我要問問題']])
        update.message.reply_text('你為了避免鳴人獨自行動，從後追趕鳴人，發現敵人地達羅')
        update.message.reply_sticker('CAADBQADKwADmsj5Dz20G6UobuYYAg')
        update.message.reply_text('在戰鬥數回合後你開啓了萬花筒寫輪眼，對地達羅使用可以轉換空間的曈術--神威，及控制結界，打斷了地達羅剩下的右手，磕事你才剛剛練成神威，不能熟練地控制空間的位置和大小，在體力方面亦明顯不能支撐這種術，很快就感到疲憊。')
        update.message.reply_sticker('CAADBQADKwADmsj5Dz20G6UobuYYAg')
        update.message.reply_text(text='凱也在這時候前來救援，地達羅見寡不敵衆，想要用自爆同歸於盡，這時候你該怎麼辦？',reply_markup=reply_markup)

    def on_enter_LeiQie(self, update):
        global reply_markup
        reply_markup = telegram.ReplyKeyboardMarkup([['噢不'],['重玩']])
        update.message.reply_text('結印！丑--卯--申!')
        update.message.reply_text(text='大量的查克拉集中在手上形成高強度電流！這種感覺太不現實了，我要攻擊了！等等，這一刻不應該是用雷切的，而是。。。',reply_markup=reply_markup)


    def on_enter_ShenWei(self, update):
        global reply_markup
        reply_markup = telegram.ReplyKeyboardMarkup([['成功了'],['重玩']])
        update.message.reply_text('左眼開！启动万花筒写轮眼--瞳术--神威！')
        update.message.reply_text(text='幸而卡卡西在地達羅引爆的一刻，把他和爆炸轉移到另一空間，太好了， 我就知道我沒有記錯，還能使出神威，此生無憾了，由於連續使用兩次萬花筒寫輪眼，我。。不行了。。。',reply_markup=reply_markup)

    def on_enter_Hoshigaki(self, update):
        global reply_markup
        reply_markup = telegram.ReplyKeyboardMarkup([['噢不'],['重玩']])
        update.message.reply_text('你選擇作爲第二批出發支援的隊伍，突然！一只鯊魚向你們襲擊')
        update.message.reply_sticker('CAADBQADKAADmsj5D74DtFoAASS3MgI')
        update.message.reply_text(text='是干柿鬼鮫！他使出水遁·爆水衝波，他一口氣吐出大量的水，將一大片低漥谷地瞬間變成湖泊，你與隊員深陷其中，你忙着救別人，突然眼前一黑無法動彈，在感覺查克拉被一點一點奪取而昏過去了',reply_markup=reply_markup)

    def on_enter_Kakuzu(self, update):
        global reply_markup
        reply_markup = telegram.ReplyKeyboardMarkup([['成功了'],['重玩']])
        update.message.reply_text('啊 猜錯了。是鹿丸、丁次、井野他們。因為上忍猿飛阿斯瑪在追捕『曉』成員飛段、角都時陣亡')
        update.message.reply_sticker('CAADBQADKgADmsj5D-bAIqHbLj_kAg')
        update.message.reply_sticker('CAADBQADKQADmsj5D2hGOSaSV1B1Ag')
        update.message.reply_text('第十班矢志為老師復仇，而你將暫替阿斯瑪，作為第十班的隊長，率領他們再戰飛段、角都。')
        update.message.reply_text('甫一對戰，你成功以雷遁·雷切偷襲角都，破了其土遁·土矛（因為雷屬性剋土屬性），並刺穿其心臟。正當卡卡西以為對方已被擊斃，殊不知對方原來擁有多個從其他忍者搶來的心臟，故能不死。')
        update.message.reply_sticker('CAADBQADKQADmsj5D2hGOSaSV1B1Ag')
        update.message.reply_text(text='幸虧大和及時率領鳴人、祭、櫻三人趕到，加入戰團中。你讓鳴人作第二次攻擊。鳴人亦不負所託，以影分身成功欺騙角都，並從其背後施以風遁·螺旋手裏劍，巨大的摧毀力再連破角都兩個心臟。最後，卡卡西以寫輪眼收拾倒在地上、動彈不得的角都，摧毀他最後一個心臟，及把角都的屍首帶回木葉隱村給綱手研究。',reply_markup=reply_markup)

    def on_enter_Zabuza(self, update):
        global reply_markup
        reply_markup = telegram.ReplyKeyboardMarkup([['成功了'],['重玩']])
        update.message.reply_text('啊 猜錯了。是他們志乃、雛田、牙。為了得知有關『曉』的情報、及追蹤正在尋找宇智波鼬的宇智波佐助，你們一行人決定以宇智波鼬為鎖定目標進行追捕。目前你們透過鳴人的影分身、已得知佐助的大約位置。')
        update.message.reply_text('不過途中遇上擁有特殊能力的鳶；陷入苦戰')
        update.message.reply_sticker('CAADBQADLAADmsj5DxfS7VHBjt5fAg')
        update.message.reply_text(text='然後聽到佐助身受重傷，在甩掉鳶後，趕緊及帶人已早一步前往戰場，他也率眾快馬趕往，並開啓萬花筒寫輪眼。然而到達現場時，佐助早已被帶走了',reply_markup=reply_markup)

    def on_enter_followm(self, update):
        global reply_markup
        reply_markup = telegram.ReplyKeyboardMarkup([['那就相信千代婆婆一次吧'],['不管她啦！我相信是混合毒！'],['重玩','我要問問題']])
        update.message.reply_text('我就這樣就拖去增援，雖然我還不知道發生什麼事。我們趕到的時候看見砂的醫療忍者們為勘九郎身上的毒束手無策，還有千代婆婆。。')
        update.message.reply_sticker('CAADBQADJwADmsj5Dw0cb10rWm3WAg')
        update.message.reply_sticker('CAADBQADMAADmsj5D2AZg79XpAtAAg')
        update.message.reply_text('原來我愛羅被「曉」抓去，勘九郎掛念著被地達羅帶走的我愛羅，便立刻展開追蹤，靠著我愛羅掉落在路上的砂子，總算追上蠍與地達羅的腳步…，勘九郎為了救回我愛羅而與蠍對戰，沒想到卻因此讓自己陷入了極危險的困境之中…')
        update.message.reply_text('我現在是小櫻，是得到了綱手真傳的小櫻，應該可以治療他，我心裏念阿念，查克拉！！')
        update.message.reply_sticker('CAADBQADMwADmsj5D2WJjhjaWeAGAg')
        update.message.reply_text('千代：等等！他所中的是蠍子毒，不能這樣治療的！')
        update.message.reply_text('我：可是我記得漫畫裏是說蠍很會用混合毒。。。')
        update.message.reply_text('千代：什麼漫畫？')
        update.message.reply_text(text='我：啊！沒事。。我自言自語罷，該怎麼辦呢？難道真的是我記錯？',reply_markup=reply_markup)

    def on_enter_denym(self, update):
        global reply_markup
        reply_markup = telegram.ReplyKeyboardMarkup([['鳴人你是說要去救我愛羅嗎？'],['鳴人你是說要到天地橋，等待大蛇丸身邊的臥底出現嗎？'],['重玩','我要問問題']])
        update.message.reply_sticker('CAADBQADJgADmsj5D3B58IgX0bkqAg')
        update.message.reply_text('鳴人：你發瘋了啊！都什麼時候了還在鬧別扭！我們快來不及了！')
        update.message.reply_text(text='我：來不及。。這是哪裏的劇情。。快想起來啊！不管啦！先掰一個好了',reply_markup=reply_markup)


    def on_enter_poison1(self, update):
        global reply_markup
        reply_markup = telegram.ReplyKeyboardMarkup([['噢不'],['重玩','我要問問題']])
        update.message.reply_text(text='我心裏念阿念，查克拉！！這就是漫畫裏的查克拉刀！等等！勘九郎！他！怎麼會這樣！！他身上的毒加速擴散全身，已經陣亡了。應該相信自己的。。我被砂忍包圍。。看來是兇多吉少了',reply_markup=reply_markup)


    def on_enter_poison2(self, update):
        global reply_markup
        reply_markup = telegram.ReplyKeyboardMarkup([['走！'],['重玩','我要問問題']])
        update.message.reply_text('靠着對漫畫的記憶，先是調解了解藥，在他的血管裏注入查克拉混合解藥，利用查克拉將毒排除')
        update.message.reply_text('勘九郎：嘔！！！')
        update.message.reply_sticker('CAADBQADMAADmsj5D2AZg79XpAtAAg')
        update.message.reply_text('他將毒吐出來了！！成功排解了勘九郎所中的毒，真是有驚無險。幸好相信自己，不然就小命不保了。。')
        update.message.reply_text('千代：。。。')
        update.message.reply_text('我：。。')
        update.message.reply_text('我：謝謝千代婆婆，是你提醒了我混合毒裏還有蠍子毒的成分，不然就不會成功了')
        update.message.reply_text('千代：。。。阿。。不客氣。。')
        update.message.reply_text('卡卡西：查到曉的據點，我們必須立刻動身前往')
        update.message.reply_text('千代：我也要一起去。蠍是我一手造成的，我要親自收拾掉')
        update.message.reply_text(text='我：。。。帶上剛剛調好的解毒劑好了，不然中毒了小命不保了',reply_markup=reply_markup)
    
    def on_enter_Sasori(self, update):
        global reply_markup
        reply_markup = telegram.ReplyKeyboardMarkup([['其中一份交給千代好了，不然我也戰鬥不下去啊','兩份都給自己好了，我負責戰鬥，速戰速決！'],['重玩','我要問問題']])
        update.message.reply_sticker('CAADBQADNAADmsj5D-FIP9dk0I_DAg')
        update.message.reply_text('我們找到了蠍，我與與千代婆婆聯手對抗他，千代控制我與蠍對峙。蠍以「第三代風影」傀儡迎戰，我把第三代風影的磁遁忍法-鐵礦砂結襲一一以怪力飛踢開。')
        update.message.reply_text(text='但不幸我和千代婆婆也中了毒，幸好想起拿出替勘九郎治療時，多調配出的兩份解毒劑。可是藥力只能維持三分鍾，可是突然忘記了劇情，該給誰解毒呢？',reply_markup=reply_markup)
        
    def on_enter_Chiyo(self, update):
        global reply_markup
        reply_markup = telegram.ReplyKeyboardMarkup([['成功了'],['重玩']])
        update.message.reply_text('最後我們合作，我先以怪力擊破蠍的傀儡身體。蠍雖然馬上更換身體，因千代把他的再生核刺穿而死亡。')
        update.message.reply_sticker('CAADBQADNAADmsj5D-FIP9dk0I_DAg')
        update.message.reply_sticker('CAADBQADMwADmsj5D2WJjhjaWeAGAg')
        update.message.reply_sticker('CAADBQADMQADmsj5D14Ydx8Wcb-jAg')
        update.message.reply_text(text='最後從蠍口中得知，十天後草忍村的天地橋，曉安排在大蛇丸身邊的臥底會出現。',reply_markup=reply_markup)
 
    def on_enter_self(self, update):
        global reply_markup
        reply_markup = telegram.ReplyKeyboardMarkup([['噢不'],['重玩']])
        update.message.reply_text('我現在有6分鍾的時間，來個速戰速決！')
        update.message.reply_text('剩4分鍾。。不行啊。。無法突破。。千代婆婆也撐不住了')
        update.message.reply_text('剩1分鍾。。快撐不住了。。。')
        update.message.reply_text(text='不行了。。。',reply_markup=reply_markup)

    def on_enter_kill(self, update):
        global reply_markup
        reply_markup = telegram.ReplyKeyboardMarkup([['噢不'],['重玩']])
        update.message.reply_text('鳴人：你說什麼啊。。我愛羅已經被千代婆婆復活了。。你也在場。。怎麼會不知道。。難道你不是櫻。。')
        update.message.reply_sticker('CAADBQADJgADmsj5D3B58IgX0bkqAg')
        update.message.reply_text('我：事情不是這樣的！聽我解釋！')
        update.message.reply_text('鳴人：影分身之術！！')
        update.message.reply_text(text='結果我被當成了間諜，被關入忍者大牢。。',reply_markup=reply_markup)

    def on_enter_spymeet(self, update):
        global reply_markup
        reply_markup = telegram.ReplyKeyboardMarkup([['打就打！誰叫你說佐助壞話！','先忍着！任務結束就痛扁你一頓'],['重玩','我要問問題']])
        update.message.reply_text('第七班重組並派往執行救出宇智波佐助的任務。我與新隊長大和、新隊員佐井、鳴人一起出發。在路上，佐井一直在說佐助壞話，鳴人怒不可遏想打他，可是都被我一一阻止。')
        update.message.reply_sticker('CAADBQADNgADmsj5D71cue4Rk4nBAg')
        update.message.reply_sticker('CAADBQADNQADmsj5D-KEMylKzNCSAg')
        update.message.reply_text(text='按照劇情，我應該要一拳打往佐井，並說：「你不必原諒我。」，更指如果他再說佐助壞話，便不會手下留情。可是我現在不懂得控制力道，我怕會太大力到時候打草驚蛇。怎麼辦呢？',reply_markup=reply_markup)

    def on_enter_punch(self, update):
        global reply_markup
        reply_markup = telegram.ReplyKeyboardMarkup([[':暗殺佐助。','暗殺鳴人。'],['重玩','我要問問題']])
        update.message.reply_text('我：你不必原諒我。如果你再說佐助壞話，我絕不會手下留情的。')
        update.message.reply_sticker('CAADBQADNgADmsj5D71cue4Rk4nBAg')
        update.message.reply_text('其後來到天地橋，大和在做好行前準備後，便喬裝成蠍赴約，但令人驚訝的是，曉派去的間諜竟然是藥師兜。然而大蛇丸也現身了，在情勢所逼的情況下，大和決定叫鳴人他們三個人一起現身…。')
        update.message.reply_sticker('CAADBQADLgADmsj5DwWuglCC9jTFAg')
        update.message.reply_sticker('CAADBQADMQADmsj5D14Ydx8Wcb-jAg')
        update.message.reply_text('鳴人因為憤怒使得妖狐外衣再次外漏，不惜讓自己的意識被九尾吞噬，也要得到更強大的力量好將佐助帶回')
        update.message.reply_text(text='幸好在大和的搶救下慢慢恢復了…可是他的舉動卻讓此行的任務出現了意外插曲，佐井似乎也藉著這個機會，開始了他的真正任務…',reply_markup=reply_markup)

    def on_enter_nopunch(self, update):
        global reply_markup
        reply_markup = telegram.ReplyKeyboardMarkup([['重玩']])
        update.message.reply_text(text='我：你不必原諒我。如果你再說佐助壞話，我絕不會手下留情的。',reply_markup=reply_markup)


    def on_enter_yes(self, update):
        global reply_markup
        reply_markup = telegram.ReplyKeyboardMarkup([['任務重要，要把佐井抓住','佐助重要，不顧一切也要帶他回木葉'],['重玩','我要問問題']])
        update.message.reply_text('佐井在戰鬥中不見了，我們一路找到了大蛇丸基地')
        update.message.reply_sticker('CAADBQADNQADmsj5D-KEMylKzNCSAg')
        update.message.reply_text('發現佐井！他竟然會在這裏，他一定背叛了我們，我馬上衝上前大罵')
        update.message.reply_text('突然')
        update.message.reply_text('佐助')
        update.message.reply_sticker('CAADBQADLwADmsj5D09hhJp_o8EuAg')
        update.message.reply_text('相隔三年，佐助稱斬斷所有感情，除了怨恨，並與鳴人等發生戰鬥。')
        update.message.reply_text('雖然我不是真正的小櫻，可是我還是被嚇到愣住了')
        update.message.reply_text(text='我現在應該要怎麼辦',reply_markup=reply_markup)    

    def on_enter_no(self, update):
        global reply_markup
        reply_markup = telegram.ReplyKeyboardMarkup([['重玩']])
        update.message.reply_text(text='你他媽這樣也能答錯！回去重玩！',reply_markup=reply_markup)
              

    def on_enter_catchSai(self, update):
        global reply_markup
        reply_markup = telegram.ReplyKeyboardMarkup([['成功了'],['重玩']])
        update.message.reply_sticker('CAADBQADNQADmsj5D-KEMylKzNCSAg')
        update.message.reply_text('試圖襲擊並抓住佐井，可是被發現了，佐助發動千鳥，身體被麻痹不聽使喚了')
        update.message.reply_text(text='佐助。。',reply_markup=reply_markup)

    def on_enter_catchSasuke(self, update):
        global reply_markup
        reply_markup = telegram.ReplyKeyboardMarkup([['成功了'],['重玩']])
        update.message.reply_sticker('CAADBQADNgADmsj5D71cue4Rk4nBAg')
        update.message.reply_text('我不顧一切衝前攻擊佐助以帶他回木葉。但攻擊未至，大和先行替我擋住。')
        update.message.reply_text('我是第七班中唯一沒有跟佐助交手的人。 ')
        update.message.reply_sticker('CAADBQADMQADmsj5D14Ydx8Wcb-jAg')
        update.message.reply_text('最後，佐助跟大蛇丸離開。')
        update.message.reply_text('') 
        update.message.reply_text(text='「你在這裡哭，也不會把佐助哭回來。但接下來，我也會跟你一起變強！」',reply_markup=reply_markup)

    def on_enter_Continue(self, update):
        global reply_markup
        reply_markup = telegram.ReplyKeyboardMarkup([['重玩']])
        update.message.reply_text('成功了，可是後面還有很多的故事要經歷，我到底要什麼時候才能回到現實世界，同時我也想留在這個世界。') 
        update.message.reply_text('可能是因爲在現實世界活累了吧，無論在哪一個世界，我都要努力！！活出自己的故事！') 
        update.message.reply_text(text='我們一起加油',reply_markup=reply_markup)    

    def on_enter_Death(self, update):
        global reply_markup
        reply_markup = telegram.ReplyKeyboardMarkup([['就這樣吧']])
        update.message.reply_text('失敗了，回不去現實世界了') 
        update.message.reply_text('也許') 
        update.message.reply_text('我其實也沒有這樣想回去') 
        update.message.reply_text('如果再讓我想一次，也許我會更努力')
        update.message.reply_text('也許')
        update.message.reply_text('也許，沒有也許。。')
        update.message.reply_text(text='就這樣吧',reply_markup=reply_markup)    


    def on_exit_waiting(self, update):
        print('Leaving Waiting')

    def on_exit_menu(self, update):
        print('Leaving Menu')

    def on_exit_playing(self, update):
        print('Leaving Playing')

    def is_going_back_waiting(self, update):
        text = update.message.text
        return text == '重玩' or text == '開始！' or text == '我們一起加油' or text == '就這樣吧' or text == 'Get it' 
