import telebot
from config import token
from telebot import types
import random
# from telegram import Updater


bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item1 = types.KeyboardButton('Русскій воєнний корабль НАХ#Й!')
    item2 = types.KeyboardButton('Продажа авто')
    item3 = types.KeyboardButton('Обмен авто')
    item4 = types.KeyboardButton('Ремонт')
    item5 = types.KeyboardButton('Запчасти')
    item6 = types.KeyboardButton('Другое')

    markup.add(item1, item2, item3, item4, item5, item6)

    bot.send_message(message.chat.id, 'Здравствуйте, я оффициальный бот компании '
                                      '"New Reality Car Dealer"''\n'
                                      'Для получения информации воспользуйтесь подсказками ниже' 
                                      .format(message.from_user), reply_markup=markup)


def echo(telebot, update):
    if update.message_text[-1] == '?':
        update.message.reply_text('Я Вас не понял, пожалуйста перефразируйте вопрос')


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.text == 'Продажа авто':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton('Аукцион Америка')
        item2 = types.KeyboardButton('Аукцион Европа')
        back = types.KeyboardButton('Назад')
        markup.add(item1, item2, back)

        bot.send_message(message.chat.id, 'Продажа авто', reply_markup=markup)

    elif message.text == 'Аукцион Америка':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton('Парсинг с пощадки')
        #item2 = types.KeyboardButton('Наименование машины')
        item2 = types.KeyboardButton('Mercedes-Benz')
        item3 = types.KeyboardButton('BMW')
        item4 = types.KeyboardButton('Audi')
        item5 = types.KeyboardButton('Volkswagen')
        item6 = types.KeyboardButton('Alfa Romeo')
        item7 = types.KeyboardButton('Volkswagen')
        item8 = types.KeyboardButton('Chevrolet')
        back = types.KeyboardButton('Назад')
        markup.add(item1, item2, item3, item4, item5, item6, item7, item8, back)

        bot.send_message(message.chat.id, 'Аукцион Америка', reply_markup=markup)


    elif message.text == 'Аукцион Европа':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton('Парсинг с пощадки')
        #item2 = types.KeyboardButton('Наименование машины')
        item2 = types.KeyboardButton('Mercedes-Benz')
        item3 = types.KeyboardButton('BMW')
        item4 = types.KeyboardButton('Audi')
        item5 = types.KeyboardButton('Volkswagen')
        item6 = types.KeyboardButton('Alfa Romeo')
        item7 = types.KeyboardButton('Volkswagen')
        item8 = types.KeyboardButton('Chevrolet')
        back = types.KeyboardButton('Назад')
        markup.add(item1, item2,  item3, item4, item5, item6, item7, item8, back)

        bot.send_message(message.chat.id, 'Аукцион Европа', reply_markup=markup)


    #elif message.text == 'Продажа авто':
        #markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        #item1 = types.KeyboardButton('Америка')
        #item2 = types.KeyboardButton('Европа')
        #item2 = types.KeyboardButton('Наименование машины')
        #back = types.KeyboardButton('Назад')
        #markup.add(item1, item2, back)

        #bot.send_message(message.chat.id, 'Продажа авто', reply_markup=markup)


    elif message.text == 'Обмен авто':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton('Добавить парсинг с авториа')
        back = types.KeyboardButton('Назад')
        markup.add(item1, back)

        bot.send_message(message.chat.id, 'Обмен авто', reply_markup=markup)


    elif message.text == 'Ремонт':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton('Рихтовка')
        item2 = types.KeyboardButton('Покраска')
        back = types.KeyboardButton('Назад')
        markup.add(item1, item2, back)

        bot.send_message(message.chat.id, 'Ремонт', reply_markup=markup)


    elif message.text == 'Запчасти':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton('Mercedes-Benz')
        item2 = types.KeyboardButton('BMW')
        item3 = types.KeyboardButton('Audi')
        item4 = types.KeyboardButton('Volkswagen')
        item5 = types.KeyboardButton('Alfa Romeo')
        item6 = types.KeyboardButton('Volkswagen')
        item7 = types.KeyboardButton('Chevrolet')
        back = types.KeyboardButton('Назад')
        markup.add(item1, item2, item3, item4, item5, item6, item7, back)

        bot.send_message(message.chat.id, 'Запчасти', reply_markup=markup)


    elif message.text == 'Другое':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton('Тут должно что-то быть')
        item2 = types.KeyboardButton('И тут должно что-то быть')
        back = types.KeyboardButton('Назад')
        markup.add(item1, item2, back)

        bot.send_message(message.chat.id, 'Другое', reply_markup=markup)


    elif message.text == 'Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton('Русскій воєнний корабль НАХ#Й!')
        item2 = types.KeyboardButton('Продажа авто')
        item3 = types.KeyboardButton('Обмен авто')
        item4 = types.KeyboardButton('Ремонт')
        item5 = types.KeyboardButton('Запчасти')
        item6 = types.KeyboardButton('Другое')

        markup.add(item1, item2, item3, item4, item5, item6)

        bot.send_message(message.chat.id, 'Назад', reply_markup=markup)


    elif message.text == 'Всего наилучшего':
        bot.send_message(message.chat.id)


if __name__ == '__main__':
    bot.polling(none_stop=True)