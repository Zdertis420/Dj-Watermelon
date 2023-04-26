from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


keyboard = ReplyKeyboardMarkup(resize_keyboard=True)


genres = InlineKeyboardMarkup(row_width=2)
n = 0
for btn in ["Джаз", "Классическая Музыка", "Поп-музыка", "Рок/металл", "Хип-хоп", "Шансон"]:
    n += 1
    button = InlineKeyboardButton(text=btn,
                                  callback_data=f"genre_{n}")
    genres.add(button)


actions = InlineKeyboardMarkup(row_width=2)
n = "more"
for btn in ["Ещё", "Сначала"]:
    button = InlineKeyboardButton(text=btn,
                                  callback_data=f"btn_{n}")
    actions.add(button)
    n = "again"
