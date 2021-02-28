import random
import telebot
import datetime
from Character import Character

bot = telebot.TeleBot("1339981204:AAGfBHbWW4Bycellhh4cqWtgD1YAwUmF7WQ")

data = {0: {"message": None, "first_name": "Rihana", "second_name": "Fenty", "character": 2,
            "login_time": datetime.datetime.now()}, }


@bot.message_handler(commands=['start'])
def welcome(message):
    data[message.chat.id] = {"first_name": message.from_user.first_name,
                             "second_name": message.from_user.last_name,
                             "login_time": datetime.datetime.now(),
                             "character": None,
                             "message": None}
    images = []
    path = "content/images/characters/"
    images.append(telebot.types.InputMediaPhoto(open(path+"x1.jpg", "rb"), caption="Рицар"))
    images.append(telebot.types.InputMediaPhoto(open(path+"x2.jpg", "rb"), caption="Варвар"))
    images.append(telebot.types.InputMediaPhoto(open(path+"x3.jpg", "rb"), caption="Воїн"))
    images.append(telebot.types.InputMediaPhoto(open(path+"x4.jpg", "rb"), caption="Вор"))
    images.append(telebot.types.InputMediaPhoto(open(path+"x5.jpg", "rb"), caption="Дуелянтка"))
    images.append(telebot.types.InputMediaPhoto(open(path+"x6.jpg", "rb"), caption="Берсеркер"))
    images.append(telebot.types.InputMediaPhoto(open(path+"x7.jpg", "rb"), caption="Мандрівник"))
    images.append(telebot.types.InputMediaPhoto(open(path+"x8.jpg", "rb"), caption="Піратка"))
    images.append(telebot.types.InputMediaPhoto(open(path+"x9.jpg", "rb"), caption="Алебардщик"))
    images.append(telebot.types.InputMediaPhoto(open(path+"x10.jpg", "rb"), caption="Темний воїн"))
    # images.append(telebot.types.InputMediaPhoto(open(path+"x11.jpg", "rb"), caption = "Лучніца"))
    # images.append(telebot.types.InputMediaPhoto(open(path+"x12.jpg", "rb"), caption = "Копейщіця"))

    bot.send_media_group(message.chat.id, media=images)
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton("1 - Рицар", callback_data="ch_1"))
    markup.add(telebot.types.InlineKeyboardButton("2 - Варвар", callback_data="ch_2"))
    markup.add(telebot.types.InlineKeyboardButton("3 - Воїн", callback_data="ch_3"))
    markup.add(telebot.types.InlineKeyboardButton("4 - Вор", callback_data="ch_4"))
    markup.add(telebot.types.InlineKeyboardButton("5 - Дуелянтка", callback_data="ch_5"))
    markup.add(telebot.types.InlineKeyboardButton("6 - Берсеркер", callback_data="ch_6"))
    markup.add(telebot.types.InlineKeyboardButton("7 - Мандрівник", callback_data="ch_7"))
    markup.add(telebot.types.InlineKeyboardButton("8 - Піратка", callback_data="ch_8"))
    markup.add(telebot.types.InlineKeyboardButton("9 - Алберадщик", callback_data="ch_9"))
    markup.add(telebot.types.InlineKeyboardButton("10 - Темний воїн", callback_data="ch_10"))
    # markup.add(telebot.types.InlineKeyboardButton("11 - Лучніца", callback_data="ch_11"))
    # markup.add(telebot.types.InlineKeyboardButton("12 - Копейщіця", callback_data="ch_12"))
    data[message.chat.id]["message"] = bot.send_message(message.chat.id, "Hello {}\nВиберіть персонажа: ".format(
        message.from_user.first_name), reply_markup=markup)

    print(data)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if "ch_" in call.data:
        if not call.from_user.id in data:
            data[call.from_user.id] = {"first_name": call.from_user.first_name,
                                       "second_name": call.from_user.last_name,
                                       "login_time": datetime.datetime.now(),
                                       "character": None,
                                       "message": None}

        if data[call.from_user.id]["message"] != None:
            bot.delete_message(call.from_user.id, data[call.from_user.id]["message"].message_id)
            data[call.from_user.id]["message"] = None
        data[call.from_user.id]["character"] = Character.return_character(int(call.data[3:]))

        markup = telebot.types.InlineKeyboardMarkup()
        for key in Character.params:
            markup.add(
                telebot.types.InlineKeyboardButton(key + ": " + str(data[call.from_user.id]["character"].params[key]),
                                                   callback_data="wo_" + key))
        data[call.from_user.id]["message"] = bot.send_photo(call.from_user.id,
                                                            data[call.from_user.id]["character"].get_picture(),
                                                            caption=data[call.from_user.id]["character"].get_info(),
                                                            reply_markup=markup)

    elif "wo_" in call.data:
        if data[call.from_user.id]["message"] != None:
            bot.delete_message(call.from_user.id, data[call.from_user.id]["message"].message_id)
            data[call.from_user.id]["message"] = None
        data[call.from_user.id]["character"].params_up(str(call.data)[3:])
        markup = telebot.types.InlineKeyboardMarkup()
        if data[call.from_user.id]["character"].params_points > 0:
            for key in Character.params:
                markup.add(telebot.types.InlineKeyboardButton(
                    key + ": " + str(data[call.from_user.id]["character"].params[key]), callback_data="wo_" + key))
            data[call.from_user.id]["message"] = bot.send_photo(call.from_user.id,
                                                                data[call.from_user.id]["character"].get_picture(),
                                                                caption=data[call.from_user.id]["character"].get_info(),
                                                                reply_markup=markup)
        else:
            markup.add(telebot.types.InlineKeyboardButton("Завершити, перейти до навиків", callback_data="sk_"))
            data[call.from_user.id]["message"] = bot.send_photo(call.from_user.id,
                                                                data[call.from_user.id]["character"].get_picture(),
                                                                caption=data[call.from_user.id]["character"].get_info(
                                                                    info=1), reply_markup=markup)
    elif "sk_" in call.data:
        bot.send_message(call.from_user.id, "444")  # , reply_markup=markup)
    elif "end" in call.data:
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3, one_time_keyboard=True)
        markup.add("Weak enemie")
        markup.add("Middle enemie")
        markup.add("Strong enemie")
        bot.send_message(call.from_user.id, "Виберіть ворога", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def conversation(message):  # message.chat.id message.text
    if message.text == "Weak enemie":
        start_battle(message)


def start_battle(message):
    bot.send_message(message.chat.id, "В Вашого героя: 1000 хелсів, у ворога 400 хелсів")
    health = [1000, 400]
    counter = 0
    while health[0] > 0 and health[1] > 0:
        counter += 1
        health[counter % 2] -= min(random.randint(10, 100), health[counter % 2])
        bot.send_message(message.chat.id, "В Вашого героя: {} хелсів, у ворога {} хелсів".format(*health))
        if health[0] <= 0 or health[1] <= 0:
            if health[0] <= 0:
                bot.send_message(message.chat.id, "Ви програли")
            elif health[1] <= 0:
                bot.send_message(message.chat.id, "Ви виграли")
            else:
                bot.send_message(message.chat.id, "Нічя")


bot.polling(none_stop=True)