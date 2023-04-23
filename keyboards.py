from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton('start'))

genres = InlineKeyboardMarkup(row_width=2)
n = 0
for btn in ["Джаз", "Классическая Музыка", "Поп-музыка", "Рок/металл", "Хип-хоп", "Шансон"]:
    n += 1
    button = InlineKeyboardButton(text=btn,
                                  callback_data=f"genre_{n}")
    genres.add(button)