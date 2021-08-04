from telegram.ext import CommandHandler
from Lesson43.second_bot.controller import bop


bop_command_handler = CommandHandler('bop',bop)