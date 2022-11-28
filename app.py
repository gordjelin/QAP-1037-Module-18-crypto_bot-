############################################################################################################
######################### Мой первый телеграмм бот "Конвертер валют/монет" #################################
############################################################################################################

import telebot
from config import coins, TOKEN
from extensions import APIException, Coin

bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start', 'help'])
def show_info(message):
  bot.send_message(message.chat.id, '📣 Для корректной работы отправьте сообщение в формате:\n\
|<b>имя валюты, цену которой вы хотите узнать</b>| |<b>имя валюты, в которой необходимо узнать \
 цену</b>| |<b>сумма первой валюты</b>|\n\n✅<b><u>Пример корректного запроса:</u></b> доллар \
 рубль 100\n\n💹 Для просмотра списка доступных валют используйте команду /values ', parse_mode='html')

@bot.message_handler(commands=['values'])
def show_coins(message):
  currency_list = list(coins.keys())
  bot.send_message(message.chat.id, f'📌 Перечень доступных валют:\n{", ".join(currency_list)}')

@bot.message_handler(content_types=['text'])
def convert_currency(message):
  try:
    user_message = message.text.lower().split()
    if len(user_message) != 3:
      raise APIException('Неверное количество аргументов.')
    base, quote, amount = user_message
    text = Coin.get_price(base, quote, amount)
  except APIException as e:
    bot.reply_to(message, f'❗ Ошибка ввода ❗\n{e}')
  else:
    bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)
