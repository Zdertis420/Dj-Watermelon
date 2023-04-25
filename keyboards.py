from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


start = ReplyKeyboardMarkup(resize_keyboard=True)
start.add(KeyboardButton('start'))




genres = InlineKeyboardMarkup(row_width=2)
n = 0
for btn in ["Джаз", "Классическая Музыка", "Поп-музыка", "Рок/металл", "Хип-хоп", "Шансон"]:
    n += 1
    button = InlineKeyboardButton(text=btn,
                                  callback_data=f"genre_{n}")
    genres.add(button)