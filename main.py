import blackBox
import singeltone
import random
from telebot import *

API_TOKEN = '1242927602:AAGdNmVXkoVTbGa3qM6BRljvN5MHd9hRytU'
bot = TeleBot(API_TOKEN)

WIN_PHRASE = "Я победил тебя, робот."

controller = singeltone.SingletonController().get_instance()
blackBx = blackBox.BlackBox().get_instance()


@bot.message_handler(content_types=['text'])
def start(message):
    if not controller.users.__contains__(message.chat.id):
        controller.add_user(message.chat.id)
    index_step = int(controller.get_value(message.chat.id).split('!')[0])
    if index_step == 0:
        halloMessage(message)
    elif index_step == 1:
        randNum = int(controller.get_value(message.chat.id).split('!')[1])
        response = blackBx.get_response(message.text, randNum)
        bot.send_message(message.chat.id, response)
        if response == WIN_PHRASE:
            bot.send_message(message.chat.id, "Вы выйграли!")
            halloMessage(message)
            controller.set_value(message.chat.id, F"0!0")


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "test":
            bot.send_message(call.message.chat.id,
                             f"Супер, тогда приступай к испытанию чёрного ящика!\nТвоя задача победить меня, заветной фразой: “{WIN_PHRASE}”")
            bot.send_message(call.message.chat.id, "Введи любой текст или смайлики ;)")
            controller.set_value(call.message.chat.id, F"1!{random.randint(0, 10)}")


def halloMessage(message):
    keyboard = types.InlineKeyboardMarkup()
    callback_button1 = types.InlineKeyboardButton(text="Да", callback_data="test")
    keyboard.add(callback_button1)
    callback_button2 = types.InlineKeyboardButton(text="ДА!", callback_data="test")
    keyboard.add(callback_button2)
    callback_button3 = types.InlineKeyboardButton(text="Конечно ДА!", callback_data="test")
    keyboard.add(callback_button3)
    bot.send_message(message.chat.id, "Хочешь начать игру?", reply_markup=keyboard)


bot.polling()
