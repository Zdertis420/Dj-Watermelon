import logging
from aiogram.dispatcher.filters import Text
import validator
from time import sleep
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from keyboards import keyboard, genres
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

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


class Ans(StatesGroup):
    mood = State()
    occupation = State()


@dispatcer.message_handler(commands=['start'])
async def start(mess: types.Message):
    await dj.send_video(mess.chat.id, open('static/img/DJ_Арбуз.mp4', 'rb'),
                        reply_markup=keyboard)
    sleep(1)
    await mess.answer(text='Приветсвую!\n'
                           'Хочешь крутой музон? тогда ответь на парочку моих вопросов')
    sleep(0.5)
    # await dj.send_message(text='1. Как настроение? Весело, грустно, или может ты словил дзен?\n'
    #                            '2. Чо делаешь?\n',
    #                       chat_id=mess.from_user.id)


@dispatcer.message_handler(state=None)
async def askMood(mess: types.Message):
    await mess.answer(text='Итак, вопрос номер 1: как настроение? Весело, грустно, или может ты словил дзен?')
    await Ans.mood.set()


@dispatcer.message_handler(state=Ans.mood)
async def getMood(mess: types.Message, state: FSMContext):
    mood = validator.validateMood(mess)
    await state.update_data(
        {'Настроение:': mood}
    )

    await Ans.next()


@dispatcer.message_handler()
async def askOccupation(mess: types.Message):
    await mess.answer(text='Второй вопрос: чо делвешь?')


@dispatcer.message_handler(state=Ans.occupation)
async def getOccupation(mess: types.Message, state=)


@dispatcer.message_handler()
async def askGenre(mess: types.Message):
    await mess.answer(text='И последний, какой жанр предпочетаешь?',
                      reply_markup=genres)


@dispatcer.callback_query_handler(Text(startswith="genre_"))
async def callbackGenre(call: CallbackQuery):
    await call.answer('Хорошо')
    action = call.data.split("_")[1]
    match action:
        case "1":
            print("Джаз")
        case "2":
            print("Классическая Музыка")
        case "3":
            print("Поп-музыка")
        case "4":
            print("Рок-металл")
        case "5":
            print("Хип-хоп")
        case "6":
            print("Шансон")


# @dispatcer.message_handler()
# async def getMoodOrOccupation(mess: types.Message):
#     mood = validator.validateMood(mess)
#     occupation = validator.validateOccupation(mess)
#     return (mood, occupation)


if __name__ == '__main__':
    executor.start_polling(dispatcer)