from ctypes import resize
import telebot 
from googletrans import Translator
from telebot import types 


token = '5138723321:AAFonWgMTmPy6yqreCgtI1IRWVRjF3zhVvs'

bot = telebot.TeleBot(token=token)
translator = Translator()


a = translator.translate('milk', dest='ru')
print(a.text)

@bot.message_handler(commands=['start'])
def send(message):
    bot.send_message(message.chat.id,'Выберите язык')
    

@bot.message_handler(commands=['lang'])
def menu(message):
    markup = types.ReplyKeyboardarkup(resize_keyboard=True)
    item = types.KeyboardButton("Иди на хуй")
    item2 = types.KeyboardButton("Иди на нафиг")
    markup.add(item)
    markup.add(item2)
    bot.send_message(message.chat.id, 'Выберите язык для перевода', reply_markup=markup)

print('Бот работает....')
bot.infinity_polling()