import logging
from pickle import POP_MARK
from telegram import Bot, Update, ReplyKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, Updater, Filters
TOKEN = '5603821420:AAGapAh0Q2RoCCNH2Ech4NZSVFEvw2gTzZs'
bot = Bot(TOKEN)
# enable logging of errors
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def run_start(update, callback):
    chat_id = update.message.chat.id  # get user's chat id
    keyboard = ReplyKeyboardMarkup(
        [['dry noodle'], ['soup noodle']], resize_keyboard=True)
    bot.send_message(chat_id, 'What nOoDlE YoU WAnt', reply_markup=keyboard)


def dry_noodle(update, poduct):
    chat_id = update.message.chat.id
    bot.send_message(chat_id, 'goood choice')
    bot.send_message(chat_id,
                     '''1. Indomee
2. jajeongman
3. Mee_pok''',reply_markup=keyboard)
    keyboard = ReplyKeyboardMarkup(['1', '2', '3'])


def soup_noodle(update,product):
    chat_id = update.message.chat.id
    bot.send_message(chat_id, 'heathier choicee')
    bot.send_message(chat_id,
                     '''1. Roasted sesame
 2. Curry Maggi
 3. Chicken noodle''',reply_markup=keyboard)
    keyboard = ReplyKeyboardMarkup(['1', '2', '3'])

def echo(update, callback):
    chat_id = update.message.chat.id
    text = update.message.text  # get whatever text the user sent
    keyboard = ReplyKeyboardMarkup(
        [['cook it'], ['I go home cook']], resize_keyboard=True)
    bot.send_message(chat_id, 'heres your noodle', reply_markup=keyboard)




def main() -> None:
    updater = Updater(TOKEN)
    # this passes your bot token into the Updater, allowing for messages sent to your bot to be passed as Update objects

    # initialize a dispatcher, to register handlers
    dispatcher = updater.dispatcher
    # add handlers, which dictates how your bot would handle different inputs
    dispatcher.add_handler(CommandHandler('start', run_start))
    dispatcher.add_handler(MessageHandler(
        Filters.regex('dry noodle'), dry_noodle))
    dispatcher.add_handler(MessageHandler(
        Filters.text & ~Filters.command, echo))

    # start the bot
    updater.start_polling()
    updater.idle()


# run main function
if __name__ == '__main__':
    main()
