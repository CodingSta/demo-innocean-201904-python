from telegram.ext import Updater, Filters
from telegram.ext import CommandHandler, ConversationHandler, MessageHandler


TELEGRAM_TOKEN = '********************************'    # FIXME: 각자의 Token 적용


def start(bot, update):
    chat_id = update.message.chat_id
    text = update.message.text
    bot.send_message(chat_id=chat_id, text="안녕. 나는 봇이야. 나랑 이야기해~")


def echo(bot, update):
    chat_id = update.message.chat_id
    text = update.message.text
    bot.send_message(chat_id=chat_id, text=text)


def main(token):
    bot = Updater(token=token)
    handler = CommandHandler('start', start)
    bot.dispatcher.add_handler(handler)
    handler = MessageHandler(Filters.text, echo)
    bot.dispatcher.add_handler(handler)
    bot.start_polling()
    print('running telegram bot ...')
    bot.idle()


if __name__ == '__main__':
    main(TELEGRAM_TOKEN)

