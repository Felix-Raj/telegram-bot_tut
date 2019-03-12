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

# https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions-%E2%80%93-JobQueue/0c79111ed68022f4936c2725f9827eac0a5240a0
job_queue = updater.job_queue


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


def callback_minute(bot, job):
    bot.send_message(chat_id='409803880',
                     text='One message per blah interval {}'.format(job.interval))
    # job interval can be changed here
    job.interval += 10
    if job.interval > 60.0:
        job.schedule_removal()


def callback_alarm(bot, job):
    bot.send_message(chat_id=job.context, text='BEEP!')


def callback_timer(bot, update, **kwargs):
    args = kwargs.get('args')
    _job_queue = kwargs.get('job_queue')
    time_out = int(args[0])
    bot.send_message(chat_id=update.message.chat_id,
                     text='Setting reminder after {} seconds'.format(time_out))
    _job_queue.run_once(callback_alarm, time_out, context=update.message.chat_id)


start_handler = CommandHandler('start', start)  # for /start command
echo_handler = MessageHandler(Filters.text, echo)  # for any text messages
caps_handler = CommandHandler('caps', caps, pass_args=True)  # /caps felix -> FELIX
inline_caps_handler = InlineQueryHandler(inline_caps)  # @felix_first_bot input input
job_minute = job_queue.run_repeating(callback_minute, interval=10, first=0)
timer_handler = CommandHandler('timer', callback_timer, pass_args=True,
                               pass_job_queue=True)  # /timer 1
unknown_handler = MessageHandler(Filters.command, unknown)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(caps_handler)
dispatcher.add_handler(inline_caps_handler)
job_minute.enabled = False  # disable the job temporarily
# job_minute.schedule_removal()  # remove completely
dispatcher.add_handler(timer_handler)
dispatcher.add_handler(unknown_handler)

updater.start_polling()
