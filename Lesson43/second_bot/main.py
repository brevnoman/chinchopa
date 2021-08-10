from telegram.ext import Updater
from Lesson43.second_bot.hendlers import bop_command_handler
from Lesson43.second_bot.utils import get_logger


def main():
    my_token = open("token").read()
    updater = Updater(token=my_token, use_context=True)
    get_logger()
    dp = updater.dispatcher
    updater.start_polling()
    dp.add_handler(bop_command_handler)
    updater.idle()


if __name__ == '__main__':
    main()