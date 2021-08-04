


def check_time_and_send_info(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)