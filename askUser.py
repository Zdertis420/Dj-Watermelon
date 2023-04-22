import validator
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

G = ["джаз", "классическая музыка", "поп-музыка", "рок/металл", "хип-хоп", "шансон"]


def askMood(update):
    update.message.reply_text('Как натроение?')
    mood = update.message.text()
    return validator.validateMood(mood)


def askOccupation(update):
    update.message.reply_text('Чо делаешь?')
    occupation = update.message.text()
    return validator.validateOccupation(occupation)


def askGenre(update):
    genres = [
        [InlineKeyboardButton(G[0], callback_data=G[0]),
         InlineKeyboardButton(G[1], callback_data=G[1])],
        [InlineKeyboardButton(G[2], callback_data=G[2]),
         InlineKeyboardButton(G[3], callback_data=G[3])],
        [InlineKeyboardButton(G[4], callback_data=G[4]),
         InlineKeyboardButton(G[5], callback_data=G[5])]
    ]
    genresMarkup = InlineKeyboardMarkup(genres)
    update.message.reply_text('Какой жанр предпочитаешь?',
                              reply_markup=genresMarkup)