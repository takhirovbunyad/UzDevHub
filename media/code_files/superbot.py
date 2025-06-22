import logging
from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater, CallbackContext, ConversationHandler

# Bot tokenini o'zgartiring
TOKEN = '7724111174:AAHMDyhm4UjtVnpJHpQpeFrIndeDnN8WHEc'

# Adminlar ro'yxati
ADMIN_IDS = [7117614290, 6788761764]

# Javoblar va kalitlar saqlanadigan lug'at
answers = {}

# Logging sozlamalari
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# /rules komandasi
def send_rules(update: Update, context: CallbackContext):
    if update.message.chat.username == 'super_chat_team':  # Faqat super_chat_team guruhida ishlaydi
        update.message.reply_text("ASSALOMU ALEKUM HURMATINGIZGA SIKAY! BU GURUHDA SOKISH MAHORATINGIZ SINAB KORISHINGIZ MUMKIN")
    else:
        update.message.reply_text("Bu komanda faqat @super_chat_team guruhida ishlaydi.")

# Adminlar uchun /admin komandasini qo'shish
def admin_menu(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    if user_id not in ADMIN_IDS:
        update.message.reply_text("Siz admin emassiz!")
        return

    # Adminlarga kalit va javob qo'shish uchun komandalar
    update.message.reply_text("Admin menyusi:\n"
                              "/add_key - Kalit va javob qo'shish\n"
                              "/key_list - Kalit va javoblar ro'yxatini ko'rish")

# Kalit qo'shish komandasini yuborish
def add_key(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    if user_id not in ADMIN_IDS:
        return

    update.message.reply_text("Iltimos, kalitni kiriting:")
    return "await_key"  # Kalitni kutish holatiga o'tamiz

# Yangi kalitni qabul qilish
def process_new_key(update: Update, context: CallbackContext):
    key = update.message.text
    context.user_data['key'] = key  # Kalitni saqlash
    update.message.reply_text(f"Kalit '{key}' qabul qilindi. Iltimos, javobni kiriting:")
    return "await_answer"  # Javob kutish holatiga o'tamiz

# Yangi javobni qabul qilish
def process_new_answer(update: Update, context: CallbackContext):
    answer = update.message.text
    key = context.user_data['key']
    answers[key] = answer  # Kalit va javobni saqlash
    update.message.reply_text(f"Kalit: '{key}' va javob: '{answer}' muvaffaqiyatli qo'shildi.")
    return ConversationHandler.END  # Dialogni tugatish

# Kalitga mos javob yuborish
# Kalitga mos javob yuborish
def respond_to_key(update: Update, context: CallbackContext):
    text = update.message.text
    response = answers.get(text)  # Agar kalit mavjud bo'lsa, javobni olish
    if response:  # Faqat javob bo'lsa, yuborish
        update.message.reply_text(response)

# Kalit va javoblar ro'yxatini yuborish
def send_key_list(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    if user_id not in ADMIN_IDS:
        return

    if not answers:
        update.message.reply_text("Hozircha hech qanday kalit va javoblar mavjud emas.")
    else:
        key_list = "\n".join([f"Kalit: {key} - Javob: {answer}" for key, answer in answers.items()])
        update.message.reply_text(f"Kalit va javoblar:\n{key_list}")


def main():

    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher


    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('add_key', add_key)],
        states={
            "await_key": [MessageHandler(Filters.text, process_new_key)],
            "await_answer": [MessageHandler(Filters.text, process_new_answer)],
        },
        fallbacks=[]
    )


    dp.add_handler(CommandHandler('rules', send_rules))
    dp.add_handler(CommandHandler('admin', admin_menu))
    dp.add_handler(conv_handler)
    dp.add_handler(CommandHandler('key_list', send_key_list))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, respond_to_key))  # Kalitga mos javob yuborish

    # Botni ishlatish naxuy kayf ishla naxuy asaaaaaaaab buvingni
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
