import logging
import validator
from time import sleep
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

with open('token') as token:
    TOKEN = token.read()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

dj = Bot(TOKEN)

dispatcer = Dispatcher(dj)

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton('start'))




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
async def getMoodOrOccupation(mess: types.Message):
    mood = validator.validateMood(mess)
    occupation = validator.validateOccupation(mess)
    return (mood, occupation)


if __name__ == '__main__':
    executor.start_polling(dispatcer)
