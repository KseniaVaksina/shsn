import telebot
from telebot import *

bot = telebot.TeleBot("1438804180:AAErCm_DWjlTS5X7vCFVoFqvrQ3thCOQRHk", parse_mode=None)

joinedFile = open("joined.txt", "r")
joinedUsers = set()
for line in joinedFile:
    joinedUsers.add(line.strip())
joinedFile.close()


@bot.message_handler(commands=['start'])
def startJoin(message):
    if not str(message.chat.id) in joinedUsers:
        joinedFile = open("joined.txt", "a")
        joinedFile.write(str(message.chat.id) + "\n")
        joinedUsers.add(message.chat.id)
    var = "Чтобы посмотреть список команд, напиши /help"    
    bot.send_message(message.from_user.id, var)
    print(var)
        
        
@bot.message_handler(commands=['students'])
def get_op(message):
      keyboard = types.InlineKeyboardMarkup()
      key_pol = types.InlineKeyboardButton(text='Политология', callback_data='pol')
      key_soc = types.InlineKeyboardButton(text='Cоциология', callback_data='soc')
      key_gmu = types.InlineKeyboardButton(text='ГМУ', callback_data='gmu')
      key_psy = types.InlineKeyboardButton(text='Психология', callback_data='psy')
      key_lyc = types.InlineKeyboardButton(text='Лицей НИУ ВШЭ', callback_data='lyc')
      keyboard.add(key_pol, key_soc,key_psy,key_gmu, key_lyc)
      question = 'Выберите образовательную программу'
      bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'pol':
        var = 'По всем интересующим вас вопросам об ОП «Политология» вы можете обратиться к этим студентам: \n' \
              'Георгий Комендантов, 2 курс – https://vk.com/zzimablue\n' \
              'Елена Алыбина, 2 курс – https://vk.com/elenaalybina\n' \
              'Артур Арзуманян, 2 курс – https://vk.com/artshic\n' \
              'Георгий Шишкин, 3 курс – https://vk.com/goshishsh \n' \
              'Варя Филиппова, 3 курс – https://vk.com/sadwwitch'
    elif call.data == 'soc':
        var = 'По всем интересующим вас вопросам об ОП «Социология» вы можете обратиться к этим студентам: \n' \
              'Лариса Преображенская, 1 курс – https://vk.com/plutotlavie \n' \
              'Дмитрий Максименко, 1 курс – https://vk.com/maximenko_dm \n' \
              'Артём Колодяжный, 2 курс – https://vk.com/id_tomas_rock \n' \
              'Чен Сун Хи (Анастасия Ли), 2 курс – https://vk.com/nastya_chen \n' \
              'Елизавета Толстогузова, 2 курс – https://vk.com/lizok.keepsintouch \n' \
              'Маргарита Жданкина, 3 курс – https://vk.com/mamiezh \n' \
              'Ксения Ваксина, 3 курс – https://vk.com/id415749948 \n' \
              'Валерия Мошенко, 4 курс – https://vk.com/leruff \n' \
              'Дарья Жукова, 4 курс – https://vk.com/prosto_zhuk'
    elif call.data == 'gmu':
        var = 'По всем интересующим вас вопросам об ОП «ГМУ» вы можете обратиться к этим студентам: \n' \
              'Дарья Дергачева, 2 курс – https://vk.com/d.dergacheva \n' \
              'Алан Гадзаонов, 2 курс – https://vk.com/alangadzaonov \n' \
              'Анастасия Правосуд, 2 курс – https://vk.com/pravosudnastya \n' \
              'Илья Кузьмин, 2 курс – https://vk.com/existancevk \n' \
              'Даниил Ползиков, 3 курс – https://vk.com/dankaplz \n' \
              'Артём Шаюк, выпускник бакалавриата – https://vk.com/ashayuk'
    elif call.data == 'psy':
        var = 'По всем интересующим вас вопросам об ОП «Психология» вы можете обратиться к этим студентам: \n' \
              'Ксения Хлебникова, 2 курс – https://vk.com/id273613605 \n' \
              'Алина Шевелева, 2 курс – https://vk.com/sergeevnaa__a \n' \
              'Салават Юлушев, 2 курс – https://vk.com/yulushevs \n' \
              'Дария Шипова, 2 курс – https://vk.com/thisis_mydesign \n' \
              'Николай Купцов, 2 курс – https://vk.com/id152807979 \n' \
              'Александра Рожанская, 2 курс – https://vk.com/alex_the_witch \n' \
              'Василиса Грабарь, 2 курс – https://vk.com/vgraba \n' \
              'Софья Захарова, 2 курс – https://vk.com/ssssoncha \n' \
              'Алёна Харитонова, 3 курс – https://vk.com/alykharit'
    elif call.data == 'lyc':
        var = 'По всем интересующим вас вопросам о Лицее НИУ ВШЭ, в том числе и организационным моментам, вы можете обратиться к этим студентам:\n' \
              'Дмитрий Максименко, выпускник Лицея – https://vk.com/maximenko_dm \n' \
              'Лариса Преображенская, выпускница Лицея – https://vk.com/plutotlavie \n' \
              ' \n' \
              'А также вся актуальная информация о Лицее – https://vk.com/hsemeetingarea'
    bot.send_message(call.message.chat.id, var, disable_web_page_preview = True)
        
        

@bot.message_handler(commands=['special'])
def mess(message):
    for user in joinedUsers:
        bot.send_message(user, message.text[message.text.find(' '):])

        
@bot.message_handler(commands=['help'])
def process_help(message):
    var = "В данном боте вы можете воспользоваться следующими командами: \n" \
          "/timetable – ссылка на расписание \n" \
          "/link – ссылка на все онлайн-мероприятия \n" \
          "/social_net – ссылки на основные социальные сети  \n" \
          "/contacts – основные контакты организаторов \n" \
          "/students - контакты студентов, у которых вы можете уточнить любые вопросы о Вышке и ФСН"
    bot.send_message(message.from_user.id, var)
    print(var)

@bot.message_handler(commands=['timetable'])
def process_help(message):
    var = "Вот ссылочка на расписание: \n" \
          "https://docs.google.com/spreadsheets/d/1fiXalUl5fkmh0THK3X8dEwTZMgYW6zK5L-VP94AX94I/edit#gid=1916275378" 
    bot.send_message(message.from_user.id, var)
    print(var)
    
    
@bot.message_handler(commands=['contacts'])
def process_help(message):
    var = "Если вы столкнулись с проблемой, то можете обратиться к следующим людям:\n" \
          "Валерия Мошенко – координатор Школы социальных наук – 2021. +7 (977) 445-02-50. https://vk.com/leruff \n" \
          "Эльвина Амирова – главный организатор школы. +7 (965) 627-56-33. https://vk.com/aknivor \n" \
          "Алина Хаматдинова – глава учебной программы.+7 (985) 198-11-86. https://vk.com/alina.khamat \n" \
          "Илья Кузьмин – глава внеучебной программы. +7 (917) 700-62-18. https://vk.com/existancevk \n" \
          "Анастасия Ли – глава PR. +7 (914) 742-97-05. https://vk.com/nastya_chen \n" \
          "Дмитрий Пикулькин – глава технического сопровождения. +7 (983) 518-60-25 https://vk.com/id553263075 "
    bot.send_message(message.from_user.id, var, disable_web_page_preview = True)
    print(var)
    
    
@bot.message_handler(commands=['link'])
def process_help(message):
    var = "Вот ссылочка на все онлайн-мероприятия:\n" \
          "https://zoom.us/j/8281678013?pwd=KzA3TVdrVTlGS0lWeU0yUDh6Tjkxdz09#success\n" \
          "Идентификатор конференции: 828 167 8013\n" \
          "Код доступа: UWq295"
    bot.send_message(message.from_user.id, var)
    print(var)
    
@bot.message_handler(commands=['social_net'])
def process_help(message):
    var = "Вот ссылки на основные социальные сети:\n" \
          "https://t.me/joinchat/EbDf81Q3jvw68Gdo – общий чат в Telegram. \n" \
          "https://t.me/school_fsn – канал в Telegram.  ОБЯЗАТЕЛЬНО ПОДПИШИСЬ! \n" \
          "https://t.me/addstickers/school_fsn – стикеры в Telegram \n"\
          "https://instagram.com/school_fsn – страничка в Instagram \n" \
          "https://vk.com/school_fsn – открытая группа ВКонтакте \n" \
          "https://vk.com/school_fsn21 – закрытая группа ВКонтакте"
    bot.send_message(message.from_user.id, var, disable_web_page_preview = True)
    print(var)


bot.polling(none_stop=True, timeout=123)
