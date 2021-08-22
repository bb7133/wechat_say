import logging

try:
    from telegram.ext import Updater
    from telegram.ext import MessageHandler, Filters
except ImportError:
    import sys
    print >> sys.stderr, "Error importing Python bot for Telegram, try to use `pip install python-telegram-bot` to install it"

import chat_img_gen

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


updater = Updater(token='<token>', use_context=True)
dispatcher = updater.dispatcher

# def start(update, context):
#    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

# from telegram.ext import CommandHandler
# start_handler = CommandHandler('start', start)
# dispatcher.add_handler(start_handler)


def echo(update, context):
    # context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
    text = update.message.text
    chat_img_gen.generate_result(text)

    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(chat_img_gen.RESULT_PATH, 'rb'))


echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()
