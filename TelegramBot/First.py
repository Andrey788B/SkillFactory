import telebot
from config import exchanger, TOKEN
from extensions import ConverterException, Convertor, UserDB

bot = telebot.TeleBot(TOKEN)

db = UserDB()

@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    text = r'''/set - команда для установки конвертируемых криптовалют,
По-умолчению идёт конвертация из рублей в BTC,
Введите сумму чтобы произвести конверцию'''
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in exchanger.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(commands=['set'])
def set(message: telebot.types.Message):
    markup = telebot.types.InlineKeyboardMarkup()
    for vol, form in exchanger.items():
        button = telebot.types.InlineKeyboardButton(text=vol.capitalize(), callback_data=f'vall {form}')
        markup.add(button)

    bot.send_message(chat_id=message.chat.id, text='Выберите криптовалюту, из которой будем конвертировать', reply_markup=markup)

    markup = telebot.types.InlineKeyboardMarkup()
    for vol, form in exchanger.items():
        button = telebot.types.InlineKeyboardButton(text=vol.capitalize(), callback_data=f'val2 {form}')
        markup.add(button)

    bot.send_message(chat_id=message.chat.id, text='выберите криптовалюту, в которую будем конвертировать', reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def handle_query(call):
    t, st = call.data.split()
    user_id = call.message.chat.id
    if t == "vall":
        db.change_from(user_id, st)

    if t == "val2":
        db.change_from(user_id, st)

    pair=db.get_pair(user_id)
    bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=f"Теперь конвертируем из {pair[0]} в {pair[1]} " )


@bot.message_handler(content_types=['text', ])
def converter(message: telebot.types.Message):
    pair = db.get_pair(message.chat.id)
    values = [*pair, message.text.strip()]
    print(message.chat.id)
    try:
        total = Convertor.get_price(values)

    except ConverterException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {values[2]} {values[0]} в {values[1]} - {total} {pair[1]}'
        bot.reply_to(message, text)


bot.polling(none_stop=True, interval=2)