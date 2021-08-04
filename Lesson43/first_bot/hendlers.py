from telegram.ext import CommandHandler, MessageHandler, Filters, InlineQueryHandler
from Lesson43.first_bot.controller import start, echo, caps, unknown
from Lesson43.first_bot.inline_controllers import inline_caps


"""
Handlers
"""
start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
caps_handler = CommandHandler('caps', caps)
inline_caps_handler = InlineQueryHandler(inline_caps)
unknown_handler = MessageHandler(Filters.command, unknown)
