import logging
from time import sleep
from aiogram.dispatcher.filters import Text
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import CallbackQuery, KeyboardButton
from keyboards import keyboard, genres, actions
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


@dispatcer.message_handler(commands=['recommend'])
async def recommend(mess: types.Message):
    await dj.send_message(text=recomendRM(), chat_id=mess.from_user.id)


@dispatcer.message_handler(commands=['questions'])
async def questions(mess: types.Message):
    await askMood(mess)


@dispatcer.message_handler(commands=['help'])
async def help(mess: types.Message):
    await mess.answer(text='Йоу! Кароче, я тут местный DJ, ну там на вертушках и туц-туц-туц, ну понял.'
                           'Могу подсказать реально годный музон. Йоу!')

@dispatcer.message_handler(commands=['more'])
async def more(mess: types.Message):
    await dj.send_message(text="Также можешь послушать это:\n\n" + recomend(li, str(mess.from_user.id)),
                          chat_id=mess.from_user.id)
    sleep(1)
    await dj.send_message(text='Что дальше?', reply_markup=actions, chat_id=mess.from_user.id)


@dispatcer.message_handler(commands=['again'])
async def again(mess: types.Message):
    await askMood(mess)


@dispatcer.message_handler(commands=['start'])
async def start(mess: types.Message):
    await dj.send_video(mess.chat.id, open('static/img/DJ_Арбуз.mp4', 'rb'),
                        reply_markup=keyboard)
    sleep(0.5)
    await mess.answer(text='Здарова, йоу!\n'
                           'Хочешь крутой музон? Тогда ответь на парочку моих вопросов. йоу')

    sleep(0.3)

    await askMood(mess)


@dispatcer.message_handler()
async def askMood(mess: types.Message):
    li[str(mess.from_user.id)] = []
    sleep(0.5)

    await dj.send_message(text='Итак, вопрос номер один: как настроение? Веселое, грустное, или может ты словил дзен? Йоу',
                          chat_id=mess.from_user.id)
    print("gvklhiftyjfgfvyfytif")
    await Ans.mood.set()


@dispatcer.message_handler(state=Ans.mood)
async def getMood(mess: types.Message, state: FSMContext):
    mood = validator.validateMood(mess.text)
    await state.update_data(
        {'Настроение:': mood}
    )
    print(mood)

    li[str(mess.from_user.id)].append(mood)

    file1 = open("answersM.txt", 'a', encoding='utf-16')
    file1.write(mess.text + "\n")
    file1.close()

    await mess.answer(text='Второй вопрос: что делаешь? Йоу')

    await Ans.next()


@dispatcer.message_handler(state=Ans.occupation)
async def getOccupation(mess: types.Message, state=FSMContext):
    occupation = validator.validateOccupation(mess.text)
    await state.update_data(
        {'Занятие:': occupation}
    )

    print(occupation)

    li[str(mess.from_user.id)].append(occupation)

    file2 = open("answersO.txt", 'a', encoding='utf-16')
    file2.write(mess.text + "\n")
    file2.close()

    await mess.answer(text='И последний, какой жанр предпочитаешь? Йоу',
                      reply_markup=genres)
    await Ans.next()


@dispatcer.callback_query_handler(Text(startswith="genre_"), state=Ans.genre)
async def callbackGenre(call: CallbackQuery, state=FSMContext):
    await call.answer('Хорошо')
    action = call.data.split("_")[1]

    match action:
        case "1":
            print("Джаз")
            li[str(call.from_user.id)].append("Джаз")
        case "2":
            print("Классическая Музыка")
            li[str(call.from_user.id)].append("Классическая Музыка")
        case "3":
            print("Поп-музыка")
            li[str(call.from_user.id)].append("Поп-музыка")
        case "4":
            print("Рок-металл")
            li[str(call.from_user.id)].append("Рок-металл")
        case "5":
            print("Хип-хоп")
            li[str(call.from_user.id)].append("Хип-хоп")
        case "6":
            print("Шансон")
            li[str(call.from_user.id)].append("Шансон")

    print(li)

    await dj.send_message(text=f"Тогда тебе стоит послушать это:\n\n{recomend(li, str(call.from_user.id))}\nНу как тебе? Йоу",
                          chat_id=call.from_user.id)
    await state.finish()
    sleep(1.0)
    keyboard.add(KeyboardButton('more'))
    await dj.send_message(text='Что дальше?', reply_markup=actions, chat_id=call.from_user.id)
    await whatIsNext(call)


@dispatcer.callback_query_handler(Text(startswith="btn_"))
async def whatIsNext(call: CallbackQuery):
    await call.answer('Хорошо')
    action = call.data.split("_")[1]

    match action:
        case "more":
            await more(call)
        case "again":
            await again(call)


if __name__ == '__main__':
    executor.start_polling(dispatcer)
