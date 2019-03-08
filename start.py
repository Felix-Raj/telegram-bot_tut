import logging
import sys

from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler

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


def inline_caps(bot, update):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    bot.answer_inline_query(update.inline_query.id, results)


def unknown(bot, update):
    bot.send_message(update.message.chat_id, text='What do you mean??')


start_handler = CommandHandler('start', start)  # for /start command
echo_handler = MessageHandler(Filters.text, echo)  # for any text messages
caps_handler = CommandHandler('caps', caps, pass_args=True)  # /caps felix -> FELIX
inline_caps_handler = InlineQueryHandler(inline_caps)  # @felix_first_bot input input
unknown_handler = MessageHandler(Filters.command, unknown)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(caps_handler)
dispatcher.add_handler(inline_caps_handler)
dispatcher.add_handler(unknown_handler)

updater.start_polling()
