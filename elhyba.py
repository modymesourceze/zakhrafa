from config import Config
import requests , html , re
import telebot
import random
from datetime import datetime
import zz

roo = zz.rmoss()

roo2 = zz.rmoss2()

roo3 = zz.rmoss3()

roo4 = zz.rmoss4()

anum = zz.numr()

cookies = {
    'PHPSESSID': '4qp6upnbba034600cjohth03r6',
}

headers = {
    'authority': 'coolnames.online',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'dnt': '1',
    'origin': 'https://coolnames.online',
    'referer': 'https://coolnames.online/English-decoration',
    'sec-ch-ua': '"Chromium";v="105", "Not)A;Brand";v="8"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; M2004J19C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

token = Config.TG_BOT_TOKEN
bot = telebot.TeleBot(token,num_threads=30,skip_pending=True)

@bot.message_handler(commands=["start"])
def Welcome(message):
	
	keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)
	keyboard.add(
	telebot.types.InlineKeyboardButton('قسم الزخرفة', callback_data='zkk'),
	telebot.types.InlineKeyboardButton('قسم الرموز', callback_data='3'),
	telebot.types.InlineKeyboardButton('ارقام مزخرفه',callback_data='4'),
	telebot.types.InlineKeyboardButton('نسبة الحب',callback_data='5'),
	telebot.types.InlineKeyboardButton('حساب العـمر',callback_data="6")
        )
       
	
	bot.reply_to(message,'• اهلا بك في بوت الزخرفة المتميز 🌻\n• اختر من القائمة بالاسفل ⤵️',reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == "zkk")
def zkrfaa(call):
	
	keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)
	keyboard.add(
	telebot.types.InlineKeyboardButton('عربي', callback_data='1'),
	telebot.types.InlineKeyboardButton('انكليزي', callback_data='2'),
	telebot.types.InlineKeyboardButton('رجوع',callback_data='back')

        )
	
	bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="• قم باختيار نوع لزخرفة 📎\nتستطيع الزخرفه باللغتين ❨ ar • en ❩", reply_markup=keyboard)

# مصدر : @ELHYBA & @Source_Ze
 
@bot.callback_query_handler(func=lambda call: call.data == "2")   
def en(call):
    bot.send_message(call.message.chat.id,'*- حسنآ قم بأرسال اسمڪ باللغه الانكليزيه . !*',parse_mode="markdown")
    bot.register_next_step_handler(call.message, enzk)

def enzk(message):
    text = message.text
    if re.search(r'[a-z-A-Z]',text):
    	data = {
    	    'name': text,
    	    'get': 'english',
    	}
    	response = requests.post('https://coolnames.online/cool.php', cookies=cookies, headers=headers, data=data).text
    	zz = re.findall(r'<textarea.*?>(.*?)<\/textarea>',response)
    	cleaned_results = [html.unescape(xx) for xx in zz if xx.strip()]
    	for xx in cleaned_results:
    		bot.send_message(message.chat.id,xx)
    	bot.send_message(message.chat.id,"• تم زخرفة الاسم {}\n• اضغط على زر رجوع في الاسفل".format(text),reply_markup=telebot.types.InlineKeyboardMarkup([[telebot.types.InlineKeyboardButton(text='زخرفة مرة اخرى', callback_data='2')],[telebot.types.InlineKeyboardButton(text='رجوع', callback_data='zkk')]]))
    else:
    	bot.reply_to(message,'*فقط انكليزي. ¿*',parse_mode="markdown")


@bot.callback_query_handler(func=lambda call: call.data == '1')
def ar(call):
	bot.send_message(call.message.chat.id,'*- حسنآ قم بأرسال اسمڪ باللغه ﺄلعربيه . !*',parse_mode="markdown")
	bot.register_next_step_handler(call.message, arzk)

def arzk(message):
	text = message.text
	if re.search(r'[a-z-A-Z]',text):
		bot.reply_to(message,'*فقط عربي ¿*',parse_mode="markdown")
	else:
		url = f"http://xn--ogbjjc1f.com/inc/php/fancy-fonts.php?q={text}"
		req = requests.get(url).text
		aa = re.findall('value="(.*?)"',req)
		for zk in aa:
			bot.send_message(message.chat.id,zk)
		bot.send_message(message.chat.id,"• تم زخرفة الاسم {}\n• اضغط على زر رجوع في الاسفل".format(text),reply_markup=telebot.types.InlineKeyboardMarkup([[telebot.types.InlineKeyboardButton(text='زخرفة مرة اخرى', callback_data='1')],
	[telebot.types.InlineKeyboardButton(text='رجوع', callback_data='zkk')]
    ]))

@bot.callback_query_handler(func=lambda call: call.data == "4")
def numz(call):
	b = random.choice(anum)
	bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=b,reply_markup=telebot.types.InlineKeyboardMarkup([[telebot.types.InlineKeyboardButton(text='ارقام مزخرفه', callback_data='4')],
	[telebot.types.InlineKeyboardButton(text='رجوع', callback_data='back')]
    ]))

# مصدر : @ELHYBA & @Source_Ze

@bot.callback_query_handler(func=lambda call: call.data == "5")
def love(call):
	bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*• أهـلا بـك عزيزي .\n- فـي قسم قياس نسبه الحب  .\n- ارسل اسمك او اسم حبيبتك  .\nمثال : بروك و بروك*",parse_mode="markdown",reply_markup=telebot.types.InlineKeyboardMarkup([
        [telebot.types.InlineKeyboardButton(text='رجوع', callback_data='back')]
    ]))
	bot.register_next_step_handler(call.message, lov)
    
    
def lov(message):
	try:
		namex = message.text.split(" و ")
		if len(namex) == 2:
		      list = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
		      sT = random.choice(list)
		      bot.send_message(message.chat.id, f"- نـسبـه الحب والـثـقـه بـين {namex[0]} و {namex[1]} هـي 💞\n »  *{sT}*  «", parse_mode="markdown")
	except:
		pass
	
	
	
@bot.callback_query_handler(func=lambda call: call.data == "6")
def omr(call):
	bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*• اهلا بك عزيزي في قسم حساب العمر •\n• ارسل تاريخ ميلادك لحساب عمرك •\n• مثال : احسب 2000/1/1*",parse_mode="markdown",reply_markup=telebot.types.InlineKeyboardMarkup([
        [telebot.types.InlineKeyboardButton(text='رجوع', callback_data='back')]
    ]))
	bot.register_next_step_handler(call.message, omrr)

def omrr(message):
    try:
    	text = message.text
    	birth_date = datetime.strptime(text, "%Y/%m/%d")
    	current_date = datetime.now()
    	
    	age_diff = current_date - birth_date
    	years = age_diff.days // 365
    	months = (age_diff.days % 365) // 30
    	res = "تم حساب عمرك،\n\nعمرك هو الآن: {} سنة، و {} اشهر،".format(years,months)
    	bot.reply_to(message, res)
    except:
    	pass
# مصدر : @ELHYBA & @Source_Ze

@bot.callback_query_handler(func=lambda call: call.data == "3")
def romos(call):
	keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)
	keyboard.add(
	telebot.types.InlineKeyboardButton('رموز 1', callback_data='rm-1'),
	telebot.types.InlineKeyboardButton('رموز 2', callback_data='rm-2'),
	telebot.types.InlineKeyboardButton('رموز 3',callback_data="rm-3"),
	telebot.types.InlineKeyboardButton('رموز 4',callback_data="rm-4"),
	telebot.types.InlineKeyboardButton('رجوع',callback_data='back')
	)
	bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="أختر من يناسبك من رموز",reply_markup=keyboard)
	# مصدر : @ELHYBA & @Source_Ze

@bot.callback_query_handler(func=lambda call: call.data == 'rm-1')
def rm1(call):
	bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=roo,reply_markup=telebot.types.InlineKeyboardMarkup([
        [telebot.types.InlineKeyboardButton(text='رجوع', callback_data='3')]
    ]))

@bot.callback_query_handler(func=lambda call: call.data == 'rm-2')
def rm2(call):
	bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=roo2,reply_markup=telebot.types.InlineKeyboardMarkup([
        [telebot.types.InlineKeyboardButton(text='رجوع', callback_data='3')]
    ]))

@bot.callback_query_handler(func=lambda call: call.data == 'rm-3')
def rm3(call):
	bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=roo3,reply_markup=telebot.types.InlineKeyboardMarkup([
        [telebot.types.InlineKeyboardButton(text='رجوع', callback_data='3')]
    ]))
    
@bot.callback_query_handler(func=lambda call: call.data == 'rm-4')
def rm3(call):
	bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=roo4,reply_markup=telebot.types.InlineKeyboardMarkup([
        [telebot.types.InlineKeyboardButton(text='رجوع', callback_data='3')]
    ]))


@bot.callback_query_handler(func=lambda call: call.data == 'back')
def back_callback(call):
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(
    telebot.types.InlineKeyboardButton('قسم الزخرفة', callback_data='zkk'),
    telebot.types.InlineKeyboardButton('قسم الرموز', callback_data='3'),
    telebot.types.InlineKeyboardButton('ارقام مزخرفه',callback_data='4'),
    telebot.types.InlineKeyboardButton('نسبة الحب',callback_data='5'),
    telebot.types.InlineKeyboardButton('حساب العـمر',callback_data="6")
        )
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="• اهلا بك في بوت الزخرفة المتميز 🌻\n• اختر من القائمة بالاسفل ⤵", parse_mode='markdown',reply_markup=keyboard)
    
bot.infinity_polling()

'''تذكر مصدري حق تعبي
ولا تخمط تثبت فشلك هو اصلن انتا فاشل
قناتي : @Source_Ze
مبرمج الملف : @ELHYBA
'''