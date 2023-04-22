import logging
from telegram.ext import Application, MessageHandler, filters, CommandHandler, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from time import sleep
import validator

with open('token') as token:
    TOKEN = token.read()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

replyKeyboard = [['/start']]
markup = ReplyKeyboardMarkup(replyKeyboard, one_time_keyboard=True, resize_keyboard=True)

keyboard = [[InlineKeyboardButton("Да", callback_data="Да")]]

replyMarkup = InlineKeyboardMarkup(keyboard)


async def start(update, context):
    await update.message.reply_video(video='static/img/DJ_Арбуз.mp4',
                                     reply_markup=markup)
    sleep(1)
    await hello(update)


async def hello(update):
    await update.message.reply_text(text='Приветсвую!\n'
                                         'Какую музыку желаешь послушать? Ответишь на парочку моих вопросов?',
                                    reply_markup=replyMarkup)


async def askMood(update):
    await update.message.reply_text(text='Как настроение?')
    mood = update.message.text()
    return validator.validateMood(mood)


async def askOccupation(update):
    await update.message.reply_text('Чо делаешь?')
    occupation = update.message.text()
    return validator.validateOccupation(occupation)


async def callbackInline(update, callback: CallbackQueryHandler):
    if callback:
        mood = await askMood(update)
        occupation = await askOccupation(update)
        # genre = askUser.askGenre(update)


async def closeKeyboard(update, context):
    await update.message.reply_text(
        "Ok",
        reply_markup=ReplyKeyboardRemove()
    )


async def echo(update, context):
    await update.message.reply_text(update.message.text)


async def reply(update, context):
    await update.message.reply_text('Отлично! Les go~')


def main():
    application = Application.builder().token(TOKEN).build()
    text_handler = MessageHandler(filters.TEXT, echo)
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler("close", closeKeyboard))
    application.add_handler(CallbackQueryHandler(callbackInline))
    application.add_handler(text_handler)
    application.run_polling()


if __name__ == '__main__':
    main()
