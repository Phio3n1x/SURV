import os
from datetime import datetime
from telegram.ext import Updater, MessageHandler, Filters

TOKEN = "8307381193:AAFayHVWYPbAwYlWudf3zyCc6uCb1wTCnzA"  # توکن بات
FOLDER = "user_messages"

if not os.path.exists(FOLDER):
    os.makedirs(FOLDER)

def log_message(user, content):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = os.path.join(FOLDER, f"{user.id}.txt")
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"[{now}] {user.first_name} ({user.id}): {content}\n")

def handle_message(update, context):
    user = update.message.from_user

    if update.message.text:
        log_message(user, update.message.text)

    elif update.message.photo:
        file_id = update.message.photo[-1].file_id
        file = context.bot.get_file(file_id)
        log_message(user, f"📷 Photo: {file.file_path}")

    elif update.message.voice:
        file_id = update.message.voice.file_id
        file = context.bot.get_file(file_id)
        log_message(user, f"🎤 Voice: {file.file_path}")

    elif update.message.video:
        file_id = update.message.video.file_id
        file = context.bot.get_file(file_id)
        log_message(user, f"🎬 Video: {file.file_path}")

    elif update.message.document:
        file_id = update.message.document.file_id
        file = context.bot.get_file(file_id)
        log_message(user, f"📄 Document: {file.file_path}")

    update.message.reply_text("پیامت ذخیره شد 📂")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.all, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
   
   
