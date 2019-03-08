import logging
import sys

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(level=logging.INFO, stream=sys.stdout, datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)
stdout = logging.StreamHandler(stream=sys.stdout)
formatter = logging.Formatter('%(asctime)s %(funcName)s %(lineno)d %(message)s')
stdout.setFormatter(formatter)
logger.addHandler(stdout)
logger.setLevel(logging.INFO)

# https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions-%E2%80%93-Your-first-Bot/c8dd272e26b939168eaa5812de5bf2b066ff10d6
updater = Updater(token='708241383:AAF6c7kwoPN3MsYJNQrc2L2XSdjSeUxZ4X0')
dispatcher = updater.dispatcher


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Hello World')


def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)


def caps(bot, update, args):
    text_caps = ' '.join(args).upper()
    bot.send_message(chat_id=update.message.chat_id, text=text_caps)


start_handler = CommandHandler('start', start)  # for /start command
echo_handler = MessageHandler(Filters.text, echo)  # for any text messages
caps_handler = CommandHandler('caps', caps, pass_args=True) # /caps felix -> FELIX

dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(caps_handler)

updater.start_polling()
