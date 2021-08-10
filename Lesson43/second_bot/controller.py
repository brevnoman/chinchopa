from Lesson43.second_bot.utils import get_image_url

def bop(bot, update):
    url = get_image_url()
    chat_id = bot.effective_chat.id
    update.bot.send_photo(chat_id=chat_id, photo=url)


