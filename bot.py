import telebot
import re

# ضع توكن البوت الخاص بك هنا بين العلامتين
API_TOKEN = '9022886772:AAGPGuErGjRdGwGnncGXqQ16dlataSOd-40'

bot = telebot.TeleBot(API_TOKEN)

# كود الترحيب وفحص عمل البوت
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "مرحباً بك! بوت TWAIN GUARD يعمل الآن لحماية المجموعة 24 ساعة.")

# فحص الرسائل وحذف الروابط والسبام والكلمات المخالفة
@bot.message_handler(func=lambda message: True)
def filter_messages(message):
    # كشف الروابط
    urls = re.findall(r'(https?://[^\s]+|www\.[^\s]+|\bt\.me/[^\s]+)', message.text)
    
    # إذا كانت الرسالة تحتوي على رابط، يتم حذفها فوراً
    if urls:
        try:
            bot.delete_message(message.chat.id, message.message_id)
            # إرسال تحذير للعضو (اختياري)
            bot.send_message(message.chat.id, f"⚠️ عزيزي {message.from_user.first_name}، يمنع إرسال الروابط في هذه المجموعة.")
        except Exception as e:
            print(f"Error: {e}")

# تشغيل البوت بشكل مستمر
bot.infinity_polling()
