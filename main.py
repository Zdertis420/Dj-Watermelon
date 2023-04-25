import logging
from aiogram.dispatcher.filters import Text
from time import sleep
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import CallbackQuery
from keyboards import keyboard, genres
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from obrabotka_db import recomend
import validator

with open('token') as token:
    TOKEN = token.read()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

dj = Bot(TOKEN)

dispatcer = Dispatcher(dj, storage=MemoryStorage())


class Ans(StatesGroup):
    mood = State()
    occupation = State()
    genre = State()


li = dict()


@dispatcer.message_handler(commands=['start'])
async def start(mess: types.Message):
    await dj.send_video(mess.chat.id, open('static/img/DJ_Арбуз.mp4', 'rb'),
                        reply_markup=keyboard)
    sleep(0.5)
    await mess.answer(text='Приветсвую!\n'
                           'Хочешь крутой музон? тогда ответь на парочку моих вопросов')

    sleep(0.5)
    li[mess.from_user.id] = []


@dispatcer.message_handler(state=None)
async def askMood(mess: types.Message):
    await mess.answer(text='Итак, вопрос номер один: как настроение? Веселое, грустное, или может ты словил дзен?')
    await Ans.mood.set()


@dispatcer.message_handler(state=Ans.mood)
async def getMood(mess: types.Message, state: FSMContext):
    mood = validator.validateMood(mess.text)
    await state.update_data(
        {'Настроение:': mood}
    )
    print(mood)

    li[mess.from_user.id].append(mood)
    await mess.answer(text='Второй вопрос: что делаешь?')

    await Ans.next()


@dispatcer.message_handler(state=Ans.occupation)
async def getOccupation(mess: types.Message, state=FSMContext):
    occupation = validator.validateOccupation(mess.text)
    await state.update_data(
        {'Занятие:': occupation}
    )
    print(occupation)
    li[mess.from_user.id].append(occupation)
    print(li)
    await mess.answer(text='И последний, какой жанр предпочитаешь?',
                      reply_markup=genres)
    await Ans.next()


@dispatcer.callback_query_handler(Text(startswith="genre_"), state=Ans.genre)
async def callbackGenre(call: CallbackQuery):
    await call.answer('Хорошо')
    action = call.data.split("_")[1]

    match action:
        case "1":
            print("Джаз")
            li[call.from_user.id].append("Джаз")
        case "2":
            print("Классическая Музыка")
            li[call.from_user.id].append("Классическая Музыка")
        case "3":
            print("Поп-музыка")
            li[call.from_user.id].append("Поп-музыка")
        case "4":
            print("Рок-металл")
            li[call.from_user.id].append("Рок-металл")
        case "5":
            print("Хип-хоп")
            li[call.from_user.id].append("Хип-хоп")
        case "6":
            print("Шансон")
            li[call.from_user.id].append("Шансон")

    print(li)

    await dj.send_message(text=recomend(li, call.from_user.id), chat_id=call.from_user.id)


if __name__ == '__main__':
    executor.start_polling(dispatcer)
