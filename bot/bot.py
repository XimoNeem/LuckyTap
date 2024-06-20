import telebot
from telebot import types
from config import TOKEN, GAME_URL

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(text="Play Game", url=GAME_URL)
    markup.add(btn)
    bot.send_message(message.chat.id, "Welcome! Click the button below to play the game.", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, "Send /start to see the game button.")

if __name__ == '__main__':
    bot.polling(none_stop=True)