import telebot

bot = telebot.TeleBot("1491942471:AAEded51LZEFr9Bi391xr5ZPTQawKcpZGoA", parse_mode=None)

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

@bot.message_handler(commands=['spesial'])
def mess(message):
    for user in joinedUsers:
        bot.send_message(user, message.text[message.text.find(' '):])


@bot.message_handler(commands=['error'])
#def process_help(message):
#    var = "Если вы столкнулись с проблемой, то можете обратиться к следующим людям:"
 #   bot.send_message(message.from_user.id, var)
  #  print(var)


@bot.message_handler(commands=['help'])
def process_help(message):
    var = "В данном боте вы можете воспользоваться следующими командами: \n" \
          "/contacts - основные контакты организаторов и вожатых \n" \
          "/students - контакты студентов, готовых ответить вам на все вопросы о Вышке"
    bot.send_message(message.from_user.id, var)
    print(var)

@bot.message_handler(commands=['contacts'])
def process_help(message):
    var = "Если вы столкнулись с проблемой, то можете обратиться к следующим людям:\n" \
          "Валерия Мошенко - координатор Школы социальных наук 2021. +7 (977) 445-02-50. https://vk.com/leruff \n" \
          "Эльвина Амирова - главный организатор школы. +7 (965) 627-56-33. https://vk.com/aknivor \n" \
          "Алина Хаматдинова - глава учебной программы.+7 (985) 198-11-86. https://vk.com/alina.khamat \n" \
          "Илья Кузьмин - глава внеучебной программы. +7 (917) 700-62-18. https://vk.com/existancevk \n" \
          "Анастасия Ли - глава PR. +7 (914) 742-97-05. https://vk.com/nastya_chen \n" \
          "Дмитрий Пикулькин - глава технического сопровождения. +7 (983) 518-60-25 https://vk.com/id553263075  "
    bot.send_message(message.from_user.id, var)
    print(var)

@bot.message_handler(commands=['students'])
def process_help(message):
    var = "Вы можете узнать подробнее о жизни Вышки и факультета социальных наук у этих людей:"
    bot.send_message(message.from_user.id, var)
    print(var)



bot.polling(none_stop=True, timeout=123)
