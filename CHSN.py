import telebot

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
        

@bot.message_handler(commands=['special'])
def mess(message):
    for user in joinedUsers:
        bot.send_message(user, message.text[message.text.find(' '):])

        
@bot.message_handler(commands=['help'])
def process_help(message):
    var = "В данном боте вы можете воспользоваться следующими командами: \n" \
          "/contacts – основные контакты организаторов \n" \
          "/students – контакты студентов, готовых ответить вам на все вопросы о Вышке \n"\
          "/timetable – ссылка на расписание" 
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
          "Дмитрий Пикулькин – глава технического сопровождения. +7 (983) 518-60-25 https://vk.com/id553263075  "
    bot.send_message(message.from_user.id, var, disable_web_page_preview = True)
    print(var)

@bot.message_handler(commands=['students'])
def process_help(message):
    var = "Вы можете узнать подробнее о жизни Вышки и факультета социальных наук у этих людей:"
    bot.send_message(message.from_user.id, var)
    print(var)



bot.polling(none_stop=True, timeout=123)
