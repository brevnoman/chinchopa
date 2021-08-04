from telegram.ext import Updater
import logging

def main():
    my_token = open("token").read()
    updater = Updater(token=my_token, use_context=True)
    dispatcher = updater.dispatcher
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    updater.start_polling()
