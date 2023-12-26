import telebot
from telebot import types
import time
from telebot.types import ReplyKeyboardRemove

bot = telebot.TeleBot('6478519890:AAE6xLraVJnNPeG08WdmFwUIkQXFSmA51qU')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Помощь'))

    bot.send_message(message.chat.id, f'Здравствуйте,  {message.from_user.first_name}')

    bot.send_message(message.chat.id, f'Для навигации по боту используйте кнопку "Помощь"', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


def on_click(message):
    print(message.text)
    btns = types.ReplyKeyboardMarkup()
    btns.add(types.KeyboardButton('Ссылки'))
    btns.add(types.KeyboardButton('FAQ'))
    btns.add(types.KeyboardButton('Оставить заявку'))
    btns.add(types.KeyboardButton('Контакты'))
    print('test')
    if message.text == "Помощь":
        bot.send_message(message.chat.id, f'Навигация', reply_markup=btns)
    elif message.text == "ку":
        bot.send_message(message.chat.id, 'Пожалуйста, для продолжения нажмите на кнопку "Помощь')
    print(message.text, "test2")
    bot.register_next_step_handler(message, menu)


def menu(message):
    url = types.InlineKeyboardMarkup()
    url.add(types.InlineKeyboardButton('Help', url="https://github.com"))
    url.add(types.InlineKeyboardButton('WiKi', url="https://github.com"))
    url.add(types.InlineKeyboardButton('Справочник', url="https://github.com"))
    url.add(types.InlineKeyboardButton('Меню', callback_data="menu"))

    if message.text == 'Ссылки':
        bot.reply_to(message, f'Ссылки на все источники', reply_markup=url)
        bot.send_message(message.chat.id, 'Если хотите вернуться назад нажмите "Меню"',
                         reply_markup=types.ReplyKeyboardRemove())

    elif message.text == 'FAQ':
        bot.reply_to(message, 'Часто задаваемые вопросы')
    elif message.text == 'Оставить заявку':
        bot.reply_to(message, 'Пожалуйста заполните заявку по форме')
        bot.send_message(message.chat.id, "1: \n2: \n3: \n4: \n5: \n6: \n7:")


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "menu":
        bot.send_message(call.message.chat.id, 'ХУй', reply_markup=on_click(call.message))

while True:
		try:
			bot.polling(none_stop=True)
		except:
			print('bolt')
			time.sleep(5)
