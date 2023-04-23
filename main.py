import logging

from aiogram.dispatcher.filters import Text

import validator
from time import sleep
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

with open('token') as token:
    TOKEN = token.read()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

dj = Bot(TOKEN)

dispatcer = Dispatcher(dj)

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton('start'))

genres = InlineKeyboardMarkup(row_width=2)
n = 0
for btn in ["Джаз", "Классическая Музыка", "Поп-музыка", "Рок/металл", "Хип-хоп", "Шансон"]:
    n += 1
    button = InlineKeyboardButton(text=btn,
                                  callback_data=f"genre_{n}")
    genres.add(button)



@dispatcer.message_handler(commands=['start'])
async def start(mess: types.Message):
    await dj.send_video(mess.chat.id, open('static/img/DJ_Арбуз.mp4', 'rb'),
                        reply_markup=keyboard)
    sleep(1)
    await mess.answer(text='Приветсвую!\n'
                           'Хочешь крутой музон? тогда ответь на парочку моих вопросов')
    sleep(0.5)
    await dj.send_message(text='1. Как настроение? Весело, грустно, или может ты словил дзен?\n'
                               '2. Чо делаешь?\n',
                          chat_id=mess.from_user.id)


@dispatcer.message_handler()
async def askGenre(mess: types.Message):
    await dj.send_message(text='И последний, какой жанр предпочетаешь?',
                          chat_id=mess.from_user.id,
                          reply_markup=genres)


@dispatcer.callback_query_handler(Text(startswith="genre_"))
async def callbackGenre(call: CallbackQuery):
    await call.answer('Хорошо')
    action = call.data.split("_")[1]
    if action == "1":
        print("Джаз")
    if action == "2":
        print("Классическая Музыка")
    if action == "3":
        print("Поп-музыка")
    if action == "4":
        print("Рок/металл")
    if action == "5":
        print("Хип-хоп")
    if action == "6":
        print("Шансон")



@dispatcer.message_handler()
async def getMoodOrOccupation(mess: types.Message):
    mood = validator.validateMood(mess)
    occupation = validator.validateOccupation(mess)
    return (mood, occupation)


if __name__ == '__main__':
    executor.start_polling(dispatcer)
