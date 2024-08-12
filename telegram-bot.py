import telebot

bot = telebot.TeleBot("7466476435:AAFV0b34k6dI5K2Ay4U4fIdFlxdZ7cO-jIo", parse_mode=None)


@bot.message_handler(commands=['start', 'hello', 'help'])
def send_welcome(message):
    name = message.from_user.first_name
    bot.reply_to(message,  str(name) + ", how are you doing?")
    print(message)
 
@bot.message_handler(func=lambda m: True, content_types=["text", "photo"])
def echo_all(message):
    print(message)
    if message.content_type == "photo":
        bot.reply_to(message, "Thanks for the photo")
    else:
        bot.reply_to(message, message.text)
 
bot.infinity_polling()