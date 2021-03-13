import blackBox
import random
from telebot import *

API_TOKEN = '1242927602:AAGdNmVXkoVTbGa3qM6BRljvN5MHd9hRytU'
bot = TeleBot(API_TOKEN)


class SingletonController:
    __instance = None

    def __init__(self):
        self.users = {}

    def add_user(self, id_player):
        self.users[id_player] = "0!0"  # ключ - это id; значение 1 - это level, значение 2 - это рандомное число сдвига

    def get_value(self, key):
        return self.users[key]

    def set_value(self, key, value):
        self.users[key] = value

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = SingletonController()
        return cls.__instance


controller = SingletonController().get_instance()
blackBx = blackBox.BlackBox().get_instance()


@bot.message_handler(content_types=['text'])
def start(message):
    if not controller.users.__contains__(message.chat.id):
        controller.add_user(message.chat.id)
    index_step = int(controller.get_value(message.chat.id).split('!')[0])
    if index_step == 0:
        keyboard = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="Да", callback_data="test")
        keyboard.add(callback_button1)
        callback_button2 = types.InlineKeyboardButton(text="ДА!", callback_data="test")
        keyboard.add(callback_button2)
        callback_button3 = types.InlineKeyboardButton(text="Конечно ДА!", callback_data="test")
        keyboard.add(callback_button3)
        bot.send_message(message.chat.id, "Привет дружище! Хочешь начать игру?", reply_markup=keyboard)
    elif index_step == 1:
        randNum = int(controller.get_value(message.chat.id).split('!')[1])
        isComplete = True
        text = message.text
        res = ""
        for i in text:
            letterNum = ord(i) - 1072
            print(str(ord(i)) + " " + str(letterNum))
            if 0 <= letterNum <= 33 or ord(i) == 32:
                if ord(i) == 32:
                    num = 128513 + randNum + 32
                else:
                    num = 128513 + randNum + letterNum
                res += chr(num)
            else:
                isComplete = False
                break
        if isComplete:
            bot.send_message(message.chat.id, res)
        else:
            bot.send_message(message.chat.id, "Вводи только русские буквы или пробел!")


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "test":
            bot.send_message(call.message.chat.id, "Супер, тогда приступай к испытанию чёрного ящика!\nТвоя задача победить меня, заветной фразой: “Я победил тебя, робот!”")
            bot.send_message(call.message.chat.id, "Введи любой текст(без цифр)")
            controller.set_value(call.message.chat.id, F"1!{random.randint(0, 10)}")

bot.polling()
